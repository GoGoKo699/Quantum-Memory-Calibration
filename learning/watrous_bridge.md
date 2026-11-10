# From Watrous to quantum memory calibration

[Learning route](README.md) · [30-milestone map](milestones.md) · [Scientific statements](../science/README.md)

A quantum memory must preserve an unknown state, including its entanglement with other systems. A common fluctuating field can leave large subspaces unaffected, but using such a subspace may require knowing how each physical qubit couples to that field. This project separates those two resources: the structure of the noise and the classical information available to the controls.

The selected educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**. The [official author page](https://jhwatrous.github.io/books-and-courses.html) identifies the April 2018 publication and provides manuscript chapters; the [publisher record](https://www.cambridge.org/core/books/theory-of-quantum-information/AE4AA5638F808D2CFEB070C55431D897) identifies the published book. The section and theorem numbers below were checked against those author-provided chapters. Links point to that manuscript rather than reproducing it.

This bridge selects the parts needed for the memory problem. It supplies the project-specific steps between them, including a complete two-qubit encoding, the channel comparison behind both converses, and the construction that attains the continuous lifetime order. The [milestone map](milestones.md) organizes the full scientific story; it does not require a preliminary reading of the entire book.

## The memory task and its resource boundary

Let $`Z=\mathrm{diag}(1,-1)`$. For $`n`$ physical qubits, the fixed spatial coupling profile $`\boldsymbol g`$ determines

```math
A_{\boldsymbol g}=\sum_{j=1}^n g_jZ_j.
```

The storage channel for time $`t`$ is

```math
\Phi_{\boldsymbol g,t}(\rho)
=\mathbb E_{\Theta\sim N(0,t)}
e^{-i\Theta A_{\boldsymbol g}}\rho e^{i\Theta A_{\boldsymbol g}}
=e^{-t[A_{\boldsymbol g},[A_{\boldsymbol g},\,\cdot\,]]/2}(\rho).
```

There is one Gaussian phase $`\Theta`$ for the entire register. The coefficients $`g_j`$ are fixed during storage. The Gaussian representation is the integrated common white-noise field in the stated model; it does not mean independent physical phases at different sites.

The payload has dimension $`D`$, so it carries $`k=\log_2D`$ logical qubits. An encoder prepares the physical register, it undergoes one passive storage interval, and a terminal recovery returns the payload. Both endpoints can be arbitrary joint quantum channels. Every quantum system that persists across the interval is included in the $`n`$ noisy carriers. No control pulse, new probe, or syndrome measurement occurs inside that interval.

Before the payload arrives, calibration supplies a classical transcript $`C`$. It describes the static profile and is independent of the subsequent phase realization, conditional on the profile and any independent shared key $`K`$. Every profile-dependent choice of endpoint operation must pass through $`(C,K)`$. An encoder may also retain a payload-dependent classical record $`X`$; it may not retain an uncounted quantum system. The [model](../science/model.md) states this interface precisely.

These conditions are essential to the question. Knowing a code that would work for each profile does not yet give a single admissible protocol: its selection must use the information actually supplied to the endpoints. Conversely, a lower bound must allow all the endpoint encoders, recoveries, physical probes, and classical records that the interface permits.

## A selective route through Watrous

The following pointers support particular steps rather than prescribing whole chapters. The descriptions in the final column refer to the repository's use of the source.

| Ingredient | Verified source locator | Where it enters this project |
|---|---|---|
| Tensor products, operators, spectra, and probability | [Chapter 1](https://jhwatrous.github.io/TQI.1.pdf), §§1.1.1–1.1.3, spectral Theorem 1.3, and §1.2.2 | Reference systems, eigenvalue phases, Gaussian averages, and the first-moment error bound |
| States, classical registers, and channels | [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), §§2.1–2.2; Choi formula (2.64); Theorem 2.22 | A common description of general endpoint operations and the equivalence between complete positivity and a positive Choi operator |
| State distinguishability and fidelity | [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), §3.1 and Theorem 3.4; §3.2 and Definition 3.11 | Relating operational error to a maximally entangled-state test, with the fidelity convention translated below |
| Reference-complete channel error | [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), §3.3.2, Definition 3.43, Propositions 3.44 and 3.48 | Diamond norm, norm one for channels, and bounds preserved under endpoint composition |
| Random unitary and Schur maps | [Chapter 4](https://jhwatrous.github.io/TQI.4.pdf), §§4.1.1–4.1.3; Proposition 4.17 | Endpoint Pauli averaging and the positive-semidefinite matrix test for the dephasing comparison |
| Classical information and relative entropy | [Chapter 5](https://jhwatrous.github.io/TQI.5.pdf), §5.1; §5.2.3, Theorem 5.35 | Charging conditional calibration information and comparing the actual advice law with a decorrelated one |
| Separability and destruction of entanglement | [Chapter 6](https://jhwatrous.github.io/TQI.6.pdf), §6.1.1, Proposition 6.15 and Example 6.16; §6.4, Exercise 6.1 | The separable-state overlap bound and the measure-and-prepare characterization of entanglement-breaking channels |
| Capacity terminology, if needed | [Chapter 8](https://jhwatrous.github.io/TQI.8.pdf), §8.2.1 | Distinguishing a standard repeated-channel capacity from this single growing, spatially correlated block |

The source supplies the general mathematics. The Gaussian coupling model, the conditional profile averages, the calibration resource definitions, the protected-block construction, and the particular asymptotic limits are supplied in the scientific pages. The explicit phase code below is a local explanation of that construction, not an attribution of the project's code to a textbook theorem.

## Notation that must be translated

Several otherwise harmless conventions matter when moving between the source and the proofs.

| Watrous convention | Convention here | Consequence |
|---|---|---|
| $`\mathrm L(\mathcal X)`$, $`\mathrm D(\mathcal X)`$, and $`\mathrm C(\mathcal X,\mathcal Y)`$ | Operators, density operators, and quantum channels, often written without set notation | All endpoint maps are completely positive and trace preserving |
| An adjoint is written $`A^*`$ | Usually $`A^\dagger`$ | The operations are identical |
| Completely bounded trace norm, Definition 3.43 | Diamond norm | The norm is the same; the project's error includes a factor of one half |
| Fidelity $`F`$ in Definition 3.11 | Entanglement fidelity $`F_e`$ in the overlap convention | For the pure test target, $`F_e`$ is the square of the source's fidelity |
| Choi representation $`J(\Phi)`$, formula (2.64) | A normalized maximally entangled input and its output state | Divide the Choi operator by the input dimension, with tensor factors ordered consistently |
| Classical mutual information and relative entropy use base-two logarithms | Calibration is measured in bits | No conversion factor is needed |

More explicitly, let

```math
|\Phi_D\rangle=\frac1{\sqrt D}\sum_{a=1}^D|a\rangle|a\rangle,
\qquad \varphi_D=|\Phi_D\rangle\langle\Phi_D|,
\qquad \rho_\Lambda=(\mathrm{id}\otimes\Lambda)(\varphi_D).
```

Then

```math
F_e(\Lambda)=\mathrm{Tr}(\varphi_D\rho_\Lambda)
=F_{\text{Watrous}}(\varphi_D,\rho_\Lambda)^2.
```

The test with outcomes $`\{\varphi_D,I-\varphi_D\}`$ accepts with probability $`F_e`$. If the half-diamond error of $`\Lambda`$ is at most $`\epsilon`$, the trace distance between these two reference–payload states is at most $`\epsilon`$. Their acceptance probabilities therefore differ by at most $`\epsilon`$, giving

```math
\frac12\|\Lambda-\mathrm{id}_D\|_\diamond\le\epsilon
\quad\Longrightarrow\quad F_e(\Lambda)\ge1-\epsilon.
```

This implication is the direction needed for the converses. High fidelity for this one input is not being substituted for a uniform diamond-norm guarantee in the achievable constructions.

Watrous's Choi operator has trace $`D`$ for a channel with input dimension $`D`$; $`\rho_\Lambda`$ has trace one. The symbol $`J`$ also denotes the information budget on the [calibration page](../science/calibration_rate.md). To avoid confusing those objects, this bridge writes the information budget as $`\mathcal I`$.

Finally, independent randomness is averaged before the operational norm:

```math
\epsilon=\sup_{\boldsymbol g}\frac12
\|\Lambda_{\boldsymbol g}-\mathrm{id}_D\|_\diamond,
```

where $`\Lambda_{\boldsymbol g}`$ already includes the calibration outcomes and key. The construction guarantees this channel error. It does not assert the same bound separately for every random key.

## One bit selects an exact two-qubit memory

Consider two qubits with signed couplings

```math
A_s=\delta(s_1Z_1+s_2Z_2),\qquad s_1,s_2\in\{-1,+1\}.
```

The payload is $`\alpha|0\rangle+\beta|1\rangle`$. Calibration supplies only the parity $`p=s_1s_2`$, one classical bit. The endpoints do not learn the individual signs or the phase $`\Theta`$.

If $`p=+1`$, define the encoding isometry by

```math
V_+|0\rangle=|01\rangle,
\qquad V_+|1\rangle=|10\rangle.
```

Both basis states have zero eigenvalue under $`A_s`$: the contributions from the two equal signs cancel. If $`p=-1`$, instead use

```math
V_-|0\rangle=|00\rangle,
\qquad V_-|1\rangle=|11\rangle.
```

The two signs now cancel on these equal-bit states. In either case,

```math
A_sV_p=0,
\qquad e^{-i\theta A_s}V_p=V_p
\quad\text{for every real }\theta.
```

Recovery applies the inverse isometry on its image, extended arbitrarily to a channel on the rest of the physical space. It returns the original payload exactly. The same identity holds when the payload is entangled with a reference, because the encoded channel acts as the identity on every matrix element of the logical space. The final maximally entangled-state test accepts with probability one. There is no measurement during storage and no estimate of the realized field.

The calibration bit selects a subspace, rather than correcting a phase observed after the fact. Its usefulness does not require identifying the entire device profile: changing both signs leaves $`p`$ and the selected subspace unchanged.

For comparison, suppose the endpoints always use $`V_+`$ even when $`s_1=-s_2`$. Its two codewords then have eigenvalues $`+2\delta s_1`$ and $`-2\delta s_1`$. Their coherence acquires $`e^{-4i\delta s_1\Theta}`$, whose Gaussian average is

```math
\mathbb E e^{-4i\delta s_1\Theta}=e^{-8t\delta^2}.
```

This calculation diagnoses that particular incorrect code choice. The impossibility of *every* exact uncalibrated code needs the general converse developed below.

With $`B`$ disjoint pairs, the $`B`$ pair parities select a tensor product of these subspaces and store $`B`$ logical qubits exactly, provided $`n\ge2B`$. Unused carriers are initialized in computational-basis states and discarded at recovery. Under the uniform sign prior, the independent parity bits carry exactly $`B`$ bits of information. Thus $`D=2^B`$ saturates the finite exact information bound in this range.

This pair construction uses the signed model $`g_0=0`$. For two positive values $`g_0\pm\delta`$, the higher-rate construction instead groups calibrated sites by their coupling value and fixes the Hamming weight within each group; the details appear in [the subset constructions](../science/calibration_rate.md#subset-construction-for-two-positive-coupling-values).

## From profile averaging to a channel comparison

The converse starts with a necessary condition for uniform storage: a code that succeeds for every fixed profile must also succeed after averaging over any chosen prior on those profiles. This is a mathematical averaging step. The actual register still has one fixed profile throughout its storage interval.

Hold the common phase $`\theta`$ fixed before taking the profile average. For independent uniform signs,

```math
\mathbb E_{s_j}e^{-2i\delta s_j\theta}=\cos(2\delta\theta).
```

For independent uniform interval coefficients $`G_j\in[g_0-\delta,g_0+\delta]`$,

```math
\mathbb E_{G_j}e^{-2iG_j\theta}
=e^{-2ig_0\theta}\mathrm{sinc}(2\delta\theta),
\qquad \mathrm{sinc}(x)=\frac{\sin x}{x},\quad \mathrm{sinc}(0)=1.
```

The factor two is the eigenvalue difference of $`Z`$. In either case, conditional profile averaging produces a tensor product of one-qubit dephasing maps, composed with the center rotation when $`g_0\ne0`$. Write the real attenuation as $`\lambda(\theta)`$, equal to cosine or sinc as appropriate.

This conditional tensor product does not make the final channel memoryless. The same $`\theta`$ is subsequently averaged over the entire block; that shared average retains correlations.

The one-qubit map is an entrywise, or Schur, multiplier with matrix

```math
Q_\lambda=
\begin{pmatrix}1&\lambda\\\lambda&1\end{pmatrix}.
```

Its largest eigenvalue is $`1+|\lambda|`$. Consequently,

```math
Q_\lambda^{\otimes n}\le (1+|\lambda|)^nI.
```

Watrous's Proposition 4.17 turns this matrix inequality into a completely positive comparison. If $`\mathcal N_\theta`$ is the conditional profile-averaged channel and $`\Delta_n`$ is complete computational-basis dephasing, then

```math
\mathcal N_\theta\le_{\mathrm{CP}}c_\theta\Delta_n,
\qquad c_\theta=(1+|\lambda(\theta)|)^n.
```

The notation means that $`c_\theta\Delta_n-\mathcal N_\theta`$ is completely positive; it need not preserve trace. The center rotation leaves $`\Delta_n`$ unchanged. Complete positivity makes the comparison survive an untouched reference, arbitrary encoding, and arbitrary recovery. This is why a matrix eigenvalue calculation can constrain all admissible codes.

The other half of the argument is entanglement breaking. Complete dephasing measures a computational label and prepares that same basis state. After any allowed encoder, dephasing all the physical qubits leaves a mixture of product states across the reference–decoder cut. The extra record $`X`$ is classical, so it preserves this structure. A terminal operation on the decoder's side cannot turn such a mixture into an entangled state with the reference.

For any normalized product vectors $`a,b`$,

```math
|\langle\Phi_D|a\otimes b\rangle|^2
=\frac1D\left|\sum_j a_jb_j\right|^2\le\frac1D.
```

Convexity gives the same bound for separable states, the $`r=1`$ case of Watrous's Proposition 6.15 and Example 6.16. Therefore every fixed endpoint code obeys

```math
f(\theta)\le\min\{1,c_\theta/D\}.
```

The classical-record qualification matters: $`\Delta_n\otimes\mathrm{id}_X`$ would not destroy all reference entanglement if $`X`$ were an unrestricted persistent quantum memory. [Appendix A of the calibration proof](../science/calibration_rate.md#appendix-a-classical-records-and-the-physical-carrier) gives the precise allowed-record argument.

The Schur comparison as a memory converse is inherited from [Quantum-Spectral-Memory](https://github.com/GoGoKo699/Quantum-Spectral-Memory/blob/ee5dc0e5529c7775bfaeabb2a5e744c51eb9431d/science/spectral_law.md). The present use adds a profile-information bottleneck and its consequences for these coupling families.

## The continuous lifetime argument

For interval uncertainty, write $`\tau=t\delta^2`$ and $`Y=\delta\Theta\sim N(0,\tau)`$. The conditional attenuation is $`\lambda=\mathrm{sinc}(2Y)`$. Without calibration, the comparison just proved gives

```math
\overline F_e\le
\mathbb E_Y\min\left\{1,\frac{(1+|\mathrm{sinc}(2Y)|)^n}{D}\right\}.
```

Here the bar includes the converse prior on fixed profiles. A uniform operational error at most $`\epsilon`$ requires $`\overline F_e\ge1-\epsilon`$.

### Why the converse has the scale $`\delta^{-2}`$

Set $`s=\log_2D/n>0`$. Outside the interval

```math
|Y|\le\frac1{2(2^{s/2}-1)},
```

the bound $`|\mathrm{sinc}(2Y)|\le1/(2|Y|)`$ makes the integrand at most $`2^{-sn/2}`$. The Gaussian density is everywhere at most $`1/\sqrt{2\pi\tau}`$. Its probability of the displayed interval is therefore at most $`a_s/\sqrt\tau`$, where

```math
a_s=\frac{\sqrt{2/\pi}}{2(2^{s/2}-1)}.
```

Combining the two regions gives

```math
\overline F_e\le\min\{1,a_s\tau^{-1/2}+2^{-sn/2}\}.
```

At a fixed positive rate and fixed error below one, $`\tau`$ cannot grow without bound. This yields a lifetime upper bound proportional to $`\delta^{-2}`$, uniformly over arbitrary endpoint codes. The [finite-block converse](../science/lifetime.md#a-finite-block-converse) also includes a hard calibration budget: replace $`s`$ by $`(\log_2D-B)/n`$ when it is positive.

### Why a matching code must retain the correlations

An upper bound alone would not establish the optimal lifetime order. The matching construction first uses a fixed block of $`m`$ physical qubits to remove the known center $`g_0`$. Computational basis vectors of equal Hamming weight have the same value of $`\sum_jZ_j`$, so this term is scalar on their span. Choose

```math
r=\left\lfloor\log_2\binom m{\lfloor m/2\rfloor}\right\rfloor
```

logical qubits inside that subspace. The residual diagonal generator on any block, denoted $`B_b`$, satisfies $`\|B_b\|\le m\delta`$. The subspace is exactly invariant for every allowed profile.

Channel norm one and composition bounds from Watrous's §3.3.2 give the local estimate used in the proof. For

```math
\mathcal L_{B_b}(\rho)=B_b\rho B_b-\tfrac12\{B_b^2,\rho\},
```

left and right multiplication bounds imply $`\|\mathcal L_{B_b}\|_\diamond\le2\|B_b\|^2`$. Integrating the semigroup derivative yields

```math
\frac12\|e^{t\mathcal L_{B_b}}-\mathrm{id}\|_\diamond
\le t\|B_b\|^2\le tm^2\delta^2.
```

There are $`N=\lfloor n/m\rfloor`$ inner blocks and $`L=rN`$ logical qubits before the outer code. Apply independent random logical $`X`$ conjugations at the two endpoints, using a key independent of the profile. A diagonal unitary has an expansion

```math
U_\theta=\sum_{z\in\{0,1\}^L}u_z(\theta)Z^z.
```

The random conjugations multiply each term by a binary character. Averaging the key cancels cross terms between different $`z`$, producing a probability mixture of phase errors $`Z^z`$. The distribution remains correlated through $`\theta`$.

Let $`W`$ count inner blocks with a nonidentity phase error. The marginal block bound implies

```math
\mathbb EW\le Ntm^2\delta^2.
```

A classical binary linear code in the Hadamard basis corrects these phase errors. If its minimum distance exceeds $`2rw`$, it corrects every pattern with at most $`w`$ affected inner blocks, since such a pattern has at most $`rw`$ phase flips. Choosing $`w=\lfloor\alpha N\rfloor`$ gives

```math
\epsilon\le\Pr(W>w)
\le\frac{\mathbb EW}{w+1}
\le\frac{tm^2\delta^2}{\alpha}.
```

This first-moment inequality requires no independence between blocks. The [outer-code proof](../science/lifetime.md#a-finite-outer-code-construction) supplies a parity-check existence argument with asymptotic rate at least $`(r/m)[1-h_2(2\alpha)]`$. Taking $`m`$ large and then $`\alpha`$ small reaches every prescribed rate below one. Taking $`t`$ to be a sufficiently small positive multiple of $`\delta^{-2}`$ reaches any fixed error tolerance.

### A complete phase-correction example inside that construction

The smallest illustrative classical code is $`\{000,111\}`$, with parity-check matrix

```math
H=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}.
```

Its Hadamard-basis quantum encoding sends a qubit to

```math
\alpha|+++\rangle+\beta|---\rangle.
```

A phase error $`Z^z`$ becomes the bit shift $`z`$ after applying a Hadamard to each carrier. For $`z=000,100,010,001`$, the syndromes $`Hz`$ are respectively $`00,10,11,01`$. They identify no error or the location of a single phase error. The syndrome has the same value for both shifted codewords, because $`H000=H111=0`$. Measuring it therefore preserves the superposition coefficients. Undo the identified shift and decode $`000`$ and $`111`$ to $`0`$ and $`1`$.

This code corrects one phase error; it is not a code for an arbitrary one-qubit error. The lifetime proof uses larger classical codes and counts whole inner blocks, but the coherent syndrome mechanism is exactly this one. All syndrome extraction takes place at terminal recovery. The [verification example](../verification/README.md) evaluates a larger code under the actual correlated distribution.

Together, the converse and construction establish

```math
T_{R,\epsilon}^{(n)}(\delta)=\Theta_{R,\epsilon}(\delta^{-2})
```

for every fixed $`0\lt R<1`$, $`0<\epsilon<1`$, and sufficiently large $`n`$. The constants depend on rate and tolerated error; the statement does not optimize them.

## The calibration-information argument

For a binary profile $`g_j=g_0+\delta s_j`$, use the uniform prior on $`S\in\{-1,+1\}^n`$. The attenuation is now $`\cos(2\delta\theta)`$. Define

```math
\ell(\theta)=\log_2(1+|\cos(2\delta\theta)|),
\qquad c_\theta=2^{n\ell(\theta)}.
```

There are two separate ways to charge advice. A hard alphabet of size $`M`$ costs $`B=\log_2M`$ bits. A possibly stochastic or continuous transcript costs

```math
\mathcal I=I(S:C\mid K)
```

under the specified prior. The latter is defined by relative entropy of classical probability laws, not by differential entropy.

### A menu of endpoint codes

For fixed key, let $`f_c(s,\theta)`$ be the fidelity of the code selected by transcript $`c`$. Since $`0\le P(c\mid s)\le1`$,

```math
\mathbb E_S\sum_cP(c\mid S)f_c(S,\theta)
\le\sum_c\mathbb E_S f_c(S,\theta)
\le\frac{M c_\theta}{D}.
```

The code for any one $`c`$ is held fixed while its profile average is taken. Cap the expression by one and average the phase and key to obtain the [hard-bit converse](../science/calibration_rate.md#3-finite-block-hard-bit-converse):

```math
\overline F_e\le
\mathbb E_\Theta\min\{1,2^{B+n\ell(\Theta)-k}\}.
```

This permits compressed global features such as pair parities. It does not assume that calibration reveals individual signs.

### Comparing informative advice with decorrelated advice

The information-budget proof cannot replace $`M`$ by an average message length in that counting argument. Instead it compares two classical laws, passed through the same physical preparation map at a fixed phase:

```math
P=P_KP_SP_{C\mid S,K},
\qquad Q=P_KP_SP_{C\mid K}.
```

Under $`P`$, the transcript may carry information about the profile. Under $`Q`$, it has the same key-conditioned marginal but is independent of the profile. Their relative entropy is exactly $`\mathcal I`$.

For each classical input $`(s,c,k_0)`$, the preparation map initializes a maximally entangled test state, applies the endpoint code indexed by $`(c,k_0)`$, and inserts the physical channel for $`s`$ at phase $`\theta`$. Thus both laws pass through the same map; only their statistical correlation differs. Call the output states $`\rho_\theta`$ and $`\sigma_\theta`$. For finite classical records, Watrous's Theorem 5.35 directly gives the data-processing inequality below. For general classical records, the classical-probability-measure and state-preparation version used in [Appendix B](../science/calibration_rate.md#appendix-b-a-calibration-comparison-lemma) gives the same inequality:

```math
D_{\mathrm{rel}}(\rho_\theta\Vert\sigma_\theta)\le\mathcal I.
```

The decorrelated law permits uniform sign averaging separately for every chosen code, so its target-test probability satisfies

```math
g(\theta)=\mathrm{Tr}(\varphi_D\sigma_\theta)
\le\min\{1,c_\theta/D\}.
```

Let $`f(\theta)=\mathrm{Tr}(\varphi_D\rho_\theta)`$ be the actual probability. Applying the same two-outcome target test to both states is another channel. Data processing a second time gives

```math
\mathcal I\ge d_2(f\Vert g)
=f\log_2\frac1g-h_2(f)-(1-f)\log_2(1-g).
```

When $`k>n\ell(\theta)`$, dropping the final nonnegative term gives the direct bound

```math
f(\theta)[k-n\ell(\theta)]-h_2(f(\theta))\le\mathcal I.
```

In particular, $`h_2(f)\le1`$ bounds $`f(\theta)`$ by $`(\mathcal I+1)/(k-n\ell(\theta))`$, capped at one. [The finite information theorem](../science/calibration_rate.md#4-finite-block-information-converse) states the resulting phase integral. Its [comparison lemma](../science/calibration_rate.md#appendix-b-a-calibration-comparison-lemma) also gives the additive form needed for continuous profiles. General classical transcripts are handled through classical relative entropy and the induced state-preparation map; they are not charged by assigning a differential entropy to an analog value.

Conditioning on the shared key cannot be dropped. If signs are written as bits and $`C=S\oplus K`$ with a uniform independent key, then $`I(S:C)=0`$, while the endpoints know all of $`S`$ and $`I(S:C\mid K)=n`$. The conditional definition prices the information actually available to the controls.

### From the finite inequalities to exact and asymptotic statements

At $`\theta_0=\pi/(4\delta)`$, the cosine vanishes and $`c_{\theta_0}=1`$. If a code is perfect after Gaussian averaging at any $`t>0`$, its conditional fidelity is one at every phase: the Gaussian has positive density everywhere, fidelity is at most one, and the conditional fidelity is continuous. Evaluating the two bounds at $`\theta_0`$ therefore gives

```math
D\le M,
\qquad \log_2D\le I(S:C\mid K).
```

This proves the missing arbitrary-code limitation in the two-qubit example. Its parity bit attains equality with $`D=2`$.

For vanishing-error rates, a neighborhood of $`\theta_0`$ replaces the single phase. If the logical rate exceeds the calibration budget per physical qubit, choose a neighborhood on which $`\ell(\theta)`$ is sufficiently small. The hard-bit conditional fidelity then decays with $`n`$ on that event; the information bound keeps conditional fidelity bounded away from one. At fixed positive $`t\delta^2`$, the neighborhood has positive Gaussian probability, so the total error cannot vanish.

The [uniform bad-event bound](../science/calibration_rate.md#appendix-c-a-uniform-gaussian-bad-event-bound) makes this argument valid also for sequences with $`t_n\delta_n^2\ge\tau_*>0`$. This condition matters. When the noise scale tends to zero with $`n`$, a positive-rate uncalibrated register can behave differently.

Matching codes in the signed model $`g_0=0`$ reveal the signs of $`m`$ selected sites. The endpoints apply known $`X`$ conjugations on the negative-sign sites, converting the selected generator to $`\delta\sum_jZ_j`$. An ordinary constant-weight subspace is then protected. Its dimension is $`\binom m{\lfloor m/2\rfloor}`$, giving $`m-O(\log m)`$ logical qubits for $`m`$ calibration bits. For two positive coupling values, separate the selected sites into the two calibrated classes and fix the weight within each class. If their sizes are $`m_+`$ and $`m_-`$, the dimension obeys

```math
\binom{m_+}{\lfloor m_+/2\rfloor}
\binom{m_-}{\lfloor m_-/2\rfloor}
\ge\frac{2^m}{(m+1)^2}.
```

A common payload dimension can be chosen below this bound for every transcript. The remaining ceiling is the physical carrier dimension: after transmission through $`n`$ quantum carriers, the reference–payload state has entanglement rank at most $`2^n`$ on each classical branch. Proposition 6.15 bounds its target overlap by $`2^n/D`$, so reliable rate cannot exceed one; [Appendix A](../science/calibration_rate.md#appendix-a-classical-records-and-the-physical-carrier) includes this argument. Combining the information obstruction, this ceiling, and the exact codes gives reliable rate $`\min\{b,1\}`$ for a hard-bit or conditional-information budget of at most $`bn+o(n)`$.

This is a vanishing-error frontier, not a claim that fidelity approaches zero above it. At weak fixed noise, the obstructing phase neighborhood may have extremely small probability. The fixed-error continuous lifetime theorem addresses a different limit, as quantified on the [interpretation page](../science/interpretation.md).

## What is imported and what is proved here

Watrous provides a coherent foundation for channel representations, complete positivity, reference-complete error, entropy, and entanglement. The proof-specific connections are as follows.

| Role | Ingredient | Attribution and location |
|---|---|---|
| Textbook foundation | Choi/complete-positivity equivalence, channel norms, Schur positivity, relative-entropy data processing, separability | The verified Watrous locators above |
| Inherited memory method | Comparing a Schur channel with complete dephasing; storing in a densely occupied spectral interval | [Quantum-Spectral-Memory, pinned source](https://github.com/GoGoKo699/Quantum-Spectral-Memory/blob/ee5dc0e5529c7775bfaeabb2a5e744c51eb9431d/science/spectral_law.md) |
| Inherited construction approach | Protected inner blocks, endpoint randomization, and an outer code | [Inhomogeneous-Collective-Memory, pinned source](https://github.com/GoGoKo699/Inhomogeneous-Collective-Memory/blob/b6bbf3cae33b300d0c793628e168616dc4919bdc/science/model.md) |
| Derivation supplied here | Cosine and sinc profile averages; hard-menu and decorrelated-advice bounds; exact and reliable calibration frontiers | [Calibration proof](../science/calibration_rate.md), including its appendices |
| Derivation supplied here | The uniform fixed-error lifetime order, explicit classical phase-code existence, and the correlated first-moment bound | [Lifetime proof](../science/lifetime.md) |
| Model-specific benchmark | Known-profile spectral storage and an explicit finite-precision calibration scheme | [Supplied-coupling memory](../science/calibrated_memory.md) |

The known-profile comparison explains the physical value of calibration. If the spectrum of a supplied generator contains many eigenvalues in a width-$`w`$ interval, their span has half-diamond error at most $`tw^2/4`$. Counting spectral cells gives a code with

```math
D\ge\frac{2^n}{1+G_1\sqrt{t/\epsilon}},
\qquad G_1=\sum_j|g_j|.
```

For bounded couplings and polynomial storage times, this permits a rate approaching one. The code depends on the profile. Supplying a finite-precision description is an explicit additional resource, whose sufficient cost is analyzed on the benchmark page; the full continuous-profile information tradeoff remains unresolved.

The project does not introduce data processing, decoherence-free subspaces, phase-error correction, or the general outage idea. Its statements combine those tools within a specified passive interface and price the retained description of an extensive static coupling profile. [Related work](../references/related_work.md) preserves the relevant research comparisons, including earlier studies of calibration and incomplete noise knowledge.

Three boundaries remain visible throughout the route. Calibration information is not the experimental cost of acquiring it. A single growing correlated register is not an independently repeated fixed channel of the kind defined in Watrous's §8.2.1. Permitting controls during storage changes the problem: the [control comparison](../science/interpretation.md) shows explicitly why the passive theorem should not be transferred to that setting.

For exact hypotheses and constants, return to the [model](../science/model.md), [lifetime theorem](../science/lifetime.md), and [calibration theorem](../science/calibration_rate.md). The [verification guide](../verification/README.md) distinguishes finite numerical checks from the analytical arguments that establish the all-code and asymptotic statements.
