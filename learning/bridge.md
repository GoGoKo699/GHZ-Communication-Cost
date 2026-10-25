# From Watrous to GHZ communication cost

Two Bell pairs can be fused into one three-party GHZ state, but the parties need a correction message. This project asks how much of that communication remains necessary when the pair resources are unrestricted and the protocol may be adaptive. The answer depends on whether every execution must fit a fixed budget, only the average cost is charged, or the output is accepted on a heralded subset of executions.

Watrous supplies the language of states, channels, instruments, fidelity, entropy and LOCC. This bridge connects that language to independent-source networks and charged communication. The [30-milestone map](milestones.md) organizes the understanding route. The [scientific overview](../science/README.md) leads to the authoritative statements and complete proofs.

## Anchor and reading route

The single educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**. The section and equation numbers below refer to the official author manuscript available from the [author's book page](https://jhwatrous.github.io/books-and-courses.html). Its chapter PDFs are linked for targeted reading; the book is not reproduced here.

| Project use | Focused reading in Watrous | Connection to this project |
|---|---|---|
| Registers, states and discarded systems | [Chapter 2, §§2.1.1–2.1.3](https://jhwatrous.github.io/TQI.2.pdf) | Identify a laboratory's registers and compute reduced states without confusing a party with one qubit. |
| Local physical operations | [Chapter 2, §2.2](https://jhwatrous.github.io/TQI.2.pdf) | Completely positive maps describe the operations allowed within a laboratory; channels include all outcomes. |
| A particular outcome and its probability | [Chapter 2, §2.3.2, Eqs. (2.258)–(2.262)](https://jhwatrous.github.io/TQI.2.pdf) | An instrument gives an unnormalized branch, its probability, and a normalized conditional state. |
| Distance and target fidelity | [Chapter 3, §3.2, Definition 3.11 and Eq. (3.64)](https://jhwatrous.github.io/TQI.3.pdf) | Translate the book's root fidelity into the project's squared overlap with a pure target. |
| Entropy and information under processing | [Chapter 5, §§5.1.1 and 5.2.1; §5.2.3, Theorem 5.35](https://jhwatrous.github.io/TQI.5.pdf) | Entropy measures transcript uncertainty; relative-entropy data processing supports the exact tree and helper-hub converses. |
| Separable maps and LOCC | [Chapter 6, §6.1.2, Definition 6.25 and Proposition 6.26](https://jhwatrous.github.io/TQI.6.pdf) | Read an adaptive local protocol as a composition of local instruments and communicated outcomes. The book formulates this discussion bipartitely; the network protocol is specified separately here. |

These are lookups alongside the project. Reading the whole book is not a prerequisite.

Fractional graph packing, quantum Finner, information-bearing schedules, and the conditional-total-correlation message identities are additional ingredients developed in the [model](../science/model.md), [branch proof](../science/branch-bound.md), and [exact-cost account](../science/achievability-and-limits.md). The primary research citations in [related work](../references/related-work.md) establish attribution and proof dependencies. They do not form a second educational anchor.

## Notation and conventions

| Book object or convention | Project notation | Meaning |
|---|---|---|
| A vector $`u`$, its adjoint $`u^*`$, and the projector $`uu^*`$ | $`\lvert\psi\rangle`$, $`\langle\psi\rvert`$, and $`\lvert\psi\rangle\langle\psi\rvert`$ | The same pure state written in Dirac notation. |
| A channel $`\Phi`$ | A local deterministic operation | Completely positive and trace preserving; any local auxiliary systems can be included. |
| An instrument element $`\Phi_a`$ | A local branch map $`\Lambda_{v,t}`$ | Completely positive and trace nonincreasing. The outcome is not normalized away. |
| The instrument output before conditioning | $`\sigma_{t\mid r}`$ | The unnormalized network output for complete transcript $`t`$ and shared seed $`r`$. |
| Classical entropy and quantum entropy | $`H`$ and $`S`$ | Both use base-two logarithms; information and communication are measured in bits. |
| Root fidelity in Definition 3.11 | $`F_{\rm W}`$ below | The project instead writes $`F`$ for squared pure-target overlap. |

For a pure target, the fidelity translation is

```math
F_{\rm W}\!\left(\rho,|\psi\rangle\langle\psi|\right)
=\sqrt{\langle\psi|\rho|\psi\rangle},
\qquad
F=\langle\psi|\rho|\psi\rangle=F_{\rm W}^{\,2}.
```

The linear quantity $`F`$ is what can be summed over unnormalized branches. If an instrument produces $`\sigma_t`$ with trace $`p_t`$, then

```math
p_t=\operatorname{Tr}\sigma_t,
\qquad
f_t=\frac{\langle\psi|\sigma_t|\psi\rangle}{p_t}
\quad(p_t>0),
\qquad
F=\sum_t p_t f_t.
```

The seed average is added when the protocol uses shared randomness. A branch with fidelity one contributes only its probability to the unconditional fidelity.

The tensor product in the input model is over **source edges**, conditional on the shared seed:

```math
\rho^{\rm in}_r=\bigotimes_{e\in E}\rho_{e,r}
\otimes\bigotimes_{v\in V}\tau_{v,r}.
```

Different edges are independent at fixed $`r`$. Within one edge, the resource may be a large state used collectively across many target copies. Thus the model does not assume an independent repetition of a single-copy protocol. Averaging over $`R`$ can create classical correlations between edges; the proofs condition on $`R`$ before using independence.

## One-bit fusion example

Let $`A`$ hold qubits $`a_1,a_2`$, let $`B`$ hold $`b`$, and let $`C`$ hold $`c`$. Supply two independent Bell pairs,

```math
|\Phi_2\rangle_{a_1b}\otimes|\Phi_2\rangle_{a_2c}
=\frac12\sum_{x,y=0}^{1}
|x\rangle_{a_1}|x\rangle_b|y\rangle_{a_2}|y\rangle_c.
```

Party $`A`$ applies a controlled-NOT from $`a_1`$ to $`a_2`$, then measures $`a_2`$ in the computational basis. Write the measurement outcome as $`s=y\oplus x`$. Each $`s`$ occurs with probability $`1/2`$. The conditional state of the three output qubits is

```math
|\psi_s\rangle_{ABC}
=\frac1{\sqrt2}\sum_{x=0}^{1}
|x\rangle_A|x\rangle_B|x\oplus s\rangle_C.
```

If $`A`$ sends the bit $`s`$ to $`C`$, then $`C`$ applies $`X^s`$. Both branches become

```math
|\mathrm{GHZ}_{3,2}\rangle
=\frac{|000\rangle+|111\rangle}{\sqrt2}.
```

The communicated protocol has two complete transcripts. After correction, each unnormalized branch is one half of the target projector, so their sum is the exact target. This is the elementary fusion construction attributed in [related work](../references/related-work.md#grudka2008).

If the outcome remains private at $`A`$ and $`C`$ makes no correction, the actual output is

```math
\rho=\frac12|\psi_0\rangle\langle\psi_0|
+\frac12|\psi_1\rangle\langle\psi_1|,
\qquad
F=\frac12.
```

The two shifted GHZ states are orthogonal. Knowing at $`A`$ which state occurred does not physically correct the remote output at $`C`$.

This example separates three objects: the local measurement outcome, the communicated transcript, and the final quantum state. The zero-message protocol has one complete communicated transcript, even though $`A`$ has two possible private outcomes. Its local map sums both histories.

The source graph is a three-vertex star, with all three vertices retained as outputs and $`\alpha=2`$. The dimension-dependent theorem gives $`F\le M/2`$. It is attained by the two-transcript corrected protocol and by this one-transcript uncorrected output. For larger stars, the [full construction](../science/achievability-and-limits.md#star-fusion-with-the-hub-retained-as-an-output) generates one correction symbol per added vertex.

## From instruments to communication bounds

### Fix the classical record while keeping the original sources

A complete communicated transcript specifies every communicated classical dependence in an adaptive protocol. At fixed seed and transcript, each party has a compatible local trace-nonincreasing map. Composing local operations and summing its compatible private histories gives

```math
\sigma_{t|r}
=\left(\bigotimes_{v\in V}\Lambda_{v,t|r}\right)
\left(\rho^{\rm in}_r\right).
```

The output systems of helpers are traced out. The [factorization lemma](../science/branch-bound.md#factorization-of-a-fixed-transcript) explains why summing private histories preserves complete positivity and trace nonincrease.

This representation acts on the original independent sources. It does not assert that the normalized state obtained after conditioning on a transcript is itself an independent-source network.

### Pull output events back to local effects

For an output party $`i`$, the adjoint of its branch map sends the basis projector $`|x\rangle\langle x|`$ to a positive input effect. The effects for different $`x`$ have a sum at most the identity because the map is trace nonincreasing.

Quantum Finner bounds joint event probabilities in terms of these local effects and a feasible fractional independent-set weight vector. Summing over the common basis label with a weighted Hölder inequality gives

```math
\sum_{x=0}^{d-1}q_x^{1/\alpha}\le1,
\qquad
q_x=\langle x^n|\sigma_{t|r}|x^n\rangle.
```

The [branch proof](../science/branch-bound.md#the-diagonal-mass-constraint) supplies the graph parameter, the inequality, and its research attribution. This is the step that introduces the independent-source restriction into the instrument formalism.

### Control coherence before normalizing

For a qubit GHZ target, positivity bounds the off-diagonal entry by $`\sqrt{q_0q_1}`$. The diagonal constraint then bounds that coherence by $`2^{-\alpha}`$. A branch of probability $`p`$ contributes at most $`p/2+2^{-\alpha}`$ to target fidelity.

For $`\alpha\ge2`$ and a positive-probability branch, interpolation instead gives

```math
g\le\frac1d\,p^{(\alpha-2)/(\alpha-1)}.
```

Here $`g`$ is the unnormalized target overlap. At $`\alpha=2`$, zero-probability branches are omitted and the positive branches satisfy $`g\le1/d`$. The proof treats this endpoint directly.

A normalized branch may have excellent fidelity when its probability is small. Dividing by $`p`$ too early would hide precisely the probability cost that the converse needs.

### Sum the complete transcripts

A depth-$`c`$ binary protocol has at most $`2^c`$ complete leaves. Summing the qubit coherence estimate gives the extensive communication bound. Summing the dimension-dependent estimate by concavity gives

```math
F\le\min\left\{1,\frac{M^{1/(\alpha-1)}}d\right\}
\qquad(\alpha\ge2).
```

The statement holds after averaging over a free shared seed when the leaf bound is uniform in that seed.

For $`k`$ qubit GHZ copies, grouping each party's qubits into a register sets $`d=2^k`$. This yields the [collective global-fidelity converse](../science/communication-converses.md#collective-preparation-of-many-ghz-states). It concerns overlap with the entire target block. High fidelity of the separate marginals alone is insufficient.

## Exact costs through entropy

Watrous's relative-entropy data-processing theorem supplies a second route to exact communication costs. For groups of laboratories $`B_1,\ldots,B_m`$, total correlation is

```math
J(B_1:\cdots:B_m)
=D\!\left(\rho_{B_1\cdots B_m}
\middle\Vert\bigotimes_{j=1}^{m}\rho_{B_j}\right).
```

It is zero for a product state and cannot increase under a product of local channels. When a classical transcript and seed are present, the argument averages this nonnegative quantity over their values.

The project proves two additional message identities. A local instrument and announced outcome originating **inside** one group cannot increase the conditional total correlation. A message originating **outside** all the groups can increase it by at most the message's conditional entropy, hence by at most one per transmitted binary bit. These identities require the explicit accounting in [the exact-cost proof](../science/achievability-and-limits.md#conditional-total-correlation-and-a-public-message); they are not a theorem quoted directly from the textbook.

For an all-output source tree, remove a vertex $`v`$. The remaining components start independently after tracing out $`v`$. Exact GHZ output, with $`v`$ subsequently traced out, leaves a common classical label in all $`\deg(v)`$ components. Their required total correlation is

```math
[\deg(v)-1]\log_2d.
```

Only messages from $`v`$ can supply the increase. Summing over vertices and using the degree sum of a tree gives $`(n-2)\log_2d`$. Sequential growth attains this exact binary cost for $`d=2^k`$.

For a separate helper hub and $`N\ge2`$ output leaves, the final leaf target is itself pure. Its joint entropy is zero and each leaf has entropy $`\log_2d`$, giving total correlation $`N\log_2d`$. The resulting hub-outbound lower bound matches fusion followed by a Fourier measurement and one phase correction. Keeping or discarding the hub changes both the target and the exact cost.

The proofs include almost-surely terminating protocols of finite mean length. Their fixed public cutoff argument retains completed target branches and resets unfinished outputs, then takes the completion probability to one. No approximate entropy-continuity claim is needed.

## Choosing the right resource question

| Question | Relevant resource | Correct conclusion to carry forward |
|---|---|---|
| Must every execution fit a fixed communication allowance? | Maximum binary length $`c`$ | Use the finite-transcript converse and the collective exponential bound. |
| Is only the average number of transmitted bits limited? | Mean prefix-free length $`L`$ | Use transcript entropy and cutoff bounds. On a retained-hub star with $`n\ge3`$ outputs, the asymptotic optimum at fixed global fidelity $`f\in(0,1]`$ is $`(n-2)f`$ bits per copy. |
| Is the output required only after acceptance? | Acceptance probability, accepted transcripts and conditional fidelity | Retain $`P`$ in $`P(dF_{\rm acc})^{\alpha-1}\le M_{\rm acc}`$ for $`\alpha\ge2`$, and charge useful acceptance signaling. |
| Is the target exact on a tree? | Outbound communication from each vertex | Conditional total correlation gives the matching $`k(n-2)`$-bit cost for $`d=2^k`$. |
| Is the source graph dense? | Available source edges and the output set | Extra source edges preserve the general packing converse but invalidate the tree-component independence argument. The exact dense-graph coefficient remains unresolved. |

A shared random decision to run an exact star protocol only a fraction of the time explains the mean-cost frontier. It creates a mixture of an exact target and a zero-cost product output. The [mean-cost analysis](../science/expected-and-heralded.md#a-matching-mean-cost-frontier-on-a-star) gives finite upper and lower bounds with matching leading terms, followed by the limit.

The [verification guide](../verification/README.md) reproduces finite state transformations and accounting examples. Those examples help identify what is being charged and what output is physically present. The universal lower bounds rely on the complete analytical proofs.

The learning route ends by combining these resource distinctions, matching constructions, imported ingredients and remaining limits into one account of the preparation problem. The milestones do not assert that the book already contains the network converse or that the project resolves every source topology.

