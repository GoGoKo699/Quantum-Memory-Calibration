# Efficient compilation at the sharp continuous calibration budget

Does the minimum amount of calibration information also suffice when the encoder and recovery must be compiled efficiently? For one Gaussian dephasing field, the answer is yes at polynomial hold times. The code uses exact integer spectral bands inside fixed-weight sectors, followed by a terminal phase-error recovery.

## Statement

Use the [passive storage model](model.md) with $`n`$ qubits, fixed $`g_j\in[g_0-\delta,g_0+\delta]`$, $`\delta\gt 0`$, and a centered Gaussian field phase of variance $`t`$. Fix a logical rate $`0\lt R\lt 1`$ and write $`\tau=t\delta^2`$. Suppose $`\tau\to\infty`$ and $`\log_2\tau=o(n)`$. For sufficiently large $`n`$, one can store $`\lceil Rn\rceil`$ logical qubits with error, uniformly over the coupling box, at most

```math
\frac12\|\Lambda_{\boldsymbol g}-\mathrm{id}\|_\diamond
\le\frac1{\lfloor\log_2\tau\rfloor},
```

using a hard calibration budget of

```math
B=\left(\frac R2+o(1)\right)n\log_2\tau.
```

The endpoint circuits are uniformly constructible with deterministic preprocessing and gate count polynomial in $`n`$ and $`\sqrt\tau`$. These costs are polynomial in $`n`$ whenever $`\tau`$ is polynomially bounded. The encoder clears all work qubits before storage and uses at most $`n`$ independent uniform classical key bits shared with the recovery. The profile enters the compiler only through the finite transcript. The [continuous calibration converse](continuous_calibration.md#converse) establishes the sharp leading coefficient even for unrestricted endpoint operations. The cost here describes a supplied transcript and ideal endpoint operations. Physical calibration experiments and fault-tolerant overhead are separate resources.

## Exact finite spectral bands

Put $`u=\lfloor\log_2\tau\rfloor`$, $`w=1/u`$, $`m=\lfloor\min\{u^2,\sqrt{nu}\}\rfloor`$, and $`J=2^{\lceil(u+1)/2\rceil}`$. Then $`u=o(m)`$, $`m=o(n)`$, $`\log_2m=O(\log u)`$, and $`\sqrt\tau\le J\le2\sqrt\tau`$. Use $`N`$ blocks of $`m`$ active carriers chosen in advance. Prepare other carriers in fixed computational-basis states.

Divide $`[-1,1]`$ into $`L=2mJu`$ equal cells. Use a fixed convention for shared boundaries and assign the right endpoint to the last cell. At each active site the transcript records the index $`a_j\in\{0,\ldots,L-1\}`$ of the cell containing $`(g_j-g_0)/\delta`$. Its midpoint is $`q_j/L`$, with $`q_j=2a_j+1-L`$. The scaled rounding error at a site is at most $`\sqrt\tau/L\le w/(2m)`$.

Restrict each block to Hamming weight $`h=\lfloor m/2\rfloor`$. On this sector the contribution from $`g_0`$ is constant. Each string $`x`$ has integer energy $`S(x)=\sum_{j=1}^m q_j(1-2x_j)`$, which gives estimated centered scaled energy $`(\sqrt\tau/L)S(x)`$. Partition $`[-mL,mL)`$ into $`L`$ half-open bins of integer width $`2m`$. Every string lies in the partition because $`|q_j|\le L-1`$. Find a maximally occupied bin with a fixed tie rule and take its first $`2^r`$ strings in lexicographic order, where

```math
r=\left\lfloor\log_2\left\lceil\binom{m}{h}/L\right\rceil\right\rfloor.
```

This choice gives a common payload size across all transcripts and blocks. Since $`\binom{m}{h}\ge2^m/(m+1)`$ and $`\log_2 L=u/2+O(\log m+\log u)`$, we have $`r=m-O(u+\log m)`$. Estimated energies in the chosen bin have diameter at most $`2m\sqrt\tau/L\le w`$. Changing to the true profile adds at most $`2m\sqrt\tau/L\le w`$ to the diameter. The actual centered scaled energies in the invariant code span therefore have diameter at most $`2w`$.

## Compile and invert the inner encoding

Use the [fixed-weight band compiler](https://github.com/GoGoKo699/Quantum-Spectral-Memory/blob/main/science/fixed_weight_encoder.md) in Quantum Spectral Memory. It extends the [original reversible band compiler](https://github.com/GoGoKo699/Quantum-Spectral-Memory/blob/adf4eaf8fa4ff831c12954e9fcb39af010eff7eb/science/encoder.md) by tracking weight and signed integer energy together. Specifically, the number $`F_i(k,s)`$ of suffix strings of weight $`k`$ and signed energy $`s`$ obeys

```math
F_i(k,s)=F_{i+1}(k,s-q_i)+F_{i+1}(k-1,s+q_i),\qquad
F_{m+1}(k,s)=\mathbf 1_{\{k=0,\ s=0\}}.
```

Impossible indices count zero. The table has $`O(m^2(mL+1))`$ count words of at most $`m+1`$ bits. For each possible next bit, the compiler can count accepted suffixes from the residual weight and energy interval. This gives rank and unrank Boolean circuits with polynomial count, storage and gate-description size. Table lookups can be implemented with a scan of classical addresses and controlled XOR, using ordinary reversible gates.

With fresh physical block wires, compute reversible unrank from the input rank. Then use the rank of the block string to XOR away the input rank. Each computation uncomputes its internal work. The inverse recovers the logical bits and clears the physical block wires on the invariant code span. The same permutation acts on superpositions and protects any reference system. Since $`L=O(mu\sqrt\tau)`$, both the classical preprocessing and the explicit reversible endpoints in this step have the stated polynomial dependence.

## The actual channel is a correlated phase-error mixture

Use one independent uniform logical $`X`$ mask on each of the $`M=rN`$ inner bits. Apply the mask immediately before inner encoding and undo it after inner decoding. For a fixed Gaussian phase, the encoded storage unitaries are diagonal in the rank bases. The mask average cancels interference between distinct $`Z`$ patterns by character orthogonality. This gives a classical mixture of phase errors whose block supports may be correlated through the common field.

For one block, let $`\lambda_x`$ denote the centered scaled energy at rank $`x`$. Averaging the squared normalized trace of the block unitary gives the marginal probability of an identity error,

```math
P(I)=2^{-2r}\sum_{x,y}e^{-(\lambda_x-\lambda_y)^2/2}.
```

The other block outcomes sum to one conditional on each phase, so this is the marginal of the joint mixture. With $`x,y`$ independent uniform ranks, the probability of a nonidentity error satisfies

```math
1-P(I)\le\tfrac12\mathbb E(\lambda_x-\lambda_y)^2
=\mathrm{Var}(\lambda_x)\le w^2.
```

The last inequality uses the diameter bound $`2w`$. If $`W`$ counts affected blocks, then $`\mathbb E W\le Nw^2`$ by linearity, and

```math
\Pr\{W\gt \lfloor N/u\rfloor\}
\le\frac{Nw^2}{\lfloor N/u\rfloor+1}\le w.
```

Outside this event, at most $`T=\lfloor M/u\rfloor`$ inner bits carry a phase error. This bit count remains valid when the outer code groups bits from different physical blocks.

## Explicit outer code and terminal syndrome recovery

We need a binary code of rate approaching one and polynomial-time decoding for every error of weight at most $`T`$. The following concatenation also works when the number of inner bits per physical block is smaller than $`\log_2 n`$.

Set $`s=\lceil\log_2(n+1)\rceil`$ and $`p=\lfloor\sqrt u\rfloor`$. Choose the smallest $`\ell\in[s,2s]`$ satisfying

```math
2^{s-1}\sum_{j=0}^{\lfloor\ell/p\rfloor}\binom{\ell}{j}\lt 2^\ell .
```

For sufficiently large $`n`$, such an $`\ell`$ exists and $`\ell/s\to1`$. Indeed, for $`p\ge2`$ the volume sum is at most $`2^{\ell h_2(1/p)}`$, with $`h_2(1/p)\to0`$. To construct the binary inner code of the concatenation, start with the zero subspace. At each of $`s`$ steps, take the first vector outside all radius-$`\lfloor\ell/p\rfloor`$ balls centered at the current subspace, and adjoin it as a generator. The inequality guarantees a choice. Each new nonzero sum has weight greater than $`\lfloor\ell/p\rfloor`$, so the resulting linear code corrects

```math
b=\left\lfloor\lfloor\ell/p\rfloor/2\right\rfloor
```

errors per word. Search over $`2^\ell=O(n^2)`$ candidates during compilation and scan $`2^s=O(n)`$ codewords per local decoding. If none lies within radius $`b`$, use a fixed decoded symbol.

Group $`M`$ bits into $`P=\lfloor M/\ell\rfloor`$ binary codewords and set the leftover coordinates to zero in the classical code. Use a Reed–Solomon code at $`P`$ distinct points of $`\mathbb F_{2^s}`$ with dimension $`P-2e`$, where $`e=\lfloor T/(b+1)\rfloor`$. The field has more than $`n`$ points. When the bit error count is at most $`T`$, any wrongly decoded symbol costs at least $`b+1`$ bit errors, so at most $`e`$ symbols can be wrong. Reed–Solomon decoding corrects them all. One can construct the field by enumerating monic binary polynomials of degree $`s`$ with polynomial-time irreducibility tests. Standard [Welch–Berlekamp decoding](https://courses.csail.mit.edu/6.440/spring08/scribe/lec10.pdf) runs in polynomial time. Choose a fixed classical fallback for failures outside the guaranteed radius.

For $`M=\Theta(n)`$, we have $`P\gt 0`$ and $`e/P=O(u^{-1/2})`$ for large $`n`$ because $`b+1\gt \ell/(2p)`$. The concatenated code carries $`s(P-2e)=(1-o(1))M`$ bits. Its binary-linear encoding has a polynomial Clifford implementation.

To use this outer code coherently, apply bitwise Hadamards after its binary-linear encoder. Undo these Hadamards at recovery after decoding the spectral bands. A phase error now shifts the binary codeword by a vector $`a`$. Let $`H`$ be a full-row-rank parity-check matrix of the complete binary code, including any fixed zero coordinates. Measure only the syndrome $`Ha`$, which is the same for every shifted encoded basis word. For each syndrome, choose a fixed representative $`v`$ satisfying $`Hv=Ha`$, and run the classical decoder on $`v`$. If $`a`$ has weight at most $`T`$, then $`v+a`$ is the unique decoded codeword. Correct by adding $`v+(v+a)=a`$ and invert the outer encoder. This recovery preserves all payload amplitudes and correlations with a reference. Finite linear algebra implements syndrome extraction, choice of representative and the remaining ideal endpoint operations. Any decoder fallback defines a channel outside the guaranteed error radius.

The averaged logical channel is the identity on every phase-error branch within the radius. All other branches contribute at most one to the half-diamond distance, so the worst-profile error is bounded by the tail probability $`w`$.

## Calibration cost and comparison

For any constant $`a\in(0,1)`$, choosing $`N=\lfloor an/m\rfloor`$ gives $`M=(a+o(1))n`$ and $`s(P-2e)=(a+o(1))n`$. Scan feasible $`N`$ and take the smallest with at least $`\lceil Rn\rceil`$ outer logical coordinates, using a fixed state for any surplus coordinates. Every feasible choice uses at least $`\lceil Rn\rceil`$ active carriers. For every fixed $`a\gt R`$, the scan can succeed with at most $`\lfloor an/m\rfloor`$ blocks for large $`n`$. Consequently $`Nm=Rn+o(n)`$.

The transcript lists one of $`L`$ indices per active carrier. It has at most $`L^{Nm}`$ possible values, with hard budget

```math
Nm\log_2 L=\left(\frac R2+o(1)\right)n\log_2\tau.
```

Packing the indices in radix $`L`$ adds at most one bit. The independent key uses $`M\le n`$ bits and carries no profile information. The [continuous converse](continuous_calibration.md#converse) supplies the matching lower bound. The [finite checks](../verification/README.md#compiled-calibration-checks) exercise the exact band selection and rank/unrank, the classical and coherent-syndrome recovery conditions, and common-phase correlations.

The protected-space concatenation and classical decoding ingredients are established methods. [Related work](../references/related_work.md#efficient-endpoint-compilation) compares this result with supplied-profile compilers, decoherence-free subspace concatenation and prior uses of Reed–Solomon codes in correlated-noise memory.
