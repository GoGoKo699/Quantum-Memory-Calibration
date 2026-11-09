# Interpretation and boundaries

[Science map](README.md) · [Model](model.md) · [Lifetime](lifetime.md) · [Calibration rate](calibration_rate.md)

## One noise field does not specify its protected subspaces

A common dephasing field acts through one operator, $A_{\boldsymbol g}=\sum_j g_jZ_j$. If the coefficients are supplied, the encoder can group computational-basis vectors with nearly equal eigenvalues. A narrow spectral interval then contains a large code on which the field produces nearly the same phase. [The supplied-profile bound](calibrated_memory.md) makes this counting argument quantitative.

Unknown coefficients change the encoding problem. One endpoint protocol must protect the payload for every allowed placement of eigenvalues, without an uncounted device-specific setting. With independent interval uncertainty, no universal positive-rate code can obtain a fixed-error lifetime growing with register size at fixed $\delta$. This is an arbitrary-code statement, including mixed encoders, counted probes, classical encoder records, and independent shared randomness. It is stronger than showing that one chosen decoherence-free code is sensitive to miscalibration.

The uncertainty has $n$ independently variable coordinates. A low-dimensional uncertainty model, such as one unknown common scale multiplying an otherwise known profile, is a different task. The theorem does not replace that structured model by independent uncertainty or claim the same obstruction for it.

## Two results with different error limits

| Result | Quantity held fixed | Asymptotic conclusion |
|---|---|---|
| Interval-profile lifetime | Positive rate $R$, admissible error $\epsilon$, and uncertainty width $\delta$ | For sufficiently large registers, useful uncalibrated lifetime lies between positive multiples of $\delta^{-2}$. |
| Two-value calibration frontier | Dimensionless noise strength bounded away from zero; error required to vanish | Reliable logical rate equals the calibration-information rate, capped at one. |
| Supplied-profile spectral code | Bounded couplings; storage time and error satisfying a subexponential condition | The retained rate approaches one. |

The lifetime result addresses a fixed operational tolerance. The binary frontier addresses arbitrarily reliable asymptotic storage. A nonzero but extremely rare event can obstruct the latter without being a practically important error at a chosen finite tolerance.

For example, let $v=t\delta^2$ and let the hard-bit rate deficit be $q=R-b=1/2$. The binary converse gives the asymptotic error-floor lower bound

$$
\liminf_{n\to\infty}\epsilon_n
\ge
\Pr_{Y\sim N(0,v)}
\left[|\cos(2Y)|<2^{1/2}-1\right].
$$

The following values are computed by the [calibration verification program](../verification/check_calibration.py), with an independent wrapped-Gaussian Fourier check where numerically appropriate.

| Dimensionless noise strength $v$ | Error-floor lower bound |
|---:|---:|
| 0.01 | $1.0741244\times10^{-8}$ |
| 0.1 | $0.068964356$ |
| 1 | $0.27172564$ |
| 10 | $0.27188667$ |

These are lower bounds, not the exact optimal errors. In particular, “zero reliable rate without calibration” at a fixed nonzero $v$ can coexist with very good finite-tolerance performance when $v$ is small. The rate theorem does not assert a uniform error floor as $v\to0$, and it does not assert fidelity tending to zero above the frontier.

## Why correlations survive the achievable construction

The short-time lifetime construction removes the known common coupling within each fixed-magnetization block. Independent logical $X$ randomization makes the remaining diagonal noise a stochastic phase-error channel. The block errors still share the same Gaussian phase and can therefore remain strongly correlated.

The proof needs only the expected number of erroneous blocks and a code correcting every error below a weight threshold. Markov's inequality bounds the probability of exceeding that threshold. Replacing the joint distribution by independent errors would not justify this proof.

The [seven-block example](../verification/check_phase_code.py) makes the difference visible. Each block uses two physical qubits with $g_0=0.7$ and $\delta=0.2$, the storage time is $t=0.35$, and a classical $[7,4,3]$ Hamming code in the Hadamard basis protects four logical qubits against phase errors. This is a phase-only code, not a quantum code correcting arbitrary single-qubit errors.

| Quantity | Value |
|---|---:|
| Actual correlated recovery failure | 0.0319897475 |
| Failure after incorrectly imposing independence with the same marginals | 0.0150189610 |
| Expected number of erroneous blocks | 0.200072447 |
| Markov bound using the integer failure threshold | 0.100036223 |

For this recovery, every nontrivial residual logical error is a Pauli error. Its total probability equals the logical half-diamond error, so the first row is a channel-error calculation. The finite example confirms the correlation accounting and the error bound; it does not prove the asymptotic coding statement.

## Calibration describes the device, not the error realization

The transcript is prepared before the unknown payload and carries information about the fixed spatial profile. It does not identify the common field realization in a later storage run. The same transcript may be reused for later payloads. Information from monitoring the data-run environment belongs to a different interface.

The hard alphabet budget and the conditional mutual-information budget also answer different questions. A rare outcome can reveal an entire profile while contributing little mean information. Conversely, representing a large alphabet by an analog number does not make its worst-case description short. Both budgets have the same binary vanishing-error frontier, but their fixed-error converses differ. For continuous uncertainty and diverging $t\delta^2$, the results give

$$
B_n\ge\log_2D_n-o(n)
$$

for a hard budget when fidelity stays bounded away from zero, while a fixed error tolerance $\epsilon$ implies

$$
I(\boldsymbol G;C\mid K)
\ge(1-\epsilon)\log_2D_n-o(n)
$$

for the stated uniform prior and information budget. [The lifetime page](lifetime.md#calibration-information-for-diverging-storage-times) gives the precise hypotheses. A direct finite-precision construction supplies long storage with a larger sufficient budget; the optimal continuous-profile information cost remains unresolved.

## Allowing control during storage changes the task

The passive restriction is operationally consequential. Consider the signed model $A_s=\delta\sum_j s_jZ_j$ under the same Markovian white-noise dynamics, but now allow ideal instantaneous local $X$ pulses during storage.

Choose $M$ equal subintervals and signs $r_{j\ell}\in\{-1,+1\}$ satisfying

$$
\frac1M\sum_{\ell=1}^M r_{i\ell}r_{j\ell}=\delta_{ij}.
$$

For example, take $n$ rows of a Walsh matrix of power-of-two order $M\ge n$. Local pulses switch each qubit's toggling sign between subintervals. Undo the final known frame at recovery. In subinterval $\ell$, the generator is

$$
A_{s,\ell}=\delta\sum_j s_jr_{j\ell}Z_j.
$$

All corresponding double-commutator superoperators commute. Consequently the product of their Markov semigroups is exactly

$$
\begin{aligned}
\Phi^{\mathrm{ctrl}}_{s,t}
&=\exp\left[-\frac{t}{2M}\sum_{\ell=1}^M
\operatorname{ad}_{A_{s,\ell}}^2\right]\\
&=\exp\left[-\frac{t\delta^2}{2}\sum_{j=1}^n
\operatorname{ad}_{Z_j}^2\right]
=\mathcal D_{e^{-2t\delta^2}}^{\otimes n},
\end{aligned}
$$

where $\operatorname{ad}_A(B)=[A,B]$. The unknown signs disappear, and the resulting independent phase-flip probability is

$$
p=\frac{1-e^{-2t\delta^2}}2<\frac12
$$

at every finite $t$. Standard phase-error coding then permits positive reliable rate, for example any rate below $1-h_2(p)$, without supplying the sign profile. This familiar coding step treats phase errors as binary errors in the Hadamard basis.

One can see the achievable rate directly. For any small $\eta>0$, Bernoulli-$p$ errors have a typical set $\mathcal T_n$ of size at most $2^{n(h_2(p)+\eta)}$ and probability approaching one. Choose a random binary parity-check matrix with $h=\lceil n(h_2(p)+2\eta)\rceil$ rows. A fixed typical error has a syndrome collision with another typical error with probability at most $|\mathcal T_n|2^{-h}\le2^{-n\eta}$. Thus some matrix has average decoding failure at most

$$
\Pr(E\notin\mathcal T_n)+2^{-n\eta}\longrightarrow0.
$$

Encode its kernel in the Hadamard basis and correct the unique typical error associated with each syndrome. The syndrome is independent of the logical codeword, so the same recovery corrects coherent quantum superpositions. At least $n-h$ logical qubits are stored, and the logical half-diamond error is bounded by the decoding-failure probability. Letting $\eta$ decrease establishes the stated rate. The case $p=0$ needs no correction.

The sequence is an explicit boundary example, not a proposed new control method or a control-cost optimum. Taking the smallest power-of-two order uses $n\le M<2n$ intervals, whose duration is $t/M$; it does not establish the same result with fixed control bandwidth as $n$ grows. The positive rate stated above is for fixed finite $t\delta^2$ and tends to zero for this construction if that quantity diverges. The derivation uses independent white-noise increments and composition of Markov semigroups; it must not be read as a derivation for a frozen quasistatic field. Those additional operations are absent from the passive theorem.

## What the result establishes

Within the stated passive interface, supplied knowledge of an extensive coupling profile changes the accessible storage rate and lifetime. The continuous theorem quantifies this at fixed error, and the two-value theorem gives an exact retained-information frontier. The proof tools and supplied-spectrum comparison have established antecedents, detailed in [Related work](../references/related_work.md).

The account does not establish the optimal cost of acquiring calibration experimentally, an efficient implementation of the general endpoint codes, the optimal continuous calibration frontier, or the best control-assisted memory. These are separate questions from the proved resource tradeoff.
