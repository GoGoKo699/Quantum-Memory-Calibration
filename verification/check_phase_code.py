#!/usr/bin/env python3
"""Check a correlated-noise instance of the passive lifetime construction.

Seven dual-rail inner blocks use a binary [7,4,3] Hamming code in the Hadamard
basis.  A single Gaussian phase drives every block.  Deterministic Gauss-Hermite
quadrature computes the joint phase-error distribution after independent X
randomization.  Every error pattern is passed through the actual Hamming
syndrome recovery; independent-noise probabilities are used only for comparison.

This finite example checks the construction and its first-moment error bound.
It does not establish an all-size coding theorem or the all-code converse.

Run from the repository root with NumPy 2.3.5:
    python verification/check_phase_code.py \
        --output verification/phase_code_results.json
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import numpy as np


TOLERANCE = 2e-13
BLOCKS = 7


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean_float(value: float) -> float:
    if value == 0:
        return 0.0
    return float(f"{value:.14g}")


def bits_of(mask: int, length: int) -> list[int]:
    """Bit j labels physical block j; integer masks are little endian."""
    return [(mask >> j) & 1 for j in range(length)]


def syndrome(mask: int) -> int:
    """The parity-check columns are the nonzero three-bit labels 1,...,7."""
    result = 0
    for j in range(BLOCKS):
        if mask & (1 << j):
            result ^= j + 1
    return result


def hamming_code() -> tuple[dict[int, int], np.ndarray]:
    """Return codeword-to-logical-label map for a linear systematic encoder."""
    free_positions = (2, 4, 5, 6)
    pivot_positions = (0, 1, 3)
    lookup: dict[int, int] = {}
    for logical in range(16):
        codeword = sum(
            ((logical >> j) & 1) << position
            for j, position in enumerate(free_positions)
        )
        free_syndrome = syndrome(codeword)
        for row, position in enumerate(pivot_positions):
            codeword |= ((free_syndrome >> row) & 1) << position
        require(syndrome(codeword) == 0, "Encoder missed the Hamming kernel")
        lookup[codeword] = logical

    require(len(lookup) == 16, "The encoder does not contain 16 codewords")
    require(min(word.bit_count() for word in lookup if word) == 3,
            "The claimed [7,4,3] code distance is incorrect")
    parity_check = np.array(
        [[((j + 1) >> row) & 1 for j in range(BLOCKS)]
         for row in range(3)], dtype=int,
    )
    return lookup, parity_check


def gaussian_phase_distribution(
    mismatches: np.ndarray, time: float, order: int, patterns: np.ndarray
) -> np.ndarray:
    """Integrate p(z|theta)=product sin^2/cos^2 using one common theta."""
    nodes, weights = np.polynomial.hermite.hermgauss(order)
    phases = math.sqrt(2 * time) * nodes
    conditional_flip = np.sin(phases[:, None] * mismatches[None, :]) ** 2
    likelihood = np.prod(
        np.where(
            patterns[None, :, :] == 1,
            conditional_flip[:, None, :],
            1 - conditional_flip[:, None, :],
        ), axis=2,
    )
    return (weights / math.sqrt(math.pi)) @ likelihood


def run_check() -> dict[str, Any]:
    g0 = 0.7
    delta = 0.2
    time = 0.35
    mismatch_fractions = np.array((1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4))
    first_couplings = g0 + delta * mismatch_fractions
    second_couplings = g0 - delta * mismatch_fractions
    couplings = np.column_stack((first_couplings, second_couplings))
    mismatches = first_couplings - second_couplings
    require(bool(np.all(couplings >= g0 - delta - TOLERANCE))
            and bool(np.all(couplings <= g0 + delta + TOLERANCE)),
            "A physical coupling lies outside the uncertainty interval")

    patterns = np.array([bits_of(z, BLOCKS) for z in range(2**BLOCKS)])
    weights = patterns.sum(axis=1)
    probability = gaussian_phase_distribution(mismatches, time, 64, patterns)
    refined = gaussian_phase_distribution(mismatches, time, 128, patterns)
    quadrature_change = float(np.max(np.abs(probability - refined)))
    require(quadrature_change <= TOLERANCE, "Gaussian quadrature is not stable")
    require(abs(float(probability.sum()) - 1) <= TOLERANCE,
            "The correlated phase-error probabilities do not sum to one")
    require(float(probability.min()) >= -TOLERANCE,
            "A phase-error probability is negative")

    marginals = probability @ patterns
    analytic_marginals = (1 - np.exp(-2 * time * mismatches**2)) / 2
    marginal_error = float(np.max(np.abs(marginals - analytic_marginals)))
    require(marginal_error <= TOLERANCE, "Gaussian marginal identity failed")
    mean_weight = float(probability @ weights)
    analytic_mean = float(analytic_marginals.sum())
    require(abs(mean_weight - analytic_mean) <= TOLERANCE,
            "The integrated mean weight differs from the exact Gaussian mean")

    lookup, parity_check = hamming_code()
    logical_probability = np.zeros(16)
    for error, mass in enumerate(probability):
        value = syndrome(error)
        correction = 0 if value == 0 else 1 << (value - 1)
        residual = error ^ correction
        require(residual in lookup, "Recovery residual is not a codeword")
        logical_error = lookup[residual]
        if error.bit_count() <= 1:
            require(logical_error == 0, "Recovery failed on a correctable error")
        logical_probability[logical_error] += mass

    failure = float(probability[weights > 1].sum())
    logical_error_mass = float(logical_probability[1:].sum())
    require(abs(failure - logical_error_mass) <= TOLERANCE,
            "Enumerated syndrome recovery and error-weight accounting differ")
    require(abs(float(logical_probability.sum()) - 1) <= TOLERANCE,
            "The recovered logical Pauli probabilities do not sum to one")

    coefficient_bound = time * float(np.square(mismatches).sum())
    uniform_bound = BLOCKS * 4 * time * delta**2
    require(failure <= mean_weight / 2 + TOLERANCE,
            "The integer-threshold Markov bound failed")
    require(mean_weight <= coefficient_bound + TOLERANCE,
            "The coefficient-specific marginal bound failed")
    require(coefficient_bound <= uniform_bound + TOLERANCE,
            "The allowed-interval bound failed")

    independent_probability = np.prod(
        np.where(patterns == 1, analytic_marginals, 1 - analytic_marginals),
        axis=1,
    )
    independent_failure = float(independent_probability[weights > 1].sum())
    covariance = patterns.T @ (probability[:, None] * patterns)
    covariance -= np.outer(marginals, marginals)
    distribution_difference = float(
        np.max(np.abs(probability - independent_probability))
    )
    require(distribution_difference > 1e-6,
            "This chosen example did not exhibit correlated phase errors")

    return {
        "schema_version": 1,
        "scope": (
            "One finite correlated-noise construction with exhaustive Hamming "
            "syndrome recovery; not an all-size coding proof or converse."
        ),
        "arithmetic": {
            "backend": "numpy",
            "numpy_version": np.__version__,
            "precision": "float64",
            "tolerance": TOLERANCE,
            "quadrature_orders": [64, 128],
            "maximum_quadrature_probability_change": clean_float(quadrature_change),
            "maximum_analytic_marginal_error": clean_float(marginal_error),
        },
        "physical_register": {
            "physical_qubits": 14,
            "dual_rail_blocks": BLOCKS,
            "g0": g0,
            "delta": delta,
            "time_and_gaussian_phase_variance": time,
            "dimensionless_time_t_delta_squared": clean_float(time * delta**2),
            "coupling_pairs": [[clean_float(x) for x in row] for row in couplings],
            "logical_Z_generator_coefficients": [clean_float(x) for x in mismatches],
        },
        "phase_code": {
            "classical_code_parameters": [7, 4, 3],
            "stored_logical_qubits": 4,
            "correctable_phase_error_weight": 1,
            "parity_check_matrix": parity_check.tolist(),
            "error_patterns_checked": len(probability),
            "recovery_type": "Hamming syndrome, followed by its single-bit correction",
            "key": "7 independent logical X-randomization bits",
        },
        "correlated_noise": {
            "phase_error_marginals": [clean_float(x) for x in marginals],
            "mean_weight": clean_float(mean_weight),
            "analytic_mean_weight": clean_float(analytic_mean),
            "failure_probability_weight_above_one": clean_float(failure),
            "first_two_error_indicators_covariance": clean_float(covariance[0, 1]),
            "logical_half_diamond_error": clean_float(logical_error_mass),
            "logical_X_error_probabilities": {
                format(mask, "04b"): clean_float(mass)
                for mask, mass in enumerate(logical_probability)
            },
        },
        "bounds": {
            "integer_threshold_markov_mean_weight_over_two": clean_float(mean_weight / 2),
            "coarse_markov_mean_weight": clean_float(mean_weight),
            "coefficient_specific_t_sum_mismatch_squared": clean_float(coefficient_bound),
            "uniform_7_times_4_t_delta_squared": clean_float(uniform_bound),
        },
        "independent_noise_with_same_marginals": {
            "failure_probability_weight_above_one": clean_float(independent_failure),
            "correlated_minus_independent_failure": clean_float(failure - independent_failure),
            "maximum_joint_distribution_difference": clean_float(distribution_difference),
        },
        "logical_error_interpretation": (
            "After recovery this is a logical Pauli-X mixture.  Its half-diamond "
            "distance from identity equals its total nonidentity mass: the "
            "maximally entangled input distinguishes its orthogonal Pauli branches."
        ),
        "all_checks_passed": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write deterministic JSON to this path.")
    args = parser.parse_args()
    report = run_check()
    encoded = json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if args.output is None:
        print(encoded, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
        print(f"Phase-code checks passed; report written to {args.output}")
        print(
            "Correlated failure="
            f"{report['correlated_noise']['failure_probability_weight_above_one']:.12g}; "
            "independent comparison="
            f"{report['independent_noise_with_same_marginals']['failure_probability_weight_above_one']:.12g}"
        )


if __name__ == "__main__":
    main()
