# Reproducing the physical checks

The scientific claims are analytical. This directory checks the physical constructions and several accounting boundaries on explicit small quantum states. It does not replace the arbitrary-dimension proofs in [science/](../science/README.md).

## Requirements and command

Use Python 3.10 or newer. The program uses only the Python standard library; no package installation or network access is needed.

From the repository root, run:

```bash
python3 verification/check_science.py
```

To regenerate the machine-readable report included in the repository, run:

```bash
python3 verification/check_science.py --write-results verification/results.json
```

The successful run prints one `PASS` line per named physical check and finishes with:

```text
All 16 finite physical checks passed.
```

A failed equality or bound raises an assertion and exits unsuccessfully. A JSON report is written only after all checks have passed. The report records the Python version, actual checked architectures, dimensions, branch probabilities, transcript counts and fidelities.

## What the checks establish

| Physical question | Implementation | Checked outcome |
|---|---|---|
| Does star fusion produce the target on every branch? | Start from a product of edge Bell states, apply modular controlled subtraction, project measured registers, correct the output leaves, and trace measured registers. | Every unnormalized branch equals its probability times the full GHZ density matrix. Binary and ternary examples check the correction convention. |
| Does sequential growth work away from a star? | Apply the same register operations on paths and a branched six-vertex tree. | Old output registers remain consistent when an already-added non-root party controls a later fusion. |
| Are private outcomes being charged as communicated messages? | Keep all fine star syndromes, communicate only a prefix, group the other histories under the same public word, and average their output density matrices. | Public transcript count is smaller than the fine-history count; omitted corrections reduce fidelity as described in the construction. |
| Is coarse success/failure communication a valid two-leaf protocol? | The hub broadcasts whether all private syndromes are zero; all outputs reset locally on failure. | Eight private histories give only two public transcripts in the checked example, with exact conditional success and unconditional fidelity $`9/16`$. |
| Does discarding the hub require a phase correction? | Apply a qubit Hadamard, measure the retained hub output, and correct a leaf's phase. | Two- and three-leaf outputs are exact; forgetting the phase gives fidelity $`1/2`$. |
| Why is mean cost different from worst-case cost? | Mix an explicitly prepared two-copy GHZ target with a zero-cost product output using a shared classical coin. | The checked mixture has one expected bit, four worst-case bits, and global fidelity $`7/16`$. |
| Why are absolute values needed in the Finner contraction? | Contract three Bell sources with complex entangled local projectors in a triangle. | The event probability is $`1/16`$ and the Finner bound is $`1/8`$. Replacing absolute squares by plain complex squares would falsely give a zero upper bound. |

The register simulation uses integer state-vector numerators with a common squared normalization denominator. Modular permutations, computational-basis measurements, qubit Hadamards and Pauli corrections preserve this representation. Partial traces, branch weights and GHZ fidelities are then evaluated with `fractions.Fraction`, so those comparisons have no floating-point tolerance.

The complex triangle diagnostic uses matrix entries whose real and imaginary parts are binary fractions. It is a small diagnostic of the complex-valued contraction, with a stated tolerance of $`10^{-14}`$ for its scalar imaginary residual. It is not a numerical search over quantum networks or a test of all fractional weights.

## Analytical claims outside these finite checks

The complete reasoning for quantum Finner, fixed-transcript CP-map factorization, the dimension-independent communication converse and the conditional-total-correlation bounds is in the corresponding [scientific pages](../science/README.md). No finite state simulation establishes those universal statements.

The checks also do not determine the optimal communication coefficient on a complete source graph, extend the pair-source theorem to multipartite sources, or replace global block fidelity with a single-copy marginal criterion. The [construction and limits page](../science/achievability-and-limits.md) gives the exact scope and counterexamples.
