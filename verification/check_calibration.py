#!/usr/bin/env python3
"""Finite checks for the calibration-information storage theorem.

These checks reconstruct physical sign averages and code eigenspaces.  They do
not prove the all-size information converse or the asymptotic rate theorem.
The JSON output is deterministic: it contains no timestamp or random samples.

Run from the repository root:
    python verification/check_calibration.py \
        --output verification/calibration_results.json
"""

from __future__ import annotations

import argparse
from collections import Counter
import itertools
import json
import math
from pathlib import Path
from typing import Any

import numpy as np


TOLERANCE = 2e-12
OUTAGE_TOLERANCE = 2e-14


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean_float(value: float) -> float:
    """Keep a compact report without hiding small numerical discrepancies."""
    if value == 0.0:
        return 0.0
    return float(f"{value:.14g}")


def bitstrings(length: int):
    return itertools.product((0, 1), repeat=length)


def signs(length: int):
    return itertools.product((-1, 1), repeat=length)


def tensor_power(matrix: np.ndarray, exponent: int) -> np.ndarray:
    result = np.ones((1, 1), dtype=complex)
    for _ in range(exponent):
        result = np.kron(result, matrix)
    return result


def check_sign_average() -> dict[str, Any]:
    """Build the average from exp(-i theta A_s), not from a dephasing formula."""
    cases = []
    max_matrix_error = 0.0
    max_eigenvalue_error = 0.0
    minimum_cp_eigenvalue = 0.0
    max_complete_dephasing_error = 0.0
    angles = (0.0, math.pi / 8, math.pi / 4, 3 * math.pi / 8,
              math.pi / 2, 0.37)
    for n in range(1, 5):
        z = np.array(
            [[1 - 2 * bit for bit in word] for word in bitstrings(n)],
            dtype=float,
        )
        for g0 in (0.0, 2.0):
            for theta in angles:
                physical = np.zeros((2**n, 2**n), dtype=complex)
                for pattern in signs(n):
                    energies = z @ (g0 + np.array(pattern, dtype=float))
                    phases = np.exp(-1j * theta * energies)
                    physical += np.outer(phases, phases.conj()) / 2**n

                attenuation = math.cos(2 * theta)
                one_qubit = np.array(
                    [[1, attenuation], [attenuation, 1]], dtype=complex
                )
                center = np.exp(-1j * theta * g0 * z.sum(axis=1))
                predicted = tensor_power(one_qubit, n)
                predicted *= np.outer(center, center.conj())
                c_theta = (1 + abs(attenuation)) ** n

                matrix_error = float(np.max(np.abs(physical - predicted)))
                eigenvalues = np.linalg.eigvalsh(physical)
                eigenvalue_error = abs(float(eigenvalues[-1]) - c_theta)
                cp_eigenvalues = np.linalg.eigvalsh(
                    c_theta * np.eye(2**n) - physical
                )
                cp_min = float(cp_eigenvalues[0])

                require(matrix_error <= TOLERANCE,
                        f"Physical sign average mismatch: n={n}, theta={theta}")
                require(eigenvalue_error <= TOLERANCE,
                        f"Schur eigenvalue mismatch: n={n}, theta={theta}")
                require(cp_min >= -TOLERANCE,
                        f"CP comparison failed: n={n}, theta={theta}")

                complete_error = None
                if theta == math.pi / 4:
                    complete_error = float(
                        np.max(np.abs(physical - np.eye(2**n)))
                    )
                    require(complete_error <= TOLERANCE,
                            "The claimed complete-dephasing phase is incorrect")
                    max_complete_dephasing_error = max(
                        max_complete_dephasing_error, complete_error
                    )
                max_matrix_error = max(max_matrix_error, matrix_error)
                max_eigenvalue_error = max(
                    max_eigenvalue_error, eigenvalue_error
                )
                minimum_cp_eigenvalue = min(minimum_cp_eigenvalue, cp_min)
                cases.append({
                    "n": n,
                    "g0": g0,
                    "delta": 1,
                    "theta": clean_float(theta),
                    "attenuation": clean_float(attenuation),
                    "physical_average_error": clean_float(matrix_error),
                    "schur_top_eigenvalue_error": clean_float(eigenvalue_error),
                    "cp_difference_min_eigenvalue": clean_float(cp_min),
                    "complete_dephasing_error": (
                        None if complete_error is None
                        else clean_float(complete_error)
                    ),
                })
    return {
        "case_count": len(cases),
        "maximum_physical_average_error": clean_float(max_matrix_error),
        "maximum_top_eigenvalue_error": clean_float(max_eigenvalue_error),
        "minimum_cp_difference_eigenvalue": clean_float(minimum_cp_eigenvalue),
        "maximum_complete_dephasing_error": clean_float(
            max_complete_dephasing_error
        ),
        "cases": cases,
    }


def check_pair_codes() -> dict[str, Any]:
    """Enumerate every sign pattern, advice value, and logical basis state."""
    cases = []
    total_energy_checks = 0
    for logical_qubits in range(1, 5):
        for idle_sites in (0, 1):
            n = 2 * logical_qubits + idle_sites
            parity_counts: Counter[tuple[int, ...]] = Counter()
            energy_checks = 0
            for pattern in signs(n):
                parity = tuple(
                    pattern[2 * j] * pattern[2 * j + 1]
                    for j in range(logical_qubits)
                )
                parity_counts[parity] += 1
                for logical_word in bitstrings(logical_qubits):
                    physical_word = []
                    for p, logical_bit in zip(parity, logical_word):
                        if p == 1:
                            pair = (logical_bit, 1 - logical_bit)
                        else:
                            pair = (logical_bit, logical_bit)
                        physical_word.extend(pair)
                    physical_word.extend([0] * idle_sites)
                    energy = sum(
                        s * (1 - 2 * bit)
                        for s, bit in zip(pattern, physical_word)
                    )
                    expected_energy = sum(pattern[2 * logical_qubits:])
                    require(energy == expected_energy,
                            "Parity-selected code is not a generator eigenspace")
                    energy_checks += 1
            expected_count = 2 ** (n - logical_qubits)
            require(len(parity_counts) == 2**logical_qubits,
                    "Not all parity transcripts occur")
            require(set(parity_counts.values()) == {expected_count},
                    "Pair parities are not uniform independent bits")
            cases.append({
                "physical_qubits": n,
                "logical_qubits": logical_qubits,
                "idle_sites": idle_sites,
                "sign_patterns": 2**n,
                "calibration_values": len(parity_counts),
                "energy_checks": energy_checks,
                "common_energy_verified_exactly": True,
            })
            total_energy_checks += energy_checks
    return {
        "total_exact_energy_checks": total_energy_checks,
        "cases": cases,
    }


def check_positive_couplings() -> dict[str, Any]:
    """Test constant weight separately in the two actual coupling classes."""
    cases = []
    for n in range(1, 9):
        dimensions = []
        energy_checks = 0
        all_words = tuple(bitstrings(n))
        for pattern in signs(n):
            plus = tuple(j for j, s in enumerate(pattern) if s == 1)
            minus = tuple(j for j, s in enumerate(pattern) if s == -1)
            target_plus = len(plus) // 2
            target_minus = len(minus) // 2
            codewords = [
                word for word in all_words
                if sum(word[j] for j in plus) == target_plus
                and sum(word[j] for j in minus) == target_minus
            ]
            expected_dimension = (
                math.comb(len(plus), target_plus)
                * math.comb(len(minus), target_minus)
            )
            require(len(codewords) == expected_dimension,
                    "Positive-coupling class code has the wrong dimension")
            expected_energy = (
                3 * (len(plus) - 2 * target_plus)
                + (len(minus) - 2 * target_minus)
            )
            for word in codewords:
                energy = sum(
                    (2 + s) * (1 - 2 * bit)
                    for s, bit in zip(pattern, word)
                )
                require(energy == expected_energy,
                        "Positive-coupling class code is not an eigenspace")
                energy_checks += 1
            dimensions.append(len(codewords))
        minimum_dimension = min(dimensions)
        require(minimum_dimension * (n + 1) ** 2 >= 2**n,
                "The uniform positive-coupling dimension bound failed")
        cases.append({
            "physical_qubits": n,
            "coupling_values": [1, 3],
            "sign_patterns": 2**n,
            "minimum_code_dimension": minimum_dimension,
            "maximum_code_dimension": max(dimensions),
            "exact_energy_checks": energy_checks,
        })
    return {"cases": cases}


def check_conditional_information() -> dict[str, Any]:
    """Enumerate the masked transcript C=S xor K and compute both costs."""
    n = 3
    count = Counter(
        (s, k, s ^ k)
        for s in range(2**n)
        for k in range(2**n)
    )
    total = sum(count.values())
    sk = Counter()
    ck = Counter()
    sc = Counter()
    s_count = Counter()
    c_count = Counter()
    k_count = Counter()
    for (s, k, c), weight in count.items():
        sk[s, k] += weight
        ck[c, k] += weight
        sc[s, c] += weight
        s_count[s] += weight
        c_count[c] += weight
        k_count[k] += weight

    unconditional = sum(
        weight / total * math.log2(
            weight * total / (s_count[s] * c_count[c])
        )
        for (s, c), weight in sc.items()
    )
    conditional = sum(
        weight / total * math.log2(
            weight * k_count[k] / (sk[s, k] * ck[c, k])
        )
        for (s, k, c), weight in count.items()
    )
    require(abs(unconditional) <= TOLERANCE,
            "Masked transcript is not independent of the unconditioned profile")
    require(abs(conditional - n) <= TOLERANCE,
            "Conditional calibration information does not recover the key cost")
    return {
        "profile_bits": n,
        "enumerated_profile_key_pairs": total,
        "I_S_C_bits": clean_float(unconditional),
        "I_S_C_given_K_bits": clean_float(conditional),
    }


def normal_interval_probability(lower: float, upper: float) -> float:
    """P(lower < Z < upper), with stable subtraction in either Gaussian tail."""
    root_two = math.sqrt(2)
    if lower >= 0:
        return 0.5 * (
            math.erfc(lower / root_two) - math.erfc(upper / root_two)
        )
    if upper <= 0:
        return 0.5 * (
            math.erfc(-upper / root_two) - math.erfc(-lower / root_two)
        )
    return 0.5 * (
        math.erf(upper / root_two) - math.erf(lower / root_two)
    )


def gaussian_outage_mass(rate_gap: float, variance: float) -> tuple[float, int]:
    """Sum exact Gaussian interval masses, with an explicit tail truncation."""
    require(0 < rate_gap < 1, "Outage gap must lie strictly between zero and one")
    require(variance > 0, "Gaussian variance must be positive")
    a = 2**rate_gap - 1
    half_width = 0.5 * math.asin(a)
    period = math.pi / 2
    center_zero = math.pi / 4
    sigma = math.sqrt(variance)
    cutoff = 12 * sigma
    first = math.ceil((-cutoff - half_width - center_zero) / period)
    last = math.floor((cutoff + half_width - center_zero) / period)
    masses = []
    for index in range(first, last + 1):
        center = center_zero + index * period
        masses.append(normal_interval_probability(
            (center - half_width) / sigma,
            (center + half_width) / sigma,
        ))
    return math.fsum(masses), len(masses)


def check_outage_mass() -> dict[str, Any]:
    """Quantify the rare-tail event that drives the hard-bit rate converse."""
    gap = 0.5
    a = 2**gap - 1
    large_variance_limit = 2 * math.asin(a) / math.pi
    tail_bound = math.erfc(12 / math.sqrt(2))
    cases = []
    for variance in (0.01, 0.1, 1.0, 10.0):
        mass, interval_count = gaussian_outage_mass(gap, variance)
        require(0 < mass < 1, "Outage mass lies outside the probability range")

        # An independent periodic Fourier representation is well-conditioned
        # at these larger variances.  Small-variance cancellation is avoided.
        fourier_error = None
        if variance >= 0.1:
            half_width = 0.5 * math.asin(a)
            correction = math.fsum(
                ((-1) ** index)
                * math.exp(-8 * index * index * variance)
                * math.sin(4 * index * half_width)
                / index
                for index in range(1, 101)
            )
            fourier = large_variance_limit + (2 / math.pi) * correction
            fourier_error = abs(mass - fourier)
            require(fourier_error <= OUTAGE_TOLERANCE,
                    "Gaussian interval and wrapped-Fourier outage masses differ")
        if variance == 10.0:
            require(abs(mass - large_variance_limit) <= OUTAGE_TOLERANCE,
                    "The large-variance outage mass misses its uniform limit")
        cases.append({
            "phase_variance_t_delta_squared": variance,
            "outage_probability": clean_float(mass),
            "included_intervals": interval_count,
            "interval_fourier_discrepancy": (
                None if fourier_error is None
                else clean_float(fourier_error)
            ),
        })
    return {
        "rate_gap_R_minus_b": gap,
        "cosine_threshold": clean_float(a),
        "interval_centers": "pi/4 + j*pi/2",
        "interval_half_width": clean_float(0.5 * math.asin(a)),
        "omitted_gaussian_tail_upper_bound": float(f"{tail_bound:.14g}"),
        "large_variance_limit": clean_float(large_variance_limit),
        "cases": cases,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        help="Write the deterministic JSON report to this path.",
    )
    args = parser.parse_args()
    report = {
        "schema_version": 1,
        "scope": (
            "Finite physical-sign, code-eigenspace, conditional-information, "
            "and Gaussian-outage checks; not an all-size theorem proof."
        ),
        "arithmetic": {
            "matrix_backend": "numpy",
            "matrix_precision": "complex128 / float64",
            "matrix_tolerance": TOLERANCE,
            "outage_comparison_tolerance": OUTAGE_TOLERANCE,
            "parity_and_class_code_energies": "exact integers",
        },
        "sign_average_and_cp_comparison": check_sign_average(),
        "pair_parity_codes": check_pair_codes(),
        "positive_coupling_class_codes": check_positive_couplings(),
        "conditional_calibration_information": check_conditional_information(),
        "gaussian_outage_mass": check_outage_mass(),
        "all_checks_passed": True,
    }
    encoded = json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if args.output is None:
        print(encoded, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
        print(f"Calibration checks passed; report written to {args.output}")
        for row in report["gaussian_outage_mass"]["cases"]:
            print(
                f"v={row['phase_variance_t_delta_squared']:g}: "
                f"outage={row['outage_probability']:.12g}"
            )


if __name__ == "__main__":
    main()
