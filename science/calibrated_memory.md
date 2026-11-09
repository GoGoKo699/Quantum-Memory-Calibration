# Memory with supplied couplings

Supplying the spatial coupling profile changes what the same passive common-field dynamics can store. For bounded couplings, an encoder chosen from the known spectrum retains a rate approaching one for every subexponential storage time. This comparison identifies the information resource missing from the universal-code lifetime bound in [Continuous coupling uncertainty](lifetime.md).

The spectral-interval construction is an existing ingredient from [Quantum-Spectral-Memory](https://github.com/GoGoKo699/Quantum-Spectral-Memory/blob/ee5dc0e5529c7775bfaeabb2a5e744c51eb9431d/science/spectral_law.md). It is included here with explicit constants and a finite-precision calibration construction. The common channel and endpoint conventions are those of [the model](model.md).

## Storage in a narrow spectral interval

Let $A$ be a known Hermitian operator and let a code be spanned by its eigenvectors whose eigenvalues lie in an interval of width $w$. The code is invariant under $A$. After subtracting the midpoint of that interval, its restricted generator $B$ satisfies $\|B\|\le w/2$; subtracting a scalar changes no channel.

The restricted Gaussian dephasing channel is

$$
\Psi_t=e^{t\mathcal L_B},
\qquad
\mathcal L_B(\omega)=B\omega B-\tfrac12\{B^2,\omega\}.
$$

The elementary diamond-norm estimates

$$
\|\mathcal L_B\|_\diamond\le2\|B\|^2,
\qquad
\|\Psi_u\|_\diamond=1
$$

and $\Psi_t-\operatorname{id}=\int_0^t\mathcal L_B\Psi_u\,du$ imply

$$
\boxed{
\frac12\|\Psi_t-\operatorname{id}\|_\diamond
\le t\|B\|^2\le\frac{tw^2}{4}.}
$$

This is a channel bound, valid with an arbitrary reference and for every input state in the code. It is not restricted to basis-state fidelities or to a short-time expansion.

## A supplied-profile dimension bound

For the qubit generator

$$
A_{\boldsymbol g}=\sum_{j=1}^n g_jZ_j,
\qquad
G_1=\sum_{j=1}^n|g_j|,
$$

all $2^n$ eigenvalues, counted with multiplicity, lie in $[-G_1,G_1]$. Fix $t>0$ and $0<\epsilon<1$, and partition that interval into

$$
K=\max\left\{1,\left\lceil G_1\sqrt{t/\epsilon}\right\rceil\right\}
$$

cells of width at most $2\sqrt{\epsilon/t}$. Assign boundary eigenvalues to one adjacent cell so that every eigenvector is counted exactly once. At least one cell contains at least $2^n/K$ eigenvectors. Its span gives an exact invariant code with half-diamond storage error at most $\epsilon$ and dimension

$$
\boxed{
D\ge\frac{2^n}{K}
\ge\frac{2^n}{1+G_1\sqrt{t/\epsilon}}.}
$$

The dimension $D$ is an integer; the inequalities are lower bounds on it. If a qubit payload is desired, retain a power-of-two-dimensional subspace. Thus, when $|g_j|\le G$,

$$
\log_2D\ge n-\log_2\left(1+nG\sqrt{t/\epsilon}\right),
$$

and one can store at least

$$
\max\left\{0,
\left\lfloor n-\log_2\left(1+nG\sqrt{t/\epsilon}\right)\right\rfloor
\right\}
$$

logical qubits. No randomness of the supplied couplings is required.

For a sequence of bounded profiles, times $t_n$, and error targets $\epsilon_n$, the condition

$$
\log_2\left(1+nG\sqrt{t_n/\epsilon_n}\right)=o(n)
$$

therefore implies $\log_2D_n/n\to1$. In particular, this holds for fixed $\epsilon>0$ and $t_n=2^{o(n)}$. It also holds with vanishing error whenever $\log_2(1/\epsilon_n)=o(n)$ and $\log_2(1+t_n)=o(n)$.

The encoder depends on the supplied profile. Consequently, this construction does not contradict the dimension-independent lifetime of a single encoder/recovery pair that must handle every profile in an uncertainty interval. Arbitrary ideal endpoint compilation is allowed, as in [the model](model.md); the dimension bound does not assert an efficient spectral-search algorithm.

## An explicit finite-precision calibration scheme

Exact real-valued coupling data is a useful comparison, but finite classical advice also suffices for long storage. The following deterministic construction makes that statement quantitative.

Assume $g_j\in[g_0-\delta,g_0+\delta]$ and set $G=|g_0|+\delta$. For given $n$, $t>0$, and $0<\epsilon<1$, define

$$
a=\sqrt{\epsilon/t},
\qquad
\eta=\frac{a}{2n},
\qquad
L=\max\left\{1,\left\lceil\frac\delta\eta\right\rceil\right\}
=\max\left\{1,\left\lceil2n\delta\sqrt{t/\epsilon}\right\rceil\right\}.
$$

Partition the allowed coupling interval into $L$ equal cells, and let $\widehat g_j$ be the midpoint of the cell containing $g_j$. The transcript is the list of the $n$ cell indices. It has $M=L^n$ possible values and can be represented in

$$
B=\left\lceil n\log_2L\right\rceil
\le n\log_2\left(1+2n\delta\sqrt{t/\epsilon}\right)+1
$$

hard bits. The estimates stay inside the allowed interval and satisfy $|g_j-\widehat g_j|\le\eta$.

Using the supplied estimates, partition the spectrum of $A_{\widehat{\boldsymbol g}}$ into cells of width at most $a$, and choose a most populated cell. Since $|\widehat g_j|\le G$, this produces a code of dimension

$$
D\ge\frac{2^n}{1+2nG\sqrt{t/\epsilon}}.
$$

To keep the payload dimension independent of the transcript, retain exactly

$$
D_* = \left\lceil\frac{2^n}{1+2nG\sqrt{t/\epsilon}}\right\rceil
$$

basis vectors for every transcript. The occupancy bound guarantees that this many are available. A common power-of-two-dimensional subspace may be used instead for a qubit payload.

Choose its basis from computational-basis eigenvectors. It is then invariant under both $A_{\widehat{\boldsymbol g}}$ and the true $A_{\boldsymbol g}$. On every such eigenvector, the discrepancy between the two eigenvalues has magnitude at most

$$
\sum_{j=1}^n|g_j-\widehat g_j|\le n\eta.
$$

Hence the true eigenvalues on the chosen code lie in an interval of width at most

$$
a+2n\eta=2a=2\sqrt{\epsilon/t}.
$$

The spectral-interval bound proves uniform half-diamond error at most $\epsilon$ for every profile consistent with the transcript. Every coupling-dependent endpoint choice factors through these finite cell indices; no uncharged analog setting is needed.

This gives a simple sufficient advice budget

$$
B=O\!\left(n\log\left(1+n\delta\sqrt{t/\epsilon}\right)\right)
$$

and the displayed dimension bound. For fixed bounded couplings, polynomial storage time and inverse-polynomial error require $O(n\log n)$ hard calibration bits while retaining rate approaching one.

## What is and is not tight

The supplied-spectrum construction explains the contrast with unknown continuous couplings: the same spectrum has large narrow intervals, but the encoder must know which eigenvectors lie together in one of them.

The finite-precision scheme is a sufficient construction, not an optimal characterization of the calibration cost. The [continuous-uncertainty converse](lifetime.md#calibration-information-for-diverging-storage-times) requires $\log_2D-o(n)$ hard bits for extensive storage with diverging $t\delta^2$ and fidelity bounded away from zero. The direct rounding scheme can use an additional logarithmic factor in $n$ for polynomial times. That gap is not resolved here.

The [two-value coupling model](calibration_rate.md) has a sharper answer: its reliable storage rate equals the calibration-information rate, capped at one. Exact fixed-magnetization sectors make its achievability possible without increasing the calibration precision with storage time. Continuous coefficient uncertainty lacks that exact discrete simplification.

Noise-adapted codes with supplied unequal couplings were already studied by [Layden, Chen, and Cappellaro](https://arxiv.org/abs/1903.01046). The present use of spectral occupancy is attributed to the prior spectral-memory analysis above. The separate contribution examined in this repository is the resource-sensitive comparison with unknown profiles; [Related work](../references/related_work.md) gives the detailed distinctions.
