#!/usr/bin/env python3
"""Finite physical checks for GHZ fusion; Python standard library only.

The Bell-source state is represented by integer amplitudes with one shared
squared normalization denominator. Modular gates, projective measurements,
qubit Hadamards and Pauli corrections preserve this representation. Output
density matrices and their fidelities are therefore checked with Fractions.
The small complex Finner example uses exactly representable binary complex
entries and a numerical tolerance only for its reported scalar square root.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable


Basis = tuple[int, ...]
Vector = dict[Basis, int]
Density = dict[tuple[Basis, Basis], Fraction]


@dataclass
class Simulation:
    n: int
    d: int
    denominator: int
    outputs: tuple[int, ...]
    branches: list[tuple[tuple[int, ...], Vector]]


def permute(vector: Vector, rule: Callable[[Basis], Basis]) -> Vector:
    result: defaultdict[Basis, int] = defaultdict(int)
    for basis, amplitude in vector.items():
        result[rule(basis)] += amplitude
    return {basis: amplitude for basis, amplitude in result.items() if amplitude}


def subtract_control(vector: Vector, control: int, target: int, d: int) -> Vector:
    def rule(basis: Basis) -> Basis:
        changed = list(basis)
        changed[target] = (basis[target] - basis[control]) % d
        return tuple(changed)

    return permute(vector, rule)


def shift(vector: Vector, register: int, amount: int, d: int) -> Vector:
    def rule(basis: Basis) -> Basis:
        changed = list(basis)
        changed[register] = (basis[register] + amount) % d
        return tuple(changed)

    return permute(vector, rule)


def measure(vector: Vector, register: int) -> dict[int, Vector]:
    branches: dict[int, Vector] = {}
    for basis, amplitude in vector.items():
        branches.setdefault(basis[register], {})[basis] = amplitude
    return branches


def hadamard(vector: Vector, register: int) -> Vector:
    """Return integer numerators; caller multiplies the denominator by two."""
    result: defaultdict[Basis, int] = defaultdict(int)
    for basis, amplitude in vector.items():
        for outcome in (0, 1):
            changed = list(basis)
            changed[register] = outcome
            result[tuple(changed)] += amplitude * (-1) ** (basis[register] * outcome)
    return {basis: amplitude for basis, amplitude in result.items() if amplitude}


def phase_z(vector: Vector, register: int, power: int) -> Vector:
    return {
        basis: amplitude * (-1) ** (power * basis[register])
        for basis, amplitude in vector.items()
    }


def reduced_density(vector: Vector, keep: tuple[int, ...], denominator: int) -> Density:
    """Partial trace, retaining the unnormalized probability of this branch."""
    if not vector:
        return {}
    register_count = len(next(iter(vector)))
    keep_set = set(keep)
    discard = tuple(i for i in range(register_count) if i not in keep_set)
    by_environment: dict[Basis, dict[Basis, int]] = {}
    for basis, amplitude in vector.items():
        output = tuple(basis[i] for i in keep)
        environment = tuple(basis[i] for i in discard)
        block = by_environment.setdefault(environment, {})
        block[output] = block.get(output, 0) + amplitude
    density: defaultdict[tuple[Basis, Basis], Fraction] = defaultdict(Fraction)
    for block in by_environment.values():
        for left, left_amplitude in block.items():
            for right, right_amplitude in block.items():
                density[left, right] += Fraction(left_amplitude * right_amplitude, denominator)
    return {entry: value for entry, value in density.items() if value}


def add_density(*matrices: Density) -> Density:
    result: defaultdict[tuple[Basis, Basis], Fraction] = defaultdict(Fraction)
    for matrix in matrices:
        for entry, value in matrix.items():
            result[entry] += value
    return {entry: value for entry, value in result.items() if value}


def scale_density(matrix: Density, weight: Fraction) -> Density:
    return {entry: value * weight for entry, value in matrix.items() if value * weight}


def trace(matrix: Density) -> Fraction:
    return sum((value for (left, right), value in matrix.items() if left == right), Fraction())


def ghz_density(n: int, d: int, weight: Fraction = Fraction(1)) -> Density:
    return {
        ((x,) * n, (y,) * n): weight / d
        for x in range(d)
        for y in range(d)
    }


def zero_density(n: int, weight: Fraction = Fraction(1)) -> Density:
    return {((0,) * n, (0,) * n): weight} if weight else {}


def ghz_fidelity(matrix: Density, n: int, d: int) -> Fraction:
    return sum(
        (matrix.get(((x,) * n, (y,) * n), Fraction()) for x in range(d) for y in range(d)),
        Fraction(),
    ) / d


def star(n: int) -> tuple[tuple[int, int], ...]:
    return tuple((0, v) for v in range(1, n))


def path(n: int) -> tuple[tuple[int, int], ...]:
    return tuple((v, v + 1) for v in range(n - 1))


def simulate_tree(
    edges: tuple[tuple[int, int], ...],
    d: int,
    correct_steps: set[int] | None = None,
) -> Simulation:
    """Apply sequential tree growth to an explicit product of edge Bell states.

    A value None communicates/corrects every syndrome. Otherwise only the
    selected steps are corrected. The latter option is used only for stars,
    where omitting a leaf correction cannot change a later control register.
    """
    assert d >= 2 and edges
    vertices = set(itertools.chain.from_iterable(edges))
    n = max(vertices) + 1
    assert vertices == set(range(n)) and len(edges) == n - 1
    assert all(u != v for u, v in edges)
    assert len({frozenset(edge) for edge in edges}) == len(edges)

    vector = {
        tuple(value for edge_value in values for value in (edge_value, edge_value)): 1
        for values in itertools.product(range(d), repeat=len(edges))
    }
    denominator = d ** len(edges)
    assert sum(amplitude * amplitude for amplitude in vector.values()) == denominator

    root_u, root_v = edges[0]
    outputs = {root_u: 0, root_v: 1}
    grown = {root_u, root_v}
    remaining = set(range(1, len(edges)))
    branches: list[tuple[tuple[int, ...], Vector]] = [((), vector)]

    step = 0
    while remaining:
        frontier = [
            edge_index
            for edge_index in sorted(remaining)
            if sum(vertex in grown for vertex in edges[edge_index]) == 1
        ]
        assert frontier, "The supplied edges are not a connected tree."
        edge_index = frontier[0]
        u, v = edges[edge_index]
        parent, child = (u, v) if u in grown else (v, u)
        parent_half = 2 * edge_index + (0 if parent == u else 1)
        child_half = 2 * edge_index + (0 if child == u else 1)
        new_branches = []
        for history, state in branches:
            after_gate = subtract_control(state, outputs[parent], parent_half, d)
            for syndrome, selected in measure(after_gate, parent_half).items():
                if correct_steps is None or step in correct_steps:
                    selected = shift(selected, child_half, -syndrome, d)
                new_branches.append((history + (syndrome,), selected))
        branches = new_branches
        outputs[child] = child_half
        grown.add(child)
        remaining.remove(edge_index)
        step += 1

    assert grown == vertices and step == n - 2
    return Simulation(n, d, denominator, tuple(outputs[v] for v in range(n)), branches)


def output_branches(simulation: Simulation) -> list[tuple[tuple[int, ...], Density]]:
    return [
        (history, reduced_density(state, simulation.outputs, simulation.denominator))
        for history, state in simulation.branches
    ]


def check_exact_tree(name: str, edges: tuple[tuple[int, int], ...], d: int) -> dict:
    simulation = simulate_tree(edges, d)
    expected_probability = Fraction(1, d ** (simulation.n - 2))
    matrices = output_branches(simulation)
    assert len(matrices) == d ** (simulation.n - 2)
    for _, matrix in matrices:
        assert trace(matrix) == expected_probability
        assert matrix == ghz_density(simulation.n, d, expected_probability)
    full_output = add_density(*(matrix for _, matrix in matrices))
    assert full_output == ghz_density(simulation.n, d)
    return {
        "name": name,
        "outputs": simulation.n,
        "local_dimension": d,
        "source_edges": [list(edge) for edge in edges],
        "syndrome_symbols": simulation.n - 2,
        "transcripts": len(matrices),
        "each_branch_probability": str(expected_probability),
        "global_fidelity": str(ghz_fidelity(full_output, simulation.n, d)),
        "arithmetic": "exact rational density matrices",
    }


def check_partial_star_corrections() -> list[dict]:
    n, d = 5, 3
    results = []
    for known_count in range(n - 1):
        known_steps = set(range(known_count))
        simulation = simulate_tree(star(n), d, correct_steps=known_steps)
        grouped: dict[tuple[int, ...], Density] = {}
        for history, matrix in output_branches(simulation):
            public_word = history[:known_count]
            grouped[public_word] = add_density(grouped.get(public_word, {}), matrix)
        assert len(grouped) == d ** known_count
        assert all(trace(matrix) == Fraction(1, d ** known_count) for matrix in grouped.values())
        full_output = add_density(*grouped.values())
        expected_fidelity = Fraction(1, d ** (n - 2 - known_count))
        assert trace(full_output) == 1
        assert ghz_fidelity(full_output, n, d) == expected_fidelity
        results.append({
            "name": f"private_star_syndromes_known_{known_count}",
            "outputs": n,
            "local_dimension": d,
            "fine_local_histories": len(simulation.branches),
            "communicated_transcripts": len(grouped),
            "global_fidelity": str(expected_fidelity),
            "arithmetic": "exact rational density matrices",
        })
    return results


def check_one_bit_success_flag() -> dict:
    n, d = 5, 2
    simulation = simulate_tree(star(n), d, correct_steps=set())
    accepted: Density = {}
    failed: Density = {}
    rejected_histories = 0
    for history, matrix in output_branches(simulation):
        if not any(history):
            accepted = add_density(accepted, matrix)
        else:
            # The public failure bit instructs every party to discard its
            # output and prepare |0>. The fine syndrome remains private.
            failed = add_density(failed, zero_density(n, trace(matrix)))
            rejected_histories += 1
    success_probability = trace(accepted)
    assert accepted == ghz_density(n, d, success_probability)
    assert success_probability == Fraction(1, 8)
    full_output = add_density(accepted, failed)
    assert trace(full_output) == 1
    assert ghz_fidelity(full_output, n, d) == Fraction(9, 16)
    return {
        "name": "one_bit_coarse_success_flag",
        "fine_local_histories": len(simulation.branches),
        "communicated_transcripts": 2,
        "private_histories_in_failure_map": rejected_histories,
        "success_probability": str(success_probability),
        "conditional_success_fidelity": "1",
        "unconditional_fidelity": "9/16",
        "arithmetic": "exact rational density matrices",
    }


def check_discarded_hub(output_leaves: int) -> dict:
    simulation = simulate_tree(star(output_leaves + 1), 2)
    hub_register = simulation.outputs[0]
    leaf_registers = simulation.outputs[1:]
    denominator = 2 * simulation.denominator
    corrected: list[Density] = []
    phase_unreported: list[Density] = []
    for _, vector in simulation.branches:
        after_fourier = hadamard(vector, hub_register)
        for phase, selected in measure(after_fourier, hub_register).items():
            phase_unreported.append(reduced_density(selected, leaf_registers, denominator))
            fixed = phase_z(selected, leaf_registers[0], phase)
            matrix = reduced_density(fixed, leaf_registers, denominator)
            assert matrix == ghz_density(output_leaves, 2, Fraction(1, 2 ** output_leaves))
            corrected.append(matrix)
    assert len(corrected) == 2 ** output_leaves
    full_output = add_density(*corrected)
    assert full_output == ghz_density(output_leaves, 2)
    forgotten_phase = add_density(*phase_unreported)
    assert trace(forgotten_phase) == 1
    assert ghz_fidelity(forgotten_phase, output_leaves, 2) == Fraction(1, 2)
    return {
        "name": f"discarded_hub_{output_leaves}_leaves",
        "output_leaves": output_leaves,
        "source_edges": output_leaves,
        "syndrome_bits": output_leaves - 1,
        "phase_bits": 1,
        "transcripts": len(corrected),
        "global_fidelity": "1",
        "fidelity_if_phase_is_unreported": "1/2",
        "arithmetic": "exact rational density matrices",
    }


def check_randomized_abort() -> dict:
    n, k, d = 4, 2, 4
    simulation = simulate_tree(star(n), d)
    exact_output = add_density(*(matrix for _, matrix in output_branches(simulation)))
    q = Fraction(1, 4)
    mixed_output = add_density(scale_density(exact_output, q), zero_density(n, 1 - q))
    exact_cost = k * (n - 2)
    assert trace(mixed_output) == 1
    assert ghz_fidelity(mixed_output, n, d) == Fraction(7, 16)
    return {
        "name": "shared_seed_randomized_abort",
        "outputs": n,
        "qubit_ghz_copies": k,
        "exact_run_probability": str(q),
        "worst_case_bits": exact_cost,
        "expected_bits": str(q * exact_cost),
        "global_fidelity": "7/16",
        "arithmetic": "exact rational density matrices",
    }


def check_complex_finner_example() -> dict:
    """Triangle of Bell pairs with genuinely complex entangled local effects."""
    def bell_effect(phase: complex) -> list[list[complex]]:
        effect = [[0j for _ in range(4)] for _ in range(4)]
        effect[0][0] = effect[3][3] = 0.5
        effect[0][3] = phase.conjugate() / 2
        effect[3][0] = phase / 2
        return effect

    effects = [bell_effect(1j), bell_effect(-1j), bell_effect(1 + 0j)]
    edge_values = list(itertools.product((0, 1), repeat=3))

    def local_indices(values: tuple[int, int, int]) -> tuple[int, int, int]:
        ab, bc, ca = values
        return 2 * ab + ca, 2 * ab + bc, 2 * bc + ca

    probability = 0j
    for bra_edges in edge_values:
        bra_indices = local_indices(bra_edges)
        for ket_edges in edge_values:
            ket_indices = local_indices(ket_edges)
            probability += math.prod(
                effect[bra][ket]
                for effect, bra, ket in zip(effects, bra_indices, ket_indices)
            ) / 8

    marginals = [sum(effect[i][i].real for i in range(4)) / 4 for effect in effects]
    bound = math.sqrt(math.prod(marginals))
    correct_squared_norms = [sum(abs(z) ** 2 for row in effect for z in row) / 4 for effect in effects]
    incorrect_plain_squares = [sum(z ** 2 for row in effect for z in row) / 4 for effect in effects]
    assert abs(probability.imag) <= 1e-14
    assert probability.real == 1 / 16
    assert bound == 1 / 8 and probability.real <= bound
    assert correct_squared_norms == [1 / 4] * 3
    assert incorrect_plain_squares[0] == incorrect_plain_squares[1] == 0
    assert probability.real > 0
    return {
        "name": "complex_triangle_event_finner",
        "source": "three independent Bell pairs",
        "local_effects": "projectors onto (|00>+phase|11>)/sqrt(2), phases i,-i,1",
        "event_probability": probability.real,
        "local_event_probabilities": marginals,
        "finner_bound": bound,
        "correct_squared_norms": correct_squared_norms,
        "incorrect_plain_square_norms": [value.real for value in incorrect_plain_squares],
        "plain_square_rhs_would_incorrectly_be_zero": True,
        "arithmetic": "binary-exact complex entries; scalar diagnostic tolerance 1e-14",
    }


def run_checks() -> dict:
    cases = [
        ("star_n2_d2", star(2), 2),
        ("star_n4_d2", star(4), 2),
        ("star_n4_d3", star(4), 3),
        ("star_n5_d2", star(5), 2),
        ("path_n5_d2", path(5), 2),
        ("path_n4_d3", path(4), 3),
        ("branched_tree_n6_d2", ((0, 1), (1, 2), (1, 3), (3, 4), (3, 5)), 2),
    ]
    checks = [check_exact_tree(name, edges, d) for name, edges, d in cases]
    checks.extend(check_partial_star_corrections())
    checks.append(check_one_bit_success_flag())
    checks.extend(check_discarded_hub(leaves) for leaves in (2, 3))
    checks.append(check_randomized_abort())
    checks.append(check_complex_finner_example())
    return {
        "schema_version": 1,
        "status": "passed",
        "python_version": platform.python_version(),
        "check_count": len(checks),
        "checks": checks,
        "scope": (
            "Finite physical register-map checks and a complex-event diagnostic. "
            "They do not prove the arbitrary-dimension Finner inequality, "
            "the transcript factorization theorem, or the entropy converses."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-results", type=Path, help="Write the successful check report as JSON.")
    args = parser.parse_args()
    report = run_checks()
    for check in report["checks"]:
        print(f"PASS {check['name']}")
    print(f"All {report['check_count']} finite physical checks passed.")
    if args.write_results is not None:
        args.write_results.parent.mkdir(parents=True, exist_ok=True)
        args.write_results.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"Results written to {args.write_results}")


if __name__ == "__main__":
    main()
