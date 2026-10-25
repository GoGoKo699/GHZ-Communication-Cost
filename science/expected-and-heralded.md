# Expected communication and heralded preparation

The [fixed-budget theorem](communication-converses.md) controls the number of complete transcripts. This page treats two different tasks: limiting the **mean** transcript length, and allowing an explicitly **heralded** output. Both use the [same model](model.md) and the probability-sensitive [branch bound](branch-bound.md).

All logarithms are base two. Write $`\alpha=\alpha_O(G)`$ and $`F=\mathbb E_R\sum_t g_{t|R}`$.

## Exact preparation: every transcript has small probability

Suppose the unconditional output is exactly $`\mathrm{GHZ}_{n,d}`$. Since its fidelity is one, every positive-probability branch has normalized fidelity one for almost every shared seed. [Corollary B6](branch-bound.md#coherence-and-fidelity-of-one-branch) then bounds the probability of each exact branch.

Therefore

```math
p_{t|r}\le d^{\,1-\alpha}.
\tag{E1}
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
\tag{E2}
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
\tag{E3}
```

Equivalently,

```math
L\ge
2b\left[F-\frac12-2^{b-\alpha}\right]_+,
\qquad [x]_+=\max\{x,0\}.
\tag{E4}
```

For fixed $`F>1/2`$ and $`\alpha\to\infty`$, choose $`b=\lfloor\alpha-\log_2\alpha\rfloor`$ once it is positive. Then $`2^{b-\alpha}\le1/\alpha`$, and

```math
L\ge(2F-1)\alpha-O(\log\alpha).
\tag{E5}
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
\tag{E6}
```

For a fixed required fidelity $`f\ge1/d`$, the right side is increasing for actual fidelities $`F\ge f`$, so it also bounds protocols whose fidelity is at least $`f`$.

Equation (E6) is a weak mean-cost converse. Its leading coefficient for a fixed nonunit fidelity is different from the worst-case strong-converse threshold.

## A matching mean-cost frontier on a star

Take a star on $`n\ge3`$ output parties, including its hub, and let $`d=2^k`$. Write $`L_k^*(f)`$ for the infimum of mean communication over protocols with global fidelity at least a fixed $`f\in(0,1]`$.

Here $`\alpha=n-1`$. Equation (E6) gives

```math
L_k^*(f)
\ge(n-2)\,[f(k+\log f)]_+.
\tag{E7}
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
\tag{E8}
```

For $`f\le2^{-k}`$, the product output already meets the requirement at zero cost. For every fixed $`n\ge3`$ and $`f\in(0,1]`$, (E7) and (E8) imply the exact asymptotic frontier

```math
\lim_{k\to\infty}\frac{L_k^*(f)}k=(n-2)f.
\tag{E9}
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
\tag{E10}
```

For a qubit target, the complementary coherence estimate is

```math
P\left(F_{\mathrm{acc}}-\frac12\right)
\le M_{\mathrm{acc}}2^{-\alpha}.
\tag{E11}
```

These are success-probability bounds for an explicit collection of complete transcripts. A physically useful herald must be available to the required parties. Communicating a global acceptance decision belongs to the protocol and is charged; selecting on a hidden collection of distant private outcomes is not a free implementation.

### Star saturation and the price of postselection

The [star fusion construction](achievability-and-limits.md) has $`d^{n-2}`$ equiprobable correction words. Choose a subset of $`M_{\mathrm{acc}}`$ words. The hub announces failure for the other outcomes; on acceptance it communicates the word's index, allowing every affected leaf to apply its correction.

This protocol has exactly $`M_{\mathrm{acc}}`$ accepted transcripts,

```math
P=\frac{M_{\mathrm{acc}}}{d^{n-2}},
\qquad F_{\mathrm{acc}}=1,
```

and saturates (E10), since $`\alpha=n-1`$. If the subset is proper, a flag followed by a fixed-length accepted index uses at most $`1+\lceil\log_2 M_{\mathrm{acc}}\rceil`$ bits. When all words are accepted, no failure flag is required.

In particular, accepting just the all-zero correction word needs only a single announced success/failure bit, but succeeds with probability $`d^{-(n-2)}`$. The exponentially small probability is the resource consequence that disappears if postselection is left uncharged.

## Which conclusion applies?

| Task | Supported conclusion |
|---|---|
| Exact deterministic output, mean prefix-free communication | $`L\ge(\alpha-1)\log d`$ |
| Approximate qubit output, mean communication | Cutoff bound (E3); extensive cost at fixed $`F>1/2`$ |
| Approximate $`d`$-level output, $`\alpha\ge2`$, mean communication | Entropy bound (E6) |
| Star, fixed global fidelity, $`k`$ collective qubit targets | Exact mean-cost rate $`(n-2)f`$ |
| A specified accepted set of transcripts | Success–fidelity bounds (E10) and (E11) |
| Fixed worst-case budget for a whole block | [Collective strong converse](communication-converses.md) |

The full comparison with classical PIN communication and other quantum network resource measures is in [related work](../references/related-work.md).

