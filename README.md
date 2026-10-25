# GHZ Communication Cost

How much classical communication is needed to turn independent pairwise quantum resources into a coherent multipartite GHZ state?

The amount of pairwise entanglement is unrestricted. Each source may have arbitrary finite dimension, local processing may be coherent and adaptive, and shared classical randomness is free. Nevertheless, preparing a qubit GHZ state at fixed fidelity above one half requires a number of classical bits proportional to the number of output parties. The same obstruction gives an exponential loss of global fidelity when many GHZ states are prepared below a graph-dependent communication rate.

## Principal results

Let $`G`$ be the graph of independent bipartite sources, $`O`$ its $`n`$ designated output parties, and $`\alpha=\alpha^*(G[O])`$ the fractional independence number of the output-induced graph. Helper laboratories have weight zero. Fidelity is the squared overlap with the specified pure GHZ target, averaged over every execution.

For at most $`M`$ complete communication transcripts, the [finite-transcript converse](science/communication-converses.md#finite-transcript-fidelity-bounds) gives

```math
F_{\mathrm{GHZ}_{n,2}}
\le \min\left\{1,\frac12+M\,2^{-\alpha}\right\},
\qquad
F_{\mathrm{GHZ}_{n,d}}
\le\min\left\{1,\frac{M^{1/(\alpha-1)}}d\right\}
\quad(\alpha\ge2).
```

A worst-case budget of $`c`$ binary bits implies $`M\le2^c`$. Since $`\alpha\ge n/2`$, any fixed qubit fidelity $`F>1/2`$ obeys

```math
c\ge\frac n2+\log_2\left(F-\frac12\right).
```

This applies even when every pair of outputs shares an arbitrarily large resource and additional finite helper laboratories are available. It counts communication volume; it does not assert a latency bound.

| Task and architecture | Established result | Proof or construction |
|---|---|---|
| $`k`$ qubit GHZ copies, global fidelity, $`\alpha\ge2`$ | $`F_k\le\min\{1,2^{\,c_k/(\alpha-1)-k}\}`$ | [Collective converse](science/communication-converses.md#collective-preparation-of-many-ghz-states) |
| Exact output at every vertex of a tree | Optimal worst-case and mean cost $`k(n-2)`$ bits | [Tree entropy bound and sequential growth](science/achievability-and-limits.md#exact-output-at-every-tree-vertex) |
| Star with its hub retained, fixed global fidelity $`f>0`$ | Optimal asymptotic mean cost per copy $`(n-2)f`$ | [Mean-cost frontier](science/expected-and-heralded.md#a-matching-mean-cost-frontier-on-a-star) |
| $`N`$ leaves with a separate discarded hub, exact output | Optimal cost $`Nk`$ bits; the hub alone must send at least this many on average | [Discarded-hub theorem](science/achievability-and-limits.md#a-hub-that-is-discarded-changes-the-task) |
| Heralded $`d`$-level output, $`\alpha\ge2`$ | $`P(dF_{\rm acc})^{\alpha-1}\le M_{\rm acc}`$ | [Success–fidelity tradeoff](science/expected-and-heralded.md#heralded-preparation) |

Here $`P`$ is the acceptance probability and $`M_{\rm acc}`$ counts accepted complete transcripts. In the exact-cost rows, $`k`$ qubit copies are locally equivalent to one $`d=2^k`$ target.

## Why the bound survives adaptive communication

Fixing a complete transcript turns the protocol into a product of local trace-nonincreasing maps. The inherited quantum Finner inequality then constrains the unnormalized probability of a common GHZ basis label. A fidelity estimate retains both the coherence and the probability of that branch. Summing over the allowed transcripts gives the communication bound.

The branch probability is essential: a rare selected outcome can prepare an exact GHZ state. The converse charges the full protocol, including how often that outcome occurs and how acceptance becomes available to the parties. [The branch proof](science/branch-bound.md) gives the complete derivation and attribution.

The exact tree and discarded-hub benchmarks use a second argument. Conditional total correlation starts at zero across suitable groups of laboratories. Messages sent from outside those groups increase it by at most their entropy. The exact GHZ output requires a specified amount of that correlation.

## Reading routes

| Goal | Start here |
|---|---|
| Learn the project through the selected Watrous anchor | [Learning overview](learning/README.md), [source bridge](learning/bridge.md), and [30 milestones](learning/milestones.md) |
| Follow the complete scientific argument | [Scientific overview](science/README.md) |
| Check the resource assumptions and conventions | [Model and charged resources](science/model.md) |
| Inspect the central inequality and transcript factorization | [Branch bound](science/branch-bound.md) |
| Check finite-budget and collective claims | [Communication converses](science/communication-converses.md) |
| Compare mean cost, fixed cost and heralding | [Expected communication and heralding](science/expected-and-heralded.md) |
| Inspect physical protocols and exact special cases | [Constructions and limits](science/achievability-and-limits.md) |
| Identify inherited results and the closest comparisons | [Related work](references/related-work.md) and [bibliography](references/references.bib) |
| Reproduce finite construction checks | [Verification guide](verification/README.md) |

## Learning route

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [bridge](learning/bridge.md) gives targeted book sections, translates the root-fidelity convention, and develops a complete one-bit fusion example before connecting instruments and entropy to the network bounds.

The [shared map of 30 milestones](learning/milestones.md) has 12 background/preliminaries milestones and 18 narrative/innovation milestones. Each phase moves from local objects and mechanisms to the complete preparation problem. The [learning overview](learning/README.md) offers direct routes for foundations, the main converse, exact benchmarks, and reproduction.

## Scope and interpretation

The resources are independent **bipartite** quantum sources, conditional on a shared classical seed. Free multipartite quantum sources or later quantum communication change the problem. All information-bearing choices of messages, routing, timing, silence and termination must be charged or fixed by the protocol.

The strong converse concerns a fixed worst-case bit budget and fidelity with the entire output block. Mean communication admits randomized abort strategies and has a different optimal frontier on a star. High fidelity of individual copies alone does not imply high global block fidelity.

For a complete source graph the exact qubit cost is bounded between $`\lceil n/2-1\rceil`$ and $`n-2`$; its optimal coefficient is not established here. The exact tree theorem does not supply a stronger approximate-fidelity exponent on every tree. The dimension-dependent Finner converse requires $`\alpha\ge2`$; the three-output triangle is outside that range.

The [source comparison](references/related-work.md) attributes quantum Finner, the zero-communication GHZ benchmark, classical PIN packing laws and elementary fusion to prior work. It distinguishes a charged quantum communication converse from bounds on rounds, source yield and costs of particular protocols.

## Reproduction

From the repository root, run:

```bash
python3 verification/check_science.py
```

The suite uses only the Python standard library. It checks explicit small-system state transformations, correction conventions, private and coarse-grained syndromes, heralding, discarded-hub phases, and a complex-amplitude Finner diagnostic. The [verification guide](verification/README.md) states the coverage and its limits. These finite checks support the constructions; the analytical proofs establish the unrestricted converses.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

