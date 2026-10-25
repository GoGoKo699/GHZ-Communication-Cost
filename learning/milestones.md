# Thirty milestones for understanding GHZ communication cost

This map follows the scientific problem: how much classical communication is needed to prepare a specified coherent GHZ state from independent bipartite quantum sources of unrestricted finite dimension? Its targets depend on the project and its mathematical structure. The canonical assumptions and results remain in the [scientific account](../science/README.md).

The sole educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, cited below as [Watrous](../references/related-work.md#watrous2018). The [bridge](bridge.md) connects its notation and foundations to this project. Primary papers cited for Finner, classical network information, or GHZ protocols provide research attribution and proof dependencies; they are not additional educational anchors.

## Allocation and progression

| Phase | Milestones | Scientific purpose |
|---|---|---|
| Background/preliminaries | M01–M12: 12 milestones | Build from individual quantum registers and local operations to branch probabilities, a distributed-source model, charged communication, graph weights, and entropy. M12 integrates these into one precisely specified preparation task. |
| Narrative/innovation | M13–M30: 18 milestones | Assemble the branch converse, its communication consequences, the distinctions between fixed, mean and heralded cost, and the separate entropy mechanism for exact architectures. M30 integrates the established landscape and its remaining gap. |

The allocation gives more space to the narrative because the project connects two converse mechanisms and three communication conventions. Understanding why their conclusions differ is as central as understanding the inequalities. The background supplies the shared language once; the narrative follows how local events become a global resource constraint, then places matching constructions and limitations alongside it. Neither phase attempts to reproduce every technical calculation in the scientific pages.

## Phase I: Background/preliminaries

<a id="m01"></a>
### M01: Registers and reduced states

**Central question:** What mathematical objects describe the systems inside a laboratory and the information available when other systems are ignored?

**Understanding target:** Interpret a finite-dimensional register, a density operator, a tensor product, and a reduced state obtained by partial trace. Distinguish the dimension of a system from the number of laboratories holding it, and distinguish a pure global state from its potentially mixed local reductions.

**Dependencies and story role:** None within this map. This establishes the local objects that will later be grouped into source edges, output registers, and laboratory components.

**Conceptual connection:** A source can supply two laboratories with a pure entangled state while neither laboratory has a pure local state. Both the branch proof and the entropy proof require consistent movement between these global and local descriptions.

**Source pointers:** [Watrous](../references/related-work.md#watrous2018), §§2.1.1–2.1.2, Definitions 2.1 and 2.5, and §1.1, Eqs. (1.120)–(1.121) for partial traces; [source and output registers](../science/model.md#independent-quantum-sources-and-helpers).

<a id="m02"></a>
### M02: Coherent GHZ states and common classical labels

**Central question:** What distinguishes the GHZ target from laboratories merely possessing the same classical value?

**Understanding target:** Interpret $`|\mathrm{GHZ}_{n,d}\rangle=d^{-1/2}\sum_x|x\rangle^{\otimes n}`$ as a coherent superposition. Distinguish it from the mixture of the corresponding basis states, even though both produce identical common-label statistics when measured in that basis. Recognize the two-party case as a maximally entangled pair.

**Dependencies and story role:** M01. This gives the preparation task a physical target before introducing its allowed operations and communication accounting.

**Conceptual connection:** The difference is carried by off-diagonal terms. It explains why shared classical randomness is free without making coherent GHZ preparation free, and why a converse must constrain coherence as well as matching outcomes.

**Source pointers:** [Watrous](../references/related-work.md#watrous2018), §2.1.2 for quantum-state formalism; [target definition](../science/model.md#the-preparation-task); [classical correlations and coherent output](../science/achievability-and-limits.md#perfect-classical-correlations-do-not-give-a-coherent-ghz-state).

<a id="m03"></a>
### M03: Local channels and physical operations

**Central question:** How are general physical operations within a laboratory represented?

**Understanding target:** Explain the roles of linearity, complete positivity, and trace preservation in a quantum channel. Connect a channel to its operator representation, local ancillas, and discarded registers. Distinguish a local channel acting jointly on all systems in one laboratory from an operation coupling different laboratories.

**Dependencies and story role:** M01–M02. This expands the setting beyond particular gates and makes the unrestricted local-operation class precise.

**Conceptual connection:** The converses must allow coherent processing of all incident edge systems. Treating local processing as a general channel prevents a proof about one fusion circuit from being mistaken for a proof about every protocol.

**Source pointers:** [Watrous](../references/related-work.md#watrous2018), §2.2, Definition 2.13, Theorem 2.22 and Corollary 2.27; [allowed source dimensions and local memories](../science/model.md#independent-quantum-sources-and-helpers).

<a id="m04"></a>
### M04: Instruments and unnormalized branches

**Central question:** How can an operation describe both a classical outcome and the quantum state associated with that outcome?

**Understanding target:** Interpret an instrument as a family of completely positive, trace-nonincreasing maps whose sum is a channel. Read the trace of an unnormalized output as its outcome probability, and distinguish that output from the normalized state obtained after conditioning.

**Dependencies and story role:** M03. This introduces the central object on which the later converse acts: a physical branch with its probability still attached.

**Conceptual connection:** A rare branch may contain an exact GHZ state. Retaining the branch probability makes it possible to constrain a whole preparation protocol without incorrectly treating a postselected state as a deterministic network output.

**Source pointers:** [Watrous](../references/related-work.md#watrous2018), §2.3.2, Eqs. (2.258)–(2.262); [branch-state notation](../science/model.md#output-states-branches-and-collective-copies).

<a id="m05"></a>
### M05: Independent pair sources and the shared seed

**Central question:** Which correlations are initially supplied, and which independence assumption survives free shared classical randomness?

**Understanding target:** Describe an edge as one bipartite quantum source and a laboratory as the holder of its incident source registers. Explain why the initial state factors across edges after conditioning on the shared seed $`R`$, even when the unconditional state is a correlated classical mixture. Identify designated outputs and helper laboratories.

**Dependencies and story role:** M01–M04. This connects local quantum objects into the distributed physical setting.

**Conceptual connection:** Independence is a property of the source preparation, not of measurement outcomes or of a normalized postselected branch. It is the structural input to Finner and to the initial-product-state step of the tree entropy proof.

**Source pointers:** [independent sources and helpers](../science/model.md#independent-quantum-sources-and-helpers); [Watrous](../references/related-work.md#watrous2018), §§2.1.2 and 2.2 for composite states and local operations.

<a id="m06"></a>
### M06: Adaptive LOCC trees

**Central question:** How does a sequence of local operations become an interactive distributed protocol?

**Understanding target:** Describe local operations and classical communication as a tree in which later instruments depend on earlier messages and private local memory. Distinguish the complete communicated transcript from the collection of all private measurement outcomes. Explain how a fixed transcript determines the incoming messages seen by each party.

**Dependencies and story role:** M04–M05. This supplies the operational structure needed to move from one local outcome to one full protocol branch.

**Conceptual connection:** Watrous supplies a finite two-party LOCC paradigm. The project specifies the multipartite, charged transcript model and later proves why arbitrary private histories can be summed inside local success maps.

**Source pointers:** [Watrous](../references/related-work.md#watrous2018), §6.1.2, Definition 6.25 and Proposition 6.26; [complete transcripts](../science/model.md#complete-transcripts).

<a id="m07"></a>
### M07: Transcript counts, bit budgets, and stopping

**Central question:** What exactly is counted when a protocol is said to use classical communication?

**Understanding target:** Distinguish a maximum number $`M`$ of complete transcripts, a worst-case bit length $`c`$, and a mean length $`L`$. Explain prefix-freeness and the implication $`M\le2^c`$, without assuming that every interactive $`M`$-leaf protocol has depth $`\lceil\log_2M\rceil`$. Account for information conveyed by routing, speaker choice, silence, timing, and stopping.

**Dependencies and story role:** M06. This turns the protocol tree into a well-defined resource model before any communication lower bound is stated.

**Conceptual connection:** A bit-volume converse survives free broadcast and therefore also lower-bounds total point-to-point communication. Turning that volume into a time or round bound requires additional assumptions.

**Source pointers:** [communication conventions](../science/model.md#classical-communication), especially the transcript table, broadcast convention, and finite/mean protocol definitions.

<a id="m08"></a>
### M08: Pure-target fidelity and global block fidelity

**Central question:** Which aspect of the output is required to be close to the desired state?

**Understanding target:** Interpret the project's fidelity as $`F=\langle\mathrm{GHZ}|\rho|\mathrm{GHZ}\rangle`$, the square of Watrous's fidelity with a pure target. Explain its linearity in an unnormalized branch or an output mixture. Distinguish fidelity with an entire block of GHZ states from the fidelities of its individual marginals.

**Dependencies and story role:** M02, M04 and M06. This fixes the quality criterion that the communication bounds will control.

**Conceptual connection:** Linearity permits branch contributions to be summed exactly. The global criterion also permits $`k`$ target qubits at each laboratory to be relabeled as one $`2^k`$-dimensional register without imposing independence between copies.

**Source pointers:** [Watrous](../references/related-work.md#watrous2018), §3.2, Definition 3.11, Eq. (3.64), and Proposition 3.13, Eq. (3.80); [fidelity convention](../science/model.md#the-preparation-task); [collective output definition](../science/model.md#output-states-branches-and-collective-copies).

<a id="m09"></a>
### M09: Fractional independence and helper weights

**Central question:** How can a source graph encode a restriction on simultaneous local events?

**Understanding target:** Interpret feasible weights $`0\le w_v\le1`$ with $`w_u+w_v\le1`$ on every edge, and helper weights fixed to zero. Explain why their maximum sum is $`\alpha=\alpha^*(G[O])`$, why $`\alpha\ge n/2`$, and why retained-hub and discarded-hub stars have different output-induced graphs.

**Dependencies and story role:** M05 and M07. This introduces the graph parameter that will convert source structure into quantitative communication statements.

**Conceptual connection:** The weights express admissible exponents in an event inequality. They provide a valid converse parameter, not a complete characterization of all network capabilities or all effects of helpers.

**Source pointers:** [graph parameter and examples](../science/model.md#the-graph-parameter); [feasible weights](../science/branch-bound.md); [Finner attribution](../references/related-work.md#finner1992).

<a id="m10"></a>
### M10: Positivity and Hölder as probability tools

**Central question:** Which elementary inequalities connect diagonal probabilities, coherence, and sums over possible labels?

**Understanding target:** Explain why positivity bounds an off-diagonal matrix element by the geometric mean of its two diagonal entries. Interpret Hölder's inequality as a way to control a sum of products using separate sums, and recognize that its exponents must satisfy their stated conditions. Connect $`0\le A\le I`$ to $`A^2\le A`$ for a measurement effect.

**Dependencies and story role:** M01, M04, M08 and M09. This supplies the mathematical links used repeatedly between an event constraint and a fidelity constraint.

**Conceptual connection:** These inequalities do not create network independence. They turn the independently established network constraint into bounds on common-label mass and coherent target overlap.

**Source pointers:** [half-weight Finner proof](../science/branch-bound.md#the-half-weight-inequality); [diagonal mass](../science/branch-bound.md#the-diagonal-mass-constraint); [positivity and interpolation](../science/branch-bound.md#coherence-and-fidelity-of-one-branch).

<a id="m11"></a>
### M11: Entropy and data processing

**Central question:** How can information quantities describe uncertainty and correlations without referring to a particular gate circuit?

**Understanding target:** Distinguish Shannon entropy, von Neumann entropy, mutual information, and quantum relative entropy. Explain conditional entropy with a classical record as an average over its branches. Interpret relative-entropy data processing as the statement that applying a physical channel cannot increase distinguishability.

**Dependencies and story role:** M01, M03–M04 and M08. This supplies the second mathematical language needed for transcript entropy and exact architecture-specific converses.

**Conceptual connection:** Entropy will serve two distinct purposes: bounding the information carried by a transcript, and measuring correlations created across groups of laboratories. The latter requires a separate message-by-message argument.

**Source pointers:** [Watrous](../references/related-work.md#watrous2018), §5.1.1, Definition 5.1; §5.2.1, Definitions 5.17–5.18 and Eqs. (5.90)–(5.91); §5.2.3, Theorem 5.35; [conditional total correlation](../science/achievability-and-limits.md#conditional-total-correlation-and-a-public-message).

<a id="m12"></a>
### M12: Synthesis: the complete preparation problem

**Central question:** What must be specified before a claim about GHZ communication cost has a definite meaning?

**Understanding target:** Integrate the source graph, designated outputs, shared seed, allowed local processing, charged transcript, and output-fidelity criterion into one preparation model. Distinguish unrestricted finite-dimensional pair resources from free multipartite sources or later quantum communication. Explain why changing the outputs, cost convention, or error criterion can change the conclusion.

**Dependencies and story role:** M01–M11. This is the background synthesis: all local objects and prerequisite ideas now fit into a single operational problem.

**Conceptual connection:** The model determines which statements can be compared. It also reveals the task of the narrative: retain branch probability while deriving communication restrictions that remain valid for arbitrary allowed local processing.

**Source pointers:** [complete model](../science/model.md); [scientific overview](../science/README.md); [anchor-to-project bridge](bridge.md#notation-and-conventions).

## Phase II: Narrative/innovation

<a id="m13"></a>
### M13: Quantum Finner from local events

**Central question:** What limits the joint probability of local success events on independent bipartite sources?

**Understanding target:** Interpret the inherited quantum Finner inequality $`P\le\prod_{v:w_v>0}P_v^{w_v}`$. Explain the roles of source independence, local effects, and feasible weights. Understand why mixed edge states, local ancillas, complex amplitudes, and zero-weight vertices are included in the proof.

**Dependencies and story role:** M05, M09–M10 and M12. The narrative begins with a local-event constraint that already applies to a whole source network.

**Conceptual connection:** Purifying each edge preserves its two-endpoint structure. Taking absolute values in the tensor contraction allows the classical Finner inequality to control complex quantum amplitudes; positivity then relates the local norms back to event probabilities.

**Source pointers:** [Theorem B1 and its proof](../science/branch-bound.md#quantum-finner-inequality); [Renou et al.](../references/related-work.md#ren2019); [Finner](../references/related-work.md#finner1992).

<a id="m14"></a>
### M14: Factorizing a complete transcript

**Central question:** How can an adaptive interactive protocol be related to local success events on its original sources?

**Understanding target:** Explain the fixed-seed, fixed-transcript identity $`\sigma_{t|r}=(\bigotimes_v\Lambda_{v,t|r})(\rho^{\mathrm{in}}_r)`$, with local completely positive, trace-nonincreasing maps. Understand why private histories consistent with the transcript are summed inside these maps, and why this does not require statistical independence between those histories.

**Dependencies and story role:** M04–M07, M12 and M13. This connects the distributed protocol to the event inequality without imposing restrictions on adaptivity.

**Conceptual connection:** A complete transcript fixes every incoming classical message. Each party can then enforce consistency locally. The factorization applies to an unnormalized branch and does not assert independent sources for its normalized conditional output.

**Source pointers:** [Lemma B2](../science/branch-bound.md#factorization-of-a-fixed-transcript); [Watrous](../references/related-work.md#watrous2018), §2.3.2 and §6.1.2 for instruments and LOCC foundations.

<a id="m15"></a>
### M15: The common-label mass constraint

**Central question:** How does the network event inequality constrain all possible GHZ basis labels within one branch?

**Understanding target:** Interpret $`q_x=\langle x^n|\sigma|x^n\rangle`$ as unnormalized common-label mass. Explain how pulling basis measurements back through the local success maps gives local effects with total probability at most one. Connect Finner and weighted Hölder to

```math
\sum_x q_x^{1/\alpha}\le1.
```

**Dependencies and story role:** M09–M10 and M13–M14. This condenses the source graph and local operations into the single branch constraint used by the fidelity arguments.

**Conceptual connection:** The inequality concerns a collection of mutually exclusive target labels. It retains the cost of local success while allowing the branch state itself to be entangled.

**Source pointers:** [Lemma B3](../science/branch-bound.md#the-diagonal-mass-constraint); [branch notation](../science/model.md#output-states-branches-and-collective-copies).

<a id="m16"></a>
### M16: Coherence and the qubit branch bound

**Central question:** Why does a small amount of branchwise coherence limit the fidelity of a qubit GHZ output?

**Understanding target:** Connect the two GHZ basis populations to the off-diagonal matrix element through positivity. Explain the bound $`|\sigma[0^n,1^n]|\le2^{-\alpha}`$ and the resulting unnormalized fidelity contribution $`g\le p/2+2^{-\alpha}`$, where $`p=\operatorname{Tr}\sigma`$.

**Dependencies and story role:** M02, M08, M10 and M15. This is the first conversion of the network constraint into a quantum-quality bound.

**Conceptual connection:** The population contribution has a total budget of one half after summing all unnormalized branches of a normalized protocol. Communication can add coherent branch contributions, but each contribution is bounded by the source graph. This argument does not require $`\alpha\ge2`$.

**Source pointers:** [Proposition B4](../science/branch-bound.md#coherence-and-fidelity-of-one-branch); [Theorem C1](../science/communication-converses.md#finite-transcript-fidelity-bounds).

<a id="m17"></a>
### M17: Branch probability and dimension-dependent fidelity

**Central question:** How can the branch's probability strengthen the bound when the target has many basis labels?

**Understanding target:** Explain how positivity and Hölder interpolate the common-label mass constraint with $`\sum_xq_x\le p`$. For $`\alpha\ge2`$ and $`p>0`$, interpret

```math
g\le\frac1d\,p^{(\alpha-2)/(\alpha-1)}.
```

Understand why $`\alpha=2`$ is handled directly and zero-probability branches contribute zero.

**Dependencies and story role:** M08, M10 and M15–M16. This provides the branch estimate that will govern large target registers and collective preparation.

**Conceptual connection:** The power of $`p`$ records the probabilistic cost of concentrating fidelity into selected branches. Its derivation requires $`\alpha\ge2`$; it cannot be extended to the triangle merely by reusing the formula.

**Source pointers:** [Proposition B5](../science/branch-bound.md#coherence-and-fidelity-of-one-branch); [domain and triangle counterexample](../science/communication-converses.md#finite-transcript-fidelity-bounds).

<a id="m18"></a>
### M18: From branches to a bit converse

**Central question:** What survives when all communicated branches are combined into the unconditional output?

**Understanding target:** Explain how linearity of pure-target fidelity, normalization of transcript probabilities, and concavity yield $`F_2\le1/2+M2^{-\alpha}`$ and, for $`\alpha\ge2`$, $`F_d\le M^{1/(\alpha-1)}/d`$, with fidelity also bounded by one. Translate a worst-case bit budget using $`M\le2^c`$.

**Dependencies and story role:** M07–M08 and M14–M17. This completes the passage from local events to a whole-protocol communication bound.

**Conceptual connection:** The transcript limit is imposed for each shared seed, and the final inequality remains valid after averaging the seed. Summing probabilities is essential; counting normalized successful branches would lose the operational constraint.

**Source pointers:** [Theorems C1–C2](../science/communication-converses.md#finite-transcript-fidelity-bounds); [Corollary C3](../science/communication-converses.md#worst-case-binary-communication).

<a id="m19"></a>
### M19: Helper networks and extensive communication

**Central question:** Can arbitrarily large pair resources or additional helper laboratories eliminate the party-number cost?

**Understanding target:** Use the feasible half weights on all outputs to understand $`\alpha\ge n/2`$ for any finite helper network. Interpret the consequence $`c\ge n/2+\log_2(F_2-1/2)`$ at fixed $`F_2>1/2`$. Explain why all helper communication remains charged even though helper weights are zero.

**Dependencies and story role:** M05, M09 and M18. This turns the graph-dependent converse into a uniform statement across architectures and source dimensions.

**Conceptual connection:** More initial pairwise entanglement does not remove the need to communicate a coherent multipartite correction. The result constrains communication volume; it neither assigns a latency nor asserts that helpers have no operational use.

**Source pointers:** [Corollary C4 and finite helper networks](../science/communication-converses.md#arbitrary-finite-helper-networks); [broadcast and delivery conventions](../science/model.md#broadcast-convention-and-other-delivery-models).

<a id="m20"></a>
### M20: Collective preparation and the strong converse

**Central question:** What changes when all target copies and all local resources are processed together?

**Understanding target:** Explain the local equivalence between $`k`$ qubit GHZ copies and one $`d=2^k`$ GHZ target. For $`\alpha\ge2`$, interpret

```math
F_k\le\min\{1,2^{\,c_k/(\alpha-1)-k}\}.
```

Understand exponential decay of global fidelity below the proved worst-case communication rate, while allowing arbitrary correlations between copies within each source edge.

**Dependencies and story role:** M08, M17–M19. This extends the one-branch mechanism to an unrestricted block protocol.

**Conceptual connection:** No independent-copy approximation enters the proof. The restriction is independence between source edges, and the conclusion concerns the full block. The rate $`\alpha-1`$ is a converse rate; optimality for an architecture additionally needs a matching construction.

**Source pointers:** [Corollary C5](../science/communication-converses.md#collective-preparation-of-many-ghz-states); [global versus marginal fidelity](../science/achievability-and-limits.md#global-block-fidelity-and-single-copy-marginals).

<a id="m21"></a>
### M21: Star fusion and a matching exact rate

**Central question:** Which physical protocol attains the converse on a star whose hub remains an output?

**Understanding target:** Describe fusion of the hub's maximally entangled pairs through controlled subtraction, measurement of correction syndromes, and local corrections at the leaves. Explain the $`d^{n-2}`$ equiprobable correction words and the exact cost $`k(n-2)`$ when $`d=2^k`$ and all $`n\ge3`$ star vertices are outputs.

**Dependencies and story role:** M02–M04, M09 and M18–M20. This supplies a concrete matching architecture for the abstract converse.

**Conceptual connection:** The syndrome records identify which coherent GHZ state was produced. Communicating them turns branchwise success into the specified unconditional target. The construction is repeated elementary fusion, with its prior attribution retained.

**Source pointers:** [star fusion and communication accounting](../science/achievability-and-limits.md#star-fusion-with-the-hub-retained-as-an-output); [Grudka et al.](../references/related-work.md#grudka2008); [one-bit example](bridge.md#one-bit-fusion-example).

<a id="m22"></a>
### M22: Exact transcript entropy

**Central question:** What does exact output imply about the probability and information content of every transcript?

**Understanding target:** Explain why an exact unconditional pure target forces every positive-probability branch to have that target for almost every seed. Use the common-label constraint to interpret $`p_{t|r}\le d^{1-\alpha}`$, and connect this to transcript entropy and the mean-cost lower bound $`L\ge(\alpha-1)\log_2d`$.

**Dependencies and story role:** M07–M08, M11 and M15. This changes the communication currency from a maximum number of leaves to expected prefix-free length.

**Conceptual connection:** Exact preparation places an information requirement on each transcript distribution. The argument remains available when the approximate dimension-dependent theorem's condition $`\alpha\ge2`$ is unavailable.

**Source pointers:** [Corollary B6](../science/branch-bound.md#coherence-and-fidelity-of-one-branch); [exact mean-cost converse, E1–E2](../science/expected-and-heralded.md#exact-preparation-every-transcript-has-small-probability); [Watrous](../references/related-work.md#watrous2018), §5.1.1.

<a id="m23"></a>
### M23: Approximate mean cost and the star frontier

**Central question:** Why does limiting average communication give a different fidelity-rate relation from limiting every execution?

**Understanding target:** Explain how a transcript-length cutoff yields an extensive mean-cost bound for qubit fidelity above one half. For $`\alpha\ge2`$, interpret $`L\ge(\alpha-1)[F\log_2(dF)]_+`$. Connect this entropy bound to a shared-seed mixture of exact star fusion and product output, giving the asymptotic mean cost $`(n-2)f`$ per copy at fixed global fidelity $`f\in(0,1]`$.

**Dependencies and story role:** M07, M11 and M16–M22. This integrates branch probabilities, entropy, and an achievable mixture into the mean-cost landscape.

**Conceptual connection:** Rare or selected expensive executions are allowed under a mean budget. Their contribution to average fidelity prevents the worst-case strong converse from being transferred unchanged to expected communication.

**Source pointers:** [cutoff bound, E3–E5](../science/expected-and-heralded.md#approximate-qubit-ghz-a-cutoff-bound); [entropy bound, E6](../science/expected-and-heralded.md#approximate-higher-dimensional-ghz-an-entropy-bound); [star frontier, E7–E9](../science/expected-and-heralded.md#a-matching-mean-cost-frontier-on-a-star).

<a id="m24"></a>
### M24: Heralding and rare successful branches

**Central question:** What does a protocol owe when it promises a good state only on announced successful executions?

**Understanding target:** Distinguish acceptance probability $`P`$, accepted-output fidelity $`F_{\mathrm{acc}}`$, and the per-seed bound $`M_{\mathrm{acc}}`$ on accepted complete transcripts. For $`\alpha\ge2`$, interpret $`P(dF_{\mathrm{acc}})^{\alpha-1}\le M_{\mathrm{acc}}`$. Explain how selecting star correction words saturates this relation, including the single-word success probability.

**Dependencies and story role:** M04, M07, M17–M18 and M21. This completes the comparison between unconditional, mean-cost, and heralded tasks.

**Conceptual connection:** A one-bit announced success flag can identify a rare exact outcome without making that outcome deterministic. Acceptance must be available through the specified charged protocol; hidden remote measurement records do not supply a free herald.

**Source pointers:** [heralded preparation and star saturation, E10–E11](../science/expected-and-heralded.md#heralded-preparation); [private and coarse-grained syndromes](../science/achievability-and-limits.md#private-syndromes-and-uncorrected-outputs).

<a id="m25"></a>
### M25: How a public message changes total correlation

**Central question:** Which messages can create correlations across groups of laboratories, and by how much?

**Understanding target:** Interpret conditional total correlation as the average relative entropy between each joint branch state and the product of its marginals. Explain why a message produced within one group cannot increase it after conditioning on that message, while a message from an outside party can increase it by at most its conditional Shannon entropy.

**Dependencies and story role:** M04–M06 and M11–M12. This begins the second converse mechanism, with a local message-level statement rather than a packing inequality.

**Conceptual connection:** Data processing controls the local instrument; revealing its outcome changes the conditioning record. Distinguishing inside from outside senders exposes which party must supply the information in an exact architecture-specific preparation.

**Source pointers:** [message identities A9–A11](../science/achievability-and-limits.md#conditional-total-correlation-and-a-public-message); [Watrous](../references/related-work.md#watrous2018), §§5.2.1–5.2.2, Proposition 5.20, and §5.2.3, Theorem 5.35; [data-processing attribution](../references/related-work.md#lindblad1975).

<a id="m26"></a>
### M26: Exact costs on trees

**Central question:** Why is the exact tree cost determined even when the packing converse is not tight on that tree?

**Understanding target:** Remove a tree vertex $`v`$, group the remaining laboratories into components, and explain their initial conditional independence. Connect the exact GHZ target to required total correlation $`(\deg(v)-1)\log_2d`$, proving the corresponding outbound mean-cost bound. Sum over vertices and relate the result to sequential growth, which attains $`k(n-2)`$ bits for $`d=2^k`$.

**Dependencies and story role:** M05, M21 and M25. This assembles a message-level inequality into an exact whole-network benchmark.

**Conceptual connection:** All tree vertices are outputs. Arbitrary independent edge states and interaction are allowed, and a fixed-cutoff argument extends the exact bound to almost-sure termination with finite mean length. This exact result alone supplies no stronger approximate-fidelity exponent on every tree.

**Source pointers:** [Theorem A1](../science/achievability-and-limits.md#exact-output-at-every-tree-vertex); [sequential growth](../science/achievability-and-limits.md#sequential-growth-on-any-connected-source-graph); [termination extension](../science/achievability-and-limits.md#almost-sure-termination-in-the-exact-entropy-benchmarks).

<a id="m27"></a>
### M27: A discarded hub and the phase cost

**Central question:** Why does discarding the star hub change the exact communication benchmark?

**Understanding target:** Distinguish $`N\ge2`$ output leaves plus a separate helper hub from a star with its hub included among the outputs. Explain the additional Fourier-measurement phase correction in the construction. Connect the pure leaf target's total correlation $`N\log_2d`$ to a matching hub-outbound lower bound, even with interactive leaf messages.

**Dependencies and story role:** M05, M21 and M25–M26. This identifies a second exact architecture and makes the output/helper distinction operational.

**Conceptual connection:** In the tree-vertex argument, the excluded output is traced from an exact GHZ state, leaving classical common-label correlation. The discarded-hub task instead requires a pure GHZ state across all leaf groups, with a different entropy requirement.

**Source pointers:** [Theorem A2 and the phase correction](../science/achievability-and-limits.md#a-hub-that-is-discarded-changes-the-task); [Chen et al. and the extension of its source/operation class](../references/related-work.md#chen2024).

<a id="m28"></a>
### M28: Attribution and the unresolved dense-graph gap

**Central question:** What is established by this communication account beyond its inherited ingredients, and what remains open?

**Understanding target:** Distinguish quantum Finner, prior zero-communication bounds, classical PIN packing laws, elementary fusion, and communication-round measures from the charged adaptive quantum conclusions here. Explain why a classical measure-first reduction needs justification. Locate the remaining exact complete-graph cost between the packing lower bound and the $`n-2`$-bit construction for one qubit target, with the appropriate integer rounding.

**Dependencies and story role:** M13–M27. This places the assembled results in their scientific context before the final scope synthesis.

**Conceptual connection:** A known coefficient or a known construction does not settle a converse for a larger source and operation class. Conversely, the proven packing rate is not an asserted optimum on every graph, and the exact tree theorem does not resolve the dense case.

**Source pointers:** [related work](../references/related-work.md), particularly [Chan et al.](../references/related-work.md#chan2018), [Neumann et al.](../references/related-work.md#neumann2025), and [Xu et al.](../references/related-work.md#xu2025); [dense-graph gap](../science/achievability-and-limits.md#dense-graphs-and-unproved-optimal-coefficients).

<a id="m29"></a>
### M29: Verification and boundary examples

**Central question:** Which examples distinguish a proved claim from a tempting but unsupported extension?

**Understanding target:** Explain the roles of the common-label classical mixture, the achieved triangle fidelity above one half, randomized expensive executions, and a block with high marginal fidelity but zero global fidelity. Distinguish finite checks of explicit state transformations and correction conventions from analytical proofs covering arbitrary source dimensions and adaptive protocols.

**Dependencies and story role:** M02, M08, M17, M20, M23–M24 and M28. This brings the model boundaries and the evidence together before the final synthesis.

**Conceptual connection:** Each example changes or tests a specific logical link: coherence, the $`\alpha\ge2`$ domain, the cost convention, or the error criterion. The verification suite supports explicit constructions and diagnostics; it does not enumerate all allowed quantum strategies.

**Source pointers:** [boundaries and examples](../science/achievability-and-limits.md#boundaries-that-change-the-conclusion); [triangle domain check](../science/communication-converses.md#finite-transcript-fidelity-bounds); [verification scope](../verification/README.md).

<a id="m30"></a>
### M30: Synthesis: the complete communication landscape

**Central question:** How do the mechanisms, matching cases, and limitations fit into one explanation of GHZ communication cost?

**Understanding target:** Connect independent pair sources to local transcript maps, common-label mass, branch fidelity, and the appropriate whole-protocol converse. Integrate the separate entropy argument for exact trees and a discarded hub. Distinguish fixed worst-case, mean, and heralded conclusions; identify where a construction matches the bound and where the dense-graph coefficient remains unresolved.

**Dependencies and story role:** M12–M29. This is the narrative synthesis: local mathematical objects and physical protocols now support a complete account of the project's established results and scope.

**Conceptual connection:** The shared theme is that unlimited pairwise quantum resources do not remove the cost of coordinating a specified coherent multipartite output. The quantitative conclusion depends on which output, quality criterion, and communication resource are required.

**Source pointers:** [scientific overview](../science/README.md); [canonical model](../science/model.md); [communication converses](../science/communication-converses.md); [mean and heralded conclusions](../science/expected-and-heralded.md); [exact architectures and limits](../science/achievability-and-limits.md); [attribution](../references/related-work.md).
