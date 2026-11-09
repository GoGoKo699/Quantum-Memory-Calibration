# Passive storage and calibration information

[Science map](README.md) · [Lifetime theorem](lifetime.md) · [Calibration frontier](calibration_rate.md)

## One field, a fixed spatial profile

A register contains $n$ physical qubits. Its coupling to a common dephasing field is described by the Hermitian operator

$$
A_{\boldsymbol g}=\sum_{j=1}^{n}g_jZ_j.
$$

The coefficients $\boldsymbol g$ remain fixed during storage. They describe the register, while the field fluctuates. For storage time $t\geq0$, the channel is

$$
\Phi_{\boldsymbol g,t}(\rho)
=e^{-t[A_{\boldsymbol g},[A_{\boldsymbol g},\,\cdot\,]]/2}(\rho)
=\mathbb E_{\Theta\sim N(0,t)}
\left[e^{-i\Theta A_{\boldsymbol g}}\rho e^{i\Theta A_{\boldsymbol g}}\right].
$$

The last expression is the channel obtained by integrating one common Gaussian white-noise field. It does not assign an independently sampled phase to each qubit. The convention is $\operatorname{Var}(\Theta)=t$; thus $t\delta^2$ is dimensionless when $\delta$ is a coupling scale.

Two families isolate different aspects of calibration:

| Family | Information supplied in advance | Unknown profile | Main question |
|---|---|---|---|
| Interval uncertainty | $g_0$, $\delta>0$, $t$, and $n$ | Every $g_j\in[g_0-\delta,g_0+\delta]$ | How long can a positive-rate code work uniformly without further calibration? |
| Binary profile | $\delta>0$, $t$, and $n$ | $g_j=\delta s_j$, with $s_j\in\{-1,+1\}$ | How much classical profile information is needed for a prescribed reliable rate? |

The interval result is uniform over every allowed fixed profile. The binary result also admits $g_j=g_0+\delta s_j$, including two positive coupling values; its construction is given in [Calibration frontier](calibration_rate.md). The product distributions used in converses are priors for proving a worst-case obstruction. The physical couplings need not be redrawn between or during storage runs.

## The storage interface

An unknown quantum payload occupies a logical space $L$ of dimension $D$. It may be entangled with an arbitrary untouched reference. A protocol consists of a preparation/encoding operation, one storage interval, and a recovery operation.

The encoder and recovery can be arbitrary joint quantum channels. They may use the known values $n,t,g_0,\delta$ and may reserve some physical carriers as probes. Any quantum system that persists from encoding to recovery is included in the $n$ noisy carriers. Fresh local ancillas at either endpoint are allowed; no quantum system can carry payload information around the storage channel. No operation, new quantum probe, or syndrome extraction is inserted inside the interval.

The encoder may retain an arbitrary classical record $X$, including a measurement record that depends on the payload. It is passed to the recovery without noise. The protocol may also use shared randomness $K$, independent of the unknown profile and payload. Classical memory for $X$ and $K$ is not restricted. Neither resource communicates an arbitrary unknown quantum state without using the noisy carriers.

The noiseless classical path makes the converse cover the full endpoint protocol class: a failure caused merely by forbidding ordinary encoder records would not establish the intended memory limitation. All statements here allow those records.

## What calibration supplies

Before the unknown payload arrives, a calibration procedure supplies a classical transcript $C$. It may depend on the profile and on $K$ through any stochastic law $p(c\mid\boldsymbol g,k)$. Both endpoints receive it. Every profile-dependent influence on the endpoint operations must factor through $(C,K)$.

Calibration describes the static profile. It supplies no information about the field realization in the subsequent data-storage interval: conditional on the profile and key, $C$ and the data-run $\Theta$ are independent. Calibration may have been acquired through earlier experiments or supplied by an oracle; the results price the retained information, without asserting an optimal experimental acquisition cost.

In particular, profile-dependent analog settings, prepared quantum programs, or extra quantum calibration outputs cannot be supplied outside this bottleneck. A laboratory retaining such resources implements a different interface. Information about a fixed register can be reused for many later payloads; the calibration charge here is not a communication charge that must be paid afresh on every run.

Writing the encoder and recovery as

$$
\mathcal E_{c,k}:L\longrightarrow A^nX,
\qquad
\mathcal R_{c,k}:A^nX\longrightarrow L,
$$

the logical channel for profile $\boldsymbol g$ is

$$
\Lambda_{\boldsymbol g}
=\mathbb E_{K,C\mid\boldsymbol g,K}
\left[
\mathcal R_{C,K}\circ
(\Phi_{\boldsymbol g,t}\otimes\operatorname{id}_X)
\circ\mathcal E_{C,K}
\right].
$$

$X$ is a classical register: the encoder's output is block diagonal in its recorded basis. It may be absorbed into the recovery notation when no confusion results.

## Error and rate

The operational error is the worst-profile, reference-complete error of the averaged logical channel,

$$
\varepsilon(\Lambda)
=\sup_{\boldsymbol g}\frac12
\|\Lambda_{\boldsymbol g}-\operatorname{id}_L\|_\diamond.
$$

The average over the protocol's randomness and calibration outcomes occurs *before* the diamond norm. This is the channel obtained when the protocol uses its classical records and finally discards them. The guarantee is uniform over the coupling profile and logical input; it is not a maximum over every random key or calibration outcome. The achievable lifetime proof uses this permitted randomization.

For a maximally entangled logical-reference state $\varphi_D$, define

$$
F_e(\Lambda_{\boldsymbol g})
=\operatorname{Tr}\left[
\varphi_D(\operatorname{id}\otimes\Lambda_{\boldsymbol g})(\varphi_D)
\right].
$$

Here fidelity means overlap with the pure target, not its square root. The operational error bound implies $F_e\geq1-\varepsilon$ for every profile. The converses often use this weaker necessary condition. The matching binary-profile codes are exact logical identities, so they establish the same rate under either criterion.

The stored rate is $R_n=\log_2D_n/n$. A reliable asymptotic rate $R$ means $\liminf_nR_n\geq R$ and $\varepsilon_n\to0$. These rates refer to a single growing, spatially correlated storage block. They are distinct from repeatedly using one fixed finite-dimensional memoryless channel with independently refreshed noise.

For interval uncertainty, fixed $0<R<1$ and $0<\varepsilon<1$, let $T_{R,\varepsilon}^{(n)}(\delta)$ be the supremum of times for which some allowed uncalibrated protocol has $\log_2D\geq Rn$ and error at most $\varepsilon$. The code may depend on its intended storage time. [The lifetime theorem](lifetime.md) bounds this quantity above and below by positive multiples of $\delta^{-2}$ for all sufficiently large $n$.

## Two different information budgets

All entropies and information quantities use base-two logarithms.

**Hard description budget.** For every key $k$, the transcript has at most $M$ possible values. Its worst-case length is $B=\log_2M$ bits. A fixed-length binary representation can use $\lceil B\rceil$ bits. Encoding a transcript by a large-alphabet analog number does not give it a smaller alphabet.

**Information budget.** For the binary family, take the converse prior $S$ uniform on $\{-1,+1\}^n$, independent of $K$, and charge

$$
I(S;C\mid K).
$$

This definition covers noisy, stochastic, or continuous transcripts through relative entropy; it does not use differential entropy as a bit count. The storage guarantee remains uniform in $s$ even though the information budget is evaluated under this specified prior. For the interval family, the analogous converse uses independent uniform coefficients $G_j$ and $I(G;C\mid K)$.

A hard alphabet bound implies $I(S;C\mid K)\leq\log_2M$. The converse need not hold: a rare transcript can reveal the entire profile while carrying little mean information. The budgets therefore agree on the binary vanishing-error rate frontier but produce different fixed-error bounds.

Conditioning on the free key is essential. After converting signs into bits, a one-time-padded description $C=S\oplus K$ has $I(S;C)=0$, yet the endpoints recover all of $S$ from $(C,K)$ and $I(S;C\mid K)=n$. It is fully charged by the stated definition.

## Why complete dephasing remains a valid benchmark

Let $\Delta_n$ completely dephase all physical carriers in the computational basis. Applied after any allowed encoder, it leaves a classical mixture of computational labels and encoder records. The reference and everything available to the decoder are then separable. Recovery cannot create entanglement with the untouched reference, and the final overlap with $\varphi_D$ is at most $1/D$.

This observation incorporates physical probes, mixed encoders, and payload-dependent classical records into the same comparison. It is the entanglement-breaking step used in the [calibration converse](calibration_rate.md) and [lifetime converse](lifetime.md). The remaining ingredient is a completely positive comparison of the sign- or interval-averaged dephasing channel with a multiple of $\Delta_n$.

## Reading the result within its interface

The [interpretation page](interpretation.md) explains the contrast with calibrated storage, the finite-error meaning of the asymptotic frontier, and a control sequence that changes the task when operations during storage are admitted. The assumptions above are part of the claimed resource tradeoff. They allow arbitrary ideal endpoint codes while isolating the information supplied about one fixed spatial coupling profile.
