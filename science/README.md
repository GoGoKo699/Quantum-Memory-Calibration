# Scientific account

The question is whether a common noise field provides an accessible quantum memory when its fixed spatial coupling profile is not fully known. The account separates the operational interface, the continuous-uncertainty lifetime theorem, the discrete information frontier, and the supplied-profile comparison.

| Page | Role in the argument |
|---|---|
| [Model](model.md) | Defines the common Gaussian field, passive endpoint protocol, classical calibration transcript, counted quantum systems, worst-profile error, and two information budgets. |
| [Continuous coupling uncertainty](lifetime.md) | Proves dimension-independent positive-rate lifetime at fixed uncertainty, with explicit upper and lower constants; derives advice requirements for diverging storage times. |
| [Two-value calibration frontier](calibration_rate.md) | Establishes the hard-alphabet and mutual-information converses, the exact asymptotic rate, finite exact-code examples, and general comparison lemmas. |
| [Memory with supplied couplings](calibrated_memory.md) | Proves the inherited spectral-occupancy baseline and a finite-precision calibration construction, and identifies the unresolved continuous-cost gap. |
| [Interpretation and boundaries](interpretation.md) | Connects the results, quantifies the rare-event qualification, explains the correlated-noise example, and exhibits the change caused by during-storage control. |

## Proof dependencies

The common converse ingredient is an entanglement-breaking benchmark. After an appropriate profile average at a fixed Gaussian phase, a Schur-channel comparison bounds the channel by a scalar multiple of complete dephasing. Complete dephasing destroys reference entanglement even when the encoder retains an arbitrary classical record.

For interval uncertainty, the scalar is governed by a sinc attenuation. Its decay gives the lifetime upper bound. The matching construction first removes the known collective component inside fixed-magnetization blocks, then randomizes the remaining diagonal channel into correlated phase errors and corrects a bounded fraction of them. Its probability estimate uses the first moment, so it does not assume independence between blocks.

For two coupling values, the scalar is governed by a cosine attenuation. A hard transcript budget permits a union bound over codes. A conditional information budget instead permits a relative-entropy comparison with a decorrelated reference experiment. Intervals of unfavorable Gaussian phases have positive probability, giving an error floor above the calibration frontier. Revealing selected coupling classes and encoding into their exact eigenspaces attains the frontier.

The generic information comparison is proved once in [the calibration appendix](calibration_rate.md#appendix-b-a-calibration-comparison-lemma) and used in the continuous-profile analysis. The supplied-spectrum argument is logically independent of those converses: it establishes what becomes possible when the endpoint code may depend on the profile.

## Attribution and verification

[Related work](../references/related_work.md) distinguishes the contribution from supplied-profile noise-adapted coding, compound and averaged channels, outage, and side-information-assisted correction. It credits the inherited Schur comparison and spectral baseline. The [source record](../references/source_evidence.md) states which primary texts were inspected and one remaining full-text access limitation.

The [verification guide](../verification/README.md) connects each finite check to its scientific purpose. These computations verify examples and algebra; they do not replace the analytic arguments or constitute an external review.

[Repository overview](../README.md)
