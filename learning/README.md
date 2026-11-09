# Learning route

The central question is how knowledge of a fixed device profile changes the quantum information that can be stored under one common dephasing field. Understanding the answer requires both a physical picture of protected subspaces and channel-level bounds that apply to every allowed endpoint code.

The educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [official author page](https://jhwatrous.github.io/books-and-courses.html) links the book and author-provided manuscript. The route below selects the foundations needed for this project; reading the entire book first is unnecessary.

## Start with the source bridge

[From Watrous to quantum memory calibration](watrous_bridge.md) identifies the relevant sections, translates notation, and supplies the steps between the textbook framework and the project's results. Its worked example shows how a short description of the coupling profile selects a protected quantum subspace. It then connects that construction to the arbitrary-code converses and the distinction between fixed-error lifetime and vanishing-error rate.

The bridge separates three roles: textbook foundations, derivations supplied in this repository, and research ingredients credited in [Related work](../references/related_work.md). The selected textbook supports the mathematics; the precise memory model and calibration theorems are stated in the scientific pages.

## Follow the 30-milestone map

The [milestone map](milestones.md) contains exactly 30 understanding targets in two phases.

| Phase | Milestones | Purpose |
|---|---|---|
| Background and preliminaries | M01–M11 | Build from states, channels, phases and reference entanglement to the information and coding tools needed to formulate the passive storage task. |
| Narrative and innovation | M12–M30 | Connect profile averaging, code selection, information comparison and protected-subspace constructions to the two global theorems, their verification and their physical boundaries. |

This allocation gives the two converse routes and their matching constructions enough space to meet in a final synthesis. Each phase moves from individual ingredients toward the complete framework. Every milestone identifies its central question, understanding target, dependencies, role in the argument, conceptual connection, and source pointers. The map is a common guide to the project rather than a record of any reader's progress.

## Return to the exact scientific statements

| When you need to resolve… | Authoritative source |
|---|---|
| Which systems, records, operations and information are counted | [Model](../science/model.md) |
| How long positive-rate storage works at a fixed error tolerance | [Continuous coupling uncertainty](../science/lifetime.md) |
| How retained calibration information determines reliable rate | [Two-value calibration frontier](../science/calibration_rate.md) |
| What supplied or finite-precision coupling data makes possible | [Memory with supplied couplings](../science/calibrated_memory.md) |
| Why the limit order, correlations and passive restriction matter | [Interpretation and boundaries](../science/interpretation.md) |
| What is checked numerically and what is proved analytically | [Verification guide](../verification/README.md) |

The distinction between a fixed error tolerance and an error required to vanish is essential throughout. So is the difference between information retained about the device and the experiments used to acquire it. The bridge and milestone map keep those distinctions aligned with the exact statements.

[Repository overview](../README.md) · [Science map](../science/README.md)
