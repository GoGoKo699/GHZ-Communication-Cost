# Constructions, exact tree costs, and limits

The communication converses allow arbitrary independent pair states, with no bound on their finite dimensions. A matching construction may choose a simpler resource. On a star, maximally entangled pairs and local controlled subtraction attain the exact transcript bound. On every tree, a separate entropy argument proves that the same qubit communication cost is optimal. These exact benchmarks do not determine the optimum on dense source graphs.

The [model](model.md) defines the public-board communication convention, shared randomness, and global squared-overlap fidelity. The constructions below also specify where a point-to-point implementation has the same cost. The [verification program](../verification/README.md) follows the physical register maps, including measured registers and uncommunicated outcomes.

## Star fusion with the hub retained as an output

Let the star have $`n\ge2`$ output vertices: a hub $`C`$ and leaves $`L_1,\ldots,L_m`$, where $`m=n-1`$. Every vertex, including the hub, keeps one final $`d`$-dimensional output. On edge $`CL_j`$, choose the maximally entangled state

```math
|\Phi_d\rangle_{C_jL_j}
=\frac1{\sqrt d}\sum_{x=0}^{d-1}|x\rangle_{C_j}|x\rangle_{L_j}.
```

All arithmetic on basis labels is modulo $`d`$. Write $`X_d|x\rangle=|x+1\rangle`$. The initial state is

```math
|\Psi_{\mathrm{in}}\rangle
=d^{-m/2}
\sum_{x_1,\ldots,x_m}
|x_1,\ldots,x_m\rangle_C
\bigotimes_{j=1}^{m}|x_j\rangle_{L_j}.
\tag{A1}
```

The hub retains $`C_1`$. For every $`j\ge2`$, it applies controlled subtraction

```math
|x_1\rangle_{C_1}|x_j\rangle_{C_j}
\longmapsto
|x_1\rangle_{C_1}|x_j-x_1\rangle_{C_j},
```

then measures $`C_j`$ in the computational basis. Denote the result by $`s_j=x_j-x_1`$. For the complete syndrome $`s=(s_2,\ldots,s_m)`$, the unnormalized state of the outputs is

```math
|\psi_s\rangle
=d^{-m/2}\sum_{x=0}^{d-1}
|x\rangle_C|x\rangle_{L_1}
\bigotimes_{j=2}^{m}|x+s_j\rangle_{L_j}.
\tag{A2}
```

Every syndrome has probability

```math
p_s=d^{1-m}=d^{-(n-2)}.
\tag{A3}
```

After learning $`s_j`$, leaf $`L_j`$ applies $`X_d^{-s_j}`$. No correction is needed at $`C`$ or $`L_1`$. Every corrected branch is therefore

```math
|\psi_s^{\mathrm{corr}}\rangle
=\sqrt{p_s}\,|\mathrm{GHZ}_{n,d}\rangle.
\tag{A4}
```

For qubits, controlled subtraction is CNOT. The three-party, one-bit fusion primitive is established in [Grudka et al.](../references/related-work.md#grudka2008); equations (A1)–(A4) give the explicit repeated-fusion construction and its dimension dependence.

### Exact communication accounting

There are exactly $`d^{n-2}`$ equiprobable syndrome words. At the level of message alphabets, the construction uses $`n-2`$ symbols from an alphabet of size $`d`$. Because a single sender knows the entire word, the hub can use an injective binary encoding of fixed length

```math
c_{\mathrm{star}}^{\mathrm{exact}}
=\left\lceil(n-2)\log_2d\right\rceil.
\tag{A5}
```

Every party receives this word on the public board and extracts its required correction. For the source star, $`\alpha=n-1`$. The [exact-branch converse](branch-bound.md#coherence-and-fidelity-of-one-branch) gives $`M\ge d^{n-2}`$, hence the matching binary lower bound in (A5), even when arbitrary larger pair states and more general LOCC protocols are allowed on the same star.

For $`d=2^k`$, each correction word is already binary. Both the worst-case and mean costs equal $`k(n-2)`$ bits. In particular, one qubit GHZ state requires exactly $`n-2`$ bits. Its point-to-point implementation sends one correction bit from the hub to each of $`L_2,\ldots,L_m`$ and has the same total cost. The collective strong-converse threshold $`n-2`$ bits per qubit GHZ copy is therefore attained on a star; see [Corollary C5](communication-converses.md#collective-preparation-of-many-ghz-states).

For a general non-power-of-two $`d`$, (A5) is a worst-case binary statement. The entropy lower bound on mean binary length is $`(n-2)\log_2d`$, and a prefix code for the uniform syndrome has mean length less than that value plus one. Equality with the entropy is not asserted when the syndrome alphabet is not a power of two.

### Private syndromes and uncorrected outputs

Measuring a syndrome does not itself communicate it. If the hub sends only some syndrome components and the remaining leaves apply no correction, the omitted labels are averaged in the physical output. If exactly $`r`$ syndrome components remain unknown, the output is a uniform mixture of $`d^r`$ orthogonal shifted GHZ states, and its target fidelity is

```math
F=d^{-r}.
\tag{A6}
```

This is an explicit example in which the number of local measurement histories exceeds the number of communicated transcripts. The [fixed-transcript CP-map representation](branch-bound.md#factorization-of-a-fixed-transcript) sums the private histories inside the hub's local map.

One can instead broadcast a single bit indicating whether every syndrome is zero. On the zero-syndrome branch, the outputs already form the exact GHZ state. On the other branch, every party discards its output and prepares $`|0\rangle`$. The unconditional state is

```math
\rho_{\mathrm{flag}}
=p_0|\mathrm{GHZ}_{n,d}\rangle\langle\mathrm{GHZ}_{n,d}|
+(1-p_0)|0\rangle\langle0|^{\otimes n},
\qquad p_0=d^{-(n-2)},
```

with

```math
F(\rho_{\mathrm{flag}})
=p_0+\frac{1-p_0}{d}.
\tag{A7}
```

Only two communicated transcripts are needed, although the hub has $`d^{n-2}`$ possible private syndromes. The exact conditional success does not imply deterministic exact preparation. The success probability is the quantity retained by the [heralded bounds](expected-and-heralded.md).

## Sequential growth on any connected source graph

Choose a spanning tree of the available source graph and put one maximally entangled pair on each of its edges. Start with one edge: its endpoints already share $`\mathrm{GHZ}_{2,d}=\Phi_d`$. Suppose a connected set $`S`$ currently shares $`\mathrm{GHZ}_{|S|,d}`$, with one output register at each vertex. Take a frontier tree edge $`vw`$, where $`v\in S`$ and $`w\notin S`$. The unused edge pair has registers $`a`$ at $`v`$ and $`b`$ at $`w`$.

Vertex $`v`$ applies controlled subtraction from its current GHZ output into $`a`$, and measures $`a`$. If the result is $`s`$, the normalized state on $`S\cup\{w\}`$ is

```math
\frac1{\sqrt d}\sum_{x=0}^{d-1}
|x\rangle^{\otimes |S|}|x+s\rangle_w.
\tag{A8}
```

Sending $`s`$ to $`w`$ and applying $`X_d^{-s}`$ extends the GHZ state by one vertex. All existing outputs remain unchanged. Each outcome is uniform over $`d`$ values, conditional on the preceding outcomes. Repeating this step adds the remaining $`n-2`$ vertices.

The construction uses $`n-2`$ transmitted $`d`$-ary symbols. For qubits it uses $`n-2`$ bits, and for $`d=2^k`$ it uses $`k(n-2)`$ bits. Each symbol needs only one direct transmission along the frontier tree edge, so these binary costs are also attainable with point-to-point communication. A different fusion order that joins already-large GHZ blocks can require distributing a correction to several parties; no such additional delivery is needed in the sequential construction above.

For general $`d`$, encoding every sequential symbol separately gives the binary upper bound $`(n-2)\lceil\log_2d\rceil`$. The star's joint encoding argument does not automatically apply to arbitrary trees because different parties generate the successive symbols. We therefore state the tree result in symbols, and give the exact binary matching claim when $`d`$ is a power of two.

This upper bound holds on any connected source graph, since unused source edges may supply trivial product states. It does not imply that the upper bound is optimal on a dense graph.

## An entropy converse that is exact on trees

The fractional-independence converse can be loose on a path. For example, a path has $`\alpha=\lceil n/2\rceil`$, whereas its exact qubit preparation cost is $`n-2`$. The following entropy argument supplies the additional topology information. Every vertex of the source tree is an output vertex in this theorem; there are no discarded helper vertices in its statement.

### Conditional total correlation and a public message

For quantum systems $`B_1,\ldots,B_m`$ and a classical record $`T`$, define conditional total correlation by

```math
J(B_1:\cdots:B_m\mid T)
=\sum_{j=1}^{m}S(B_j\mid T)-S(B_1\cdots B_m\mid T).
\tag{A9}
```

For each fixed value of $`T`$, total correlation is the relative entropy

```math
D\!\left(\rho_{B_1\cdots B_m}
\middle\Vert\bigotimes_j\rho_{B_j}\right).
```

Formally, conditional total correlation is defined by averaging this nonnegative relative entropy over the classical record. Equation (A9) is its entropy expression when the displayed conditional entropies are finite. The branchwise definition avoids an infinity-minus-infinity expression if a shared seed selects unboundedly large finite input dimensions. Equivalently, the finite-dimensional argument may be applied for each fixed seed and then averaged. Total correlation cannot increase under a product of local channels on the $`B_j`$. The imported analytic ingredient is quantum relative-entropy data processing; see [Lindblad](../references/related-work.md#lindblad1975).

There are two different ways a public message can affect (A9).

**A message from inside one component.** Suppose a local instrument in $`B_k`$ produces an updated system $`B_k'`$ and a classical message $`X`$. Data processing gives

```math
J(B_1:\cdots:B_m\mid T)
\ge
J(B_1:\cdots:B_k'X:\cdots:B_m\mid T).
```

Expanding the conditional entropies yields the identity

```math
\begin{aligned}
&J(B_1:\cdots:B_k'X:\cdots:B_m\mid T)\\
&\quad=
J(B_1:\cdots:B_k':\cdots:B_m\mid TX)
+\sum_{j\ne k}I(X:B_j\mid T).
\end{aligned}
\tag{A10}
```

Every mutual information on the right is nonnegative. Thus the conditional total correlation cannot increase when a component performs a local instrument and publishes its result. Subsequent local corrections, conditioned on the public record, cannot increase it either.

**A message from a party outside all components.** A local instrument at that party leaves the average state of $`B_1\cdots B_m`$ unchanged before its result is revealed. Consequently,

```math
\begin{aligned}
&J(B_1:\cdots:B_m\mid TX)
-J(B_1:\cdots:B_m\mid T)\\
&\quad=
I(X:B_1\cdots B_m\mid T)
-\sum_j I(X:B_j\mid T)\\
&\quad\le H(X\mid T).
\end{aligned}
\tag{A11}
```

The last step uses $`I(X:B_1\cdots B_m\mid T)\le H(X\mid T)`$ for a classical $`X`$. In particular, one publicly transmitted binary symbol increases (A9) by at most one bit. Unannounced local operations at the outside party leave the reduced component state unchanged.

These statements apply separately at each node of an adaptive public protocol tree. The speaker is fixed by the public prefix. A local instrument may depend on arbitrary private memory. The shared seed $`R`$ is included in the conditioning record throughout, so free shared randomness does not create an initial contribution to (A9).

### Exact output at every tree vertex

**Theorem A1: Exact tree communication cost.** Let the independent bipartite source graph be a tree $`\mathcal T`$ on $`n\ge2`$ vertices, all of which are designated outputs. Suppose a finite protocol, or an almost-surely terminating protocol of finite mean length, prepares $`\mathrm{GHZ}_{n,d}`$ exactly by LOCC. Let $`L_v`$ be its expected number of binary symbols sent by vertex $`v`$, averaged over outcomes and the shared seed. Then

```math
L_v\ge[\deg_{\mathcal T}(v)-1]\log_2d,
\qquad
\sum_vL_v\ge(n-2)\log_2d.
\tag{A12}
```

For $`d=2^k`$, sequential growth attains equality. The optimum exact worst-case and expected binary costs are therefore both $`k(n-2)`$.

**Proof for a finite protocol.** Fix a vertex $`v`$, remove it from the tree, and group all quantum and private registers in each of the resulting $`m=\deg_{\mathcal T}(v)`$ components into a system $`B_j`$. Keep the public transcript as a separate conditioning register. Conditional on the shared seed, the initial reduced state on the components is a product: no source joins two components after $`v`$ is traced out. Edge sources incident on $`v`$ leave independent local reduced states in their respective components. Hence the initial value of (A9) is zero.

Every message from a vertex other than $`v`$ is produced inside one of the components and cannot increase the conditional total correlation, by (A10). Only messages from $`v`$ can increase it, and (A11) bounds their total increase by their conditional entropies, which are at most $`L_v`$. Thus

```math
J(B_1:\cdots:B_m\mid RT_{\mathrm{final}})\le L_v.
\tag{A13}
```

Because the unconditional output is the pure GHZ target, every positive-probability transcript has that same target output for almost every shared seed. Trace out all extra registers locally and trace out the output at $`v`$. On the component outputs this leaves

```math
\Gamma
=\frac1d\sum_{x=0}^{d-1}
\bigotimes_{j=1}^{m}
\left(|x\rangle\langle x|\right)^{\otimes |B_j^{\mathrm{out}}|}.
\tag{A14}
```

Each component is nonempty. Its marginal entropy is $`\log_2d`$, while the joint entropy of (A14) is $`\log_2d`$. The total correlation of the reduced output is therefore $`(m-1)\log_2d`$. Local data processing implies that the left side of (A13) is at least this value. This proves the vertex bound. Summing it and using $`\sum_v\deg_{\mathcal T}(v)=2(n-1)`$ gives the total bound in (A12). The matching construction was given above. ∎

The theorem uses arbitrary pair states and arbitrary finite local dimensions on the tree; it is not restricted to the Bell resources used in the upper bound. The cutoff argument below extends the mean-cost conclusion to almost-surely terminating protocols.

Adding quantum source edges between the components invalidates their initial product structure and can invalidate the vertex bound. Thus the exact tree optimum does not prove an $`n-2`$ lower bound for complete source graphs. The entropy argument also does not supply a tree-wide strong-converse exponent at rate $`n-2`$: the established exponent remains the one in [Corollary C5](communication-converses.md#collective-preparation-of-many-ghz-states), with the star as a matching case.

## A hub that is discarded changes the task

Consider instead $`N`$ output leaves and a separate helper hub. Starting from $`N`$ maximally entangled pairs, the retained-hub protocol first produces $`\mathrm{GHZ}_{N+1,d}`$ using $`N-1`$ syndrome symbols. The hub then measures its remaining qudit in the Fourier basis

```math
|\widetilde r\rangle
=\frac1{\sqrt d}\sum_{x=0}^{d-1}\omega^{rx}|x\rangle,
\qquad \omega=e^{2\pi i/d}.
```

Conditional on result $`r`$, the leaf state is

```math
\frac1{\sqrt d}\sum_{x=0}^{d-1}\omega^{-rx}|x\rangle^{\otimes N}.
\tag{A15}
```

One designated leaf applies $`Z_d^r`$, where $`Z_d|x\rangle=\omega^x|x\rangle`$, after the hub communicates $`r`$. This construction uses $`N`$ symbols, or exactly $`N\log_2d`$ binary bits when $`d`$ is a power of two. The extra phase symbol is absent when the hub remains one of the outputs.

**Theorem A2: Exact discarded-hub cost.** Let $`N\ge2`$ output leaves share arbitrary independent bipartite states with a single helper hub $`C`$, with no quantum source joining two leaves. For any exact LOCC preparation of $`\mathrm{GHZ}_{N,d}`$, the hub's expected outbound communication satisfies

```math
L_C\ge N\log_2d.
\tag{A16}
```

This holds for arbitrary interaction and for finite or almost-surely terminating protocols of finite mean length. In particular, for $`d=2^k`$, the optimum total exact communication cost, in either the worst-case or mean model, is $`Nk`$ bits. The construction above attains it using messages from the hub alone.

**Proof for a finite protocol.** Apply (A9) to the $`N`$ leaf laboratories, retaining all their local registers. Their initial reduced state is a product conditional on the shared seed, so its conditional total correlation is zero. Any leaf's local instrument and public message cannot increase it by (A10). A hub message increases it by at most its conditional entropy by (A11). Therefore the final conditional total correlation of the leaf laboratories is at most $`L_C`$.

The designated leaf outputs are exactly $`\mathrm{GHZ}_{N,d}`$ for every positive-probability transcript and almost every shared seed. Their joint entropy is zero, and each leaf's marginal entropy is $`\log_2d`$ because $`N\ge2`$. Their total correlation is $`N\log_2d`$. Tracing other leaf registers is local data processing, so it cannot increase total correlation. Hence $`L_C\ge N\log_2d`$. The same cutoff argument below gives the variable-length case. ∎

[Chen et al.](../references/related-work.md#chen2024) give the corresponding $`N`$-bit qubit allocation protocol and prove its optimality within their one-way, Bell-input hub framework. The numerical coefficient and that protocol are established benchmarks. Theorem A2 gives a converse for arbitrary independent hub–leaf source states and arbitrary interactive local processing, and bounds hub-outbound communication even if the leaves also exchange public messages.

The helper-hub task must not be identified with the retained-hub $`n-2`$ benchmark by using the same letter for different numbers of output parties. The additional phase correction has a matching information cost in this architecture. In the general fractional-independence bound, the helper has weight zero and the $`N`$ output leaves have $`\alpha=N`$; its exact lower bound $`(N-1)\log_2d`$ is valid but weaker than Theorem A2.

### Almost-sure termination in the exact entropy benchmarks

For either theorem, truncate a protocol after at most $`b`$ public binary symbols. If it has not finished by that fixed cutoff, every party resets its designated output to $`|0\rangle`$. Whether a prefix is terminal is specified by the public protocol tree. The fixed cutoff therefore introduces no uncharged success signal or data-dependent timing choice.

Let $`q_b`$ be the probability that the original protocol has finished by the cutoff, including the shared-seed average. After retaining $`R`$ together with the truncated public record and discarding all other registers, the target outputs have the exact required state on completed branches and a product state on unfinished branches, for almost every seed. The corresponding conditional total correlation is thus $`q_b`$ times the target value: $`[\deg(v)-1]\log_2d`$ in Theorem A1 and $`N\log_2d`$ in Theorem A2. The finite-prefix message argument bounds this quantity by the expected outbound bits before truncation, which are at most the original $`L_v`$ or $`L_C`$.

Almost-sure termination gives $`q_b\to1`$. Taking the limit proves both exact expected-cost bounds. No dimension-dependent entropy continuity estimate, and no claim about approximately correct outputs, is needed in this step.

## Boundaries that change the conclusion

### Multipartite sources

If a free source may directly distribute $`\mathrm{GHZ}_{n,d}`$ to all output parties, exact preparation uses zero communication. It violates the pair-source conclusion because it violates its resource assumption. The same issue arises if an earlier quantum preparation and redistribution stage is omitted from the model and its multipartite output is treated as an independent pair input. The source-arity restriction is therefore part of the physical resource statement.

### Expected cost and randomized failure

Use the free shared seed to run an exact protocol with probability $`q`$, and otherwise let every output party prepare $`|0\rangle`$. The decision to skip the protocol requires no extra message because it is already common information. If the exact protocol has cost $`c_{\mathrm{exact}}`$, the mixture has

```math
L=q\,c_{\mathrm{exact}},
\qquad
F=q+\frac{1-q}{d}.
\tag{A17}
```

On a retained-hub star preparing $`k`$ qubit GHZ copies, take $`d=2^k`$ and $`c_{\mathrm{exact}}=k(n-2)`$. For fixed $`q>0`$, its global fidelity tends to $`q`$, while its expected cost per copy is $`q(n-2)`$. This disproves transferring the worst-case strong-converse threshold to mean cost by simply replacing the maximum length with an expectation. It does not contradict the separate expected-cost lower bounds at fixed fidelity in [Expected communication and heralding](expected-and-heralded.md).

### Perfect classical correlations do not give a coherent GHZ state

The state

```math
\frac1d\sum_x |x\rangle\langle x|^{\otimes n}
```

has perfectly matching computational-basis outcomes and is available using shared randomness. Its GHZ fidelity is only $`1/d`$. Free shared randomness therefore explains the classical baseline, while the converse controls the coherent quantum target above that baseline.

### Global block fidelity and single-copy marginals

For qubits define the orthogonal states $`|\mathrm{GHZ}^{\pm}\rangle=(|0^n\rangle\pm|1^n\rangle)/\sqrt2`$. Consider a mixture of $`k`$ tensor-product states, each having one minus GHZ and $`k-1`$ plus GHZ states, with the location of the minus sign uniformly distributed. Every individual copy has fidelity $`1-1/k`$ with the plus target, but the whole block has zero fidelity with $`|\mathrm{GHZ}^{+}\rangle^{\otimes k}`$.

This state is a counterexample to an inference between two fidelity criteria, not a claim that it is freely preparable. The collective converse concerns global block fidelity, and cannot be read as a lower bound under an individual-marginal requirement without a separate argument.

### Dense graphs and unproved optimal coefficients

For the complete graph on $`n\ge4`$ output parties, the established exact qubit bounds are

```math
\left\lceil\frac n2-1\right\rceil
\le c_{\mathrm{exact}}(K_n)
\le n-2.
\tag{A18}
```

The lower bound comes from fractional independence, and the upper bound from using a spanning tree. The tree entropy proof cannot be applied after ignoring available extra source edges in a lower-bound argument. The optimal dense-graph coefficient and a possible improvement over the spanning-tree construction are not settled by these results.

The complete-graph lower bound still establishes the central extensive resource cost: arbitrarily large independent pair states on every output pair do not allow fixed qubit GHZ fidelity above $`1/2`$ with a sublinear number of classical bits.

## What is checked computationally

The [standard-library verification script](../verification/README.md) constructs small independent Bell-source states explicitly, applies the modular gates and measurements, keeps their unnormalized branches, and traces out measured registers. It checks exact rational output density matrices for star and non-star trees, a non-binary correction sign, partial correction with private outcomes, and the one-bit success/failure protocol. A complex-valued triangle example checks the absolute-value contraction used by quantum Finner and demonstrates why ordinary squares of complex matrix elements would be invalid.

These finite physical examples can detect an incorrect gate convention, a missing correction, an incorrect branch probability, or a hidden communication record. They do not replace the dimension-independent analytical proofs.
