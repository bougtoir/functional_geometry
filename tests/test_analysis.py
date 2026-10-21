import csv
import copy
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from fgo_model import (  # noqa: E402
    center_perforation_material_ratio,
    exact_hollow_cylinder_mass_g,
    max_integer_pack,
    straw_expected_replacement_rate_break_even,
    straw_failure_probability_break_even,
    straw_material_ratio_expected_rate,
    straw_material_ratio_failure_probability,
    toilet_width_saving,
)
from build_submission import (  # noqa: E402
    format_value,
    latex_to_linear_math,
    resolve_citations,
    substitute_values,
)
from analyze_patent_width_compensation import (  # noqa: E402
    build_contrasts,
    load_rows,
)
from run_analysis import (  # noqa: E402
    regenerate_patent_contrasts,
    straw_boundary_values,
)
from run_qc import (  # noqa: E402
    expected_width_scenario_phrase,
    has_exact_unique_ids,
)
from fgo_model import load_config  # noqa: E402
import acquire_public_sources  # noqa: E402
from acquire_public_sources import retrieve, write_snapshot  # noqa: E402


def test_width_break_even_at_elasticity_minus_one():
    assert math.isclose(toilet_width_saving(95, 114, -1), 0.0, abs_tol=1e-12)


def test_width_zero_compensation_matches_width_reduction():
    assert math.isclose(toilet_width_saving(95, 114, 0), 1 - 95 / 114)


def test_center_perforation_never_assumes_half_saving():
    ratio = center_perforation_material_ratio(0.5, 1.2)
    assert math.isclose(ratio, 0.8)


def test_straw_expected_replacement_rate_break_even():
    for reduction in (0.1, 0.2, 0.3):
        for shifted_burden in (0.0, 0.05):
            boundary = straw_expected_replacement_rate_break_even(
                reduction,
                shifted_burden,
            )
            assert math.isclose(
                straw_material_ratio_expected_rate(
                    reduction,
                    boundary,
                    shifted_burden,
                ),
                1.0,
            )
            assert math.isclose(
                boundary,
                (1.0 - shifted_burden) / (1.0 - reduction) - 1.0,
            )


def test_straw_independent_failure_probability_break_even():
    for reduction in (0.1, 0.2, 0.3):
        for shifted_burden in (0.0, 0.05):
            boundary = straw_failure_probability_break_even(
                reduction,
                shifted_burden,
            )
            assert math.isclose(
                straw_material_ratio_failure_probability(
                    reduction,
                    boundary,
                    shifted_burden,
                ),
                1.0,
            )
            assert math.isclose(
                boundary,
                1.0 - (1.0 - reduction) / (1.0 - shifted_burden),
            )


def test_straw_shifted_burden_break_even_under_both_formulations():
    shifted_burden = 0.05
    for reduction in (0.1, 0.2, 0.3):
        expected_rate = straw_expected_replacement_rate_break_even(
            reduction,
            shifted_burden,
        )
        failure_probability = straw_failure_probability_break_even(
            reduction,
            shifted_burden,
        )
        assert math.isclose(
            straw_material_ratio_expected_rate(
                reduction,
                expected_rate,
                shifted_burden,
            ),
            1.0,
        )
        assert math.isclose(
            straw_material_ratio_failure_probability(
                reduction,
                failure_probability,
                shifted_burden,
            ),
            1.0,
        )


def test_primary_straw_boundaries_follow_the_configured_reduction():
    config = load_config(ROOT / "config/scenarios.json")
    changed = copy.deepcopy(config)
    changed["straw"]["primary_length_reduction_fraction"] = 0.3
    straw = pd.DataFrame(
        [
            {
                "length_reduction_fraction": reduction,
                "expected_additional_replacement_rate_break_even_zero_shift": (
                    straw_expected_replacement_rate_break_even(reduction)
                ),
                "independent_failure_probability_break_even_zero_shift": (
                    straw_failure_probability_break_even(reduction)
                ),
            }
            for reduction in (0.1, 0.2, 0.3)
        ]
    )
    values = straw_boundary_values(changed, straw)
    assert math.isclose(values["primary_expected_rate"], 3 / 7)
    assert math.isclose(values["primary_failure_probability"], 0.3)
    assert math.isclose(values["fixed_expected_rates"][0.2], 0.25)


def test_primary_straw_reduction_must_be_reported():
    config = load_config(ROOT / "config/scenarios.json")
    changed = copy.deepcopy(config)
    changed["straw"]["primary_length_reduction_fraction"] = 0.25
    straw = pd.DataFrame(
        [
            {
                "length_reduction_fraction": reduction,
                "expected_additional_replacement_rate_break_even_zero_shift": (
                    straw_expected_replacement_rate_break_even(reduction)
                ),
                "independent_failure_probability_break_even_zero_shift": (
                    straw_failure_probability_break_even(reduction)
                ),
            }
            for reduction in (0.1, 0.2, 0.3)
        ]
    )
    with pytest.raises(
        ValueError,
        match="primary_length_reduction_fraction must be included",
    ):
        straw_boundary_values(changed, straw)


def test_patent_table_2_transcription_matches_primary_values():
    expected = [
        (28, 4.5, 0.25, 3.1, 0.0072),
        (28, 5.75, 0.32, 2.6, 0.0078),
        (28, 7.0, 0.39, 1.8, 0.0065),
        (44, 4.5, 0.25, 2.6, 0.0095),
        (44, 5.75, 0.32, 2.0, 0.0094),
        (44, 7.0, 0.39, 1.6, 0.0091),
        (70, 4.5, 0.25, 1.9, 0.0111),
        (70, 5.75, 0.32, 1.8, 0.0134),
        (70, 7.0, 0.39, 1.5, 0.0136),
    ]
    rows = load_rows()
    actual = [
        (
            row["basis_weight_lb_per_3000ft2"],
            row["width_in"],
            row["sheet_area_ft2"],
            row["sheets_per_task"],
            row["total_usage_lb_per_task"],
        )
        for row in rows
    ]
    assert actual == expected
    assert all(row["source_location"] == "US6458450B1 Table 2" for row in rows)
    assert all(
        row["evidence_strength"] == "WEAK_PATENT_REPORTED_NON_POPULATION"
        for row in rows
    )


def test_patent_contrasts_use_reported_total_usage_in_narrow_over_wide_direction():
    contrasts = build_contrasts(load_rows())
    assert len(contrasts) == 9
    savings = [float(row["material_saving_fraction"]) for row in contrasts]
    assert sum(value > 0 for value in savings) == 4
    assert sum(value < 0 for value in savings) == 5
    assert math.isclose(min(savings), -0.2, abs_tol=5e-7)
    assert math.isclose(max(savings), 0.183824, abs_tol=5e-7)
    first = contrasts[0]
    assert math.isclose(
        float(first["reported_total_usage_ratio"]),
        0.0072 / 0.0078,
        abs_tol=5e-7,
    )
    assert math.isclose(
        float(first["material_saving_fraction"]),
        1 - 0.0072 / 0.0078,
        abs_tol=5e-7,
    )


def test_patent_contrasts_are_regenerated_from_observed_inputs(tmp_path):
    output = tmp_path / "patent_contrasts.csv"
    expected = regenerate_patent_contrasts(output)
    with output.open(newline="", encoding="utf-8") as handle:
        stored = list(csv.DictReader(handle))
    assert stored == expected


def test_audit_coverage_requires_exact_unique_ids():
    expected = {"A", "B"}
    assert has_exact_unique_ids(
        [{"identifier": "A"}, {"identifier": "B"}],
        "identifier",
        expected,
    )
    assert not has_exact_unique_ids([], "identifier", expected)
    assert not has_exact_unique_ids(
        [{"identifier": "A"}],
        "identifier",
        expected,
    )
    assert not has_exact_unique_ids(
        [{"identifier": "A"}, {"identifier": "A"}, {"identifier": "B"}],
        "identifier",
        expected,
    )
    assert not has_exact_unique_ids(
        [{"identifier": "A"}, {"identifier": "B"}, {"identifier": "C"}],
        "identifier",
        expected,
    )


def test_width_scenario_phrase_uses_configured_dimensions():
    config = load_config(ROOT / "config/scenarios.json")
    changed = copy.deepcopy(config)
    changed["toilet_width"]["primary_candidate_width_mm"] = 90.0
    assert (
        expected_width_scenario_phrase(changed)
        == "illustrative 114-to-90-mm reference scenario"
    )


def test_manuscript_separates_fixed_primary_and_logistics_scenarios():
    template = (ROOT / "manuscript/manuscript_template.md").read_text(
        encoding="utf-8"
    )
    assert (
        "shortening by {{pct:straw_10pct_length_reduction}}, "
        "{{pct:straw_20pct_length_reduction}}, and "
        "{{pct:straw_30pct_length_reduction}}"
    ) in template
    assert (
        "The configured primary case was "
        "{{pct:straw_primary_length_reduction}}"
    ) in template
    assert "{{pct:logistics_mid_length_reduction}} reduction" in template


def test_short_packing_length_preserves_canonical_decimal():
    assert format_value("num1", 115.5) == "115.5"
    rendered = substitute_values(
        "{{num1:logistics_short_length_mm}}",
        {"logistics_short_length_mm": 115.5},
    )
    assert rendered == "115.5"


def test_exact_hollow_cylinder_mass_positive_and_length_proportional():
    short = exact_hollow_cylinder_mass_g(6, 0.2, 100, 0.92)
    long = exact_hollow_cylinder_mass_g(6, 0.2, 165, 0.92)
    assert short > 0
    assert math.isclose(long / short, 1.65)


def test_integer_pack_searches_orientations():
    count, orientation = max_integer_pack([400, 300, 250], [165, 20, 20])
    assert count > 0
    assert sorted(orientation) == [20, 20, 165]


def test_vectorized_width_saving():
    values = toilet_width_saving(np.array([95, 100]), 114, -0.35)
    assert values.shape == (2,)
    assert np.all(values > 0)


def test_latex_equations_are_converted_to_readable_linear_math():
    rendered = latex_to_linear_math(
        r"\Delta_M=1-\frac{E[M_k\mid\text{success}]}{E[M_0]}"
    )
    assert rendered == "Δ_M=1-(E[M_k∣success])/(E[M_0])"
    assert "\\" not in rendered


def test_citations_render_as_author_year():
    references = {
        "later": {
            "author": "Zulu et al.",
            "year": "2022",
            "reference": "Zulu Z. Later reference. 2022.",
        },
        "earlier": {
            "author": "Alpha and Beta",
            "year": "2020",
            "reference": "Alpha A, Beta B. Earlier reference. 2020.",
        },
    }
    rendered, order = resolve_citations(
        "Claim {cite:later,earlier}.", references
    )
    assert rendered == "Claim (Alpha and Beta, 2020; Zulu et al., 2022)."
    assert order == ["later", "earlier"]


def test_same_second_snapshots_never_overwrite(tmp_path):
    retrieved_at = datetime(2026, 9, 24, 7, 31, tzinfo=timezone.utc)
    first = write_snapshot(
        tmp_path, "source", ".txt", b"first", retrieved_at
    )
    second = write_snapshot(
        tmp_path, "source", ".txt", b"second", retrieved_at
    )
    assert first != second
    assert first.read_bytes() == b"first"
    assert second.read_bytes() == b"second"


def test_retrieval_uses_runtime_utc_date(monkeypatch, tmp_path):
    class FakeResponse:
        status = 200
        headers = {"Content-Type": "text/plain"}

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            return False

        def read(self):
            return b"snapshot"

        def geturl(self):
            return "https://example.org/source.txt"

    monkeypatch.setattr(acquire_public_sources, "ROOT", tmp_path)
    monkeypatch.setattr(
        acquire_public_sources.urllib.request,
        "urlopen",
        lambda request, timeout: FakeResponse(),
    )
    retrieved_at = datetime(
        2027, 1, 2, 3, 4, 5, 6000, tzinfo=timezone.utc
    )
    record = retrieve(
        "source",
        "https://example.org/source",
        tmp_path / "data/raw/sources",
        retrieved_at,
    )
    assert record["access_date"] == "2027-01-02"
    assert record["retrieved_utc"] == retrieved_at.isoformat()
    assert "2027-01-02" in record["local_path"]
