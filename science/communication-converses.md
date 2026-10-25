# Communication volume and global GHZ fidelity

Unlimited pairwise entanglement does not remove the classical communication required to prepare a coherent GHZ state. The bounds here charge the total number of possible communication transcripts. They apply to adaptive LOCC with arbitrary local quantum memories and arbitrary finite source dimensions.

The [model](model.md) specifies a finite source graph $`G=(V,E)`$, output vertices $`O`$ with $`|O|=n`$, helpers $`H=V\setminus O`$, and free shared classical randomness $`R`$. Conditioned on $`R=r`$, the initial state is a tensor product of independent bipartite edge states. Every transmitted bit, including any data carried by routing, stopping, or a speaker choice, belongs to the charged communication record. There is no subsequent quantum communication.

Write

```math
\alpha=\alpha_O(G)
=
\max
\left\{
\sum_{v\in V}w_v:
0\le w_v\le1,\qquad
w_h=0\ (h\in H),\qquad
w_u+w_v\le1\ (\{u,v\}\in E)
\right\}.
```

For a complete transcript $`t`$ and fixed seed $`r`$, let $`\sigma_{t|r}`$ denote its unnormalized output, and put

```math
p_{t|r}=\operatorname{Tr}\sigma_{t|r},
\qquad
\rho^{(r)}=\sum_t\sigma_{t|r},
\qquad
\rho^{\mathrm{out}}=\mathbb E_R\,\rho^{(R)}.
```

The target and fidelity convention are

```math
|\mathrm{GHZ}_{n,d}\rangle
=
\frac1{\sqrt d}\sum_{x=0}^{d-1}|x\rangle^{\otimes n},
\qquad
F_d=\langle\mathrm{GHZ}_{n,d}|
\rho^{\mathrm{out}}|\mathrm{GHZ}_{n,d}\rangle.
```

In particular, $`F_d`$ is the squared overlap with a pure target, not its square root. The output of the whole protocol is normalized; any failure or abort branch is included in that output. Conditional success is treated separately in [Expected communication and heralded preparation](expected-and-heralded.md).

## Finite-transcript fidelity bounds

**Theorem C1: Qubit coherence converse.** Suppose that, for every shared seed value except a set of probability zero, the protocol has at most $`M`$ nonzero complete transcripts. Then

```math
F_2
\le
\min\left\{
1,\,
\frac12+M\,2^{-\alpha}
\right\}.
\tag{C1}
```

No condition $`\alpha\ge2`$ is required.

**Proof.** For fixed $`r`$, [Proposition B4](branch-bound.md#coherence-and-fidelity-of-one-branch) gives

```math
\langle\mathrm{GHZ}_{n,2}|\sigma_{t|r}|\mathrm{GHZ}_{n,2}\rangle
\le
\frac{p_{t|r}}2+2^{-\alpha}
```

for every nonzero branch. Since $`\sum_t p_{t|r}=1`$, summing over the at most $`M`$ branches yields

```math
\langle\mathrm{GHZ}_{n,2}|\rho^{(r)}|\mathrm{GHZ}_{n,2}\rangle
\le
\frac12+M2^{-\alpha}.
```

The right side does not depend on $`r`$. Averaging over the shared seed preserves the inequality because overlap with a pure target is linear in the output state. Finally, a normalized state's overlap with a unit vector is at most one. ∎

**Theorem C2: Dimension-dependent converse.** Under the same transcript assumption, if $`\alpha\ge2`$, then

```math
F_d
\le
\min\left\{
1,\,
\frac{M^{1/(\alpha-1)}}d
\right\}.
\tag{C2}
```

**Proof for $`\alpha>2`$.** Fix $`r`$, discard zero-probability leaves, and let their remaining number be $`m_r\le M`$. Put

```math
\beta=\frac{\alpha-2}{\alpha-1},
\qquad 0<\beta<1.
```

[Proposition B5](branch-bound.md#coherence-and-fidelity-of-one-branch) gives

```math
\langle\mathrm{GHZ}_{n,d}|\rho^{(r)}|\mathrm{GHZ}_{n,d}\rangle
\le
\frac1d\sum_{t:p_{t|r}>0}p_{t|r}^{\,\beta}.
```

Concavity of $`x^\beta`$, applied to the $`m_r`$ positive probabilities summing to one, yields

```math
\begin{aligned}
\sum_{t:p_{t|r}>0}p_{t|r}^{\,\beta}
&\le
m_r
\left(\frac1{m_r}\sum_t p_{t|r}\right)^\beta\\
&=
m_r^{\,1-\beta}\\
&=
m_r^{\,1/(\alpha-1)}
\le M^{\,1/(\alpha-1)}.
\end{aligned}
```

Averaging over $`r`$ and imposing $`F_d\le1`$ proves (C2).

**Endpoint $`\alpha=2`$.** Proposition B5 gives unnormalized target overlap at most $`1/d`$ for each nonzero leaf. There are at most $`M`$ such leaves, so $`F_d\le M/d`$, which is exactly (C2). Zero-probability leaves contribute zero and are not assigned a factor $`0^0`$. ∎

The condition $`\alpha\ge2`$ is necessary for the stated proof and cannot be dropped from the theorem. The complete three-output graph has $`\alpha=3/2`$. For $`d=2`$, [Neumann et al., Section III.1 and Appendix A.3.1](../references/related-work.md#neumann2025) give an explicit no-communication triangle protocol with two-qubit sources attaining

```math
F_2=
\frac{5+4\cos(2\pi/7)}{12+4\cos(2\pi/7)}
\approx0.5170401751>\frac12.
```

Thus extending (C2) to that triangle would give a false zero-communication bound. This counterexample uses an achieved fidelity, independently of the same paper's upper bounds.

For qubits and $`\alpha\ge2`$, the two estimates may be combined:

```math
F_2
\le
\min\left\{
1,\,
\frac12+M2^{-\alpha},\,
\frac12M^{1/(\alpha-1)}
\right\}.
\tag{C3}
```

They control different features. The coherence estimate gives the stronger party-number dependence at a fixed nonzero advantage above $`1/2`$ when $`\alpha`$ is large. The dimension-dependent estimate retains the total branch probability and controls large targets.

## Worst-case binary communication

A binary protocol that communicates at most $`c`$ bits in every run has a prefix-free set of complete transcripts of length at most $`c`$, conditioned on each shared seed. Hence it has at most $`2^c`$ leaves. The same statement holds for a protocol tree whose local actions depend arbitrarily on the preceding messages and private quantum memory.

**Corollary C3: Bit-budget bounds.** For such a protocol,

```math
F_2
\le
\min\left\{
1,\,
\frac12+2^{\,c-\alpha}
\right\}.
\tag{C4}
```

If $`\alpha\ge2`$, then

```math
F_d
\le
\min\left\{
1,\,
2^{\,c/(\alpha-1)-\log_2 d}
\right\}.
\tag{C5}
```

Consequently, an achieved qubit fidelity $`F_2>1/2`$ requires

```math
c\ge
\alpha+\log_2\!\left(F_2-\frac12\right).
\tag{C6}
```

For $`\alpha\ge2`$ and $`F_d>0`$, the general target requires

```math
c\ge
(\alpha-1)\log_2(dF_d).
\tag{C7}
```

These real-valued lower bounds are combined with $`c\ge0`$ and, when appropriate, rounded upward because the worst-case bit budget is an integer.

At exact fidelity $`F_d=1`$, (C7) gives $`c\ge(\alpha-1)\log_2d`$ in its domain. The [exact-branch bound](branch-bound.md#coherence-and-fidelity-of-one-branch) proves the same exact-preparation conclusion for every $`\alpha>0`$, even when Theorem C2 is unavailable. Its extension to transcript entropy and expected communication is developed in [Expected communication and heralded preparation](expected-and-heralded.md).

At zero communication, Theorem C2 reduces to $`F_d\le1/d`$. This special case agrees with the existing no-communication network result of [Neumann et al.](../references/related-work.md#neumann2025). The transcript-dependent factor quantifies how classical messages can raise the attainable overlap above that benchmark.

## Arbitrary finite helper networks

The feasible output weights depend only on edges joining two output vertices. Indeed, an edge from an output $`i`$ to a helper has constraint $`w_i+0\le1`$, already imposed by $`w_i\le1`$, and an edge between helpers imposes no additional restriction. Therefore

```math
\alpha_O(G)=\alpha^*(G[O]),
\tag{C8}
```

where $`G[O]`$ is the graph induced by the output vertices.

In particular, assigning $`w_i=1/2`$ to every output and zero to every helper is always feasible. Thus

```math
\alpha_O(G)\ge\frac n2.
\tag{C9}
```

The bounds consequently hold uniformly over any finite number of helpers and any independent pair sources attached to them. All helper communication is included in the transcript. The model begins with the independent edge resources; multipartite states created by earlier helper operations cannot be inserted as free initial resources.

**Corollary C4: Universal party-number cost.** For any network of independent bipartite sources with $`n`$ designated outputs,

```math
F_2\le
\min\left\{
1,\,
\frac12+2^{\,c-n/2}
\right\}.
\tag{C10}
```

Thus every fixed $`\delta>0`$ and achieved fidelity $`F_2\ge1/2+\delta`$ require

```math
c\ge\frac n2+\log_2\delta.
\tag{C11}
```

For $`n\ge4`$, the dimension-dependent universal bound is

```math
F_d
\le
\min\left\{
1,\,
\frac{2^{\,2c/(n-2)}}d
\right\}.
\tag{C12}
```

These statements allow all output pairs to share arbitrarily large entangled states. Adding independent pairwise entanglement cannot eliminate the extensive classical bit requirement.

The bound uses transmitted information volume, rather than the number of broadcast rounds or the longest communication path. It does not by itself impose a latency lower bound: several parties may communicate in parallel, and any conversion from bits to time needs a bandwidth or scheduling assumption.

## Collective preparation of many GHZ states

Suppose each output party has $`k`$ target qubits. Regroup its $`k`$ computational-basis bits into one label $`x\in\{0,1\}^k`$. This local relabeling identifies the entire target with a single larger GHZ state:

```math
|\mathrm{GHZ}_{n,2}\rangle^{\otimes k}
\simeq_{\mathrm{local}}
\frac1{\sqrt{2^k}}
\sum_{x\in\{0,1\}^k}|x\rangle^{\otimes n}
=|\mathrm{GHZ}_{n,2^k}\rangle.
\tag{C13}
```

No operation between parties is needed for this identification.

For each $`k`$, the initial edge state may be an arbitrary joint state $`\omega_e^{(k)}`$ on all registers associated with that edge. It need not factor into $`k`$ copies. Each party may process all its registers coherently, use arbitrary local memory, and communicate adaptively. Only independence *between distinct source edges*, conditioned on the shared seed, is required.

Let $`c_k`$ be the worst-case number of communicated bits and define the global target fidelity

```math
F_k
=
\langle\mathrm{GHZ}_{n,2}|^{\otimes k}
\rho^{\mathrm{out},(k)}
|\mathrm{GHZ}_{n,2}\rangle^{\otimes k}.
```

**Corollary C5: Global-fidelity strong converse.** If $`\alpha=\alpha_O(G)\ge2`$, then

```math
F_k
\le
\min\left\{
1,\,
2^{\,c_k/(\alpha-1)-k}
\right\}.
\tag{C14}
```

In particular, if $`c_k\le R_{\mathrm{bit}}k`$ for some fixed $`R_{\mathrm{bit}}<\alpha-1`$, then

```math
F_k
\le
2^{-k[1-R_{\mathrm{bit}}/(\alpha-1)]}.
\tag{C15}
```

The global fidelity therefore vanishes exponentially below $`\alpha-1`$ communicated bits per target GHZ copy. The same conclusion holds when $`\limsup_{k\to\infty}c_k/k<\alpha-1`$, by choosing an eventual strict upper bound $`R_{\mathrm{bit}}`$ on that ratio.

**Proof.** Apply Theorem C2 or Corollary C3 to the locally relabeled target with $`d=2^k`$. Source dimensions and local operations were unrestricted in the branch bounds, so the proof already includes the joint processing just described. ∎

This result concerns fidelity with all $`k`$ target copies jointly. It does not assert that every individual marginal copy has low fidelity; many outputs can have reasonable individual quality while their joint overlap with the full ideal tensor product is small.

For the complete graph on $`n\ge4`$ outputs, $`\alpha=n/2`$, and (C14) becomes

```math
F_k\le
\min\left\{
1,\,
2^{\,2c_k/(n-2)-k}
\right\}.
\tag{C16}
```

For a star whose center is one of its $`n\ge3`$ output vertices, $`\alpha=n-1`$. The threshold in (C14) is then $`n-2`$ bits per GHZ copy, attained by the [star fusion construction](achievability-and-limits.md). The same exact threshold applies to block protocols: coherent processing of many copies cannot lower it in the regime of nonvanishing global fidelity.

## Meaning and boundary of the converse

The source graph enters through a fractional packing of output vertices. The underlying graph parameter and its classical public-discussion interpretation predate these quantum bounds; see [Chan et al.](../references/related-work.md#chan2018). Quantum Finner is also an imported ingredient. The communication converse follows by combining it with the CP-map representation of each adaptive transcript, positivity of the output state, and a probability-sensitive Hölder estimate.

For dense graphs, the lower bound need not equal the communication used by a particular fusion construction. In particular, the complete-graph coefficient $`n/2-1`$ and the standard $`n-2`$-bit construction leave a factor-two gap for exact asymptotic preparation. The theorem establishes the lower bound and its exponential fidelity penalty without asserting that every graph attains it.

The [expected-cost results](expected-and-heralded.md) require separate arguments. A restriction on mean communication alone allows a protocol to mix costly successful runs with inexpensive failures, so the worst-case strong converse above cannot be transferred to that model by replacing $`c_k`$ with an expectation.
