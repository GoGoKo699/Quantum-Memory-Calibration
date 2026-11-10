# Quantum Memory Calibration

How much information about a device is needed to use its common noise field as a quantum memory?

This repository studies a register coupled to one Gaussian dephasing field through fixed, spatially unequal coefficients. When those coefficients are supplied, a large protected subspace can be chosen from the known spectrum. When each coefficient is independently uncertain within a fixed interval, one code must instead work for every allowed profile. That information constraint changes the achievable storage time even though the bath still contains only one noise field.

## Main results

For $`n`$ physical qubits, the coupling operator and storage channel are

```math
A_{\boldsymbol g}=\sum_{j=1}^n g_jZ_j,
\qquad
\Phi_{\boldsymbol g,t}
=\mathbb E_{\Theta\sim N(0,t)}\mathrm{Ad}_{e^{-i\Theta A_{\boldsymbol g}}}.
```

The register is passive during the storage interval. Arbitrary joint encoding and recovery are allowed at its endpoints, including classical records and independent shared randomness. Every quantum system retained across the interval counts among the noisy carriers. Calibration supplies a classical description of the fixed coupling profile before the payload arrives; it does not reveal the subsequent noise realization. [The model](science/model.md) specifies these resources and the worst-profile half-diamond error criterion.

**Fixed-error lifetime under interval uncertainty.** If every $`g_j`$ is unknown in $`[g_0-\delta,g_0+\delta]`$, then for any fixed rate $`0\lt R<1`$ and error tolerance $`0<\epsilon<1`$,

```math
T_{R,\epsilon}^{(n)}(\delta)=\Theta_{R,\epsilon}(\delta^{-2})
```

for all sufficiently large $`n`$, uniformly in $`g_0`$ and $`\delta>0`$. Increasing the register size cannot increase this uncalibrated positive-rate lifetime beyond a constant at fixed uncertainty. The upper bound covers every allowed endpoint protocol; a construction using fixed-magnetization inner blocks and classical phase-error coding proves the matching scaling. [Statement and proof](science/lifetime.md).

**Exact calibration-rate frontier for two coupling values.** For $`g_j=g_0+\delta s_j`$, $`s_j\in\{-1,+1\}`$, and noise strength $`t\delta^2`$ bounded away from zero, the reliable storage rate is

```math
Q_{\mathrm{cal}}(b)=\min\{b,1\}.
```

Here $`b`$ is the asymptotic number of calibration bits per carrier, measured either by a hard transcript alphabet or by conditional mutual information under the uniform sign prior. The storage guarantee remains uniform over profiles. The converse gives a nonzero error floor above the frontier; exact decoherence-free codes attain it asymptotically. The theorem also covers two known positive coupling values. [Statement, information accounting, and constructions](science/calibration_rate.md).

**Supplied-profile comparison.** For known bounded couplings, spectral occupancy gives

```math
D\ge\frac{2^n}{1+nG\sqrt{t/\epsilon}},
\qquad |g_j|\le G,
```

at half-diamond error at most $`\epsilon`$. The rate therefore approaches one for subexponential storage times and fixed error. This calibrated baseline is inherited from [Quantum-Spectral-Memory](https://github.com/GoGoKo699/Quantum-Spectral-Memory/blob/ee5dc0e5529c7775bfaeabb2a5e744c51eb9431d/science/spectral_law.md). An explicit rounding construction here supplies a finite-description counterpart, using $`O(n\log n)`$ calibration bits for polynomial times and inverse-polynomial error. [Proof and remaining cost gap](science/calibrated_memory.md).

The scientific consequence is a distinction between a small number of noise fields and access to their protected subspaces. Independent uncertainty in an extensive spatial profile can prevent scalable passive storage even when the corresponding supplied-profile device supports it.

## Reading routes

| Question | Start here |
|---|---|
| How can I build up the ideas from Watrous's textbook? | [Learning route](learning/README.md), [source bridge](learning/watrous_bridge.md), and [30 milestones](learning/milestones.md) |
| What does the result mean physically, and which limit matters? | [Interpretation and boundaries](science/interpretation.md) |
| What resources and errors are being counted? | [Model](science/model.md) |
| Why does uncalibrated lifetime stop growing with register size? | [Continuous coupling uncertainty](science/lifetime.md) |
| Why does one calibration bit per carrier buy one asymptotic logical qubit per carrier? | [Two-value calibration frontier](science/calibration_rate.md) |
| How does supplied or finite-precision calibration restore long storage? | [Memory with supplied couplings](science/calibrated_memory.md) |
| Which ideas are inherited, and how do nearby results differ? | [Related work](references/related_work.md) and [primary-source record](references/source_evidence.md) |
| What can be reproduced computationally? | [Verification guide](verification/README.md) |

The [science map](science/README.md) gives proof dependencies. [references.bib](references.bib) supplies the bibliography, and [llms.txt](llms.txt) maps reader questions to the authoritative files.

The learning route uses one educational anchor: John Watrous, *The Theory of Quantum Information* (2018). Its 11 background milestones and 19 narrative milestones connect channel and information foundations to the physical storage problem, the constructions, and the limits of the results.

## Scope and reproducibility

The results price retained classical calibration information, not the experiments needed to acquire it. They allow ideal endpoint operations and do not establish efficient code compilation or decoding. The continuous-profile information cost is bounded but not exactly characterized. Allowing ideal operations during storage changes the problem: an explicit toggling sequence removes unknown sign correlations and permits positive-rate storage without calibration. These boundaries are developed in [Interpretation](science/interpretation.md).

Two deterministic Python programs check finite physical sign averages, complete-positivity comparisons, exact code eigenspaces, information accounting, Gaussian error-floor probabilities, and an actual seven-block recovery under correlated noise. They support the calculations and examples; the all-size statements are proved in the scientific pages. See [Verification](verification/README.md) for commands, pinned dependencies, results, and numerical tolerances.

## Purpose

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The repository uses the [MIT license](LICENSE).
