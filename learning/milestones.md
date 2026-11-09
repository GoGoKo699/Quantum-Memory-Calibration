# Thirty milestones in quantum memory calibration

[Learning route](README.md) · [Watrous bridge](watrous_bridge.md) · [Scientific account](../science/README.md)

The project asks how information about a fixed spatial coupling profile changes the quantum information that can be stored under one common fluctuating field. This map connects the mathematical tools, the two principal results, and the assumptions that make their comparison meaningful.

The allocation is **11 background/preliminaries milestones and 19 narrative/innovation milestones**. The background joins three prerequisites: channel-level protection of reference entanglement, classical information about a device, and coherent correction of phase errors. The narrative first develops the local converse and encoding ingredients, then combines them into the exact calibration frontier, the fixed-error lifetime theorem, and the supplied-profile comparison. Its final milestones integrate the numerical examples, physical boundaries, attribution, and remaining continuous-calibration gap. This is a map of the project's understanding targets, not a catalogue of every technical lemma.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. Section and theorem numbers below refer to the author-provided text linked from the [official author page](https://jhwatrous.github.io/books-and-courses.html). The [source bridge](watrous_bridge.md#a-selective-route-through-watrous) identifies the selected readings and translates notation. Textbook pointers support the named prerequisite; the common-field model, calibration comparisons, phase-code construction, and resulting memory theorems are developed in the linked project pages.

## Phase I: Background and preliminaries

M01–M11 move from individual states and maps to the complete passive storage interface. Each milestone specifies the role its prerequisite plays in the later argument.

### M01. States, labels, and tensor factors

**Central question.** What distinguishes a classical record from a quantum system that can carry coherence across storage?

**Understanding target.** Represent a qubit register, a logical payload, an untouched reference, and a classical label in one joint state. Distinguish a classical mixture of labeled states from a coherent superposition, and use partial trace to identify what remains accessible to the decoder.

**Dependencies and story role.** Starting point. Establishes the objects whose dimensions and information are counted throughout the project.

**Conceptual connection.** Tensor factors express physical resources; a noiseless classical record cannot substitute for an uncounted persistent quantum subsystem.

**Sources.** Project: [the storage interface](../science/model.md#the-storage-interface). Watrous: [§§1.1.1–1.1.2][W1] for tensor products and partial trace, and [§2.1][W2] for registers and states.

### M02. Channels and their representations

**Central question.** How can one mathematical description include arbitrary encoding, noisy storage, measurement records, and recovery?

**Understanding target.** Interpret completely positive trace-preserving maps and their composition. Relate Kraus and Choi representations, and distinguish a trace-preserving channel from an individual completely positive instrument branch. Understand how summing branches includes all outcomes in the protocol.

**Dependencies and story role.** Requires [M01]. Replaces assumptions about a particular circuit by a channel interface that can support an arbitrary-code converse.

**Conceptual connection.** Complete positivity protects physical validity when the payload is entangled with a reference; classical outcome labels allow general instruments without silently granting a quantum bypass.

**Sources.** Project: [the storage interface](../science/model.md#the-storage-interface) and [classical records](../science/calibration_rate.md#appendix-a-classical-records-and-the-physical-carrier). Watrous: [§2.2, especially Theorem 2.22][W2].

### M03. Spectra, phases, and dephasing

**Central question.** Why can a common phase destroy coherence between some states while leaving an entire subspace unchanged?

**Understanding target.** Read the action of a Hermitian generator in its eigenbasis. Explain why a scalar generator on a code produces only a common phase, why differences of eigenvalues control relative phases, and why averaging rotations produces dephasing. Distinguish complete dephasing from partial attenuation of off-diagonal entries.

**Dependencies and story role.** Requires [M01] and [M02]. Supplies the local spectral mechanism used by both exact and approximate protected subspaces.

**Conceptual connection.** The same spectral structure permits a protected code when known and complicates universal encoding when its spatial embedding is unknown.

**Sources.** Project: [one field and a fixed profile](../science/model.md#one-field-a-fixed-spatial-profile) and [spectral-interval storage](../science/calibrated_memory.md#storage-in-a-narrow-spectral-interval). Watrous: [§1.1.3, Theorem 1.3][W1], and [§4.1.1][W4] for mixtures of unitaries and pinching.

### M04. Reference entanglement and operational error

**Central question.** What must a quantum memory preserve beyond the success of a few chosen input states?

**Understanding target.** Explain the half-diamond error criterion and why it includes an arbitrary untouched reference. Relate it to the necessary condition $F_e\ge1-\epsilon$. Keep the project's pure-target overlap convention for $F_e$ distinct from Watrous's root-fidelity convention.

**Dependencies and story role.** Requires [M01] and [M02]. Establishes the operational success criterion before any converse or construction is assessed.

**Conceptual connection.** A reference-complete channel guarantee tests quantum coherence, while one entangled test state gives a useful weaker condition for an impossibility proof.

**Sources.** Project: [error and rate](../science/model.md#error-and-rate); bridge: [notation translation](watrous_bridge.md#notation-that-must-be-translated). Watrous: [§3.1, Theorem 3.4; §3.2, Definition 3.11; §3.3.2, Definition 3.43][W3].

### M05. CP order and Schur multipliers

**Central question.** How can a matrix eigenvalue bound control a channel acting on an arbitrary entangled input?

**Understanding target.** Interpret $\mathcal A\le_{\mathrm{CP}}\mathcal B$ as complete positivity of their difference. Recognize dephasing as entrywise multiplication by a Schur matrix, use positivity of that matrix to test complete positivity, and connect its largest eigenvalue to comparison with complete dephasing.

**Dependencies and story role.** Requires [M02] and [M03]. Develops the channel comparison before applying it to unknown coupling profiles.

**Conceptual connection.** An operator inequality on the multiplier matrix remains useful after arbitrary encoding, reference extension, and recovery.

**Sources.** Project: [conditional sign average](../science/calibration_rate.md#2-conditional-sign-average) and [comparison with complete dephasing](../science/lifetime.md#comparison-with-complete-dephasing). Watrous: [§2.2, Theorem 2.22][W2], and [§4.1.3, Proposition 4.17][W4].

### M06. Separability as a memory benchmark

**Central question.** What quantitative limitation follows once the stored register has become classical?

**Understanding target.** Explain why complete dephasing leaves the reference separable from everything available to recovery, including classical encoder records. Obtain the target-overlap bound $1/D$ for a separable output and understand the related Schmidt-rank bound imposed by a finite quantum carrier.

**Dependencies and story role.** Requires [M01], [M02], and [M04]. Gives the operational meaning of the comparison channel prepared in [M05].

**Conceptual connection.** The obstruction concerns entanglement preservation, so adding classical records or a more complicated decoder cannot remove it.

**Sources.** Project: [the dephasing benchmark](../science/model.md#why-complete-dephasing-remains-a-valid-benchmark) and [Appendix A](../science/calibration_rate.md#appendix-a-classical-records-and-the-physical-carrier). Watrous: [§6.1.1, Proposition 6.15 and Example 6.16; §6.4, Exercise 6.1][W6].

### M07. Conditional classical information

**Central question.** Which information measure correctly charges a calibration record when free randomness is also available?

**Understanding target.** Distinguish the hard cost $\log_2M$ from the conditional information $I(S:C\mid K)$. Explain why a masked transcript may have $I(S:C)=0$ while revealing the entire profile together with $K$, and why rare informative outcomes separate mean information from a hard alphabet bound.

**Dependencies and story role.** Requires [M01]. Defines the two resources before they enter different converse arguments.

**Conceptual connection.** Resource accounting must include everything jointly available to the endpoints, rather than only the marginal statistics of one recorded variable.

**Sources.** Project: [two information budgets](../science/model.md#two-different-information-budgets) and [calibration costs](../science/calibration_rate.md#1-model-and-calibration-costs). Watrous: [§5.1][W5]. The continuous-transcript formulation is supplied by the project's relative-entropy comparison.

### M08. Relative entropy under processing

**Central question.** How can the statistical dependence between a profile and a transcript limit a recovered quantum state?

**Understanding target.** Interpret relative entropy and its monotonicity under a channel. Follow a classical-to-quantum preparation followed by a binary measurement, and explain why neither processing step can increase distinguishability. Recognize binary entropy as the finite-error term in the resulting fidelity inequality.

**Dependencies and story role.** Requires [M02], [M04], and [M07]. Supplies the information inequality used when counting transcript values is insufficient.

**Conceptual connection.** Comparing two distributions before encoding can bound two decoded quantum states without restricting the endpoint maps.

**Sources.** Project: [the general calibration comparison lemma](../science/calibration_rate.md#appendix-b-a-calibration-comparison-lemma). Watrous: [§5.1 and §5.2.3, especially Theorem 5.35][W5].

### M09. Pauli randomization and retained correlations

**Central question.** What does averaging controlled Pauli conjugations remove, and what can it leave intact?

**Understanding target.** Use Pauli commutation signs to see why averaging $X$ conjugations removes cross terms between different diagonal Pauli operators. Distinguish a coherent error expansion from a stochastic Pauli mixture, and distinguish that mixture from a product distribution over sites.

**Dependencies and story role.** Requires [M02], [M03], and [M07]. Establishes a reusable randomization mechanism; its common-field application is deferred to [M19].

**Conceptual connection.** Endpoint randomness can simplify the error representation while preserving classical correlations among the resulting errors.

**Sources.** Project: [the twirling derivation](../science/lifetime.md#randomization-yields-a-correlated-phase-error-distribution). Watrous: [§§4.1.1–4.1.2][W4] for mixtures of unitaries, Weyl operators, and their Fourier relations. The specific $X$-twirl calculation is supplied in the project.

### M10. Coherent correction from classical codes

**Central question.** When does a classical syndrome decoder also preserve superpositions of logical quantum states?

**Understanding target.** Explain how a classical linear code in the Hadamard basis corrects phase errors. Show why a syndrome that depends only on the error reveals no logical codeword, and connect minimum distance to exact correction of every error below a weight threshold. Keep phase-only correction distinct from correction of arbitrary Pauli errors.

**Dependencies and story role.** Requires [M02], [M04], and [M09]. Prepares the constructive counterpart to the channel converses.

**Conceptual connection.** Classical error separation becomes quantum error correction when the recovery preserves coherent amplitudes within every correctable syndrome sector.

**Sources.** Project: [the finite outer-code construction](../science/lifetime.md#a-finite-outer-code-construction). Watrous: [§2.2][W2] for valid channel implementations and [§4.1.2][W4] for the Fourier relation between shift and phase operators. The linear-code existence and coherent recovery proofs are local project derivations.

### M11. The passive minimax storage interface

**Central question.** What precisely is held fixed, varied, supplied, or forbidden in the memory task?

**Understanding target.** Assemble the register, reference, endpoint channels, classical encoder record, free key, and pre-payload calibration transcript into one protocol. Explain the worst-profile guarantee, the average-before-diamond-norm convention, and why a prior can refute a uniform guarantee without redrawing the physical profile. Distinguish one growing correlated block from repeated independent channel uses.

**Dependencies and story role.** Integrates [M01]–[M10] into the framework needed for the project-specific arguments.

**Conceptual connection.** The claimed tradeoff is determined jointly by the noise channel, the information bottleneck, and the permitted control interface.

**Sources.** Project: [the complete model](../science/model.md); bridge: [task and resource boundary](watrous_bridge.md#the-memory-task-and-its-resource-boundary). Watrous: [§2.2][W2], [§3.3.2][W3], and [§5.1][W5] support the combined framework; the passive minimax task is defined here.

## Phase II: Narrative and innovation

M12–M21 build the profile-averaging, advice, and encoding ingredients. M22–M26 assemble their global consequences. M27–M30 connect those conclusions to finite evidence, physical boundaries, and the complete resource comparison.

### M12. Averaging a fixed spatial profile

**Central question.** Why do binary and interval uncertainty produce different attenuation functions at the same fixed field phase?

**Understanding target.** Obtain the conditional cosine attenuation from two possible couplings and the sinc attenuation from a uniform interval. Track the factor of two from the eigenvalues of $Z$ and separate the known center rotation. Explain why conditional product form does not make the phase-averaged register memoryless.

**Dependencies and story role.** Requires [M03], [M07], and [M11]. Turns the physical uncertainty into the channel objects needed by both converse branches.

**Conceptual connection.** The characteristic function of the profile prior controls coherence; the shared latent phase retains correlations after that local calculation.

**Sources.** Project: [binary average](../science/calibration_rate.md#2-conditional-sign-average) and [interval average](../science/lifetime.md#averaging-fixed-profiles). Watrous: [§1.2.2][W1] and [§4.1.3][W4] support the probability and Schur-channel framework; the two averages are derived in the project.

### M13. Comparing arbitrary codes with complete dephasing

**Central question.** How does one conditional channel estimate constrain every allowed encoding and recovery?

**Understanding target.** Combine the Schur eigenvalue $(1+|\lambda|)^n$ with the separable overlap bound to obtain conditional profile-averaged fidelity at most $(1+|\lambda|)^n/D$, capped at one. Explain why arbitrary mixed encoders, physical probes, classical records, and joint recovery remain covered. Keep the independent carrier-dimension ceiling visible.

**Dependencies and story role.** Requires [M04]–[M06] and [M12]. Converts local attenuation into the common arbitrary-code converse ingredient.

**Conceptual connection.** Complete-positive order transports a spectral calculation through a full protocol, while entanglement geometry turns it into a payload bound.

**Sources.** Project: [channel comparison](../science/calibration_rate.md#2-conditional-sign-average) and [record/carrier bounds](../science/calibration_rate.md#appendix-a-classical-records-and-the-physical-carrier). Watrous: [§4.1.3, Proposition 4.17][W4], and [§6.1.1, Proposition 6.15][W6].

### M14. Counting calibration-selected codes

**Central question.** How much can a transcript with $M$ possible values improve the conditional fidelity bound?

**Understanding target.** Follow the inequality $P(c\mid s,k)\le1$ and the sum over possible endpoint codes. Explain why it permits stochastic transcripts, nonlinear compressed features of the entire profile, and a free independent key, yielding an $M$ factor without assuming that advice reveals individual coefficients.

**Dependencies and story role.** Requires [M07], [M11], and [M13]. Supplies the hard-alphabet converse shared by the binary and continuous models.

**Conceptual connection.** A description-length restriction limits the number of profile-adapted strategies that can be selected, even when each strategy is unrestricted.

**Sources.** Project: [finite-block hard-bit converse](../science/calibration_rate.md#3-finite-block-hard-bit-converse) and [continuous stochastic advice](../science/lifetime.md#stochastic-calibration-with-a-hard-alphabet). Watrous: [§1.2.2][W1] and [§2.2][W2] support averaging and channels; the code-selection bound is proved in these project sections.

### M15. Comparing real and decorrelated calibration

**Central question.** How can one charge noisy or continuous advice without counting its possible values?

**Understanding target.** Compare the actual law $P_KP_SP_{C|S,K}$ with $P_KP_SP_{C|K}$ while keeping the endpoint maps identical. Use data processing and a Bell test to obtain the direct information bound, and understand the additive form obtained through the separable comparison. Explain why the correct cost remains conditional on $K$.

**Dependencies and story role.** Requires [M07], [M08], and [M13]. Builds the second converse route and the generic lemma reused in the lifetime analysis.

**Conceptual connection.** Profile–transcript dependence is the resource that separates the actual protocol from its uncalibrated comparison experiment.

**Sources.** Project: [information converse](../science/calibration_rate.md#4-finite-block-information-converse) and [Appendix B](../science/calibration_rate.md#appendix-b-a-calibration-comparison-lemma). Watrous: [§5.2.3, Theorem 5.35][W5], with the binary-measurement interpretation from [§3.1][W3].

### M16. Exact storage from revealed coupling classes

**Central question.** How can a limited calibrated subset carry a quantum payload for every later field realization?

**Understanding target.** For $g_0=0$, conjugate the revealed negative-sign sites by $X$ to turn the selected generator into a uniform collective $Z$ sum, then choose an exact constant-magnetization code. Count its dimension and the logarithmic encoding overhead. For two positive coupling values, use separate fixed-magnetization sectors in the two known classes rather than applying the signed-model $X$ homogenization.

**Dependencies and story role.** Requires [M03], [M11], and [M12]. Provides the exact constructive ingredient that will attain the calibration frontier.

**Conceptual connection.** Calibration selects a degenerate eigenspace of the device generator without identifying the fluctuating phase in any storage run.

**Sources.** Project: [signed subset construction](../science/calibration_rate.md#subset-construction-for-signed-couplings) and [positive-coupling classes](../science/calibration_rate.md#subset-construction-for-two-positive-coupling-values). Watrous: [§1.1.3][W1] and [§2.2][W2] supply spectral and isometric-channel foundations; the code construction is given here.

### M17. Pair parities and finite exact cost

**Central question.** Can one calibration bit protect one logical qubit without revealing two individual coupling signs?

**Understanding target.** Follow the parity-selected two-qubit code and its tensor-product extension. Explain the exact bounds $D\le M$ and $\log_2D\le I(S:C\mid K)$, and their saturation with $D=M=2^B$ for integer $B\ge0$, $g_0=0$, and $n\ge2B$. Distinguish the continuity/full-Gaussian-support argument for perfect fidelity from the later positive-probability error-floor argument.

**Dependencies and story role.** Requires [M12], [M14], [M15], and [M16]. Gives a finite matching example of compressed calibration before the asymptotic theorem is assembled.

**Conceptual connection.** Relative signs can specify a protected subspace even when the overall sign of each pair remains unknown.

**Sources.** Project: [exact finite-block cost](../science/calibration_rate.md#6-exact-finite-block-information-cost) and [pair-parity saturation](../science/calibration_rate.md#exact-saturation-by-pair-parity-calibration). Watrous: [§§1.2.1–1.2.2][W1] and [§5.2.3][W5]; bridge: [the two-qubit example](watrous_bridge.md#one-bit-selects-an-exact-two-qubit-memory).

### M18. Removing the known mean within inner blocks

**Central question.** What protection is available when the center of an uncertainty interval is known but its individual deviations are not?

**Understanding target.** Choose computational-basis vectors of fixed Hamming weight so that the $g_0$ term becomes scalar. Explain exact invariance under every allowed diagonal generator and bound the residual block generator by $m\delta$. Relate this to a block half-diamond error bounded by $tm^2\delta^2$.

**Dependencies and story role.** Requires [M03], [M04], [M11], and [M16]. Begins the uncalibrated lifetime construction with a local block that requires no profile transcript.

**Conceptual connection.** Removing a known collective contribution leaves a controlled uncertainty scale; selecting computational-basis vectors prevents leakage even before error correction.

**Sources.** Project: [inner-block construction](../science/lifetime.md#inner-blocks-remove-the-known-common-coupling). Watrous: [§1.1.3][W1] and [§3.3.2, Propositions 3.44 and 3.48][W3]; the generator estimate is derived in the project.

### M19. Correcting correlated phase errors

**Central question.** How can an outer code give a uniform guarantee when all inner blocks share the same fluctuating phase?

**Understanding target.** Apply [M09] to the invariant inner blocks and retain the resulting correlated distribution of phase-error strings. Define the number $W$ of erroneous blocks, obtain its first-moment bound, and combine a phase-code correction threshold with Markov's inequality. Explain why no factorization or independence assumption is used.

**Dependencies and story role.** Requires [M09], [M10], and [M18]. Supplies the global recovery mechanism for the lifetime lower bound.

**Conceptual connection.** A code correcting every sufficiently low-weight error can use a coarse probability bound even when a shared latent variable produces strong correlations.

**Sources.** Project: [correlated phase mixture](../science/lifetime.md#randomization-yields-a-correlated-phase-error-distribution), [outer code](../science/lifetime.md#a-finite-outer-code-construction), and [error estimate](../science/lifetime.md#error-and-rate). Watrous: [§1.2.2][W1] and [§4.1.2][W4].

### M20. Storing in a supplied spectral interval

**Central question.** What becomes possible when the actual coupling profile may determine the encoder?

**Understanding target.** Bound the channel error on a spectral interval of width $w$ by $tw^2/4$. Use spectral occupancy to obtain a large code for every supplied bounded profile, and identify the subexponential condition under which its rate approaches one. Recognize this as an inherited calibrated baseline.

**Dependencies and story role.** Requires [M03], [M04], and [M11]. Builds the comparison construction before contrasting it with the universal-code bounds.

**Conceptual connection.** A large Hilbert space guarantees many nearby eigenvalues, but using their common interval requires knowing which basis vectors belong to it.

**Sources.** Project: [spectral-interval lemma](../science/calibrated_memory.md#storage-in-a-narrow-spectral-interval) and [dimension bound](../science/calibrated_memory.md#a-supplied-profile-dimension-bound). Watrous: [§1.1.3][W1] and [§3.3.2][W3]; attribution is in [Related work](../references/related_work.md#protection-with-a-supplied-collective-noise-model).

### M21. Replacing exact couplings by finite advice

**Central question.** How precise must a finite coefficient description be for the spectral code to remain useful?

**Understanding target.** Track how coordinate errors bounded by $\eta$ can enlarge a code's spectral interval by at most $2n\eta$. Connect the resulting precision requirement to a finite transcript alphabet, and keep one common payload dimension for every transcript. Recognize the rounding scheme as sufficient without assuming it is optimal.

**Dependencies and story role.** Requires [M07], [M14], and [M20]. Makes the supplied-profile comparison concrete within the classical calibration interface.

**Conceptual connection.** Classical description precision translates into a reference-complete quantum storage guarantee through a bound on accumulated spectral uncertainty.

**Sources.** Project: [finite-precision construction](../science/calibrated_memory.md#an-explicit-finite-precision-calibration-scheme). Watrous: [§1.1.3][W1], [§3.3.2][W3], and [§5.1][W5] provide the spectral, channel-distance, and description-size foundations.

### M22. Gaussian bad events and parameter order

**Central question.** Why can a rare phase event obstruct vanishing error without preventing useful fixed-error storage?

**Understanding target.** Identify intervals where the conditional binary-profile channel is near complete dephasing. Explain their positive Gaussian probability and the uniform lower bound when $t_n\delta_n^2$ stays above a positive constant. Distinguish a nonzero error floor from fidelity tending to zero and explain why shrinking phase variance is a different limit.

**Dependencies and story role.** Requires [M12]–[M15]. Converts the conditional converse bounds into the asymptotic obstruction needed for the calibration frontier.

**Conceptual connection.** The common latent phase creates an outage mechanism whose significance depends on the order of the size, time, and error limits.

**Sources.** Project: [Gaussian bad-event bound](../science/calibration_rate.md#appendix-c-a-uniform-gaussian-bad-event-bound) and [different error limits](../science/interpretation.md#two-results-with-different-error-limits). Watrous: [§1.2.2][W1]; the wrapped-Gaussian estimate and memory consequence are project derivations.

### M23. Assembling the exact calibration frontier

**Central question.** Why does the reliable storage rate equal the calibration-information rate, capped at one?

**Understanding target.** Combine the hard-alphabet or information converse with the exact subset construction and the physical carrier bound to obtain $Q_{\mathrm{cal}}(b)=\min\{b,1\}$. State the worst-profile, vanishing-error, classical-transcript, and positive-noise hypotheses. Explain why the same asymptotic frontier holds for both advice budgets and for two positive coupling values.

**Dependencies and story role.** Requires [M14], [M15], [M16], and [M22], with the carrier bound from [M13]. This is the first global synthesis of the converse and construction branches.

**Conceptual connection.** The information needed to select protected subspaces becomes an exact asymptotic storage resource.

**Sources.** Project: [the exact asymptotic rate theorem](../science/calibration_rate.md#5-exact-asymptotic-calibration-rate). Watrous: [§3.3.2][W3], [§5.2.3][W5], and [§6.1.1][W6] support its operational and information-theoretic ingredients; the frontier is the project result.

### M24. Sinc decay and the lifetime upper bound

**Central question.** Why does independent interval uncertainty prevent a fixed-error lifetime from growing with register size at positive rate?

**Understanding target.** Split the common-phase integral into a small interval and its complement. Use sinc decay outside that interval and the Gaussian mass inside it to obtain the finite bound governed by $(t\delta^2)^{-1/2}$ and an exponentially small term. Translate average fidelity into a worst-profile obstruction.

**Dependencies and story role.** Requires [M12], [M13], and [M14]. Assembles the continuous-profile upper bound from the common converse machinery.

**Conceptual connection.** A spatial uncertainty prior supplies local attenuation; the distribution of the common phase turns that attenuation into a time-scale bound.

**Sources.** Project: [explicit time bound](../science/lifetime.md#an-explicit-time-bound). Watrous: [§1.2.2][W1], [§3.3.2][W3], and [§4.1.3][W4]; the sinc-tail argument is proved in the project.

### M25. Matching the lifetime at every fixed rate

**Central question.** How do the converse and correlated-error construction establish the same lifetime scale?

**Understanding target.** Fix $0<R<1$ and $0<\epsilon<1$, then choose the inner block size, outer correction fraction, and sufficiently large register size in that order. Combine the construction with the upper bound to obtain $T_{R,\epsilon}^{(n)}(\delta)=\Theta_{R,\epsilon}(\delta^{-2})$. Explain the uniformity in $g_0$ and $\delta$ without asserting uniform constants as $R\to1$ or $\epsilon\to0$.

**Dependencies and story role.** Requires [M18], [M19], and [M24]. Completes the fixed-error theorem and its quantifiers.

**Conceptual connection.** Exact removal of the known mean and correction of correlated residual errors match an arbitrary-code limitation set by calibration width.

**Sources.** Project: [lifetime statement and constants](../science/lifetime.md#setting-and-lifetime-statement) and [achievable error and rate](../science/lifetime.md#error-and-rate). Watrous: [§1.2.2][W1] and [§3.3.2][W3] support the probability and operational-error steps; the matching theorem is local to this project.

### M26. Calibration requirements at diverging times

**Central question.** What calibration information becomes necessary if the storage time grows beyond the uncertainty scale?

**Understanding target.** For $t_n\delta_n^2\to\infty$, distinguish the hard-budget necessity $B_n\ge\log_2D_n-o(n)$ at fidelity bounded away from zero from the information-budget necessity $I(\boldsymbol G:C\mid K)\ge(1-\epsilon)\log_2D_n-o(n)$ at fixed error. Explain the entropy averaging in the latter and why neither condition alone is an optimal sufficiency statement for continuous profiles.

**Dependencies and story role.** Requires [M15], [M21], [M24], and [M25]. Extends the time-scale comparison into an information-resource consequence.

**Conceptual connection.** Hard descriptions and mean statistical information agree on some vanishing-error limits while charging rare informative calibration outcomes differently at fixed error.

**Sources.** Project: [diverging-time calibration bounds](../science/lifetime.md#calibration-information-for-diverging-storage-times). Watrous: [§5.1 and §5.2.3][W5] for entropy and data processing, and [§1.2.2, Theorem 1.14][W1] for Jensen averaging. The bounded-limit step is supplied in the project.

### M27. Interpreting finite verification

**Central question.** Which parts of the scientific argument can finite computation check, and what remains an analytic statement?

**Understanding target.** Read the sign-average and code-eigenspace checks as tests of conventions and constructions. Interpret the seven-block Hamming example as a phase-only recovery under a correlated error distribution. Explain its logical half-diamond error, the difference from independent errors with identical marginals, and the role of numerical tolerances.

**Dependencies and story role.** Requires [M17], [M19], [M22], [M23], and [M25]. Connects both theorem branches to reproducible finite evidence without changing their proof domains.

**Conceptual connection.** Computation can expose an incorrect factor, code assignment, or independence assumption; finite examples do not certify an arbitrary-code asymptotic theorem.

**Sources.** Project: [verification guide](../verification/README.md), [calibration checks](../verification/check_calibration.py), and [phase-code check](../verification/check_phase_code.py). Watrous: [§3.3.2][W3] and [§4.1.3][W4] define the channel-error and positivity objects being checked.

### M28. Adding control changes the storage interface

**Central question.** Why does the passive no-calibration frontier not apply after ideal controls are inserted during storage?

**Understanding target.** Follow the Walsh-sign toggling calculation under the same Markov white-noise model. Explain how orthogonal temporal patterns remove the unknown signs and produce independent dephasing with attenuation $e^{-2t\delta^2}$. Identify the growing number of control intervals, the fixed-finite-time positive coding rate, and the distinction from a frozen quasistatic field.

**Dependencies and story role.** Requires [M03], [M09]–[M11], [M23], and [M25]. Tests the physical importance of the passive-interface assumption with an explicit changed task.

**Conceptual connection.** One white-noise field has independent temporal increments; added control can redistribute them among spatial modes without learning the signs.

**Sources.** Project: [the active-control boundary](../science/interpretation.md#allowing-control-during-storage-changes-the-task). Watrous: [§1.2.2][W1] for Gaussian orthogonal invariance, [§2.2][W2] for channel composition, and [§4.1.2][W4] for phase/shift relations. The control and coding derivations are supplied in the project.

### M29. Comparing resource and error regimes

**Central question.** Which apparent tensions disappear when the supplied information, permitted operations, and error limit are stated together?

**Understanding target.** Compare uncalibrated fixed-error lifetime, the binary reliable-rate frontier, supplied-profile spectral storage, and the controlled boundary. Distinguish reusable static-profile information from data-run error feedback and from the experiments used to acquire calibration. Place the unrestricted-code results relative to known-profile and fixed-code analyses.

**Dependencies and story role.** Integrates [M20], [M21], [M23], and [M25]–[M28]. Moves from individual conclusions to a consistent comparison of physical tasks.

**Conceptual connection.** A common noise source does not by itself determine accessible storage: information and control assumptions decide which mathematical protection is available.

**Sources.** Project: [different error limits](../science/interpretation.md#two-results-with-different-error-limits), [static calibration](../science/interpretation.md#calibration-describes-the-device-not-the-error-realization), and [Related work](../references/related_work.md). Watrous: [§3.3.2][W3] for channel error and [§4.1.1, Theorem 4.8][W4] for environment-assisted correction, a contrasting information interface.

### M30. The complete calibration-memory picture

**Central question.** What has the combined theory established about access to collective-noise protection, and what precise question remains open?

**Understanding target.** Explain the fixed-error lifetime theorem and exact binary calibration frontier as complementary consequences of the passive interface. Identify the inherited Schur comparison, spectral occupancy, and protected-block methods separately from the resource-sensitive conclusions. State the unresolved continuous-profile gap: for fixed $g_0$ and $\delta>0$, diverging polynomial storage times, and inverse-polynomial error, the proved costs are linear necessary hard advice and an $O(n\log n)$ sufficient rounding budget. Neither bound is claimed optimal in this regime.

**Dependencies and story role.** Integrates [M23]–[M29]. Completes the route from elementary channel objects to the project's physical consequence and remaining boundary.

**Conceptual connection.** Knowing that a large protected subspace exists is different from possessing the classical device information needed to select it.

**Sources.** Project: [proof dependencies](../science/README.md#proof-dependencies), [what the result establishes](../science/interpretation.md#what-the-result-establishes), [the continuous-cost gap](../science/calibrated_memory.md#what-is-and-is-not-tight), and [contribution scope](../references/related_work.md#scope-of-the-resulting-contribution). Watrous: [§3.3.2][W3], [§4.1.3][W4], and [§5.2.3][W5] form the foundational chain; the [bridge](watrous_bridge.md#what-is-imported-and-what-is-proved-here) separates those foundations from the project results.

[W1]: https://jhwatrous.github.io/TQI.1.pdf
[W2]: https://jhwatrous.github.io/TQI.2.pdf
[W3]: https://jhwatrous.github.io/TQI.3.pdf
[W4]: https://jhwatrous.github.io/TQI.4.pdf
[W5]: https://jhwatrous.github.io/TQI.5.pdf
[W6]: https://jhwatrous.github.io/TQI.6.pdf

[M01]: #m01-states-labels-and-tensor-factors
[M02]: #m02-channels-and-their-representations
[M03]: #m03-spectra-phases-and-dephasing
[M04]: #m04-reference-entanglement-and-operational-error
[M05]: #m05-cp-order-and-schur-multipliers
[M06]: #m06-separability-as-a-memory-benchmark
[M07]: #m07-conditional-classical-information
[M08]: #m08-relative-entropy-under-processing
[M09]: #m09-pauli-randomization-and-retained-correlations
[M10]: #m10-coherent-correction-from-classical-codes
[M11]: #m11-the-passive-minimax-storage-interface
[M12]: #m12-averaging-a-fixed-spatial-profile
[M13]: #m13-comparing-arbitrary-codes-with-complete-dephasing
[M14]: #m14-counting-calibration-selected-codes
[M15]: #m15-comparing-real-and-decorrelated-calibration
[M16]: #m16-exact-storage-from-revealed-coupling-classes
[M17]: #m17-pair-parities-and-finite-exact-cost
[M18]: #m18-removing-the-known-mean-within-inner-blocks
[M19]: #m19-correcting-correlated-phase-errors
[M20]: #m20-storing-in-a-supplied-spectral-interval
[M21]: #m21-replacing-exact-couplings-by-finite-advice
[M22]: #m22-gaussian-bad-events-and-parameter-order
[M23]: #m23-assembling-the-exact-calibration-frontier
[M24]: #m24-sinc-decay-and-the-lifetime-upper-bound
[M25]: #m25-matching-the-lifetime-at-every-fixed-rate
[M26]: #m26-calibration-requirements-at-diverging-times
[M27]: #m27-interpreting-finite-verification
[M28]: #m28-adding-control-changes-the-storage-interface
[M29]: #m29-comparing-resource-and-error-regimes
[M30]: #m30-the-complete-calibration-memory-picture
