# Expected communication and heralded preparation

The [fixed-budget theorem](communication-converses.md) controls the number of complete transcripts. This page treats two different tasks: limiting the **mean** transcript length, and allowing an explicitly **heralded** output. Both use the [same model](model.md) and the probability-sensitive [branch bound](branch-bound.md).

All logarithms are base two. Write $`\alpha=\alpha_O(G)`$ and $`F=\mathbb E_R\sum_t g_{t|R}`$.

## Exact preparation: every transcript has small probability

Suppose the unconditional output is exactly $`\mathrm{GHZ}_{n,d}`$. Since its fidelity is one, every positive-probability branch has normalized fidelity one for almost every shared seed. [Corollary B6](branch-bound.md#coherence-and-fidelity-of-one-branch) then bounds the probability of each exact branch.

Therefore

```math
p_{t|r}\le d^{\,1-\alpha}.
\qquad\text{(E1)}
```

This argument only requires $`\alpha\ge1`$. It does not need the stronger restriction $`\alpha\ge2`$ used for the approximate dimension-dependent fidelity theorem.

For each fixed seed, both the min-entropy and Shannon entropy of the complete transcript obey

```math
H_{\min}(T|R=r)
\ge(\alpha-1)\log d,
\qquad
H(T|R=r)\ge(\alpha-1)\log d.
```

Prefix-freeness gives $`H(T|R=r)\le\mathbb E[\ell(T)|R=r]`$. For completeness, if $`K_r=\sum_t2^{-\ell(t)}\le1`$, compare the transcript distribution to $`q_t=2^{-\ell(t)}/K_r`$. Nonnegativity of their relative entropy yields

```math
H(T|R=r)
\le\mathbb E[\ell(T)|R=r]+\log K_r
\le\mathbb E[\ell(T)|R=r].
```

Averaging over the free seed proves the exact mean-cost converse

```math
L\ge H(T|R)\ge(\alpha-1)\log d.
\qquad\text{(E2)}
```

The statement concerns actual prefix-free communication, including termination. It does not charge the already available shared seed.

## Approximate qubit GHZ: a cutoff bound

Let $`d=2`$, and let $`b`$ be any positive integer. For a fixed seed, split the complete leaves into short transcripts with $`\ell(t)\le b`$ and long transcripts with $`\ell(t)>b`$. There are at most $`2^b`$ short leaves.

Let $`P_{\mathrm{s}|r}`$ and $`P_{\mathrm{l}|r}`$ be the corresponding probabilities. The qubit branch estimate gives

```math
\sum_{\ell(t)\le b}g_{t|r}
\le \frac{P_{\mathrm{s}|r}}2+2^{b-\alpha}.
```

On the long leaves, use $`g_{t|r}\le p_{t|r}`$. Thus

```math
F_r
\le\frac12+2^{b-\alpha}
+\frac{P_{\mathrm{l}|r}}2.
```

Markov's inequality and averaging over the seed give

```math
F\le
\min\left\{
1,\frac12+2^{b-\alpha}+\frac{L}{2b}
\right\}.
\qquad\text{(E3)}
```

Equivalently,

```math
L\ge
2b\left[F-\frac12-2^{b-\alpha}\right]_+,
\qquad [x]_+=\max\{x,0\}.
\qquad\text{(E4)}
```

For fixed $`F>1/2`$ and $`\alpha\to\infty`$, choose $`b=\lfloor\alpha-\log_2\alpha\rfloor`$ once it is positive. Then $`2^{b-\alpha}\le1/\alpha`$, and

```math
L\ge(2F-1)\alpha-O(\log\alpha).
\qquad\text{(E5)}
```

Since $`\alpha\ge n/2`$, even **expected** communication must grow linearly with the number of outputs at fixed fidelity above one half. This conclusion permits rare long executions; it is not obtained by replacing the worst-case budget by its expectation in the fixed-budget theorem.

## Approximate higher-dimensional GHZ: an entropy bound

Assume $`\alpha\ge2`$. For a positive-probability branch, the probability-sensitive fidelity bound gives

```math
g_{t|r}
\le\frac{p_{t|r}^{(\alpha-2)/(\alpha-1)}}d,
\qquad
f_{t|r}
\le\frac{1}{d\,p_{t|r}^{1/(\alpha-1)}}.
```

For $`f_{t|r}>0`$, rearranging gives

```math
-\log p_{t|r}
\ge(\alpha-1)\log(d f_{t|r}).
```

Multiply by $`p_{t|r}f_{t|r}`$ and sum. Since $`0\le f_{t|r}\le1`$,

```math
\begin{aligned}
H(T|R=r)
&\ge\sum_t p_{t|r}f_{t|r}(-\log p_{t|r})\\
&\ge(\alpha-1)
\sum_t p_{t|r}f_{t|r}\log(d f_{t|r})\\
&\ge(\alpha-1)F_r\log(dF_r).
\end{aligned}
```

The last line is Jensen's inequality for the convex function $`u\mapsto u\log(du)`$, with the continuous value zero at $`u=0`$. Zero-fidelity leaves contribute zero. Apply Jensen once more to the shared-seed average, and use prefix-freeness and $`L\ge0`$:

```math
L\ge(\alpha-1)\,[F\log(dF)]_+.
\qquad\text{(E6)}
```

For a fixed required fidelity $`f\ge1/d`$, the right side is increasing for actual fidelities $`F\ge f`$, so it also bounds protocols whose fidelity is at least $`f`$.

Equation (E6) is a weak mean-cost converse. Its leading coefficient for a fixed nonunit fidelity is different from the worst-case strong-converse threshold.

## A matching mean-cost frontier on a star

Take a star on $`n\ge3`$ output parties, including its hub, and let $`d=2^k`$. Write $`L_k^*(f)`$ for the infimum of mean communication over protocols with global fidelity at least a fixed $`f\in(0,1]`$.

Here $`\alpha=n-1`$. Equation (E6) gives

```math
L_k^*(f)
\ge(n-2)\,[f(k+\log f)]_+.
\qquad\text{(E7)}
```

For $`f\ge2^{-k}`$, the following construction gives a matching leading term. Use the free shared seed to choose between:

1. exact star fusion, costing $`(n-2)k`$ bits and producing fidelity one;
2. a local product output $`|0\rangle^{\otimes n}`$ in the $`d`$-level registers, costing zero bits and producing fidelity $`1/d=2^{-k}`$.

Choose the first option with probability

```math
q=\frac{f-2^{-k}}{1-2^{-k}}.
```

The average fidelity is exactly $`f`$ and the mean cost is $`q(n-2)k`$. Hence

```math
L_k^*(f)
\le(n-2)k\,\frac{f-2^{-k}}{1-2^{-k}}
\quad(f\ge2^{-k}).
\qquad\text{(E8)}
```

For $`f\le2^{-k}`$, the product output already meets the requirement at zero cost. For every fixed $`n\ge3`$ and $`f\in(0,1]`$, (E7) and (E8) imply the exact asymptotic frontier

```math
\lim_{k\to\infty}\frac{L_k^*(f)}k=(n-2)f.
\qquad\text{(E9)}
```

The same star construction also makes (E5) sharp to leading order in the **number of parties** for one qubit GHZ at fixed $`f>1/2`$: mix exact fusion with the product output using probability $`q=2f-1`$. Its mean cost is $`(2f-1)(n-2)`$.

These constructions explain why a worst-case strong converse cannot be transferred unchanged to mean communication. A constant fraction of fully successful executions can retain nonzero global fidelity while the mean rate lies below the exact-preparation rate.

## Heralded preparation

An accepted output is defined by a specified set $`\mathcal A_r`$ of complete transcripts for each seed. Suppose $`|\mathcal A_r|\le M_{\mathrm{acc}}`$ uniformly in $`r`$. Let

```math
P=\mathbb E_R\sum_{t\in\mathcal A_R}p_{t|R}>0,
\qquad
P F_{\mathrm{acc}}
=\mathbb E_R\sum_{t\in\mathcal A_R}g_{t|R}.
```

Here $`P`$ is the acceptance probability and $`F_{\mathrm{acc}}`$ the fidelity of the accepted quantum output.

For $`\alpha\ge2`$, summing the branch bound over the accepted leaves and then applying concavity to the shared-seed average gives

```math
P F_{\mathrm{acc}}
\le
\frac{M_{\mathrm{acc}}^{1/(\alpha-1)}}d
P^{(\alpha-2)/(\alpha-1)}.
```

At $`\alpha=2`$, count only nonzero accepted leaves; the same inequality follows directly without an ambiguous zero-to-zero power. Equivalently,

```math
P(dF_{\mathrm{acc}})^{\alpha-1}
\le M_{\mathrm{acc}}.
\qquad\text{(E10)}
```

For a qubit target, the complementary coherence estimate is

```math
P\left(F_{\mathrm{acc}}-\frac12\right)
\le M_{\mathrm{acc}}2^{-\alpha}.
\qquad\text{(E11)}
```

These are success-probability bounds for an explicit collection of complete transcripts. A physically useful herald must be available to the required parties. Communicating a global acceptance decision belongs to the protocol and is charged; selecting on a hidden collection of distant private outcomes is not a free implementation.

### Star saturation and the price of postselection

The [retained-hub star fusion construction](achievability-and-limits.md#star-fusion-with-the-hub-retained-as-an-output) has $`d^{n-2}`$ equiprobable correction words. Choose a subset of $`M_{\mathrm{acc}}`$ words. The hub announces failure for the other outcomes; on acceptance it communicates the word's index, allowing every affected leaf to apply its correction.

This protocol has exactly $`M_{\mathrm{acc}}`$ accepted transcripts,

```math
P=\frac{M_{\mathrm{acc}}}{d^{n-2}},
\qquad F_{\mathrm{acc}}=1,
```

and saturates (E10), since $`\alpha=n-1`$. If the subset is proper, a flag followed by a fixed-length accepted index uses at most $`1+\lceil\log_2 M_{\mathrm{acc}}\rceil`$ bits. When all words are accepted, no failure flag is required.

In particular, accepting just the all-zero correction word needs only a single announced success/failure bit, but succeeds with probability $`d^{-(n-2)}`$. The exponentially small probability is the resource consequence that disappears if postselection is left uncharged.

### Exact heralding without sources between outputs

Suppose the $`N\ge2$` output laboratories have no direct source edges between them. The network may contain any number of helper laboratories, arbitrary independent bipartite sources on the allowed edges, and interactive LOCC. For a publicly heralded exact $`d$`-level GHZ state, the stronger bound is

```math
P\le\min\{1,M_{\rm acc}/d^N\}.
\qquad\text{(E12)}
```

Equation (E12) specializes to $`P\le M_{\rm acc}/2^N$` for qubits. Equation (E10) applies under its original $`\alpha\ge2`$ condition, including imperfect accepted fidelity and direct source edges between outputs.

**Proof.** Fix a shared seed and one complete public transcript. Use the [product of local branch maps](branch-bound.md#factorization-of-a-fixed-transcript) and let $`\Lambda_i`$ be the output-laboratory map, including the local trace over systems other than its designated output. The maps include all unannounced local histories compatible with the prescribed transcript. Let $`E`$ be the effect for the product of the helper maps after discarding their registers. Trace nonincrease gives $`0\preceq E\preceq I`$. On the initial state $`\rho`$ for this seed, write $`H`$ for the collection of helper registers. Before applying the local output maps, the operator on the output laboratories is

```math
B=\operatorname{Tr}_{H}\!\left[(I\otimes E^{1/2})\rho
                      (I\otimes E^{1/2})\right]
\preceq \operatorname{Tr}_H\rho=\bigotimes_{i=1}^{N}\rho_i .
```

The operator difference is the analogous positive operator for $`I-E$`. The output marginal factors because no independent source supplies systems to two outputs. Applying the product of the local output maps gives

```math
\sigma\preceq A=\bigotimes_{i=1}^{N} A_i,
\qquad A_i=\Lambda_i(\rho_i),\qquad
A_i\succeq0,\quad\operatorname{Tr}A_i\le1 .
```

For an exact accepted branch of positive probability $`p$`, write $`\sigma=p|G\rangle\langle G|$` for the prescribed GHZ target $`|G\rangle$`. Each marginal of $`|G\rangle$` is $`I/d$`, so every $`A_i$` must have full support on its $`d$`-dimensional output. Conjugating the rank-one operator by $`A^{-1/2}$` gives $`p\langle G|A^{-1}|G\rangle\le1$`. Scalar Jensen's inequality for the logarithm of the eigenvalues of $`A^{-1}$` gives

```math
p
\le \frac1{\langle G|A^{-1}|G\rangle}
\le 2^{\langle G|\log_2 A|G\rangle}
=\prod_{i=1}^{N}(\det A_i)^{1/d}
\le d^{-N}.
```

The equality uses the tensor product for $`A$` and the maximally mixed GHZ marginals. The final step is the arithmetic–geometric mean inequality for the eigenvalues of each $`A_i$`. Exact fidelity of the accepted output implies target fidelity one in each positive-probability accepted transcript for almost every seed. Summing and then averaging over the seed proves (E12). ∎

**Bell-qudit star.** A separate hub holding one maximally entangled qudit pair per output can use the [discarded-hub construction](achievability-and-limits.md#a-hub-that-is-discarded-changes-the-task). Equivalently, the hub reads the orthonormal GHZ basis and announces the $`N-1$` relative shifts and one phase label that the leaves correct. Its maximally mixed input gives $`d^N$` equiprobable words. Selecting $`M_{\rm acc}$` such words and grouping all remaining outcomes into a failure word attains (E12) whenever $`M_{\rm acc}\le d^N$`. [Caprara Vivoli et al.](../references/related-work.md#capraravivoli2019) give the binary-herald Bell-qubit benchmark, and [Chen et al.](../references/related-work.md#chen2024) give the deterministic Bell-qubit construction and cost.

For an integer worst-case broadcast budget $`c\ge0$`, the following bound holds in every network with no direct source edges between outputs, and a Bell-qudit star attains it:

```math
P_{\rm Bell\ star}(c)=
\begin{cases}
(2^c-1)/d^N,&2^c<d^N,\\
1,&2^c\ge d^N .
\end{cases}
\qquad\text{(E13)}
```

Below the threshold, (E12) rules out deterministic success for every seed. At least one of the $`2^c$` complete binary words must then carry failure. The hub uses one common failure word and reserves the rest for accepted words. At or above the threshold, it assigns a distinct word to each GHZ-basis outcome and accepts every outcome. Separate physical delivery costs can depend on who needs each bit. Equation (E13) counts broadcast bits in the [stated model](model.md#broadcast-convention-and-other-delivery-models).

### Fixed links on a quantum star

[Quantum Star GHZ Heralding](https://github.com/GoGoKo699/Quantum-Star-GHZ-Heralding) studies the [one-way model with one calibrated pure qubit pair per leaf](https://github.com/GoGoKo699/Quantum-Star-GHZ-Heralding/blob/e5eb9af0dcdd2f7411e6a5b4eb6c6aec73ef19a3/science/MODEL.md). Its source-sensitive bounds use the actual Schmidt weights and one correction per accepted label. For three identical links with smaller Schmidt probability $`q=2/5$`, the maximum heralding probability is $`0.800$`, and [reaching it in this model requires four worst-case broadcast bits](https://github.com/GoGoKo699/Quantum-Star-GHZ-Heralding/blob/dfd1eb34407fee35c94faa3cd53ac4959631eb2c/science/COMMUNICATION.md#bits-needed-to-reach-the-unconstrained-optimum). That count includes the failure label. The general theorem above controls exact accepted transcripts even with arbitrary source dimensions and interaction. The calibrated-star analysis determines how specific resources constrain the probabilities and number of messages needed.

## Which conclusion applies?

| Task | Supported conclusion |
|---|---|
| Exact deterministic output, mean prefix-free communication | $`L\ge(\alpha-1)\log d`$ |
| Approximate qubit output, mean communication | Cutoff bound (E3); extensive cost at fixed $`F>1/2`$ |
| Approximate $`d`$-level output, $`\alpha\ge2`$, mean communication | Entropy bound (E6) |
| Star, fixed global fidelity, $`k`$ collective qubit targets | Exact mean-cost rate $`(n-2)f`$ |
| A specified accepted set of transcripts | Success–fidelity bounds (E10) and (E11) |
| Exact accepted outputs with no direct source edges between them | Per-transcript bound (E12), with the Bell-qudit star attaining the worst-case bit frontier (E13) |
| Fixed worst-case budget for a whole block | [Collective strong converse](communication-converses.md) |

The full comparison with classical PIN communication and other quantum network resource measures is in [related work](../references/related-work.md).

