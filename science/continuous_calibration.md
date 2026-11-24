# Sharp costs of calibrating continuous couplings

How finely must a passive memory be calibrated to store an extensive quantum payload for a growing time? For two known coupling values, reliable storage at fixed nonzero noise requires one hard calibration bit per logical qubit to leading order. For interval-valued couplings, the optimal number of bits per logical qubit grows as half the logarithm of the dimensionless hold time.

[Model](model.md) · [Uncalibrated lifetime](lifetime.md) · [Two-value frontier](calibration_rate.md) · [Supplied spectrum](calibrated_memory.md)

## The two calibration budgets

Use the [passive storage model](model.md) with $`n`$ qubits, $`g_j\in[g_0-\delta,g_0+\delta]`$, and hold time $`t`$. The register sees one unobserved Gaussian phase with variance $`t`$. The code and recovery may be arbitrary joint endpoint channels. They may reserve physical qubits as probes and pass classical encoder records to recovery. An independent key $`K`$ and pre-storage transcript $`C`$ govern all profile-dependent endpoint settings. Conditional on the fixed profile and pre-storage records, the storage phase still has law $`N(0,t)`$.

Let $`\tau=t\delta^2`$ and $`u=\log_2\tau`$. The limit is taken with $`\tau\to\infty`$ and $`u=o(n)`$. Fix a logical rate $`0\lt R\lt 1`$, so the payload dimension is at least $`2^{Rn}`$. For any fixed $`0\lt\epsilon\lt1`$, take the infimum of each budget over protocols whose worst-profile half-diamond error is at most $`\epsilon`$.

| Budget | Optimal leading cost |
| --- | --- |
| $`B=\log_2 M`$, where every key permits at most $`M`$ transcripts | $`(R/2+o(1))n\log_2\tau`$ |
| $`I(\boldsymbol G;C\mid K)`$, with independent uniform $`G_j\in[g_0-\delta,g_0+\delta]`$ for the budget | $`((1-\epsilon)R/2+o(1))n\log_2\tau`$ |

The performance guarantee remains uniform over the entire uncertainty box in both rows. The hard-budget construction achieves error tending to zero. Under a vanishing-error requirement, the mutual-information coefficient also tends to $`R/2`$. A hard budget with leading coefficient strictly below $`R/2`$ forces the worst-profile entanglement fidelity to vanish.

For example, if $`t\delta^2=n^\alpha`$ with fixed $`\alpha\gt0`$, the hard budget is $`(\alpha R/2+o(1))n\log_2 n`$ bits. This charges a reusable description of the device. Acquisition time and the cost of implementing the ideal endpoint operations are separate resources.

## Converse

### Why use a fidelity moment?

Fix one transcript and key, and therefore one encoder and recovery. Write $`f_\theta(\boldsymbol g)`$ for their entanglement fidelity when the field applies the unitary at phase $`\theta`$, and $`f(\boldsymbol g)=\mathbb E_\Theta f_\Theta(\boldsymbol g)`$. The same profile can support a code for many phases. The quantity that controls calibration is how many profiles can support **the same** code.

To bound that fraction, take $`k`$ mathematical copies of the fixed code on independent inputs maximally entangled with references. The profiles are kept identical across copies and the phases $`\Theta_1,\ldots,\Theta_k`$ are independent. The product overlap test has average $`f(\boldsymbol g)^k`$. The copies compute a moment of the original one-use code. The memory protocol itself uses a single interval.

### A single-site Schur matrix for the moment

Condition on the phase vector $`\boldsymbol\theta`$. Regroup the $`nk`$ physical qubits by site. Since the profile prior has independent coordinates, its averaged channel is a tensor product over the $`n`$ sites. In the $`k`$-bit occupation basis at one site, let $`x\in\{0,1\}^k`$ and define the frequency $`u_x=2\delta x\cdot\boldsymbol\theta`$. The Schur matrix at that site is, up to conjugation by a diagonal unitary from $`g_0`$,

```math
S_{xy}=\mathbb E_{V\sim\mathrm{Unif}[-1,1]} e^{iV(u_x-u_y)}
       =\mathrm{sinc}(u_x-u_y).
```

Write $`v(s)_x=e^{isu_x}`$. As $`S=\mathbb E_V v(V)v(V)^\dagger`$ is a Gram matrix, density comparison inside the positive integral yields

```math
S\preceq c_0 H,
\qquad
c_0=\sqrt{\pi/2}\,e^{1/2},
\qquad
H_{xy}=\exp\!\bigl[-(u_x-u_y)^2/2\bigr].
```

Here the density of the uniform variable is at most $`c_0`$ times the standard normal density. If every unit interval contains at most $`J`$ frequencies, counting repeated labels, then $`\|H\|\le (2+\sqrt{2\pi})J`$. To see this, group each row's differences into positive and negative shells of width one. The two shells at distance at least $`\ell`$ contribute at most $`2J e^{-\ell^2/2}`$. Summing over $`\ell\geq0`$ and bounding the sum by one plus its integral gives the stated row-sum bound. The corresponding spectral occupancy estimate comes from [Quantum-Spectral-Memory](https://github.com/GoGoKo699/Quantum-Spectral-Memory/blob/adf4eaf8fa4ff831c12954e9fcb39af010eff7eb/science/spectral_law.md#lemma-3-gaussian-row-sums-from-local-occupancy).

### Bounding the maximum occupancy

Fix an integer $`a\geq1`$ and call a phase vector good if every unit interval contains at most $`2^{a-1}`$ of the frequencies. More than $`2^{a-1}`$ distinct labels in an interval implies that their affine span has rank at least $`a`$. Indeed, an affine space of rank $`r`$ has an injective projection to some $`r`$ coordinate axes and therefore contains at most $`2^r`$ cube vertices.

Choose $`a+1`$ affinely independent labels in such an interval. The matrix $`A`$ of their $`a`$ differences from the first label is integral and has full row rank. The vector $`2\delta A\boldsymbol\Theta`$ has Gaussian covariance $`4\tau AA^{\mathsf T}`$. Its coordinates must all lie in $`[-1,1]`$. By Cauchy–Binet, $`\det(AA^{\mathsf T})\geq1`$. Multiplying the maximum joint density by the box volume and taking the union over tuples gives the bad-event bound

```math
b_k:=\Pr(\text{bad})
\ \leq\ 2^{k(a+1)}(2\pi\tau)^{-a/2}.
```

This is a bound on the most crowded interval anywhere in the spectrum. The rank-based small-box method is related to the estimates used by [Borgs, Chayes, Mertens and Nair](https://arxiv.org/abs/cond-mat/0501760) for random number partitions.

### How many profiles can one code serve?

On the good event, the site Gram norm is at most $`L_a=c_0(2+\sqrt{2\pi})2^{a-1}`$. The profile-averaged $`nk`$-qubit channel is bounded in completely positive order by $`L_a^n`$ times complete dephasing. This follows from the Schur-matrix bound by the identity at each site, followed by tensor multiplication. Complete dephasing leaves only classical information correlated with the reference. This includes any classical records passed around the storage interval, and it leaves the retained output separable from the reference after recovery. Its overlap with the maximally entangled target on dimension $`D^k`$ is at most $`D^{-k}`$.

For any fixed $`s\in(0,1)`$, a profile with $`f(\boldsymbol g)\geq s`$ contributes at least $`s^k-b_k`$ to the good-event product test. The CP bound is uniform in the good phase vector. Thus

```math
\Pr_{\boldsymbol G}\bigl(f(\boldsymbol G)\geq s\bigr)
\ \leq\
\frac{L_a^n}{D^k(s^k-b_k)}
\qquad (b_k\lt s^k).
```

Choose $`k=\lfloor(1/2-\eta)\log_2\tau\rfloor`$ for fixed $`0\lt\eta\lt1/2`$. Then choose $`a`$, independent of $`n,t`$, so that $`1/2-\eta(a+1)\lt(1/2-\eta)\log_2 s`$. The bound on $`b_k`$ gives $`b_k=o(s^k)`$. In particular, the profile fraction for any fixed code is bounded by

```math
2^{-(1/2-\eta)Rn\log_2\tau+O_{s,\eta}(n+\log_2\tau)} .
```

Here we used $`D\geq 2^{Rn}`$ before expanding the floor in $`k`$. The remainder is negligible relative to $`n\log_2\tau`$ for every fixed $`s,\eta`$.

### Charging the transcript

Let $`P`$ be the joint law of $`(\boldsymbol G,C,K)`$. Call $`A_s`$ the event that the code picked by $`(C,K)`$ has fidelity at least $`s`$ at $`\boldsymbol G`$. If the averaged entanglement fidelity is $`\overline F`$, then $`P(A_s)\geq(\overline F-s)/(1-s)`$ whenever $`\overline F\gt s`$. Uniform half-diamond error at most $`\epsilon`$ implies $`\overline F\geq1-\epsilon`$.

**Hard alphabet.** For each key, sum the fixed-code profile bound over at most $`M`$ transcripts. This upper-bounds $`P(A_s)`$ because each stochastic transcript probability is at most one. Any fixed positive fidelity floor thus requires the claimed hard-budget coefficient, using the bound for arbitrary $`\eta\gt0`$. A strictly smaller leading budget makes $`P(A_s)\to0`$ for every fixed $`s\gt0`$. Consequently $`\overline F\to0`$, and so does the infimum of the profile fidelities.

**Conditional mutual information.** Use the reference law $`Q=P_KP_{\boldsymbol G}P_{C\mid K}`$. For each fixed transcript and key under $`Q`$, the profile has its independent uniform law, so $`Q(A_s)`$ is bounded by the same fixed-code fraction. Applying relative-entropy data processing to the event gives

```math
I(\boldsymbol G;C\mid K)
\ \geq\
P(A_s)\log_2\frac{1}{Q(A_s)}-h_2(P(A_s)).
```

The statement includes stochastic or continuous transcripts through relative entropy. Divide by $`n\log_2\tau`$, take the growing-register limit, then let $`\eta\downarrow0`$ and $`s\downarrow0`$. The lower coefficient is $`(1-\epsilon)R/2`$.

## Matching code

### Round only the active blocks

Write $`u=\log_2\tau`$ and, for sufficiently large $`n`$, take

```math
m=\left\lfloor\min\{u^2,\sqrt{nu}\}\right\rfloor,\qquad w=1/u.
```

Then $`u=o(m)`$, $`m=o(n)`$, and $`\log_2 m=o(u)`$. Use $`N`$ active blocks of $`m`$ carriers, chosen in advance and accounted for below. Prepare all other carriers in fixed computational-basis states.

Within each block restrict to the basis vectors of Hamming weight $`\lfloor m/2\rfloor`$, so the known common term proportional to $`g_0`$ has one eigenvalue on the whole sector. Round each scaled centered coefficient $`x_j=\sqrt t(g_j-g_0)`$ to the midpoint of one of $`L=\lceil 2m\sqrt{\tau}/w\rceil`$ equal bins in $`[-\sqrt\tau,\sqrt\tau]`$. The rounding error is at most $`w/(2m)`$ per site. The transcript consists of these bin indices at the active sites.

The resulting estimated spectrum in one constant-weight sector fits in $`[-m\sqrt\tau,m\sqrt\tau]`$. Split that interval into $`L`$ bins of width at most $`w`$, using a fixed rule on boundaries. Pick a most populated bin and retain a predetermined power-of-two number of its eigenstrings. For every transcript the number of qubits in that inner code can be the same integer

```math
r=\left\lfloor
  \log_2\left\lceil \binom m{\lfloor m/2\rfloor}/L\right\rceil
\right\rfloor
=m-O(u+\log_2 m).
```

Every chosen vector is also an actual eigenvector. Each actual scaled eigenvalue differs from its estimate by at most $`w/2`$. The true scaled spectral width of the retained bin is therefore at most $`2w`$, which gives block half-diamond error at most $`w^2`$ by the [spectral interval estimate](calibrated_memory.md#storage-in-a-narrow-spectral-interval).

### Correct correlated block errors

Apply a uniformly random logical $`X`$ mask before storage and undo it at recovery, as in the [lifetime construction](lifetime.md#randomization-yields-a-correlated-phase-error-distribution). Averaging the masks converts the diagonal noise into a phase Pauli channel. Each block has nonidentity probability at most $`w^2`$. The total number $`W`$ of affected blocks therefore obeys $`\mathbb E W\leq Nw^2`$, including when the same field strongly correlates all the errors.

A binary linear code in the Hadamard basis can correct every phase pattern supported on at most $`\lfloor wN\rfloor`$ blocks. The corresponding Hamming weight on $`rN`$ inner bits is at most $`r\lfloor wN\rfloor`$. A classical parity check of redundancy at most $`\lceil rN h_2(2w)\rceil+1`$ can be chosen with minimum distance greater than twice that weight. This is the [same parity-check argument](lifetime.md#a-finite-outer-code-construction) as for the uncalibrated lifetime. The decoded half-diamond error is at most

```math
\Pr(W\gt\lfloor wN\rfloor)
\ \leq\ \frac{N w^2}{\lfloor wN\rfloor+1}
\ \leq\ w .
```

The construction retains $`1-o(1)`$ logical qubits per active carrier. Take the smallest number of blocks for which the dimension lower bound fits $`\lceil Rn\rceil`$ qubits. Block rounding costs at most $`m=o(n)`$ sites, so $`Nm=Rn+o(n)`$ and the protocol fits in the register for all sufficiently large $`n`$. A fixed truncation gives the required logical dimension. The per-active-carrier budget is $`\log_2 L=u/2+O(\log_2m+\log_2u)`$, proving the hard upper cost with error vanishing as $`w\to0`$.

### Fixed-error information budget

Let $`\epsilon'_n=o(1)`$ be the worst-profile error bound of this reliable code. With profile-independent probability $`p_n=(1-\epsilon)/(1-\epsilon'_n)`$, supply its calibration record and use it. Otherwise supply a flag and use a fixed output. For sufficiently large $`n`$, this is a valid probability. Since the logical channel is averaged before taking the half-diamond norm, the resulting error is at most $`p_n\epsilon'_n+1-p_n=\epsilon`$ uniformly in the profile.

The flag is independent of $`\boldsymbol G`$. The mutual-information budget therefore charges the reliable calibration only with weight $`p_n`$, giving the coefficient $`(1-\epsilon)R/2`$. The large transcript is still among the possibilities of the hard alphabet.

## Applicability

The resolved frontier is for fixed positive rate below one and diverging subexponential $`t\delta^2`$. Exponential hold times, exact zero-error storage for continuous profiles, and the number of experiments needed to acquire a transcript involve different questions. The construction also relies on ideal endpoint operations and the specified averaging of the independent key. See [related work](../references/related_work.md#continuous-description-cost) for the inherited ingredients and [finite checks](../verification/README.md#continuous-calibration-checks) for small examples of the argument.
