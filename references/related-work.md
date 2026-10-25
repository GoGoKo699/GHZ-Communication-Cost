# Related work and attribution

## Scope of the comparison

The problem studied here charges the classical information exchanged after independent bipartite quantum resources have been distributed. The resources may have arbitrary finite dimensions and may be chosen conditionally on shared classical randomness. The target is a specified multipartite GHZ state, and the error criterion is its squared overlap with the unconditional output state. The [model](../science/model.md) specifies the signaling and transcript conventions.

The main [communication converse](../science/communication-converses.md) uses the fractional vertex-packing number of the source graph. For packing weight $`\alpha\geq2`$, target local dimension $`d`$, and at most $`M`$ complete communication transcripts, it gives

```math
F\leq\min\{1,M^{1/(\alpha-1)}/d\}.
```

Its contribution is a finite-fidelity statement about adaptive quantum protocols, with an explicit transcript budget. The coefficient $`\alpha-1`$, the mathematical inequality behind the network constraint, the zero-communication GHZ obstruction, and elementary GHZ fusion all have prior antecedents. The comparisons below keep those antecedents separate from the derivations in this repository. Bibliographic keys match [references.bib](references.bib).

## Resource currencies at a glance

| Work | Starting resource and task | Quantity constrained | Relation to the present problem |
|---|---|---|---|
| [Renou et al.](#ren2019) | Independent bipartite quantum sources; local measurements | Network-compatible correlations | Supplies quantum Finner inequalities |
| [Neumann et al.](#neumann2025) | Arbitrary bipartite sources; GHZ preparation by LOSR | Fidelity with no communication | Supplies the $`n\geq4`$, $`1/d`$ benchmark |
| [Xu et al.](#xu2025) | Network states; approximate preparation by LOCC | Average steps or rounds | Messages are not charged by bit length |
| [Chan et al.](#chan2018) | Classical hypergraphical/PIN sources; secret key agreement | Asymptotic total public-discussion rate | Gives the classical vertex-packing and exact PIN laws |
| [Grudka et al.](#grudka2008) | Fixed EPR/GHZ redistribution tasks | Classical implementation rates | Gives the elementary two-EPR-to-GHZ communication primitive |
| [Chen et al.](#chen2024) | A Bell-pair hub; GHZ at endpoints | One-way hub-to-endpoint bits | Hub is discarded; measurement/recovery architecture is restricted |
| [Spee and Kraft](#spee2024) | Bell-pair networks; pure-state transformations | Feasibility under finitely many LOCC rounds | No bound on total transmitted bits |
| [Chelluri et al.](#chelluri2026) | Bell-pair networks; constructive GHZ distribution | Protocol resources and classical-message counts | Algorithm-specific costs, rather than a converse for all LOCC |
| [Murray et al.](#murray2026) | Multipartite states, including quantum PIN resources | Distillable entanglement and Rains quantities | Classical communication is uncharged |
| [Bhattacharya](#bhattacharya2025) | Quantum PIN resources; entanglement distillation | Distillation-yield upper bounds | Comparison is limited to accessible metadata and abstract |
| [Salek and Winter](#salek2025) | General multipartite quantum sources | Conference-key and GHZ rates | Explains why a measure-first classical reduction needs justification |
| [Oleynik et al.](#oleynik2026) | Fixed multipartite GHZ sources in hypergraphs | Fidelity under local-unitary decoding | Different source class and no communication budget |

## Mathematical ingredients

<a id="finner1992"></a>
### Finner: the classical product-space inequality

**Key:** `finner1992`. Helmut Finner, *A Generalization of Hölder's Inequality and Some Probability Inequalities*, Annals of Probability **20**(4), 1893–1901 (1992). [Publisher and DOI](https://doi.org/10.1214/aop/1176989534).

Finner's extension of Hölder's inequality controls products of functions depending on overlapping subsets of independent variables. Fractional packing weights describe which exponents are admissible. This is an imported mathematical ingredient. In the self-contained quantum argument in [branch-bound.md](../science/branch-bound.md), the classical inequality is applied to nonnegative functions obtained from local tensor entries. Neither the classical inequality nor the fractional-packing parameter is introduced here.

<a id="ren2019"></a>
### Renou et al.: quantum Finner for bipartite-source networks

**Key:** `ren2019`. Marc-Olivier Renou et al., *Limits on correlations in networks for quantum and no-signaling resources*, Physical Review Letters **123**, 070403 (2019). [DOI](https://doi.org/10.1103/PhysRevLett.123.070403); [author preprint, v1](https://arxiv.org/abs/1901.08287v1).

**Precise pointer:** Section III, Theorem 2, and Appendix D. Their quantum result permits arbitrary bipartite quantum sources and local joint measurements. For any fractional independent-set weights, it bounds the expectation of a product of nonnegative local functions by the corresponding product of norms. Indicator functions give the network event inequality used here.

The [branch bound](../science/branch-bound.md) specializes this ingredient to successful local operations and a common GHZ basis label, then combines it with a fidelity estimate. The finite-communication conclusion additionally needs a transcript decomposition and summation. The cited quantum theorem concerns bipartite-source graphs; it should not be described as a proved quantum Finner theorem for arbitrary source hypergraphs.

<a id="lindblad1975"></a>
### Lindblad: relative-entropy data processing

**Key:** `lindblad1975`. Göran Lindblad, *Completely positive maps and entropy inequalities*, Communications in Mathematical Physics **40**(2), 147–151 (1975). [Publisher](https://link.springer.com/article/10.1007/BF01609396); [DOI](https://doi.org/10.1007/BF01609396).

The imported statement is monotonicity of quantum relative entropy under a completely positive trace-preserving map. Applied to

```math
J(B_1:\cdots:B_r)=D(\rho_{B_1\cdots B_r}\Vert\rho_{B_1}\otimes\cdots\otimes\rho_{B_r}),
```

it gives monotonicity of quantum total correlation under a product of local channels. The calculations involving conditioning on instrument outcomes and revealing messages are established separately in the [entropy converse](../science/achievability-and-limits.md#an-entropy-converse-that-is-exact-on-trees); they are not part of this attribution.

## Closest communication and fidelity comparisons

<a id="neumann2025"></a>
### Neumann et al.: the zero-communication benchmark

**Key:** `neumann2025`. Justus Neumann et al., *No quantum advantage without classical communication: fundamental limitations of quantum networks*, arXiv:2503.09473v1 (2025). [Author preprint](https://arxiv.org/abs/2503.09473v1).

**Precise pointer:** Section III.3, Result 5, and Appendix D. For at least four parties, arbitrary bipartite quantum sources and local operations with shared randomness cannot exceed squared GHZ overlap $`1/d`$. A fully separable state attains that value. Section III.1 and Appendix A.3.1, Eq. (56), construct triangle fidelity approximately $`0.51704>1/2`$; their approximately $`0.618`$ upper bound is not an achieved value.

For $`n\geq4`$, this establishes the no-communication endpoint of the present theorem. A nonzero-communication analysis must also control the normalization and probability of each transcript branch: conditioning on a transcript changes the effective state and cannot simply be treated as another deterministic LOSR protocol. The present packing-dependent exponent is obtained from a branch inequality before normalization, rather than by applying the deterministic zero-communication statement to postselected outputs.

<a id="xu2025"></a>
### Xu et al.: steps and rounds are different communication currencies

**Key:** `xu2025`. Zhen-Peng Xu et al., *Quantum network-entanglement measures*, Quantum **9**, 1736 (2025). [DOI](https://doi.org/10.22331/q-2025-05-06-1736); [author preprint, v3](https://arxiv.org/abs/2311.13945v3).

**Precise pointer:** Section 2, Eq. (2), and Section 4. The network communication cost averages the number of steps in a preparation protocol. In a step, several senders may act and send information to neighboring receivers. The separate round measure allows one acting sender whose information can be broadcast. Neither measure counts the lengths of the messages.

Their graph-dependent preparation bounds and resource measures therefore answer a latency/interaction question. A protocol can use a small number of their steps while transmitting many bits. Section 4 explicitly leaves restrictions on classical or quantum link capacities for further study. The present transcript cardinality is an additional resource restriction, not a reinterpretation of their step count.

<a id="chan2018"></a>
### Chan et al.: the classical vertex-packing predecessor and stronger PIN law

**Key:** `chan2018` retains the preprint year. Chung Chan et al., *Upper Bounds via Lamination on the Constrained Secrecy Capacity of Hypergraphical Sources*, IEEE Transactions on Information Theory **65**(8), 5080–5093 (2019). [DOI](https://doi.org/10.1109/TIT.2019.2897129); [2018 author preprint](https://arxiv.org/abs/1805.01115v1).

**Precise pointers:** Theorem 4.3 is the vertex-packing bound $`(\tau-1)C_S(R)\leq R`$. Theorem 4.1 is the edge-partition bound. For a pairwise independent network (PIN) with $`n\geq3`$ parties, Theorem 4.2 gives the stronger, exact law

```math
C_S(R)=\min\{R/(n-2),C_S(\infty)\}.
```

The sources are classical independent edge variables; communication is interactive public discussion, charged asymptotically by total message-alphabet rate; the output is secret key. Thus the coefficient $`\alpha-1`$ and the classical $`n-2`$ cost are established predecessors. The present result allows coherent quantum sources and instruments and gives a finite-fidelity bound. It does not prove the classical $`n-2`$ law for every quantum source graph. In particular, its complete-graph coefficient is only $`n/2-1`$.

<a id="grudka2008"></a>
### Grudka et al.: entanglement redistribution and the fusion primitive

**Key:** `grudka2008`. Andrzej Grudka et al., *Entanglement-redistribution boxes*, Physical Review A **78**, 042317 (2008). [DOI](https://doi.org/10.1103/PhysRevA.78.042317); [author preprint](https://arxiv.org/abs/0807.3811v1).

**Precise pointers:** Section II.B, Definitions 2–4; Section II.C; Theorem 2. The communication quantities are introduced as asymptotic implementation rates for boxes. Their fixed-resource tasks include transforming two qubit EPR pairs sharing one party into a three-party GHZ state. They give a tight one-bit implementation cost for that primitive, alongside the two-bit entanglement-swapping cost.

Repeated Bell-pair fusion is therefore an established construction ingredient. A matching converse that allows arbitrarily large independent resources on each star edge has a larger source class than this primitive. The $`(n-2)k`$-bit star construction should be presented as repeated fusion, not as a new elementary protocol or as an immediate restatement of their fixed-task lower bound.

<a id="chen2024"></a>
### Chen et al.: a discarded hub and endpoint GHZ states

**Key:** `chen2024`. Yu-Ao Chen et al., *Quantum Entanglement Allocation through a Central Hub*, arXiv:2409.08173v2 (2024). [Author preprint](https://arxiv.org/abs/2409.08173v2).

**Precise pointers:** The central-hub model and Eq. (3); the GHZ allocation construction; supplementary Eqs. (S42)–(S45). There are $`N`$ Bell pairs between a central system and $`N`$ endpoints. The central system performs a projection-valued measurement, sends one-way messages, and endpoints apply local unitary corrections. The target GHZ state is shared only by the endpoints: the hub is discarded. Their exact GHZ cost is $`N`$ bits in this architecture.

This is distinct from a star with $`n`$ output parties including its center, where fusion costs $`n-2`$ bits. The separate [discarded-hub argument](../science/achievability-and-limits.md#a-hub-that-is-discarded-changes-the-task) in this repository extends the known benchmark to arbitrary independent hub–leaf resources and interactive LOCC, while specifically charging hub-outbound communication. The coefficient and Bell-input construction are established benchmarks; the enlarged source and operation classes are the relevant distinction.

## Other network and distillation results

<a id="spee2024"></a>
### Spee and Kraft: finite-round transformation feasibility

**Key:** `spee2024`. Cornelia Spee and Tristan Kraft, *Transformations in quantum networks via local operations assisted by finitely many rounds of classical communication*, Quantum **8**, 1286 (2024). [DOI](https://doi.org/10.22331/q-2024-03-14-1286); [author preprint, v3](https://arxiv.org/abs/2105.01090v3).

**Precise pointer:** Section 2 and the subsequent symmetry-based transformation results. The analysis starts from networks of maximally entangled qubit pairs and studies pure-state transformations, especially those described by invertible local operators, under finitely many LOCC rounds. Local symmetries constrain deterministic transformations and distinguish them from stochastic transformations.

The question is whether specified transformations can be implemented within the operational class. A finite number of rounds does not bound the total number of communicated bits. These results are relevant to the distinction between separable operations and LOCC, but do not supply the transcript-budget statement for arbitrary-dimensional independent sources used here.

<a id="chelluri2026"></a>
### Chelluri et al.: constructive protocols with explicit communication accounting

**Key:** `chelluri2026`. S. Siddardha Chelluri, Sumeet Khatri, and Peter van Loock, *A resource- and computationally-efficient protocol for multipartite entanglement distribution in Bell-pair networks*, npj Quantum Information **12**, 101 (2026). [DOI](https://doi.org/10.1038/s41534-026-01294-z); [author preprint, v4](https://arxiv.org/abs/2412.04252v4).

**Precise pointer:** The “Classical communication cost” subsection and Protocols 1, 2, and 4. The work gives explicit GHZ-distribution constructions and counts their classical correction messages, consumed Bell pairs, gates, and source requirements. In its tree-fusion accounting, measurement outcomes are delivered to descendant leaves, and the cost depends on the paths in the chosen protocol.

These are meaningful bit counts, unlike a pure round metric. They are protocol costs, rather than a lower bound on all adaptive LOCC protocols supplied with arbitrary independent edge resources. The source-count converse proved there concerns Bell-pair sources and dominating sets, a different currency from classical communication.

<a id="murray2026"></a>
### Murray et al.: multipartite Rains bounds and quantum PIN states

**Key:** `murray2026`. Hailey S. Murray et al., *Flood of multipartite Rains entanglement*, arXiv:2608.11406v1 (2026). [Author preprint](https://arxiv.org/abs/2608.11406v1).

**Precise pointers:** Section VI.C, Eqs. (255)–(260), for GHZ-distillation quantities; Section VIII for quantum PIN states. The latter are tensor products of Bell-pair resources indexed by a multigraph. The work relates multipartite Rains quantities to one-shot and asymptotic entanglement-distillation limits and evaluates the measures on this network family using cut quantities.

LOCC is an allowed transformation class without a classical-bit charge. These bounds constrain the amount of GHZ entanglement obtainable from a specified quantum resource, whereas the present question permits arbitrarily large edge resources and constrains the coordination needed afterward. A source-yield bound alone becomes uninformative when the available edge entanglement is allowed to grow without limit.

<a id="bhattacharya2025"></a>
### Bhattacharya: a comparison with limited full-text access

**Key:** `bhattacharya2025`. Sagnik Bhattacharya, *Improved Upper Bound on Multiterminal Entanglement Distillation*, 2025 IEEE International Symposium on Information Theory. [Official record](https://ieeexplore.ieee.org/document/11195492/); [DOI](https://doi.org/10.1109/ISIT63088.2025.11195492).

The accessible abstract describes improved upper bounds for multiterminal entanglement distillation in quantum PIN models, motivated by classical shared information and multipartite squashed entanglement. Murray et al. cite it in their quantum-PIN discussion. The article's full text has not been verified for this account. Accordingly, no claim is made here about the exact scope of all its theorems, or about the absence of an additional communication-cost result within it. The comparison is limited to the advertised distillation-yield problem; a stronger priority claim would require inspection of the complete paper.

<a id="salek2025"></a>
### Salek and Winter: a classical reduction is not automatic

**Key:** `salek2025`. Farzin Salek and Andreas Winter, *New Protocols for Conference Key and Multipartite Entanglement Distillation*, IEEE Transactions on Information Theory **71**(6), 4374–4384 (2025). [DOI](https://doi.org/10.1109/TIT.2025.3546794); [author preprint, v2](https://arxiv.org/abs/2308.01134v2).

**Precise pointer:** Section II.B, especially the example following Eq. (9), and the discussion of coherent analogues in Section III. Quantum information can remain useful until after messages reveal which local operation to perform. Their example demonstrates that omniscience of classical information generated before the first communication can give a suboptimal key rate, even among noninteractive protocols.

This is a general multipartite-source example, not a counterexample within the independent-pair source model. Its relevance is methodological: a classical PIN converse cannot simply be asserted for arbitrary quantum protocols by proposing that every source be measured first. The quantum branch argument avoids requiring such a reduction.

<a id="oleynik2026"></a>
### Oleynik et al.: local decoding with multipartite sources

**Key:** `oleynik2026`. Leonardo Oleynik, Shehbaz Tariq, and Symeon Chatzinotas, *Optimal GHZ-State Distribution in LOSR Quantum Networks via Local Decoding from Information Sets*, arXiv:2606.21500v1 (2026). [Author preprint](https://arxiv.org/abs/2606.21500v1).

**Precise pointers:** Sections 2 and 3. The resources are fixed maximally entangled GHZ states on hyperedges; the proposed decoding uses local unitaries and no communication. For a regular network with $`M`$ sources and $`m`$ incident sources per node, their construction concerns target local dimension $`D=d^m`$, where $`d`$ is the dimension of each source share. Its fidelity is $`d^{m-M}`$, and the stated optimality is within the local-unitary strategy class on these resources.

The source dimension $`d`$ must therefore not be identified with the present target dimension. This construction allows multipartite sources and uses a restricted decoder class; it does not give a finite-communication converse for arbitrary bipartite sources.

## Attribution boundary and remaining comparison

The graph-weighted network inequality is inherited from Finner and its quantum-network extension. The vertex-packing communication coefficient has an explicit classical predecessor. Zero-communication GHZ fidelity restrictions, small fusion primitives, and numerous Bell-network preparation algorithms are also established ingredients.

The statements proved in this repository combine those ingredients with a fixed-transcript quantum-operation argument to obtain an unconditional fidelity bound under a stated communication budget. The source class, finite-error regime, and charged currency are essential parts of that statement. The result does not establish a universal exact $`n-2`$ cost for quantum networks on every graph, nor does it identify every finite-round or yield bound as a bit bound. The unverified full-text comparison above is a remaining limitation on comprehensive priority claims.

## Educational anchor

<a id="watrous2018"></a>
### Watrous: the mathematical route into the project

**Key:** `watrous2018`. John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018). [Publisher and DOI](https://doi.org/10.1017/9781316848142); [official author page and manuscript chapters](https://jhwatrous.github.io/books-and-courses.html).

This book is the sole educational anchor. It supports the [learning bridge](../learning/bridge.md); the research antecedents above retain their separate attribution. Relevant portions are §1.1 for operator preliminaries, §§2.1–2.3 for states and instruments, §3.2 for fidelity, §§5.1–5.2 for entropy, and §6.1.2 for LOCC. Particularly useful pointers are Eqs. (2.258)–(2.262), Definition 3.11 and Proposition 3.13, Theorem 5.35, and Definition 6.25.

Watrous uses root fidelity; with a pure target the project's squared overlap is $`F_{\mathrm{project}}=F_{\mathrm{Watrous}}^2`$. His LOCC definition concerns finite compositions between two parties. The multipartite protocol tree, charged messages, independent-source restriction, and network converse are developed in this repository. The publicly linked chapter PDFs are the author's manuscript version, and section and theorem numbers identify the reading locations.
