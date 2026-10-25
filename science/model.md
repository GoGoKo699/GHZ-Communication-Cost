# Model and charged resources

## The preparation task

A quantum network starts with independently supplied bipartite states. Its parties may process their systems jointly within each laboratory, exchange classical messages, and discard systems. The question is how many classical bits are needed to prepare a coherent GHZ state across the output laboratories when the amount of initial pairwise entanglement is unrestricted.

The target at $`n\ge2`$ output parties is

```math
|\mathrm{GHZ}_{n,d}\rangle
=\frac{1}{\sqrt d}\sum_{x=0}^{d-1}|x\rangle^{\otimes n},
\qquad d\ge2.
```

Throughout this account, fidelity means the **squared overlap with this pure target**:

```math
F(\rho)=
\langle\mathrm{GHZ}_{n,d}|\rho|\mathrm{GHZ}_{n,d}\rangle.
```

This convention is linear in the output state. The unconditional output includes every execution, with all private outcomes and communicated transcripts averaged unless an explicitly specified heralded task is being considered.

The target is an actual quantum state in the stated local reference bases. Locally known Pauli corrections are free local operations. An uncommunicated correction known only at a remote laboratory cannot be silently used when evaluating the output fidelity. Keeping such remote records for later application-specific classical postprocessing defines a different output task.

## Independent quantum sources and helpers

Let $`G=(V,E)`$ be a finite undirected graph. An edge $`e=\{u,v\}`$ supplies an arbitrary finite-dimensional bipartite state $`\rho_e`$ to laboratories $`u`$ and $`v`$. Parallel sources on the same pair can be combined into one higher-dimensional source. Choose an output set $`O\subseteq V`$, with $`|O|=n`$. The remaining vertices $`H=V\setminus O`$ are helpers and may discard all their quantum systems.

A free shared classical seed $`R`$ may select both the source states and the local protocol. Conditional on $`R=r`$, the initial quantum state has the form

```math
\rho^{\mathrm{in}}_r
=\bigotimes_{e\in E}\rho_{e,r}
\otimes\bigotimes_{v\in V}\tau_{v,r}.
```

Here $`\tau_{v,r}`$ is an arbitrary local ancilla. **Independence is conditional on the shared seed.** There is no restriction on the amount of pairwise entanglement or on its finite local dimension. Local quantum memories and coherent processing across all supplied systems are allowed.

The following resources are not included in this initial-state model:

- a quantum source shared by three or more distinct laboratories;
- additional quantum communication during the protocol;
- correlated quantum source states across different edges that cannot be written in the conditional product form above.

The choice of a source graph concerns initial quantum resources. It does not impose a bandwidth, geometric distance, or latency model on the classical messages.

## Classical communication

### Complete transcripts

A protocol is described by a binary communication tree, conditional on $`R=r`$. At each node the next speaker and its available classical recipients are determined by the protocol and the previous communication. The speaker applies a local instrument to its current quantum and private classical memory, then communicates the next binary outcome. Deterministic local operations may be inserted anywhere.

Private outcomes can remain private. They are integrated into the party's local map when a complete communicated transcript is fixed. Different local private histories consistent with the same public transcript do not count as additional communicated bits.

Complete transcripts $`t`$ are prefix-free binary strings. The following quantities are distinct:

| Resource | Definition | Result that uses it |
|---|---|---|
| Transcript number $`M`$ | At most $`M`$ complete transcripts for each fixed seed | Finite-transcript fidelity bounds |
| Worst-case length $`c`$ | Every complete transcript has length at most $`c`$ | $`M\le2^c`$ and the collective strong converse |
| Mean length $`L`$ | $`\mathbb E[\ell(T)]`$, including the shared seed average | Entropy and cutoff converses |
| Success probability $`P`$ | Probability of a specified accepted set of transcripts | Heralded success–fidelity tradeoff |

An $`M`$-leaf interactive tree need not have depth $`\lceil\log_2 M\rceil`$. The implication needed in the converses is that a depth-$`c`$ binary tree has at most $`2^c`$ leaves. The star construction has a single sender who knows the complete correction word and can encode it into $`\lceil\log_2 M\rceil`$ bits.

### Broadcast convention and other delivery models

For the general converses, one classical bit may be broadcast to every laboratory at cost one. This generous convention permits all adaptive protocols with the same total point-to-point bit budget: broadcast their messages and instruct additional recipients to ignore them. Therefore a lower bound in the broadcast model also bounds the total number of delivered bits in a point-to-point implementation.

Achievability statements specify their delivery model. In particular, the sequential tree-growth construction sends each correction directly to one newly added party and attains its qubit cost with point-to-point messages.

Every information-bearing choice must be charged or fixed in advance. This includes routing, speaker identity, message timing, silence, and stopping decisions. A fixed schedule carries no new information. A data-dependent choice among possible schedules is part of the transcript and requires an encoding. This prevents a real-valued clock or an uncharged silence signal from replacing the binary channel.

No latency conclusion follows from a total bit bound alone. Converting bits into elapsed time requires additional bandwidth, propagation and scheduling assumptions.

### Finite and mean-cost protocols

The fixed-budget theorems concern a finite maximum communication length. The mean-cost statements also allow countably many complete transcripts, almost-sure termination, and finite expected length. Local registers are finite-dimensional in each execution; there is no common dimension bound over the class of allowed protocols. Prefix-freeness is retained when the length is variable.

The complete transcript is an accounting object. A lower bound does not require each party in an original point-to-point protocol to have learned the entire transcript.

## The graph parameter

For a weight vector $`w`$, require

```math
0\le w_v\le1,\qquad
w_u+w_v\le1\quad(\{u,v\}\in E),\qquad
w_h=0\quad(h\in H).
```

Define

```math
\alpha=\alpha_O(G)
=\max_w\sum_{i\in O}w_i
=\alpha^*(G[O]).
```

Thus $`\alpha`$ is the fractional independence number of the graph induced by the output parties, with weights capped at one even for isolated output vertices. Setting every output weight to one half is always feasible, so $`\alpha\ge n/2`$ regardless of the number or arrangement of finite helpers.

| Source architecture | Outputs | $`\alpha`$ |
|---|---|---:|
| Complete graph $`K_n`$ | All $`n`$ vertices | $`n/2`$ |
| Star on $`n\ge3`$ vertices | Hub and all leaves | $`n-1`$ |
| Star with $`n`$ leaves and a separate helper hub | Leaves only | $`n`$ |
| Path on $`n`$ vertices | All vertices | $`\lceil n/2\rceil`$ |

For a complete graph, summing the edge constraints gives $`\sum_i w_i\le n/2`$, attained by uniform half weights. On a star, set all leaf weights to one and the hub weight to zero. On a path, disjoint-edge constraints give the upper bound, with a possible unmatched endpoint; the alternating independent set attains it.

The general qubit coherence bound permits every feasible weight vector. The dimension-dependent bound and its strong-converse consequence require $`\alpha\ge2`$. This includes every pair-source network with $`n\ge4`$ outputs and a three-output star, but does not include the complete three-output triangle.

The parameter gives a valid converse rather than a complete characterization of every topology. For example, a disconnected quantum source graph cannot create a GHZ state across its disconnected components by LOCC, even when the displayed bit bound is finite. The exact tree result uses an additional entropy argument and can be stronger than the fractional-independence bound.

## Output states, branches and collective copies

Fixing $`r`$ and a complete transcript $`t`$ gives an unnormalized output state $`\sigma_{t|r}`$ after helpers and other retained registers have been traced out. Write

```math
p_{t|r}=\mathrm{Tr}\sigma_{t|r},
\qquad
\sum_t p_{t|r}=1,
\qquad
\rho^{\mathrm{out}}
=\mathbb E_R\sum_t\sigma_{t|R}.
```

The branch contribution to fidelity is

```math
g_{t|r}
=\langle\mathrm{GHZ}_{n,d}|
\sigma_{t|r}|\mathrm{GHZ}_{n,d}\rangle.
```

When $`p_{t|r}>0`$, let $`f_{t|r}=g_{t|r}/p_{t|r}`$ be the normalized branch fidelity. A single selected branch can be highly entangled. The proof retains its probability; it does not assume that conditioning preserves an independent-source network.

Preparing $`k`$ qubit GHZ copies is locally equivalent to preparing $`\mathrm{GHZ}_{n,2^k}`$. Each laboratory groups its $`k`$ qubits into a single register labelled by a binary word. Accordingly,

```math
F_k
=\langle\mathrm{GHZ}_{n,2}^{\otimes k}|
\rho^{\mathrm{out}}|
\mathrm{GHZ}_{n,2}^{\otimes k}\rangle
```

is the fidelity with the **whole target block**. The sources may be correlated across these copies within each edge and the local processing may act jointly on all copies. Independence is required between source edges, not between copies on an edge.

High fidelity of each individual marginal copy is a separate criterion and does not imply high global block fidelity.

## Proof route

The [branch bound](branch-bound.md) derives probability-sensitive restrictions from the inherited quantum Finner inequality. The [communication converses](communication-converses.md) sum these restrictions over transcripts. [Expected communication and heralding](expected-and-heralded.md) treat the two different relaxations of a fixed budget. [Achievability and limits](achievability-and-limits.md) gives matching constructions and the exact tree benchmark.

[Related work](../references/related-work.md) distinguishes the new operational quantum conclusions from the inherited network inequality, classical PIN packing laws, communication-round measures and specific GHZ distribution protocols.

