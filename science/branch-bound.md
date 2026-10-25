# A bound for each communication transcript

The communication converses rest on a constraint on the *unnormalized* state associated with one complete transcript. Conditioning on that transcript can create a highly entangled state, so the normalized conditional state need not be a state that the original network can prepare without communication. The useful constraint instead comes from expressing transcript consistency as a collection of local success events on the independent input sources.

The [model](model.md) fixes a finite source graph $`G=(V,E)`$, an output set $`O\subseteq V`$ of size $`n`$, helper vertices $`H=V\setminus O`$, and a shared classical seed $`R`$. Every source state and local Hilbert space is finite dimensional; no bound on these dimensions enters the results. All logarithms elsewhere in the account are binary.

For a feasible weight vector $`w`$, write

```math
\mathcal W_O(G)
=
\left\{
w\in[0,1]^V:
w_h=0\ (h\in H),\qquad
w_u+w_v\le 1\ (\{u,v\}\in E)
\right\},
\qquad
\alpha=\sum_{v\in V}w_v .
```

The optimized value is $`\alpha_O(G)=\max_{w\in\mathcal W_O(G)}\sum_v w_v`$. The branch statements below hold for every feasible $`w`$; optimization is performed only after the inequalities are proved.

## Quantum Finner inequality

**Theorem B1: Event inequality for independent bipartite sources.** Let

```math
\omega=\bigotimes_{e\in E}\omega_e
```

be an independent bipartite-source state, with independent local ancillas also allowed. For local effects $`0\le A_v\le I`$, define

```math
P=\operatorname{Tr}\!\left[
\left(\bigotimes_{v\in V}A_v\right)\omega
\right],
\qquad
P_v=\operatorname{Tr}(A_v\omega_v).
```

Here $`\omega_v`$ is the reduced input state at vertex $`v`$, including its local ancilla. For every $`w\in[0,1]^V`$ satisfying $`w_u+w_v\le1`$ on each edge,

```math
P\le\prod_{v:w_v>0}P_v^{\,w_v}.
\tag{B1}
```

This is the inherited quantum network Finner inequality of [Renou et al.](../references/related-work.md#ren2019). We give a proof with absolute values in the tensor contraction, so complex matrix elements cause no restriction. The only classical analytic input is [Finner's inequality](../references/related-work.md#finner1992) in the finite counting-measure form

```math
\sum_{(z_e)_{e\in E}}
\prod_{v\in V}g_v((z_e)_{e\ni v})
\le
\prod_{v\in V}
\left(
\sum_{(z_e)_{e\ni v}}
g_v((z_e)_{e\ni v})^2
\right)^{1/2},
\qquad g_v\ge0.
\tag{B2}
```

Each edge variable appears in exactly two functions. This is the all-half-weight case of classical Finner; it holds for finite product counting measures as well as probability measures. Normalizing each counting measure gives the same formula, because each normalization factor occurs twice with exponent $`1/2`$ on the right.

### Reduction to pure edge states

An independent local ancilla with state $`\eta_v`$ can be absorbed into the effect by replacing $`A_v`$ with

```math
\widetilde A_v
=
\operatorname{Tr}_{L_v}
\left[
(I\otimes\eta_v^{1/2})A_v
(I\otimes\eta_v^{1/2})
\right].
```

This preserves the joint event probability and the corresponding marginal probability, and $`0\le\widetilde A_v\le I`$. We may therefore suppress the independent local ancillas.

For each mixed edge state $`\omega_e`$, take a purification and assign the entire purifying register to one endpoint of that edge. Extend that endpoint's effect by the identity on the extra register. The event probabilities are unchanged, independence across edges is preserved, and each enlarged edge state is pure across its two endpoints. Thus it is enough to prove the inequality for pure edge states. Their Schmidt decompositions can be written

```math
|\psi_e\rangle
=
\sum_{a_e}\sqrt{\lambda_{e,a_e}}\,
|a_e\rangle_u|a_e\rangle_v,
\qquad
\lambda_{e,a_e}\ge0,
\qquad
\sum_{a_e}\lambda_{e,a_e}=1.
```

The Schmidt bases may be chosen independently on the distinct edge registers at each vertex. Compress each local effect to the support of its reduced input state. This preserves the event probabilities and the inequalities $`0\le A_v\le I`$, and makes the product Schmidt basis a complete basis for the local calculation below.

### The half-weight inequality

Let $`\mathbf a_v=(a_e)_{e\ni v}`$ and put

```math
r_v(\mathbf a_v)=\prod_{e\ni v}\lambda_{e,a_e}.
```

The reduced state at vertex $`v`$ is diagonal with these eigenvalues. Expanding the product of the pure edge density operators gives

```math
P
=
\sum_{(a_e,b_e)_{e\in E}}
\prod_{v\in V}f_v(\mathbf a_v,\mathbf b_v),
```

where

```math
f_v(\mathbf a_v,\mathbf b_v)
=
\langle\mathbf b_v|A_v|\mathbf a_v\rangle
\,[r_v(\mathbf a_v)r_v(\mathbf b_v)]^{1/4}.
```

These functions can be complex. Since $`P\ge0`$, the triangle inequality followed by (B2), applied to $`|f_v|`$, yields

```math
P
\le
\prod_{v\in V}
\left[
\sum_{\mathbf a,\mathbf b}
|\langle\mathbf b|A_v|\mathbf a\rangle|^2
\sqrt{r_v(\mathbf a)r_v(\mathbf b)}
\right]^{1/2}.
\tag{B3}
```

For each vertex, the arithmetic–geometric mean inequality and Hermiticity of $`A_v`$ give

```math
\begin{aligned}
\sum_{\mathbf a,\mathbf b}
|(A_v)_{\mathbf b\mathbf a}|^2
\sqrt{r_v(\mathbf a)r_v(\mathbf b)}
&\le
\frac12\sum_{\mathbf a,\mathbf b}
|(A_v)_{\mathbf b\mathbf a}|^2
[r_v(\mathbf a)+r_v(\mathbf b)]\\
&=
\operatorname{Tr}(\omega_v A_v^2)\\
&\le
\operatorname{Tr}(\omega_v A_v)
=P_v.
\end{aligned}
```

The final inequality uses $`A_v^2\le A_v`$, which follows from $`0\le A_v\le I`$. Substitution into (B3) proves

```math
P\le\prod_{v\in V}P_v^{1/2}.
\tag{B4}
```

This argument includes isolated vertices: their tensors have no edge indices, and the same scalar estimate applies.

### Arbitrary fractional weights

We first recall why the polytope

```math
\mathcal W(G)
=
\{w\in[0,1]^V:w_u+w_v\le1\text{ on every edge}\}
```

has half-integral extreme points. At an extreme point, consider the vertices with $`0<w_v<1`$, and retain only tight edges $`w_u+w_v=1`$ between them. If a connected component of this tight-edge graph were bipartite, increasing the weights in one color class by a sufficiently small $`\varepsilon`$ and decreasing those in the other by $`\varepsilon`$ would preserve every tight equality. All other inequalities have positive slack, and the fractional coordinates have positive distance from $`0`$ and $`1`$, so both signs of this perturbation would remain feasible. This contradicts extremality. An isolated fractional vertex admits the same perturbation. Hence every such component contains an odd cycle. Alternating the tight equalities around that cycle forces every weight on it to be $`1/2`$, and connectivity forces every other weight in the component to be $`1/2`$. The remaining coordinates are $`0`$ or $`1`$.

It therefore suffices first to establish (B1) when every weight belongs to $`\{0,1/2,1\}`$. Replace all zero-weight effects by the identity. This can only increase the joint event probability, since all factors act on distinct local systems and satisfy $`0\le A_v\le I`$. Trace out those zero-weight vertices. Edges crossing from a discarded vertex to a retained vertex become independent local ancillas at the retained endpoint; the other sources remain independent bipartite states.

A weight-one vertex has no edge to any other retained vertex, because $`1+w_u\le1`$ would otherwise fail. Its marginal event therefore factors out with probability $`P_v`$. The weight-half vertices form an independent bipartite-source network, possibly with local ancillas. Applying (B4) to them proves (B1) at every extreme point. The retained marginal probabilities are unchanged by replacing other effects with the identity and tracing out their systems.

Finally, express any feasible $`w`$ as a convex combination of extreme points. If $`P=0`$, the desired bound is immediate. If $`P>0`$, then every $`P_v>0`$, because $`P\le P_v`$. Taking logarithms of the extreme-point bounds and their convex combination gives

```math
\log P\le\sum_v w_v\log P_v.
```

Exponentiation proves (B1). In particular, zero marginal probabilities cause no ambiguity, and zero-weight factors are omitted. The helper-constrained polytope is a face of $`\mathcal W(G)`$, so the same theorem applies with all helper weights zero. ∎

## Factorization of a fixed transcript

**Lemma B2: Local maps for one complete transcript.** Condition on a shared seed value $`R=r`$, so the input is

```math
\omega^{(r)}=\bigotimes_{e\in E}\omega_e^{(r)}
```

with independent local ancillas understood. For a complete communication transcript $`t`$, there are local completely positive, trace-nonincreasing maps $`\Lambda_{v,t|r}`$ such that its unnormalized output state is

```math
\sigma_{t|r}
=
\left(\bigotimes_{v\in V}\Lambda_{v,t|r}\right)
\left(\omega^{(r)}\right).
\tag{B5}
```

At an output vertex, the map retains its designated $`d`$-dimensional output. At a helper, its quantum output can be traced out, so its map takes values in the scalars. Local environments and unreported classical records may also be discarded inside these maps.

**Proof.** In a fixed complete transcript, every message crossing from one vertex to another has a prescribed value. At each vertex, supply these prescribed incoming messages to its local strategy. Run the local instruments with their usual dependence on the vertex's private records. Retain only those outcomes whose outgoing messages agree with the prescribed transcript. Any disagreement is a local failure event.

This defines a valid local instrument with a success outcome. Its success map $`\Lambda_{v,t|r}`$ is completely positive and trace nonincreasing: local instruments are trace preserving when all their outcomes are summed, and rejecting some outcomes cannot increase trace. The construction does not condition the vertex's input state on a remote measurement outcome. It supplies a fixed classical incoming-message sequence to a local instrument.

More explicitly, let $`h_v`$ range over the vertex's uncommunicated local histories compatible with its part of $`t`$, and let $`\Lambda_{v,t,h_v|r}`$ be the composition of the corresponding local CP maps. Then

```math
\Lambda_{v,t|r}
=
\sum_{h_v}\Lambda_{v,t,h_v|r}.
```

Once $`t`$ is fixed, consistency of these private histories is a local condition at each vertex. Expanding the physical protocol branch over all private histories and using multilinearity therefore gives

```math
\begin{aligned}
\sigma_{t|r}
&=
\sum_{(h_v)_v}
\left(\bigotimes_v\Lambda_{v,t,h_v|r}\right)
(\omega^{(r)})\\
&=
\left(\bigotimes_v\sum_{h_v}\Lambda_{v,t,h_v|r}\right)
(\omega^{(r)}).
\end{aligned}
```

This is (B5). No statistical independence of the private histories is assumed; their correlations are evaluated on the joint quantum input. The algebra only uses the fact that every classical dependency between distinct vertices has been fixed by $`t`$.

Private records can equivalently be kept as part of the local memory throughout the protocol and traced out at the end. Thus the factorization does not require the protocol to reveal those records, and the number of transcripts counts communicated data only. Continuous local outcome spaces can be handled by the corresponding integrals, or by the local-instrument formulation above. The finite-dimensional inequalities are unchanged under trace-norm limits of the allowed output states.

The scheduling and stopping conventions in the [model](model.md) are necessary here: an uncharged, data-dependent speaker choice or success signal would be an additional classical dependency not fixed by the counted transcript. ∎

## The diagonal mass constraint

Fix $`r,t`$ and abbreviate $`\sigma=\sigma_{t|r}`$ and $`p=\operatorname{Tr}\sigma`$. For $`x\in\{0,\ldots,d-1\}`$, write

```math
|x^O\rangle=\bigotimes_{i\in O}|x\rangle_i,
\qquad
q_x=\langle x^O|\sigma|x^O\rangle.
```

**Lemma B3: Diagonal mass of a branch.** For every feasible $`w\in\mathcal W_O(G)`$ with $`\alpha=\sum_vw_v>0`$,

```math
\sum_{x=0}^{d-1}q_x^{1/\alpha}\le1.
\tag{B6}
```

**Proof.** Define local input effects at output vertices by

```math
A_i(x)=\Lambda_{i,t|r}^{*}(|x\rangle\langle x|),
\qquad i\in O,
```

and at helpers by $`A_h=\Lambda_{h,t|r}^{*}(1)`$. Here the adjoint is defined by the trace pairing. Complete positivity and trace nonincrease imply

```math
A_i(x)\ge0,\qquad
\sum_x A_i(x)=\Lambda_{i,t|r}^{*}(I)\le I,
\qquad
0\le A_h\le I.
```

Let

```math
u_i(x)=\operatorname{Tr}[A_i(x)\omega_i^{(r)}].
```

Then $`\sum_xu_i(x)\le1`$. Equation (B5) identifies $`q_x`$ with the joint event consisting of local transcript success and output $`x`$ at every output vertex, together with transcript success at every helper. Theorem B1, with all helper weights zero, gives

```math
q_x\le\prod_{i\in O:w_i>0}u_i(x)^{w_i}.
\tag{B7}
```

Set $`\theta_i=w_i/\alpha`$ for the positive-weight vertices. These numbers sum to one. Weighted Hölder gives

```math
\begin{aligned}
\sum_xq_x^{1/\alpha}
&\le
\sum_x\prod_{i:w_i>0}u_i(x)^{\theta_i}\\
&\le
\prod_{i:w_i>0}
\left(\sum_xu_i(x)\right)^{\theta_i}\\
&\le1.
\end{aligned}
```

This proves (B6). ∎

Only the original independent input state appears in this proof. The normalized conditional state $`\sigma/p`$ is never assumed to retain network independence.

## Coherence and fidelity of one branch

The target and squared-overlap convention are

```math
|\mathrm{GHZ}_{n,d}\rangle
=
\frac1{\sqrt d}\sum_{x=0}^{d-1}|x^O\rangle,
\qquad
\Phi_d(\sigma)
=
\langle\mathrm{GHZ}_{n,d}|\sigma|\mathrm{GHZ}_{n,d}\rangle.
```

For an unnormalized branch, $`\Phi_d(\sigma)`$ includes its occurrence probability. Its conditional fidelity, when $`p>0`$, is $`f=\Phi_d(\sigma)/p`$.

**Proposition B4: Qubit branch coherence.** For $`d=2`$ and every feasible weight vector,

```math
\left|\langle0^O|\sigma|1^O\rangle\right|
\le 2^{-\alpha},
\qquad
\Phi_2(\sigma)\le\frac p2+2^{-\alpha}.
\tag{B8}
```

**Proof.** Positivity of the $`2\times2`$ principal submatrix and (B7) imply

```math
\begin{aligned}
\left|\langle0^O|\sigma|1^O\rangle\right|
&\le\sqrt{q_0q_1}\\
&\le
\prod_{i:w_i>0}
\sqrt{u_i(0)u_i(1)}^{\,w_i}\\
&\le
\prod_{i:w_i>0}
\left(\frac{u_i(0)+u_i(1)}2\right)^{w_i}\\
&\le 2^{-\alpha}.
\end{aligned}
```

Also $`q_0+q_1\le p`$, so

```math
\Phi_2(\sigma)
=
\frac{q_0+q_1}{2}
+\operatorname{Re}\langle0^O|\sigma|1^O\rangle
\le\frac p2+2^{-\alpha}.
```

This proof does not require $`\alpha\ge2`$. ∎

**Proposition B5: Probability-sensitive branch fidelity.** If $`\alpha\ge2`$ and $`p>0`$, then

```math
\Phi_d(\sigma)
\le
\frac1d\,p^{\,(\alpha-2)/(\alpha-1)}.
\tag{B9}
```

The zero-probability branch has $`\Phi_d(\sigma)=0`$ and is treated separately when $`\alpha=2`$.

**Proof.** Every principal $`2\times2`$ submatrix of $`\sigma`$ is positive, so

```math
|\langle x^O|\sigma|y^O\rangle|
\le\sqrt{q_xq_y}.
```

Consequently,

```math
\Phi_d(\sigma)
\le
\frac1d
\left(\sum_x\sqrt{q_x}\right)^2.
\tag{B10}
```

For $`\alpha>2`$, put

```math
a=\frac{\alpha}{2(\alpha-1)},
\qquad
b=\frac{\alpha-2}{2(\alpha-1)}.
```

Both exponents are positive and $`a+b=1`$. Ordinary Hölder, applied to
$`\sqrt{q_x}=(q_x^{1/\alpha})^a q_x^b`$, yields

```math
\begin{aligned}
\left(\sum_x\sqrt{q_x}\right)^2
&\le
\left(\sum_xq_x^{1/\alpha}\right)^{\alpha/(\alpha-1)}
\left(\sum_xq_x\right)^{(\alpha-2)/(\alpha-1)}\\
&\le
p^{(\alpha-2)/(\alpha-1)}.
\end{aligned}
\tag{B11}
```

The second line uses Lemma B3 and $`\sum_xq_x\le p`$. Equations (B10)–(B11) prove (B9).

At the endpoint $`\alpha=2`$, Lemma B3 already says $`\sum_x\sqrt{q_x}\le1`$, so (B10) gives $`\Phi_d(\sigma)\le1/d`$ for each nonzero branch. This is exactly (B9) with exponent zero, without assigning a value to $`0^0`$. For $`\alpha<2`$, the exponent $`b`$ would be negative, and this Hölder argument is unavailable. ∎

**Corollary B6: Probability of an exact branch.** If $`\alpha>0`$ and a nonzero branch is exactly $`\sigma=p|\mathrm{GHZ}_{n,d}\rangle\langle\mathrm{GHZ}_{n,d}|`$, then

```math
p\le d^{\,1-\alpha}.
\tag{B12}
```

Indeed, $`q_x=p/d`$ for every $`x`$, and (B6) gives $`d(p/d)^{1/\alpha}\le1`$. This statement does not require $`\alpha\ge2`$.

## From a branch to a protocol

The diagonal mass constraint and the qubit coherence bound are uniform in the shared seed, source dimensions, local memories, and complete transcript. The [finite-communication converses](communication-converses.md) sum these branch bounds over a bounded set of transcripts. The [expected-cost and heralded bounds](expected-and-heralded.md) use the same ingredients while keeping branch probabilities explicit.
