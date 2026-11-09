# Fixed-error lifetime with continuous coupling uncertainty

An extensive passive quantum memory has a dimension-independent lifetime when each spatial coupling is known only within a fixed interval. For every fixed storage rate $0<R<1$ and error tolerance $0<\epsilon<1$, the optimal lifetime scales as $\delta^{-2}$, where $\delta$ is the uncertainty radius. Increasing the number of physical qubits does not change this scaling. A matching construction works even though all errors are driven by the same fluctuating field.

This page proves that statement, gives finite-block bounds, and distinguishes a hard calibration-bit budget from a mutual-information budget. The operational conventions are in [Model and resources](model.md). The sharp reliable-rate law for two possible coupling values is in [Calibration and storage rate](calibration_rate.md); the supplied-profile comparison is in [Memory with supplied couplings](calibrated_memory.md).

## Setting and lifetime statement

The unknown profile belongs to

$$
\mathcal G_n=[g_0-\delta,g_0+\delta]^n,
\qquad \delta>0,
$$

where $g_0$ and $\delta$ are known. The profile $\boldsymbol g$ remains fixed during the passive storage interval. The channel is

$$
\Phi_{\boldsymbol g,t}
=\exp\!\left[-\frac t2[A_{\boldsymbol g},[A_{\boldsymbol g},\cdot]]\right],
\qquad
A_{\boldsymbol g}=\sum_{j=1}^n g_jZ_j.
$$

For a protocol storing a $D$-dimensional payload, write $\mathcal M_{\boldsymbol g,t}$ for its decoded logical channel, including the average over any independent random key. Define

$$
e_{\boldsymbol g,t}
=\frac12\|\mathcal M_{\boldsymbol g,t}-\operatorname{id}_D\|_\diamond,
\qquad
F_e(\boldsymbol g,t)
=\langle\Phi_D|
(\operatorname{id}\otimes\mathcal M_{\boldsymbol g,t})(\Phi_D)
|\Phi_D\rangle.
$$

Here $|\Phi_D\rangle$ is a normalized maximally entangled state, and $\Phi_D$ also denotes its projector. In particular, $e_{\boldsymbol g,t}\le\epsilon$ implies $F_e(\boldsymbol g,t)\ge1-\epsilon$.

Let $T_{R,\epsilon}^{(n)}(\delta)$ be the supremum of storage times for which a protocol with no coupling-dependent calibration transcript has $\log_2D\ge Rn$ and $\sup_{\boldsymbol g\in\mathcal G_n}e_{\boldsymbol g,t}\le\epsilon$, as defined in [the model](model.md). The known center $g_0$ is suppressed in the notation; the bounds below are uniform in it. The endpoints may be arbitrary joint channels, and the permitted independent random keys and classical encoder records remain available.

**Lifetime theorem.** For every $0<R<1$ and $0<\epsilon<1$, there are positive constants $c_{R,\epsilon}$ and $C_{R,\epsilon}$ and an integer $n_0(R,\epsilon)$ such that, for every $n\ge n_0$, every $g_0\in\mathbb R$, and every $\delta>0$,

$$
\frac{c_{R,\epsilon}}{\delta^2}
\le T_{R,\epsilon}^{(n)}(\delta)
\le\frac{C_{R,\epsilon}}{\delta^2}.
$$

The proof supplies the following constants. Choose a block length $m\ge2$ and define

$$
r=\left\lfloor\log_2\binom{m}{\lfloor m/2\rfloor}\right\rfloor
\quad\text{with}\quad \frac rm>R.
$$

Choose $0<\alpha<1/4$ so that, with binary entropy $h_2$,

$$
\beta=1-h_2(2\alpha),
\qquad \rho=\frac{r\beta}{m}>R.
$$

Such choices exist because $\binom{m}{\lfloor m/2\rfloor}\ge2^m/(m+1)$ gives $r/m\to1$ as $m\to\infty$, and $h_2(2\alpha)\to0$ as $\alpha\downarrow0$. One may take

$$
c_{R,\epsilon}=\frac{\epsilon\alpha}{m^2},
\qquad
C_{R,\epsilon}
=\frac{2}{\pi(2^{R/2}-1)^2(1-\epsilon)^2}.
$$

Any integer $n_0$ at least

$$
\max\left\{
m,\ \frac{r\beta+2}{\rho-R},\
\frac2R\log_2\frac{2}{1-\epsilon}
\right\}
$$

suffices. The constants are explicit bounds, not optimized lifetime coefficients.

## A finite-block converse

### Averaging fixed profiles

Use independent uniform random variables $G_j\in[g_0-\delta,g_0+\delta]$ as a converse prior. This averaging does not change the physical assumption that a profile is fixed during storage: a guarantee for every fixed profile must also hold on average over this prior.

The Gaussian representation of the channel is

$$
\Phi_{\boldsymbol g,t}(\omega)
=\mathbb E_{\theta\sim N(0,t)}
e^{-i\theta A_{\boldsymbol g}}\omega e^{i\theta A_{\boldsymbol g}}.
$$

Conditional on $\theta$, averaging the profile gives

$$
\mathcal N_\theta
=\operatorname{Ad}_{U_{0,\theta}^{\otimes n}}
\circ\mathcal D_{\lambda(\theta)}^{\otimes n},
\qquad
U_{0,\theta}=e^{-ig_0\theta Z},
\qquad
\lambda(\theta)=\operatorname{sinc}(2\delta\theta),
$$

where $\operatorname{sinc}(x)=\sin(x)/x$ for $x\ne0$ and $\operatorname{sinc}(0)=1$. The channel $\mathcal D_\lambda$ preserves diagonal entries and multiplies off-diagonal entries by $\lambda$. The scalar characteristic-function calculation is

$$
\mathbb E_G e^{-2i\theta G}
=e^{-2ig_0\theta}\operatorname{sinc}(2\delta\theta).
$$

### Comparison with complete dephasing

Let $\Delta_n$ be complete dephasing in the computational basis. The Schur matrix of $\mathcal D_\lambda^{\otimes n}$ is the tensor power of

$$
\begin{pmatrix}1&\lambda\\\lambda&1\end{pmatrix},
$$

whose largest eigenvalue is $(1+|\lambda|)^n$. The common rotation only conjugates this Schur matrix by a diagonal unitary. Since positivity of a Schur matrix is equivalent to complete positivity of its multiplier,

$$
\mathcal N_\theta
\le_{\mathrm{CP}}(1+|\lambda(\theta)|)^n\Delta_n.
$$

This is the Schur-channel comparison used in [Quantum-Spectral-Memory](https://github.com/GoGoKo699/Quantum-Spectral-Memory/blob/ee5dc0e5529c7775bfaeabb2a5e744c51eb9431d/science/spectral_law.md). Its role here is to bound a code that must work without knowing the spatial profile.

Complete dephasing destroys entanglement between the stored register and an untouched reference. Classical encoder records do not change this fact: after dephasing, the reference, the measured computational-basis label, and all retained classical labels form a classical mixture of product states across the reference/output cut. Terminal recovery preserves separability across that cut. A normalized separable state has overlap at most $1/D$ with $\Phi_D$.

Consequently, any fixed endpoint code has conditional average fidelity at most

$$
\min\left\{1,\frac{(1+|\operatorname{sinc}(2\delta\theta)|)^n}{D}\right\}.
$$

The statement includes arbitrary joint recovery and any physical qubits reserved as probes.

### Stochastic calibration with a hard alphabet

Suppose a pre-storage classical transcript $C$ has at most $M$ possible values, conditional on each independent shared key. It selects the endpoint code. For a fixed key, let $f_c(\boldsymbol g,\theta)$ be the fidelity of code $c$. Since $0\le p(c|\boldsymbol g)\le1$,

$$
\begin{aligned}
\mathbb E_{\boldsymbol G}\sum_c
p(c|\boldsymbol G)f_c(\boldsymbol G,\theta)
&\le\sum_c\mathbb E_{\boldsymbol G}f_c(\boldsymbol G,\theta)\\
&\le\frac{M(1+|\operatorname{sinc}(2\delta\theta)|)^n}{D}.
\end{aligned}
$$

Averaging the key preserves the bound. Thus, with $\overline F_e$ denoting fidelity averaged over the profile prior, transcript, and independent key,

$$
\boxed{
\overline F_e
\le\mathbb E_{\theta\sim N(0,t)}
\min\left\{1,
\frac{M(1+|\operatorname{sinc}(2\delta\theta)|)^n}{D}
\right\}.}
$$

No calibration is the special case $M=1$. An independent key does not contribute to $M$; a key-dependent, coupling-dependent transcript still does.

### An explicit time bound

Write

$$
B=\log_2M,
\qquad s=\frac{\log_2D-B}{n}>0,
\qquad \tau=t\delta^2,
\qquad a_s=\frac{\sqrt{2/\pi}}{2(2^{s/2}-1)}.
$$

Then the integral bound implies

$$
\boxed{\overline F_e\le
\min\{1,\ a_s\tau^{-1/2}+2^{-sn/2}\}.}
$$

To prove this, set $X=\delta\theta\sim N(0,\tau)$ and

$$
x_s=\frac1{2(2^{s/2}-1)}.
$$

For $|X|\ge x_s$, the inequality $|\operatorname{sinc}(2X)|\le1/(2|X|)$ makes the integrand at most $2^{-sn/2}$. On the remaining interval use the bound one and

$$
\Pr(|X|<x_s)\le\sqrt{\frac2\pi}\frac{x_s}{\sqrt\tau}.
$$

If $\log_2D\ge Rn$ and $B=0$, the same expression with $s=R$ is valid. A uniform error bound $e_{\boldsymbol g,t}\le\epsilon$ therefore gives, whenever $2^{-Rn/2}<1-\epsilon$,

$$
t\delta^2
\le\frac{1}{
2\pi(2^{R/2}-1)^2
(1-\epsilon-2^{-Rn/2})^2}.
$$

For $2^{-Rn/2}\le(1-\epsilon)/2$, this is the upper constant in the lifetime theorem.

## Achievability despite correlated errors

The construction uses constant-magnetization inner blocks, randomization at the endpoints, and an outer phase-error-correcting code. This follows the protected-block/randomization/outer-code approach used in [Inhomogeneous-Collective-Memory](https://github.com/GoGoKo699/Inhomogeneous-Collective-Memory/blob/b6bbf3cae33b300d0c793628e168616dc4919bdc/science/model.md). In the present commuting model, a classical linear code in the Hadamard basis suffices. The proof below gives its finite-size existence bound directly.

### Inner blocks remove the known common coupling

Fix $m,r,\alpha$ as in the theorem, and use

$$
N=\lfloor n/m\rfloor,
\qquad L=rN
$$

inner blocks. Initialize unused physical qubits in a computational-basis state and discard them at recovery.

On each block choose any $2^r$ computational-basis vectors of Hamming weight $\lfloor m/2\rfloor$. They define an isometric encoding of $r$ qubits. The term $g_0\sum_jZ_j$ is scalar on this subspace. Writing $g_j=g_0+\eta_j$ with $|\eta_j|\le\delta$, the restricted generator on block $b$ is a scalar plus a diagonal operator $B_b$ satisfying

$$
\|B_b\|\le m\delta.
$$

The full generator is diagonal, so the chosen inner subspace is exactly invariant for every allowed profile. There is no leakage approximation.

The marginal channel on block $b$ is

$$
\Psi_{b,t}=e^{t\mathcal L_{B_b}},
\qquad
\mathcal L_{B_b}(\omega)
=B_b\omega B_b-\tfrac12\{B_b^2,\omega\}.
$$

Because $\|\mathcal L_{B_b}\|_\diamond\le2\|B_b\|^2$ and a channel has diamond norm one, the integral identity for the semigroup gives

$$
\frac12\|\Psi_{b,t}-\operatorname{id}\|_\diamond
\le t\|B_b\|^2
\le tm^2\delta^2.
$$

This estimate holds for all $t\ge0$. The complete inner-register channel is still correlated: it is the average over one $\theta$ of $\bigotimes_b\operatorname{Ad}_{e^{-i\theta B_b}}$.

### Randomization yields a correlated phase-error distribution

Choose a uniform independent $L$-bit key $a$. Apply the logical Pauli $X^a$ before storage and the same $X^a$ at recovery, using ideal operations within the inner subspaces. Expand the diagonal inner-register unitary as

$$
U_\theta=\sum_{z\in\{0,1\}^L}u_z(\theta)Z^z,
\qquad \sum_z|u_z(\theta)|^2=1.
$$

Conjugation by $X^a$ multiplies $Z^z$ by $(-1)^{a\cdot z}$. Averaging $a$ removes the cross terms with distinct $z$, leaving the channel

$$
\mathcal P(\omega)=\sum_z p_z Z^z\omega Z^z,
\qquad p_z=\mathbb E_\theta|u_z(\theta)|^2.
$$

These probabilities need not factor across blocks. Let $W(z)$ count the blocks whose $r$-bit segment $z_b$ is nonzero. The marginal nonidentity probability on block $b$ is

$$
\Pr(z_b\ne0)=1-F_e(\Psi_{b,t})
\le\frac12\|\Psi_{b,t}-\operatorname{id}\|_\diamond
\le tm^2\delta^2.
$$

Therefore

$$
\mathbb E W\le Ntm^2\delta^2.
$$

Only this first moment is needed. The construction does not replace the common field by independent physical noise.

### A finite outer-code construction

Set $w=\lfloor\alpha N\rfloor$ and

$$
h=\left\lceil Lh_2(2\alpha)\right\rceil+1.
$$

For sufficiently large $N$, $h\le L$. There exists a binary linear code $\mathcal C\subseteq\{0,1\}^L$ of dimension $k\ge L-h$ and minimum distance greater than $2rw$.

For completeness, choose an $h\times L$ binary parity-check matrix $H$ uniformly at random. Each fixed nonzero vector $v$ obeys $\Pr(Hv=0)=2^{-h}$. Since $2rw/L\le2\alpha<1/2$, the Hamming-ball bound gives

$$
\sum_{j=0}^{2rw}\binom Lj
\le2^{Lh_2(2\alpha)}.
$$

The Hamming-ball inequality follows, for $0<p=d/L\le1/2$, by using $p^j(1-p)^{L-j}\ge p^d(1-p)^{L-d}$ for $j\le d$ in the binomial expansion of $(p+1-p)^L$; the case $d=0$ is immediate. The union bound makes the probability that $\ker H$ contains a nonzero vector of weight at most $2rw$ strictly less than one. A suitable $H$ therefore exists, and $\dim\ker H\ge L-h$.

Use the quantum codespace spanned by

$$
\{\mathsf H^{\otimes L}|c\rangle:c\in\mathcal C\},
$$

where $\mathsf H$ is the one-qubit Hadamard gate. It stores $k$ logical qubits and corrects every phase error $Z^z$ of Hamming weight at most $rw$. Indeed, applying $\mathsf H^{\otimes L}$ converts that error to the classical shift $c\mapsto c+z$. Its syndrome is $Hz$, independent of the encoded codeword. Distinct errors of weight at most $rw$ have distinct syndromes, because their difference has weight at most $2rw$. A syndrome measurement and the corresponding shift correction restore every coherent superposition of codewords.

If $W(z)\le w$, then the Hamming weight of $z$ is at most $rw$, so this recovery succeeds exactly.

### Error and rate

The corrected part of the phase-error mixture is the identity channel. Every other branch is a channel, so the half-diamond error is at most its total probability:

$$
\begin{aligned}
\frac12\|\mathcal M_{\boldsymbol g,t}-\operatorname{id}\|_\diamond
&\le\Pr(W>w)\\
&\le\frac{\mathbb EW}{w+1}\\
&\le\frac{tm^2\delta^2}{\alpha}.
\end{aligned}
$$

The last line uses $w+1>\alpha N$. The bound is uniform over every fixed profile. The independent key is used by recovery and then averaged, exactly as specified in [the model](model.md); a maximum-over-key guarantee is not asserted.

The number of stored logical qubits satisfies

$$
k\ge L\beta-2
\ge\rho n-r\beta-2.
$$

Thus $k\ge Rn$ for $n\ge(r\beta+2)/(\rho-R)$. Taking $t\le\epsilon\alpha/(m^2\delta^2)$ proves the lower lifetime bound. The construction uses $L=rN$ independent classical key bits carrying no information about $\boldsymbol g$. It is an existence result with ideal endpoint operations; no efficient compilation claim is needed.

The [seven-block verification](../verification/check_phase_code.py) integrates the joint Gaussian phase-error distribution and applies an actual Hamming syndrome recovery to all $128$ error patterns. It checks the integer-threshold bound above and compares the result with independent errors having the same marginals, illustrating why the proof retains the correlations.

## Calibration information for diverging storage times

### Hard bit budgets

Consider any sequence of protocols with $\tau_n=t_n\delta_n^2\to\infty$. Let the calibration alphabet have size at most $M_n$ and write $B_n=\log_2M_n$. If fidelity remains bounded below by a positive constant uniformly over all profiles, then

$$
\boxed{B_n\ge\log_2D_n-o(n).}
$$

The precise content is that $(\log_2D_n-B_n)_+/n\to0$. Otherwise, some subsequence has a gap at least $sn$ for a fixed $s>0$, and the explicit converse forces its averaged fidelity to zero. This is a necessary condition; it does not establish that $\log_2D_n+o(n)$ bits suffice for general continuous profiles.

### Mutual-information budgets

A noisy or continuous transcript need not have a small alphabet. For the product-uniform profile prior define

$$
I_n=I(\boldsymbol G;C\mid K),
\qquad
J(\tau)=\mathbb E_{Z\sim N(0,1)}
\log_2\left(1+|\operatorname{sinc}(2\sqrt\tau Z)|\right),
$$

where $K$ is independent of $\boldsymbol G$. The calibration comparison lemma in [Appendix B of the rate analysis](calibration_rate.md#appendix-b-a-calibration-comparison-lemma), applied at fixed $\theta$ with comparison factor $(1+|\lambda(\theta)|)^n$, gives

$$
f_\theta\log_2D-h_2(f_\theta)
\le I_n+n\log_2(1+|\lambda(\theta)|).
$$

Averaging $\theta$ and using concavity of $h_2$ yields the finite-block bound

$$
\boxed{
\overline F_e\log_2D-h_2(\overline F_e)
\le I_n+nJ(t\delta^2).}
$$

In particular, uniform half-diamond error at most $\epsilon$ requires

$$
I_n\ge(1-\epsilon)\log_2D-1-nJ(t\delta^2).
$$

For every nonzero $Z$, $\operatorname{sinc}(2\sqrt\tau Z)\to0$ as $\tau\to\infty$. Its logarithmic contribution lies between zero and one, so dominated convergence gives $J(\tau)\to0$. Consequently, for $t_n\delta_n^2\to\infty$,

$$
\boxed{I_n\ge(1-\epsilon)\log_2D_n-o(n).}
$$

The coefficient $1-\epsilon$ must not be removed by identifying mutual information with a worst-case bit budget. A randomized transcript can convey much more information on a small fraction of runs than on the others. The hard alphabet counts every possible transcript; mutual information averages its statistical information. At vanishing error and extensive payload dimension, both converse statements require one calibration bit per logical qubit to leading order, but neither proves an optimal sufficiency theorem for continuous profiles.

## What the lifetime comparison establishes

The lifetime theorem fixes $R$ and $\epsilon$ before sending $n$ to infinity. Its constants are independent of the mean coupling $g_0$, because an inner constant-magnetization sector removes that known collective term. They depend on the uncertainty width through $t\delta^2$.

When the actual profile is supplied to the endpoints, spectral concentration instead supports rate approaching one for subexponential storage times; [the supplied-profile page](calibrated_memory.md) proves the relevant bound and gives a finite-precision implementation. The two statements compare different information resources in the same passive common-field dynamics.

The restriction to a passive interval and to the counted persistent quantum systems is essential. The converse includes probe qubits inside the register and arbitrary final recovery, but it does not cover additional interventions during storage or external retained quantum calibration programs. The attribution and the distinction from earlier noise-adapted codes are developed in [Related work](../references/related_work.md).
