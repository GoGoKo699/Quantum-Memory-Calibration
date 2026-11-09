# Calibration information and protected storage rate

A single fluctuating field can preserve an extensive quantum payload when its spatial couplings are known. This page asks how much information about those couplings the endpoint controls need.

For couplings drawn from two known values, the answer is exact at the level of asymptotic rates: one bit of information about the spatial profile is necessary per reliably stored logical qubit, and this cost is attainable. The information can be a nonlinear, stochastic, or continuous calibration transcript. The converse covers arbitrary endpoint encoding and recovery, including classical encoder records and probe qubits inside the physical register.

The rate statement concerns one growing, passively stored register. Its noise parameter $t\delta^2$ is fixed and positive, or uniformly bounded below along the sequence of registers. The separate [lifetime theorem](lifetime.md) treats fixed error and interval uncertainty in the couplings.

## 1. Model and calibration costs

The general operational definitions are in [the model](model.md). Here the unknown profile has the form

$$
A_s=\sum_{j=1}^n (g_0+\delta s_j)Z_j,
\qquad
s\in\{-1,+1\}^n,
\qquad
\delta>0.
$$

The two coupling values $g_0-\delta$ and $g_0+\delta$ are known. In particular, $g_0>\delta$ makes both values positive. The signed model is the special case $g_0=0$.

During a storage interval of length $t$, the channel is

$$
\Phi_{s,t}(\rho)
=
\mathbb E_{\Theta\sim N(0,t)}
U_{s,\Theta}\rho U_{s,\Theta}^{\dagger},
\qquad
U_{s,\theta}=e^{-i\theta A_s}.
$$

The spatial vector $s$ is fixed throughout the interval. The Gaussian phase is independent of the pre-storage calibration procedure.

A calibration transcript $C$ is produced before the unknown payload is supplied. An independent shared random key $K$ is allowed, and the transcript may have any conditional law $P_{C|S,K}$. Every dependence of the endpoint protocol on the unknown profile must pass through $C$. The endpoints may depend freely on the known parameters $n,t,g_0,\delta$.

For each $(c,k)$, an encoder maps a $D$-dimensional payload into the $n$ physical qubits and an optional classical record $X$. A terminal recovery acts jointly on the stored qubits and that record. All quantum systems that persist across the storage interval belong to the $n$-qubit register. In-register probes, entangled encodings, and arbitrary joint recoveries are allowed. A profile-dependent quantum program or analog control outside $C$ is not an additional free resource in this model.

The guaranteed error is the worst-profile half-diamond distance of the logical channel after averaging the calibration randomness and the independent key:

$$
\varepsilon
=
\sup_s
\frac12\left\|
\Lambda_s-\operatorname{id}_D
\right\|_\diamond.
$$

The guarantee is not required separately for every key or calibration outcome. Success and failure outcomes are included in the logical channel; conditioning on an uncharged postselection event is not the task.

For the converse, put the uniform prior on the static vector $S$. This prior does not replace the worst-profile task by a different noise model: a uniform guarantee must also hold after this average. We use two distinct calibration costs.

* **Hard-bit cost.** For each fixed key $k$, the transcript has at most $M$ possible values. Its cost is $B=\log_2M$.
* **Information cost.** The cost is

  $$
  J=I(S:C\mid K).
  $$

  This is the information acquired about the uniform spatial profile, measured in bits. The alphabet of $C$ need not be finite.

The conditioning on $K$ is essential. Identify the sign vector with its binary label. If $K$ is a uniform independent $n$-bit string and $C=S\oplus K$, then $I(S:C)=0$, although the endpoints recover all of $S$ from $(C,K)$. The correct cost is $I(S:C\mid K)=n$.

Hard-bit cost always bounds information cost:

$$
J\le H(C\mid K)\le \log_2M.
$$

The two budgets are not interchangeable at fixed error. A protocol can reveal a large amount of calibration information on a small fraction of runs. Its hard alphabet remains large while its mean information cost is small.

Let $\varphi_D$ denote the projector onto a maximally entangled state of the payload and an untouched reference. We use entanglement fidelity in the overlap convention:

$$
F_e(s)
=
\operatorname{Tr}\!\left[
\varphi_D
(\operatorname{id}\otimes\Lambda_s)(\varphi_D)
\right],
\qquad
\overline F_e=2^{-n}\sum_s F_e(s).
$$

Thus $\varepsilon\ge 1-\overline F_e$. Write $k=\log_2D$ for the number of logical qubits represented by the payload dimension.

## 2. Conditional sign average

Define the one-qubit dephasing channel $\mathcal D_\lambda$ by leaving diagonal entries unchanged and multiplying off-diagonal entries by $\lambda\in[-1,1]$. At a fixed phase,

$$
2^{-n}\sum_s
U_{s,\theta}\rho U_{s,\theta}^{\dagger}
=
V_\theta\,
\mathcal D_{\lambda(\theta)}^{\otimes n}(\rho)
\,V_\theta^\dagger,
$$

where

$$
V_\theta=e^{-i\theta g_0\sum_j Z_j},
\qquad
\lambda(\theta)=\cos(2\delta\theta).
$$

The factor of two comes from the two eigenvalues of $Z$: averaging $e^{-2i\delta s_j\theta}$ over $s_j=\pm1$ gives $\cos(2\delta\theta)$.

Let $\Delta_n$ be complete dephasing in the computational basis. The Schur matrix of $\mathcal D_\lambda$ is

$$
Q_\lambda=
\begin{pmatrix}
1&\lambda\\
\lambda&1
\end{pmatrix}.
$$

Its largest eigenvalue is $1+|\lambda|$. The tensor-product Schur matrix therefore satisfies

$$
Q_\lambda^{\otimes n}
\le
(1+|\lambda|)^n I_{2^n}.
$$

A Schur multiplier is completely positive exactly when its multiplier matrix is positive semidefinite. Consequently,

$$
V_\theta\mathcal D_{\lambda(\theta)}^{\otimes n}(\,\cdot\,)V_\theta^\dagger
\le_{\mathrm{CP}}
c_\theta\Delta_n,
\qquad
c_\theta=(1+|\cos(2\delta\theta)|)^n.
$$

Here $\mathcal A\le_{\mathrm{CP}}\mathcal B$ means that $\mathcal B-\mathcal A$ is completely positive. The diagonal unitary $V_\theta$ leaves $\Delta_n$ unchanged.

This is the Schur-channel comparison used in [Quantum-Spectral-Memory, Lemma 2](https://github.com/GoGoKo699/Quantum-Spectral-Memory/blob/ee5dc0e5529c7775bfaeabb2a5e744c51eb9431d/science/spectral_law.md). Its role here is to compare each conditional sign-averaged channel with an entanglement-breaking one.

Composing $\Delta_n$ with any allowed encoder and recovery gives a state separable between the untouched reference and the decoded payload. Classical encoder records do not change this fact. Every such state has overlap at most $1/D$ with $\varphi_D$. Details of this point are given in [Appendix A](#appendix-a-classical-records-and-the-physical-carrier).

For later use, set

$$
L(\theta)=\log_2(1+|\cos(2\delta\theta)|),
\qquad
0\le L(\theta)\le1.
$$

## 3. Finite-block hard-bit converse

**Theorem 1.** For any allowed protocol whose calibration alphabet has size at most $M$ for every independent key,

$$
\overline F_e
\le
\mathbb E_{\Theta\sim N(0,t)}
\min\!\left\{
1,\,
\frac{M\,2^{nL(\Theta)}}{D}
\right\}.
$$

The bound applies to both signed couplings and two positive coupling values.

**Proof.** Fix $\theta$ and a key value $k_0$. Let $f_{c,k_0}(s,\theta)$ be the entanglement fidelity of the corresponding endpoint code, with any input-dependent classical encoder outcomes already averaged. It lies in $[0,1]$. Therefore

$$
\begin{aligned}
f_{k_0}(\theta)
&=
2^{-n}\sum_s\sum_c
P(c\mid s,k_0)
f_{c,k_0}(s,\theta)
\\
&\le
\sum_c 2^{-n}\sum_s
f_{c,k_0}(s,\theta)
\\
&\le
\frac{M c_\theta}{D}.
\end{aligned}
$$

The first inequality uses only $P(c\mid s,k_0)\le1$. The second applies the conditional sign average and its CP comparison to each fixed endpoint code. Since also $f_{k_0}(\theta)\le1$, averaging over the independent key and then over $\Theta$ proves the claim. $\square$

The transcript may describe a compressed global feature of $s$, select among unrelated codes, or arise from a stochastic experiment. It need not reveal individual signs.

## 4. Finite-block information converse

**Theorem 2.** Let $J=I(S:C\mid K)$, and suppose $D>1$. At a fixed phase, let $f(\theta)$ be the actual entanglement fidelity averaged over $S,C,K$. Whenever $k>nL(\theta)$,

$$
f(\theta)\,[k-nL(\theta)]
-h_2(f(\theta))
\le J.
$$

In particular, define

$$
H_{n,k,J}(\ell)=
\begin{cases}
\displaystyle
\min\!\left\{1,\frac{J+1}{k-n\ell}\right\},
& k>n\ell,
\\[6pt]
1,
& k\le n\ell.
\end{cases}
$$

Then

$$
\overline F_e
\le
\mathbb E_\Theta
H_{n,k,J}(L(\Theta)).
$$

Here $h_2$ is binary entropy in bits. The statement allows a continuous transcript.

**Proof.** Keep $\theta$ fixed. Let $\rho_\theta$ be the final reference–payload state under the actual joint law

$$
P_K P_S P_{C|S,K}.
$$

Construct $\sigma_\theta$ by using the same endpoint maps but the decorrelated law

$$
P_K P_S P_{C|K}.
$$

These are outputs of the same physical preparation map applied to two classical input distributions. Relative-entropy data processing gives

$$
D_{\mathrm{rel}}(\rho_\theta\Vert\sigma_\theta)
\le I(S:C\mid K)=J.
$$

Under the decorrelated law, the sign average can be taken separately for every selected code. The CP comparison in Section 2 therefore bounds the target overlap of $\sigma_\theta$:

$$
g(\theta)
:=
\operatorname{Tr}(\varphi_D\sigma_\theta)
\le
\min\{1,c_\theta/D\}.
$$

Apply the binary measurement $\{\varphi_D,I-\varphi_D\}$ to both states. Another use of data processing gives

$$
J
\ge d_2(f(\theta)\Vert g(\theta)),
$$

where $d_2$ denotes relative entropy of Bernoulli distributions. If $c_\theta<D$, then

$$
\begin{aligned}
d_2(f\Vert g)
&=
f\log_2\frac1g
-h_2(f)
-(1-f)\log_2(1-g)
\\
&\ge
f\log_2(D/c_\theta)-h_2(f).
\end{aligned}
$$

This proves the first inequality. Using $h_2(f)\le1$, capping by one, and integrating over the Gaussian phase gives the explicit bound. Zero-probability cases follow by the usual relative-entropy conventions. $\square$

The same argument applies to a general profile prior and is recorded in [Appendix B](#appendix-b-a-calibration-comparison-lemma). That appendix also gives the additive information form used for the continuous-profile lifetime bound.

## 5. Exact asymptotic calibration rate

Consider a sequence of registers with known parameters $t_n,\delta_n,g_{0,n}$ and payload dimensions $D_n$. The unknown profile still consists of $n$ independent binary choices for the converse prior. Write

$$
v_n=t_n\delta_n^2,
\qquad
k_n=\log_2D_n.
$$

**Theorem 3.** Suppose $v_n\ge v_*>0$ for all sufficiently large $n$. With vanishing worst-profile half-diamond error, either calibration constraint

$$
\limsup_{n\to\infty}\frac{\log_2M_n}{n}\le b
\qquad\text{or}\qquad
\limsup_{n\to\infty}\frac{I(S_n:C_n\mid K_n)}{n}\le b
$$

implies

$$
\limsup_{n\to\infty}\frac{k_n}{n}
\le \min\{b,1\}.
$$

For every $b\ge0$, the rate $\min\{b,1\}$ is attainable with an exact, zero-error code and either calibration budget. This holds for signed couplings and for two known positive coupling values.

**Converse.** First, the physical carrier gives the upper bound one. Even with classical encoder records, a $2^n$-dimensional persistent quantum system can produce target entanglement fidelity at most $\min\{1,2^n/D_n\}$. Thus vanishing error implies $k_n\le n+o(1)$; see Appendix A.

Suppose a subsequence instead has a rate limit $R>b$, with $R\le1$. Choose

$$
0<\ell<R-b,
\qquad
a=2^\ell-1\in(0,1).
$$

For $X_n=\delta_n\Theta_n\sim N(0,v_n)$, consider

$$
E_\ell
=
\{x:|\cos(2x)|\le a\}.
$$

On this event, $L(\Theta_n)\le\ell$. The event is periodic, and [Appendix C](#appendix-c-a-uniform-gaussian-bad-event-bound) proves that

$$
\inf_{v\ge v_*}\Pr_{X\sim N(0,v)}(X\in E_\ell)>0.
$$

For the hard-bit budget, Theorem 1 makes the conditional fidelity on this event vanish exponentially along the subsequence because

$$
\log_2M_n+n\ell-k_n
\le -n(R-b-\ell-o(1)).
$$

For the information budget, Theorem 2 instead gives

$$
\limsup_{n\to\infty}
\sup_{\theta:\,L_n(\theta)\le\ell}
f_n(\theta)
\le
\frac{b}{R-\ell}
<1
$$

uniformly over the same event, where the displayed inequality is understood through the finite bound with $J_n+1$. In either case, an event with uniformly positive probability carries a fidelity deficit bounded away from zero. Hence $\overline F_e$ cannot approach one. This contradicts vanishing worst-profile error. Applying this argument to any violating subsequence proves the upper bound. $\square$

For fixed $t>0$ and $\delta>0$, the argument simply uses a neighborhood of $\theta=\pi/(4\delta)$. The periodic Gaussian estimate is what makes the result uniform when $t_n\delta_n^2$ varies or diverges.

More quantitatively, for fixed $t,\delta$ and hard-bit rates $k_n/n\to R$ and $\limsup \log_2M_n/n\le b<R$,

$$
\liminf_{n\to\infty}(1-\overline F_e)
\ge
\Pr_{\Theta\sim N(0,t)}
\left[
\log_2(1+|\cos(2\delta\Theta)|)<R-b
\right].
$$

This follows by applying Theorem 1 first on events with a strict rate margin and then increasing those events to the displayed open set. It is an error-floor bound, not a claim that fidelity tends to zero. The finite verification report evaluates this probability to show its dependence on $t\delta^2$.

### Subset construction for signed couplings

Reveal the signs on $m$ predetermined physical sites. This uses $m$ hard bits and exactly $m$ information bits under the uniform prior. Conjugate the selected sites by $X$ where their sign is negative, so their generator becomes

$$
\delta\sum_{j=1}^m Z_j.
$$

Encode into the computational-basis subspace of Hamming weight $\lfloor m/2\rfloor$. Its dimension is

$$
D_m=\binom{m}{\lfloor m/2\rfloor},
\qquad
\log_2D_m\ge m-\log_2(m+1).
$$

Every vector in this subspace has the same generator eigenvalue. The unused qubits are fixed in computational-basis states, so their contribution is also scalar on the code. Every phase realization therefore acts by an irrelevant scalar phase, and the logical channel is exactly the identity for all $s$ and all storage times.

Taking $m=\min\{n,\lfloor bn\rfloor\}$ gives the claimed asymptotic rate.

### Subset construction for two positive coupling values

When $g_0\ne0$, the preceding $X$ homogenization does not remove the known center uniformly: it also changes the sign of the $g_0Z_j$ term. Instead, reveal the signs on $m$ sites and separate those sites into their two known coupling classes.

If the class sizes are $m_+$ and $m_-$, use a constant-Hamming-weight subspace within each class. The product dimension is

$$
d(s)
=
\binom{m_+}{\lfloor m_+/2\rfloor}
\binom{m_-}{\lfloor m_-/2\rfloor}.
$$

Both class generators are scalar on this product space. Uniformly over all class splits,

$$
d(s)
\ge
\frac{2^m}{(m_++1)(m_-+1)}
\ge
\frac{2^m}{(m+1)^2}.
$$

Choose the same payload dimension for every transcript, for example a power of two with

$$
k_m
=
\max\!\left\{
0,\,
\left\lfloor m-2\log_2(m+1)\right\rfloor
\right\}.
$$

Each advice-selected product space contains such a subspace. It stores $k_m=m-O(\log m)$ logical qubits exactly at every time. Thus the asymptotic frontier also holds when both couplings are strictly positive.

## 6. Exact finite-block information cost

**Theorem 4.** Suppose $t>0$ and $\delta>0$. If a protocol stores a $D$-dimensional payload perfectly for every spatial sign vector, then

$$
D\le M
$$

under a hard alphabet budget, and

$$
\log_2D\le I(S:C\mid K)
$$

under the information budget.

These inequalities hold for both signed and two-positive-value couplings.

**Proof.** Perfect storage gives $\overline F_e=1$. The conditional fidelity $f(\theta)$ is bounded above by one and is continuous in $\theta$. Continuity follows uniformly over the endpoint choices from finite-dimensional continuity of $e^{-i\theta A_s}$ and contractivity of channels; all generators satisfy $\|A_s\|\le n(|g_0|+\delta)$. Averaging arbitrary classical transcripts and keys preserves this continuity.

The Gaussian has a strictly positive density everywhere. Therefore $\mathbb E_\Theta f(\Theta)=1$ implies $f(\theta)=1$ for every real $\theta$. In particular, at

$$
\theta_0=\frac{\pi}{4\delta},
$$

the sign-averaged conditional channel is complete dephasing, so $c_{\theta_0}=1$.

The hard-bit proof then gives $1\le M/D$. For the information bound, apply the direct binary test in Theorem 2 at $f(\theta_0)=1$:

$$
J\ge d_2(1\Vert g(\theta_0))
=\log_2\frac1{g(\theta_0)}
\ge\log_2D.
$$

This uses the binary relative entropy itself, not the relaxed $h_2(f)\le1$ estimate. $\square$

### Exact saturation by pair-parity calibration

In the signed model $g_0=0$, the finite-block bounds are simultaneously tight when $B$ is an integer and $n\ge2B$.

Partition $2B$ sites into pairs and reveal one parity per pair:

$$
P_j=S_{2j-1}S_{2j},
\qquad
j=1,\ldots,B.
$$

For equal signs, use the pair code

$$
\operatorname{span}\{|01\rangle,|10\rangle\}.
$$

For opposite signs, use

$$
\operatorname{span}\{|00\rangle,|11\rangle\}.
$$

In both cases, the selected two-dimensional subspace is annihilated by

$$
\delta(S_{2j-1}Z_{2j-1}+S_{2j}Z_{2j}).
$$

The unknown overall sign of the pair is immaterial. Tensoring the pair codes stores $B$ logical qubits exactly, for every phase and every storage time. The parities are independent uniform bits under the uniform sign prior, so

$$
D=2^B,
\qquad
M=2^B,
\qquad
I(S:C)=B.
$$

The unused sites can again be fixed in computational-basis states.

This particular saturation construction does not extend unchanged to $g_0\ne0$: the opposite-sign pair states $|00\rangle$ and $|11\rangle$ then have different center-term energies. The two-class subset construction proves the same asymptotic frontier for positive couplings; no finite-block parity saturation is claimed there.

## 7. Parameter limits and physical meaning

The static transcript describes the coupling profile. It does not reveal the later random phase. The constructions therefore work for every phase realization, whereas the converse averages that phase only to test whether a universal code can be reliable.

At $\theta_0$, each signed local rotation is, up to a scalar phase, a known phase gate followed by either $I$ or $Z$. The finite perfect-storage bound has the familiar interpretation of recovering quantum coherence with classical information about a dephasing key. Standard data processing, the Schur comparison, and DFS constructions provide the proof ingredients; the result identifies their cost for static spatial calibration. The [related-work account](../references/related_work.md) distinguishes this task from feedback about realized errors and from recovery optimization for a prescribed code.

There are several consequential limits.

* **Vanishing phase variance.** The reliable-rate converse does not cover arbitrary sequences with $t_n\delta_n^2\to0$. For example, in the signed model the unencoded register has half-diamond error at most $n^2t_n\delta_n^2$. If $t_n\delta_n^2=o(n^{-2})$, rate one is attainable with no calibration. This is consistent with the theorem.
* **Small fixed variance.** For very small positive $t\delta^2$, the Gaussian event near complete conditional dephasing can be extremely rare. The converse proves a nonzero error floor at a rate above the calibration budget; it does not rule out useful storage at a larger fixed error.
* **One correlated interval.** The asymptotic statement grows the number of physical qubits in one storage interval. Coding across independently resampled storage intervals is a different channel model.
* **Passive storage.** The register is not controlled during storage. The [model boundary discussion](model.md) explains why allowing during-storage control changes the problem.
* **Information retained versus information acquired experimentally.** $I(S:C\mid K)$ measures profile information supplied to the endpoint protocol. The theorem does not count the time or number of experiments needed to obtain it.

In the signed model $g_0=0$, independent random local $X$ conjugations before and after storage turn every fixed sign profile into the uniform sign average without calibration. This identifies the key-averaged universal channel with

$$
\mathbb E_\Theta
\mathcal D_{\cos(2\delta\Theta)}^{\otimes n}.
$$

Its error floor is a nonergodic effect: a common latent phase selects the dephasing strength for the entire register. This perspective helps explain the rate theorem but is not needed for the arbitrary-code converse.

The continuous-profile [fixed-error lifetime result](lifetime.md) supplies a complementary conclusion. It compares calibrated and uncalibrated lifetimes without relying solely on a vanishing-error limit at a small fixed noise variance. The [calibrated-memory construction](calibrated_memory.md) states the supplied-profile benchmark and its inherited spectral argument.

## Appendix A. Classical records and the physical carrier

Let $\mathcal E_x$ be the completely positive branches of an encoder instrument, with $\sum_x\mathcal E_x$ trace preserving. Applying complete dephasing to every persistent quantum qubit yields a state of the form

$$
\sum_{x,z}
\omega_R^{x,z}
\otimes |z\rangle\langle z|
\otimes |x\rangle\langle x|,
$$

where each $\omega_R^{x,z}$ is positive and the total trace is one. This state is separable between the untouched reference $R$ and all systems available to the recovery. Recovery and classical averaging preserve separability. The same conclusion holds for a continuous record by replacing the sum with an integral.

For a normalized product vector, the overlap with $\varphi_D$ is at most $1/D$ by Cauchy–Schwarz. Convexity gives the same bound for every separable state. This justifies the entanglement-breaking comparison even when the encoder retains a classical record about the payload.

The dimension bound uses the same record decomposition before dephasing. In each branch, the persistent quantum system has dimension $d=2^n$, so the reference–carrier state has Schmidt number at most $d$. A local channel cannot increase Schmidt number. A pure state of Schmidt rank at most $d$ has overlap at most $d/D$ with $\varphi_D$, again by Cauchy–Schwarz; convexity extends this to mixed states. Thus

$$
F_e(s)\le\min\{1,2^n/D\}
$$

for every allowed code, regardless of calibration. If its half-diamond error is at most $\varepsilon<1$, then

$$
\log_2D\le n-\log_2(1-\varepsilon).
$$

No uncounted quantum subsystem is available to bypass this carrier bound.

## Appendix B. A calibration comparison lemma

The following formulation also applies to the continuous-profile model. Let $X$ be a classical profile with a specified prior, $K$ an independent shared key, and $C$ a pre-payload transcript. Put

$$
J_X=I(X:C\mid K).
$$

Fix a latent noise variable $\theta$ independent of the calibration. Suppose the profile-averaged physical channel at this value obeys

$$
\overline{\mathcal N}_\theta
\le_{\mathrm{CP}}
c_\theta\mathcal B_\theta,
$$

where $\mathcal B_\theta$, including the permitted classical encoder record, gives a separable reference–payload output after every fixed endpoint code.

Let $\rho_\theta$ be the actual decoded state and $\sigma_\theta$ its counterpart with $X$ and $C$ conditionally independent given $K$. Then

$$
D_{\mathrm{rel}}(\rho_\theta\Vert\sigma_\theta)\le J_X,
\qquad
\sigma_\theta\le c_\theta\tau_\theta
$$

for a normalized separable state $\tau_\theta$.

The first assertion is data processing from

$$
P_KP_XP_{C|X,K}
\quad\text{to}\quad
P_KP_XP_{C|K}.
$$

It remains valid for continuous variables, with mutual information defined by relative entropy of probability measures. If $J_X$ is infinite, the information bounds are vacuous. For finite $J_X$, quantum data processing also guarantees the needed support inclusion.

For completeness, write $P$ and $Q$ for the two classical laws, and let $\omega_\theta(u)$ be the normalized, finite-dimensional decoded output of the common preparation map at label $u=(x,c,k)$. When $D(P\Vert Q)<\infty$, set $r=dP/dQ$. Then

$$
\rho_\theta=\int r(u)\omega_\theta(u)\,dQ(u),
\qquad
\sigma_\theta=\int\omega_\theta(u)\,dQ(u).
$$

Use the positive-operator extension $D_{\mathrm{rel}}(A\Vert B)=\operatorname{Tr}[A(\log_2A-\log_2B)]$, with the usual support and zero conventions. The integral form of joint convexity, obtained from finite mixtures by approximation and lower semicontinuity, gives

$$
\begin{aligned}
D_{\mathrm{rel}}(\rho_\theta\Vert\sigma_\theta)
&\le\int D_{\mathrm{rel}}(r(u)\omega_\theta(u)\Vert\omega_\theta(u))\,dQ(u)\\
&=\int r(u)\log_2r(u)\,dQ(u)
=D(P\Vert Q)=J_X.
\end{aligned}
$$

This establishes the same comparison for general classical transcripts while the quantum output remains finite dimensional. It does not assign differential entropy to the transcript.

The direct Bell test gives

$$
f_\theta[\log_2D-\log_2c_\theta]
-h_2(f_\theta)
\le J_X
$$

whenever $c_\theta<D$, as in Theorem 2.

A second useful form is

$$
f_\theta\log_2D-h_2(f_\theta)
\le J_X+\log_2c_\theta.
$$

To obtain it, operator monotonicity of the logarithm applied to $\sigma_\theta\le c_\theta\tau_\theta$ gives

$$
\begin{aligned}
D_{\mathrm{rel}}(\rho_\theta\Vert\tau_\theta)
&\le
D_{\mathrm{rel}}(\rho_\theta\Vert\sigma_\theta)
+\log_2c_\theta
\\
&\le J_X+\log_2c_\theta.
\end{aligned}
$$

One may first regularize the comparison operators on their common support and then take the regularization to zero. The Bell overlap of $\tau_\theta$ is at most $1/D$, so binary data processing gives the claimed additive inequality.

After averaging $\theta$, binary entropy concavity yields

$$
\overline F_e\log_2D-h_2(\overline F_e)
\le
J_X+\mathbb E_\theta\log_2c_\theta.
$$

For interval uncertainty, $X=G$ and $c_\theta=(1+|\operatorname{sinc}(2\delta\theta)|)^n$. This is the form used in [the lifetime analysis](lifetime.md).

## Appendix C. A uniform Gaussian bad-event bound

Let $0<a<1$ and

$$
E_a=\{x:|\cos(2x)|\le a\}.
$$

This event has period $P=\pi/2$. Its measure in one period is $\arcsin a>0$.

For $X\sim N(0,v)$, the law of $X$ modulo $P$ has wrapped density

$$
w_v(u)
=
\sum_{j\in\mathbb Z}
\frac{1}{\sqrt{2\pi v}}
\exp\!\left[-\frac{(u+jP)^2}{2v}\right].
$$

Fix $v_*>0$. For any $u$, at least one summand has $|u+jP|\le P/2$, so

$$
w_{v_*}(u)
\ge
\frac{1}{\sqrt{2\pi v_*}}
\exp\!\left[-\frac{P^2}{8v_*}\right]
=:m_* >0.
$$

For $v\ge v_*$, the wrapped Gaussian is the circular convolution of the variance-$v_*$ wrapped Gaussian with the variance-$(v-v_*)$ wrapped Gaussian. Convolution with a probability measure cannot decrease a uniform lower bound. Hence $w_v(u)\ge m_*$ for all $v\ge v_*$.

It follows that

$$
\inf_{v\ge v_*}
\Pr_{X\sim N(0,v)}(X\in E_a)
\ge
\frac{\arcsin a}{\sqrt{2\pi v_*}}
\exp\!\left[-\frac{\pi^2}{32v_*}\right]
>0.
$$

This explicit bound is conservative. Its purpose is to make the rate converse uniform over all sequences whose phase variance is bounded below, including sequences with variance tending to infinity.

## Finite verification

[The deterministic calibration checks](../verification/check_calibration.py) reconstruct the conditional sign average from the physical diagonal unitaries, check its Schur CP bound at positive and negative attenuation, and enumerate every sign pattern for small pair-parity codes. They also check the two-class construction for positive couplings and the conditional-information accounting in the masked-transcript example.

These finite checks test phase conventions, code degeneracies, and resource accounting. The all-size converse and asymptotic rate statements are established by the proofs above. Commands and numerical tolerances belong to [the verification guide](../verification/README.md).
