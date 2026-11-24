#!/usr/bin/env python3
"""Check the finite ingredients of continuous calibration.

Run from the repository root:
    python verification/check_continuous_calibration.py \
        --output verification/continuous_calibration_results.json

The checks use exact integer and rational arithmetic where possible, and
deterministic quadrature for continuous distributions.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations, product
import json
import math
from pathlib import Path

import numpy as np

from check_calibration import TOLERANCE, bitstrings, clean_float, require


def affine_binary_rank(labels: tuple[int, ...]) -> int:
    reference = labels[0]
    pivots: dict[int, int] = {}
    for label in labels[1:]:
        difference = label ^ reference
        while difference:
            position = difference.bit_length()
            if position not in pivots:
                pivots[position] = difference
                break
            difference ^= pivots[position]
    return len(pivots)


def check_binary_occupancy() -> dict:
    """An odd affine minor is also nonzero over the reals."""
    labels = tuple(range(16))
    checked = 0
    for size in range(1, len(labels) + 1):
        for subset in combinations(labels, size):
            rank = affine_binary_rank(subset)
            require(size <= 2**rank, f"Affine occupancy failed for {subset}")
            checked += 1
    return {"four_cube_nonempty_subsets": checked}


def check_uniform_gram() -> dict:
    """Reconstruct a two-site, three-replica profile average from unitaries."""
    theta = np.array((0.34, 1.42, -0.78))
    delta = 0.51
    center = 0.7
    z = 1 - 2 * np.array(list(bitstrings(len(theta))))
    frequencies = z @ theta
    difference = frequencies[:, None] - frequencies[None, :]
    site = np.sinc(delta * difference / math.pi) * np.exp(-1j * center * difference)
    predicted = np.kron(site, site)

    nodes, weights = np.polynomial.legendre.leggauss(20)
    observed = np.zeros_like(predicted)
    for i, j in product(range(len(nodes)), repeat=2):
        first = np.exp(-1j * (center + delta * nodes[i]) * frequencies)
        second = np.exp(-1j * (center + delta * nodes[j]) * frequencies)
        phases = np.kron(first, second)
        observed += weights[i] * weights[j] * np.outer(phases, phases.conj()) / 4
    error = float(np.max(np.abs(observed - predicted)))
    require(error <= TOLERANCE, "Direct profile integral differs from tensor Gram")

    minimum_psd_eigenvalue = 0.0
    cases = []
    density_ratio = math.sqrt(math.pi / 2) * math.exp(0.5)
    for angles in [(0,) * 6, (1, 2, 4, 8, 16, 32), (0, 1, 2, 3, 5, 8),
                   (0.1, 0.4, 1.7, 2.9, 4.1, 7.2)]:
        binary = np.array(list(bitstrings(len(angles))))
        ordered = np.sort(2 * delta * (binary @ np.array(angles)))
        distances = ordered[:, None] - ordered[None, :]
        sinc = np.sinc(distances / math.pi)
        gaussian = np.exp(-distances**2 / 2)
        occupancy = int(np.max(
            np.searchsorted(ordered, ordered + 1, side="right") - np.arange(len(ordered))
        ))
        minimum = float(np.linalg.eigvalsh(density_ratio * gaussian - sinc)[0])
        norm = float(np.linalg.eigvalsh(sinc)[-1])
        bound = density_ratio * (2 + math.sqrt(2 * math.pi)) * occupancy
        require(minimum >= -TOLERANCE, "Gaussian density CP domination failed")
        require(norm <= bound + TOLERANCE, "Occupancy spectral bound failed")
        minimum_psd_eigenvalue = min(minimum_psd_eigenvalue, minimum)
        cases.append({"occupancy": occupancy, "sinc_norm": clean_float(norm),
                      "norm_bound": clean_float(bound)})

    return {
        "direct_tensor_integral_maximum_matrix_error": clean_float(error),
        "minimum_density_domination_eigenvalue": clean_float(minimum_psd_eigenvalue),
        "occupancy_cases": cases,
    }


def check_calibration_bands() -> dict:
    """Check exact rounding, support size and width in the fixed-weight sector."""
    checked = 0
    widest_ratio = Fraction(0)
    largest_dimension = 0
    for size, radius, width in product((8, 10), (1, 2, 4),
                                       (Fraction(1, 4), Fraction(3, 8), Fraction(1, 2))):
        sector = [tuple(1 - 2 * bit for bit in label) for label in bitstrings(size)
                  if sum(label) == size // 2]
        count = math.ceil(2 * size * radius / width)
        bin_width = Fraction(2 * radius, count)
        guaranteed_support = math.ceil(Fraction(len(sector), count))
        largest_dimension = max(largest_dimension, 1 << (guaranteed_support.bit_length() - 1))
        profiles = [
            tuple(Fraction(radius * (2 * j - size + 1), size - 1) for j in range(size)),
            tuple(Fraction((-1)**j * radius) for j in range(size)),
            tuple(Fraction(radius * (((j + 1)**2 % (2 * size + 1)) - size), size)
                  for j in range(size)),
        ]
        for profile in profiles:
            indices = [min(count - 1, (value + radius) // bin_width) for value in profile]
            midpoints = [-radius + (index + Fraction(1, 2)) * bin_width
                         for index in indices]
            require(all(abs(x - y) <= width / (2 * size)
                        for x, y in zip(profile, midpoints)), "Coordinate rounding exceeded")
            bands: dict[int, list[tuple[int, ...]]] = {}
            for label in sector:
                estimate = sum(g * z for g, z in zip(midpoints, label))
                cell = min(count - 1, (estimate + size * radius) // width)
                bands.setdefault(cell, []).append(label)
            chosen = bands[min(bands, key=lambda cell: (-len(bands[cell]), cell))]
            require(len(chosen) >= guaranteed_support, "Pigeonhole support guarantee failed")
            energies = [sum(g * z for g, z in zip(profile, label)) for label in chosen]
            true_width = max(energies) - min(energies)
            require(true_width <= 2 * width, "Rounded band exceeded true width bound")
            widest_ratio = max(widest_ratio, true_width / (2 * width))
            checked += 1
    return {"profiles": checked, "largest_guaranteed_dimension": largest_dimension,
            "maximum_true_width_ratio": clean_float(float(widest_ratio))}


def check_correlated_outer_recovery() -> dict:
    """Apply a distance-six phase code to three two-qubit logical blocks."""
    width = 0.2
    energies = np.array([[-0.19, -0.05, 0.08, 0.19],
                         [-0.16, -0.07, 0.04, 0.16],
                         [-0.17, -0.025, 0.055, 0.17]])
    require(float(np.max(np.ptp(energies, axis=1))) <= 2 * width,
            "A logical block lies outside the chosen spectral width")
    labels = np.array(list(bitstrings(2)))
    walsh = (-1.0) ** (labels @ labels.T)
    patterns = np.array(list(product(range(4), repeat=len(energies))))

    phase = np.exp(-1j * 0.73 * energies)
    shifted = phase[:, np.arange(4)[:, None] ^ np.arange(4)]
    masked_gram = shifted.transpose(0, 2, 1) @ shifted.conj() / 4
    pauli_probability = np.abs(phase @ walsh / 4)**2
    predicted_gram = (walsh[None, :, :] * pauli_probability[:, None, :]) @ walsh.T
    twirl_error = float(np.max(np.abs(masked_gram - predicted_gram)))
    require(twirl_error <= TOLERANCE, "Logical X masks did not produce the phase Pauli channel")

    def joint_distribution(order: int) -> np.ndarray:
        nodes, weights = np.polynomial.hermite.hermgauss(order)
        phase = np.exp(-1j * math.sqrt(2) * nodes[:, None, None] * energies)
        pauli_probability = np.abs(phase @ walsh / 4)**2
        joint_given_phase = np.prod(
            pauli_probability[:, np.arange(len(energies)), patterns], axis=2
        )
        return (weights / math.sqrt(math.pi)) @ joint_given_phase

    probability = joint_distribution(64)
    refinement_error = float(np.max(np.abs(probability - joint_distribution(128))))
    require(refinement_error <= TOLERANCE, "Gaussian integration did not stabilize")
    require(abs(float(probability.sum()) - 1) <= TOLERANCE, "Joint mass is not normalized")
    block_weights = np.count_nonzero(patterns, axis=1)
    measured_marginals = probability @ (patterns != 0)
    differences = energies[:, :, None] - energies[:, None, :]
    marginals = 1 - np.exp(-differences**2 / 2).mean(axis=(1, 2))
    require(float(np.max(np.abs(measured_marginals - marginals))) <= TOLERANCE,
            "Pauli block-error marginal did not match the exact Schur result")
    require(float(np.max(marginals)) <= width**2 + TOLERANCE,
            "A block exceeds its marginal error bound")

    logical_failure = 0.0
    for pattern, mass in zip(patterns, probability):
        error = sum(int(block) << (2 * j) for j, block in enumerate(pattern))
        # The syndrome labels the coset {error, error XOR 111111}.
        correction = min((error, error ^ 63), key=lambda word: (word.bit_count(), word))
        residual = error ^ correction
        if np.count_nonzero(pattern) <= 1:
            require(residual == 0, "Outer recovery failed on one affected block")
        if residual:
            logical_failure += float(mass)

    tail = float(probability[block_weights > 1].sum())
    first_moment_bound = float(marginals.sum() / 2)
    independent_masks = np.array(list(bitstrings(len(energies))))
    independent_probability = np.prod(
        np.where(independent_masks, marginals, 1 - marginals), axis=1
    )
    independent_failure = float(independent_probability[independent_masks.sum(axis=1) > 1].sum())
    require(logical_failure <= tail + TOLERANCE, "Recovered error exceeds block tail")
    require(tail <= first_moment_bound + TOLERANCE, "Block tail exceeds first-moment bound")
    require(abs(tail - independent_failure) >= 1e-5, "Correlations were not resolved")
    return {
        "joint_phase_error_patterns": len(patterns),
        "maximum_pauli_twirl_matrix_error": clean_float(twirl_error),
        "maximum_quadrature_change": clean_float(refinement_error),
        "logical_half_diamond_error": clean_float(logical_failure),
        "tail_above_one_block": clean_float(tail),
        "first_moment_tail_bound": clean_float(first_moment_bound),
        "independent_tail_with_same_marginals": clean_float(independent_failure),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write a JSON report to this path.")
    args = parser.parse_args()
    report = {
        "schema_version": 1,
        "numpy_version": np.__version__,
        "tolerance": TOLERANCE,
        "affine_occupancy": check_binary_occupancy(),
        "replicated_gram": check_uniform_gram(),
        "calibration_bands": check_calibration_bands(),
        "correlated_outer_recovery": check_correlated_outer_recovery(),
        "all_checks_passed": True,
    }
    encoded = json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if args.output is None:
        print(encoded, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
        print(f"Continuous calibration checks passed; report written to {args.output}")


if __name__ == "__main__":
    main()
