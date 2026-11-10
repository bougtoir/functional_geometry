"""Exhaustive checks of the reduction claims in 04_MATHEMATICAL_EQUIVALENCE_AUDIT.md.

Not a new model: verifies, on integer grids, the textbook properties that make
the rational-choice FUGD problem a special case of the overage/denomination
(vial-size, assortment) problem. Writes results/equivalence_checks.json.
"""
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def supplied_rational(requirement, unit):
    """Rational user takes the fewest whole units covering the requirement."""
    return unit * math.ceil(requirement / unit)


def min_cover_with_denominations(requirement, units):
    """Smallest attainable supply >= requirement from non-negative unit combinations."""
    bound = requirement + max(units)
    reachable = [False] * (bound + 1)
    reachable[0] = True
    for value in range(1, bound + 1):
        reachable[value] = any(value >= u and reachable[value - u] for u in units)
    return next(v for v in range(requirement, bound + 1) if reachable[v])


def check_nested_refinement(max_requirement=240, base_units=(2, 3, 4, 6, 8, 12, 24)):
    violations = 0
    comparisons = 0
    for unit in base_units:
        for divisor in range(2, unit + 1):
            if unit % divisor:
                continue
            fine = unit // divisor
            for requirement in range(1, max_requirement + 1):
                comparisons += 1
                if supplied_rational(requirement, fine) > supplied_rational(requirement, unit):
                    violations += 1
    return {"comparisons": comparisons, "violations": violations}


def check_overage_bound(max_requirement=240, units=range(1, 25)):
    violations = 0
    for unit in units:
        for requirement in range(1, max_requirement + 1):
            overage = supplied_rational(requirement, unit) - requirement
            if not 0 <= overage < unit:
                violations += 1
    return {"violations": violations}


def non_nested_counterexamples(max_requirement=60):
    examples = []
    for coarse, fine in itertools.permutations(range(2, 9), 2):
        if fine >= coarse or coarse % fine == 0:
            continue
        for requirement in range(1, max_requirement + 1):
            if supplied_rational(requirement, fine) > supplied_rational(requirement, coarse):
                examples.append({"coarse_unit": coarse, "finer_unit": fine, "requirement": requirement,
                                 "supplied_coarse": supplied_rational(requirement, coarse),
                                 "supplied_finer": supplied_rational(requirement, fine)})
                break
    return examples


def check_grid_product_reduction(max_side=30, cells=((1, 1), (2, 3), (3, 5), (4, 4))):
    """Rectangular task w x l on an aligned a x b perforation grid = product of two 1-D roundings."""
    violations = 0
    for a, b in cells:
        for width in range(1, max_side + 1):
            for length in range(1, max_side + 1):
                brute = min(i * a * j * b for i in range(1, max_side + 2) for j in range(1, max_side + 2)
                            if i * a >= width and j * b >= length)
                if brute != supplied_rational(width, a) * supplied_rational(length, b):
                    violations += 1
    return {"violations": violations}


def check_single_size_equals_denomination(max_requirement=120, units=(5, 7, 12)):
    mismatches = 0
    for unit in units:
        for requirement in range(1, max_requirement + 1):
            if min_cover_with_denominations(requirement, (unit,)) != supplied_rational(requirement, unit):
                mismatches += 1
    return {"mismatches": mismatches}


def main():
    results = {
        "P1_nested_refinement_weakly_reduces_supply": check_nested_refinement(),
        "P2_overage_in_[0,unit)": check_overage_bound(),
        "P3_non_nested_refinement_counterexamples_first_per_pair": non_nested_counterexamples(),
        "P4_aligned_grid_rectangle_equals_product_of_1d_roundings": check_grid_product_reduction(),
        "P5_single_unit_size_is_denomination_special_case": check_single_size_equals_denomination(),
    }
    out = ROOT / "results" / "equivalence_checks.json"
    out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: (v if not isinstance(v, list) else f"{len(v)} counterexample pairs") for k, v in results.items()}, indent=2))


if __name__ == "__main__":
    main()
