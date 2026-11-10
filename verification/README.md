# Reproducing the finite checks

The analytic claims are proved in [science/](../science/README.md). The programs here reconstruct small physical instances, check exact code properties, and evaluate the examples used in the interpretation. They do not establish an all-size theorem by numerical extrapolation.

## Run

Use Python 3.10 or later and the pinned NumPy dependency. From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_calibration.py --output verification/calibration_results.json
python verification/check_phase_code.py --output verification/phase_code_results.json
```

Both programs are deterministic and use no Monte Carlo sampling. Their optional `--output` argument writes a compact JSON report. Omitting it prints the report. A failed check raises an exception and returns a nonzero exit status. The committed reports were generated with NumPy 2.3.5.

## Calibration checks

[check_calibration.py](check_calibration.py) covers:

- Direct averages of the physical unitaries for signed and two-positive-value profiles, for up to four carriers. It compares them with the derived Schur channel and tests the positive-semidefinite difference used in the completely positive domination argument. The cases include positive and negative cosine attenuation.
- Exact eigenvalue checks for the parity-transcript pair code through four logical qubits, including an unused physical site.
- Exact eigenvalue checks for the two-class constant-weight construction through eight carriers.
- Enumeration of the masked transcript example, checking that information is charged conditional on the free key.
- The Gaussian unfavorable-phase probability at rate deficit one half. Interval summation is cross-checked with a wrapped-Gaussian Fourier calculation where stable.

The [committed report](calibration_results.json) contains 48 physical-average comparisons, 14,040 parity-code checks, and 12,256 two-class checks. The largest physical-average matrix discrepancy is approximately $4.72\times10^{-16}$; the most negative numerical CP-comparison eigenvalue is approximately $-5.28\times10^{-15}$, within the $2\times10^{-12}$ tolerance. These small negative floating-point residues are not treated as exact negative eigenvalues.

The error-floor probabilities are approximately $1.0741\times10^{-8}$, $0.0689644$, $0.271726$, and $0.271887$ at $t\delta^2=0.01,0.1,1,10$. The interval calculation includes a Gaussian tail bound below $3.6\times10^{-33}$. These values support the rare-event qualification in [Interpretation](../science/interpretation.md#two-results-with-different-error-limits); they are not optimal finite-block errors.

## Correlated phase-code check

[check_phase_code.py](check_phase_code.py) constructs seven two-qubit, fixed-magnetization blocks. It enumerates all 128 phase-error patterns, passes each through a classical $[7,4,3]$ Hamming-code syndrome recovery in the Hadamard basis, and computes the resulting logical channel. The program verifies code dimension and distance, all correctable patterns, normalization, exact Gaussian marginals, and the recovery/error-weight identity.

One Gaussian phase drives all seven blocks. Gauss–Hermite quadrature of orders 64 and 128 agrees to approximately $1.11\times10^{-16}$. The [committed report](phase_code_results.json) gives correlated logical failure $0.0319897475$, versus $0.0150189610$ for the independent distribution having the same one-block marginals. The former satisfies the integer-threshold Markov bound $0.100036223$.

This example checks the part of the [lifetime construction](../science/lifetime.md) that must work with correlated block errors. The separate independent-noise calculation is a comparison, not a model substituted into the proof. This is a code for phase errors only, not a quantum code correcting every single-qubit error.

## Hosted mathematics

The separate [hosted-mathematics check](hosted_math/README.md) compares every mathematical expression in the proposed Git commit with the actual GitHub page at wide and narrow viewport sizes. It retains screenshots and a source-bound structural report. This detects presentation defects that local TeX compilation can miss; the captured screenshots still require visual inspection.

## What the checks do not certify

Finite enumeration does not replace the relative-entropy proof, the arbitrary-code converse, or the asymptotic coding argument. Floating-point checks are not exact proofs of complete positivity. The results also do not certify a physical device, pulse implementation, or decoder runtime. The scientific assumptions and proofs remain the authoritative statements.

[Repository overview](../README.md) · [Scientific account](../science/README.md)
