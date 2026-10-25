# Scientific overview

Independent bipartite entanglement provides nonlocal quantum resources, but it does not by itself specify the common coherent label of a multipartite GHZ state. Local measurements can reveal correction labels. Those labels may remain private, be partly communicated, or be used to select a rare successful branch. The scientific question is how much classical information must cross laboratories when the actual unconditional output must approximate a specified GHZ target.

This account permits arbitrarily large pair resources and arbitrary coherent local processing. Its lower bounds therefore concern coordination after resource distribution. The starting assumptions, the charged communication model, and the fidelity convention are all part of the result.

For a foundation-first route, the [Watrous bridge](../learning/bridge.md) translates the relevant textbook conventions and works through one-bit fusion. The [30-milestone map](../learning/milestones.md) follows the same scientific dependencies.

## The connected argument

Read the pages in the following order for the full derivation.

| Page | Question answered | Main content |
|---|---|---|
| [Model and charged resources](model.md) | What is supplied, what is charged, and what is the output? | Independent pair sources, helpers, shared seed, prefix-free transcripts, global fidelity, fractional independence |
| [A bound for each transcript](branch-bound.md) | What can one communicated branch contribute? | Quantum Finner with attribution, CP-map factorization, diagonal mass, coherence and probability-sensitive fidelity |
| [Communication volume and global fidelity](communication-converses.md) | How does a finite transcript budget constrain the whole output? | Finite-transcript theorem, worst-case bit bounds, finite helpers, collective strong converse |
| [Expected communication and heralding](expected-and-heralded.md) | What changes if cost is averaged or success is selected? | Exact transcript entropy, cutoff bound, mean star frontier, accepted-transcript tradeoff |
| [Constructions, exact tree costs, and limits](achievability-and-limits.md) | Which bounds match, and which assumptions matter? | Star fusion, tree growth, conditional-total-correlation converses, discarded hub, counterexamples and dense-graph gap |
| [Related work](../references/related-work.md) | Which ingredients and neighboring claims were already established? | Primary-source statements, resource currencies, classical antecedents and comparison limits |

## From independent sources to a bit bound

For a fixed shared seed and complete communication transcript, every party has a local trace-nonincreasing map. The product of these maps acts on the original tensor product of edge resources. Private measurement histories are summed within each local map. The resulting branch state is unnormalized; its trace is the probability of that transcript.

Let $`q_x`$ be the branch mass on the joint basis vector $`|x\rangle^{\otimes n}`$ and let $`\alpha`$ be the fractional independence number of the output-induced graph. Quantum Finner and a weighted Hölder step give

```math
\sum_{x=0}^{d-1}q_x^{1/\alpha}\le1.
```

For qubits, positivity bounds the off-diagonal coherence by $`\sqrt{q_0q_1}\le2^{-\alpha}`$. If the branch probability is $`p`$, its contribution to target fidelity is at most $`p/2+2^{-\alpha}`$. Summing over at most $`M`$ complete transcripts gives $`F\le1/2+M2^{-\alpha}`$.

For $`\alpha\ge2`$, interpolation gives the following dimension-dependent estimate for a positive-probability branch:

```math
g\le \frac1d\,p^{(\alpha-2)/(\alpha-1)}.
```

Concavity of the probability power then yields

```math
F\le \frac1d\,M^{1/(\alpha-1)}.
```

These formulas keep the probability cost of postselection. A normalized branch may be exactly GHZ even though the unconditional output has low fidelity.

Grouping $`k`$ qubits at each laboratory into one register sets $`d=2^k`$. A depth-$`c_k`$ binary protocol has at most $`2^{c_k}`$ leaves, so

```math
F_k\le
\min\left\{1,2^{\,c_k/(\alpha-1)-k}\right\}.
```

At a rate below $`\alpha-1`$ bits per target copy by a fixed positive amount, global fidelity decays exponentially in the number of copies. The sources and local processing may be coherent across the full block.

## Why the resource convention changes the answer

A worst-case budget restricts every execution. A mean budget can place a large cost on a selected fraction of executions. On a retained-hub star, shared randomness can choose exact preparation with probability $`q`$ and a local product output otherwise. This yields mean cost $`q(n-2)k`$ and fidelity $`q+(1-q)2^{-k}`$.

The entropy converse matches this construction to leading order: at fixed required global fidelity $`f>0`$, the optimal mean cost per copy tends to $`(n-2)f`$. The exact worst-case threshold remains $`n-2`$. [The expected-cost page](expected-and-heralded.md) states both finite bounds and the limiting statement.

A heralded task instead asks for a high-quality state only on accepted transcripts. For $`\alpha\ge2`$, its success probability is constrained by $`P(dF_{\rm acc})^{\alpha-1}\le M_{\rm acc}`$. A small announced success flag does not make a rare event deterministic.

## Exact benchmarks beyond the packing bound

The packing parameter is not the complete topology dependence. An additional entropy argument is exact for trees.

Remove a vertex $`v`$ from a source tree and regard each remaining component as a laboratory group. After tracing out $`v`$, the groups initially share no correlation conditional on the shared seed. A message from inside a group cannot increase their conditional total correlation. A bit from $`v`$ increases it by at most one. Exact GHZ output requires $`(\deg(v)-1)\log_2d`$ bits of this correlation, giving a matching lower bound on $`v`$'s outbound communication.

Summing over vertices gives $`(n-2)\log_2d`$. Sequential growth from one entangled edge uses one correction symbol per added vertex and attains this cost for $`d=2^k`$, even with point-to-point classical delivery.

If the star hub is a discarded helper and the outputs are its $`N`$ leaves, the target is pure across all leaf laboratories. Their required total correlation is $`N\log_2d`$. Only hub messages can increase it from its initial zero value, so the hub must send at least $`N\log_2d`$ bits on average. Fusion followed by a Fourier measurement and phase correction attains the bound when $`d=2^k`$.

These statements allow arbitrary independent edge states and arbitrary interaction. They do not establish an exact dense-graph coefficient or an approximate tree strong-converse rate of $`n-2`$.

## Evidence and attribution

The unrestricted statements are supported by the proofs in the topic pages. The [finite verification suite](../verification/README.md) checks explicit preparation maps and boundary examples. It does not enumerate all quantum protocols.

The inherited mathematical ingredients are Finner's product-space inequality, its quantum network formulation, and relative-entropy data processing. The closest operational antecedents include the no-communication GHZ fidelity obstruction and classical PIN public-discussion laws. The [related-work account](../references/related-work.md) gives precise source pointers and explains where a different charged resource or operation class prevents direct identification with the present statements.

