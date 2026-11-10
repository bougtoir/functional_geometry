import importlib.util
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "eq", Path(__file__).resolve().parents[1] / "scripts" / "check_equivalence_propositions.py")
eq = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(eq)


def test_nested_refinement_never_increases_supply():
    assert eq.check_nested_refinement()["violations"] == 0


def test_overage_bounded_by_unit():
    assert eq.check_overage_bound()["violations"] == 0


def test_non_nested_refinement_can_increase_supply():
    example = next(e for e in eq.non_nested_counterexamples() if (e["coarse_unit"], e["finer_unit"]) == (3, 2))
    assert example["requirement"] == 3 and example["supplied_finer"] == 4 and example["supplied_coarse"] == 3


def test_grid_reduction_and_denomination_special_case():
    assert eq.check_grid_product_reduction(max_side=12)["violations"] == 0
    assert eq.check_single_size_equals_denomination()["mismatches"] == 0
