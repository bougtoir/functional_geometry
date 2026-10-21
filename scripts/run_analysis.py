#!/usr/bin/env python3

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from analyze_patent_width_compensation import (
    build_contrasts,
    load_rows,
    write_contrasts,
)
from fgo_model import (
    center_perforation_break_even_probability,
    center_perforation_material_ratio,
    convergence_diagnostics,
    exact_hollow_cylinder_mass_g,
    load_config,
    longitudinal_break_even_ratio,
    max_integer_pack,
    run_monte_carlo,
    straw_expected_replacement_rate_break_even,
    straw_failure_probability_break_even,
    straw_material_ratio_expected_rate,
    straw_material_ratio_failure_probability,
    summarize_simulation,
    toilet_width_saving,
)


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config/scenarios.json"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
TABLES = ROOT / "tables"
PROCESSED = ROOT / "data/processed"

COLORS = {
    "blue": "#1f5a7a",
    "green": "#2f7d57",
    "orange": "#d17a22",
    "red": "#b13e3e",
    "gray": "#66717e",
    "light": "#edf2f4",
}


def setup():
    for directory in (RESULTS, FIGURES, TABLES):
        directory.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.titlesize": 11,
            "axes.labelsize": 9,
            "figure.dpi": 160,
            "savefig.dpi": 400,
            "savefig.bbox": "tight",
        }
    )


def regenerate_patent_contrasts(output=None):
    contrasts = build_contrasts(load_rows())
    if output is None:
        write_contrasts(contrasts)
    else:
        write_contrasts(contrasts, output)
    return contrasts


def save_figure(figure, name):
    for suffix in ("png", "pdf", "svg"):
        path = FIGURES / f"{name}.{suffix}"
        figure.savefig(path)
        if suffix == "svg":
            lines = path.read_text(encoding="utf-8").splitlines()
            path.write_text(
                "\n".join(line.rstrip() for line in lines) + "\n",
                encoding="utf-8",
            )
    plt.close(figure)


def width_tables(config):
    width = config["toilet_width"]
    rows = []
    for candidate in width["candidate_widths_mm"]:
        ratio = candidate / width["baseline_width_mm"]
        rows.append(
            {
                "baseline_width_mm": width["baseline_width_mm"],
                "candidate_width_mm": candidate,
                "width_reduction_fraction": 1.0 - ratio,
                "break_even_longitudinal_ratio": longitudinal_break_even_ratio(
                    candidate,
                    width["baseline_width_mm"],
                ),
                "saving_zero_compensation": toilet_width_saving(
                    candidate,
                    width["baseline_width_mm"],
                    0.0,
                ),
                "saving_moderate_compensation_elasticity_minus_0_35": toilet_width_saving(
                    candidate,
                    width["baseline_width_mm"],
                    -0.35,
                ),
                "saving_break_even_elasticity_minus_1": toilet_width_saving(
                    candidate,
                    width["baseline_width_mm"],
                    -1.0,
                ),
            }
        )
    frame = pd.DataFrame(rows)
    frame.to_csv(TABLES / "table_2_width_scenarios.csv", index=False)
    return frame


def center_tables(config):
    perforation = config["center_perforation"]
    rows = []
    for probability in perforation["reported_task_mix_scenarios"]:
        ratio = center_perforation_material_ratio(
            probability,
            perforation["reported_half_task_multiplier"],
        )
        rows.append(
            {
                "half_suitable_task_probability": probability,
                "half_task_unit_multiplier": perforation[
                    "reported_half_task_multiplier"
                ],
                "material_ratio_before_penalties": ratio,
                "material_saving_before_penalties": 1.0 - ratio,
            }
        )
    frame = pd.DataFrame(rows)
    frame.to_csv(TABLES / "table_3_center_perforation_scenarios.csv", index=False)
    return frame


def straw_tables(config):
    rows = []
    for reduction in config["straw"]["reported_length_reductions"]:
        rows.append(
            {
                "length_reduction_fraction": reduction,
                "material_saving_zero_replacement_zero_shift": reduction,
                "expected_additional_replacement_rate_break_even_zero_shift": (
                    straw_expected_replacement_rate_break_even(reduction)
                ),
                "expected_additional_replacement_rate_break_even_5pct_shift": (
                    straw_expected_replacement_rate_break_even(reduction, 0.05)
                ),
                "independent_failure_probability_break_even_zero_shift": (
                    straw_failure_probability_break_even(reduction)
                ),
                "independent_failure_probability_break_even_5pct_shift": (
                    straw_failure_probability_break_even(reduction, 0.05)
                ),
            }
        )
    frame = pd.DataFrame(rows)
    frame.to_csv(TABLES / "table_4_straw_break_even.csv", index=False)
    return frame


def straw_boundary_values(config, straw):
    reported = np.asarray(
        config["straw"]["reported_length_reductions"],
        dtype=float,
    )
    fixed_reductions = (0.1, 0.2, 0.3)
    if len(reported) != len(np.unique(reported)):
        raise ValueError("reported_length_reductions must be unique")
    for reduction in fixed_reductions:
        if not np.isclose(reported, reduction).any():
            raise ValueError(
                "reported_length_reductions must include 0.1, 0.2, and 0.3"
            )
    primary = float(config["straw"]["primary_length_reduction_fraction"])
    if not np.isclose(reported, primary).any():
        raise ValueError(
            "primary_length_reduction_fraction must be included in "
            "reported_length_reductions"
        )

    reductions = straw["length_reduction_fraction"].to_numpy(dtype=float)

    def boundary(reduction, column):
        matches = straw.loc[np.isclose(reductions, reduction), column]
        if len(matches) != 1:
            raise ValueError(
                f"Expected one straw boundary row for reduction {reduction:g}"
            )
        return float(matches.iloc[0])

    return {
        "primary_expected_rate": boundary(
            primary,
            "expected_additional_replacement_rate_break_even_zero_shift",
        ),
        "primary_failure_probability": boundary(
            primary,
            "independent_failure_probability_break_even_zero_shift",
        ),
        "fixed_expected_rates": {
            reduction: boundary(
                reduction,
                "expected_additional_replacement_rate_break_even_zero_shift",
            )
            for reduction in fixed_reductions
        },
        "fixed_failure_probabilities": {
            reduction: boundary(
                reduction,
                "independent_failure_probability_break_even_zero_shift",
            )
            for reduction in fixed_reductions
        },
    }


def logistics_table(config):
    carton = config["logistics"]["illustrative_carton_internal_mm"]
    other = config["logistics"]["illustrative_unit_other_dimensions_mm"]
    rows = []
    for length in config["logistics"]["illustrative_straw_lengths_mm"]:
        count, orientation = max_integer_pack(carton, [length, *other])
        rows.append(
            {
                "scenario_status": "HYPOTHETICAL_INTEGER_PACKING_EXAMPLE",
                "unit_length_mm": length,
                "unit_width_mm": other[0],
                "unit_height_mm": other[1],
                "units_per_carton": count,
                "best_orientation_mm": "x".join(f"{value:g}" for value in orientation),
                "carton_internal_mm": "x".join(f"{value:g}" for value in carton),
            }
        )
    frame = pd.DataFrame(rows)
    frame.to_csv(TABLES / "table_5_logistics_integer_packing.csv", index=False)
    return frame


def simulation_outputs(config):
    simulations = run_monte_carlo(config)
    summary_rows = []
    convergence_rows = []
    for case, values in simulations.items():
        summary_rows.append({"case": case, **summarize_simulation(values)})
        for row in convergence_diagnostics(
            values,
            [10000, 50000, 100000, config["monte_carlo_iterations"]],
        ):
            convergence_rows.append({"case": case, **row})
        pd.DataFrame({"material_saving_fraction": values}).to_csv(
            RESULTS / f"monte_carlo_{case}.csv.gz",
            index=False,
            compression={"method": "gzip", "mtime": 0},
        )
    summary = pd.DataFrame(summary_rows)
    convergence = pd.DataFrame(convergence_rows)
    summary.to_csv(TABLES / "table_6_monte_carlo_summary.csv", index=False)
    convergence.to_csv(RESULTS / "monte_carlo_convergence.csv", index=False)
    return simulations, summary


def sensitivity_table(config):
    width = config["toilet_width"]
    candidate = width["primary_candidate_width_mm"]
    baseline = width["baseline_width_mm"]
    rows = []
    for elasticity in np.linspace(-1.25, 0.25, 7):
        rows.append(
            {
                "case": "toilet_width",
                "parameter": "width_compensation_elasticity",
                "value": elasticity,
                "material_saving_fraction": toilet_width_saving(
                    candidate,
                    baseline,
                    elasticity,
                ),
            }
        )
    for probability in np.linspace(0.0, 1.0, 6):
        rows.append(
            {
                "case": "center_perforation",
                "parameter": "half_suitable_task_probability",
                "value": probability,
                "material_saving_fraction": 1.0
                - center_perforation_material_ratio(probability, 1.2),
            }
        )
    for replacement_rate in config["straw"][
        "reported_expected_additional_replacement_rates"
    ]:
        rows.append(
            {
                "case": "straw_expected_rate",
                "parameter": "expected_additional_replacement_rate",
                "value": replacement_rate,
                "material_saving_fraction": 1.0
                - straw_material_ratio_expected_rate(
                    config["straw"]["primary_length_reduction_fraction"],
                    replacement_rate,
                    0.0,
                ),
            }
        )
    for failure_probability in config["straw"][
        "reported_failure_probabilities"
    ]:
        rows.append(
            {
                "case": "straw_failure_probability",
                "parameter": "independent_per_attempt_failure_probability",
                "value": failure_probability,
                "material_saving_fraction": 1.0
                - straw_material_ratio_failure_probability(
                    config["straw"]["primary_length_reduction_fraction"],
                    failure_probability,
                    0.0,
                ),
            }
        )
    frame = pd.DataFrame(rows)
    frame.to_csv(RESULTS / "one_way_sensitivity.csv", index=False)
    return frame


def figure_framework():
    figure, axis = plt.subplots(figsize=(7.2, 4.2))
    axis.axis("off")
    nodes = [
        (0.08, 0.66, "Observed geometry\nand source data", COLORS["blue"]),
        (0.34, 0.66, "Functional constraints\nand task demand", COLORS["green"]),
        (0.60, 0.66, "Counterfactual\ngeometry", COLORS["orange"]),
        (0.34, 0.22, "Rebound, failure,\nand shifted burden", COLORS["red"]),
        (0.73, 0.22, "Material per\nsuccessful service", COLORS["blue"]),
    ]
    for x, y, label, color in nodes:
        axis.text(
            x,
            y,
            label,
            ha="center",
            va="center",
            color="white",
            fontweight="bold",
            bbox={"boxstyle": "round,pad=0.7", "fc": color, "ec": "none"},
            transform=axis.transAxes,
        )
    arrows = [
        ((0.18, 0.66), (0.24, 0.66)),
        ((0.44, 0.66), (0.50, 0.66)),
        ((0.64, 0.57), (0.45, 0.31)),
        ((0.66, 0.57), (0.72, 0.31)),
        ((0.47, 0.22), (0.62, 0.22)),
    ]
    for start, end in arrows:
        axis.annotate(
            "",
            xy=end,
            xytext=start,
            xycoords="axes fraction",
            arrowprops={"arrowstyle": "->", "lw": 1.8, "color": COLORS["gray"]},
        )
    axis.text(
        0.5,
        0.94,
        "Functional geometry optimization evaluates dimensions against service",
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold",
        transform=axis.transAxes,
    )
    axis.text(
        0.5,
        0.04,
        "Benefit is conditional until adequacy, acceptance, and logistics are retained.",
        ha="center",
        color=COLORS["gray"],
        transform=axis.transAxes,
    )
    save_figure(figure, "figure_1_fgo_framework")


def figure_width(config):
    baseline = config["toilet_width"]["baseline_width_mm"]
    widths = np.linspace(70, baseline, 180)
    elasticities = np.linspace(-1.5, 0.5, 180)
    mesh_width, mesh_elasticity = np.meshgrid(widths, elasticities)
    savings = toilet_width_saving(mesh_width, baseline, mesh_elasticity)
    figure, axis = plt.subplots(figsize=(7.2, 4.6))
    image = axis.contourf(
        mesh_width,
        mesh_elasticity,
        100 * savings,
        levels=np.linspace(-40, 40, 17),
        cmap="RdYlGn",
        extend="both",
    )
    axis.contour(
        mesh_width,
        mesh_elasticity,
        savings,
        levels=[0],
        colors="black",
        linewidths=2,
    )
    axis.axhline(-1, color="black", linestyle="--", linewidth=1)
    axis.set(
        xlabel="Candidate width (mm)",
        ylabel="Width-compensation elasticity",
        title="Toilet-paper material saving before acceptance and process penalties",
    )
    colorbar = figure.colorbar(image, ax=axis)
    colorbar.set_label("Material saving (%)")
    axis.text(
        72,
        -0.94,
        "Break-even: elasticity = −1",
        fontsize=8,
        bbox={"fc": "white", "ec": "none", "alpha": 0.8},
    )
    save_figure(figure, "figure_2_width_compensation_surface")


def figure_patent_and_perforation(config):
    patent = pd.read_csv(PROCESSED / "pg_patent_table2_width_contrasts.csv")
    probabilities = np.linspace(0, 1, 101)
    multipliers = [1.0, 1.2, 1.5, 2.0]
    figure, axes = plt.subplots(1, 2, figsize=(7.4, 3.6))
    axes[0].axhline(0, color="black", linewidth=1)
    axes[0].scatter(
        100 * (1.0 - patent["width_ratio"]),
        100 * patent["material_saving_fraction"],
        color=COLORS["blue"],
        s=30,
    )
    axes[0].set(
        xlabel="Width reduction (%)",
        ylabel="Calculated material saving (%)",
        title="Patent table contrasts",
    )
    axes[0].text(
        0.03,
        0.03,
        "Weak, non-population evidence",
        transform=axes[0].transAxes,
        fontsize=8,
        color=COLORS["gray"],
    )
    for multiplier in multipliers:
        saving = 1.0 - center_perforation_material_ratio(
            probabilities,
            multiplier,
        )
        axes[1].plot(
            probabilities,
            100 * saving,
            label=f"half-task units = {multiplier:g}",
        )
    axes[1].axhline(0, color="black", linewidth=1)
    axes[1].set(
        xlabel="Share of tasks suitable for half width",
        ylabel="Material saving (%)",
        title="Center-perforation task mixtures",
    )
    axes[1].legend(fontsize=7, frameon=False)
    figure.tight_layout()
    save_figure(figure, "figure_3_observed_contrasts_and_perforation")


def figure_straw_and_logistics(config, logistics):
    reductions = np.linspace(0.01, 0.4, 160)
    shifted = [0.0, 0.025, 0.05, 0.1]
    figure, axes = plt.subplots(1, 2, figsize=(7.4, 3.6))
    for burden in shifted:
        break_even = [
            straw_expected_replacement_rate_break_even(value, burden)
            for value in reductions
        ]
        axes[0].plot(
            100 * reductions,
            100 * np.asarray(break_even),
            label=f"shifted burden = {100 * burden:g}%",
        )
    axes[0].set(
        xlabel="Length reduction (%)",
        ylabel="Expected additional replacement rate at break-even (%)",
        title="Straw shortening expected-rate boundary",
        ylim=(-5, 70),
    )
    axes[0].legend(fontsize=7, frameon=False)
    axes[1].bar(
        logistics["unit_length_mm"].astype(str),
        logistics["units_per_carton"],
        color=[COLORS["gray"], COLORS["blue"], COLORS["green"]],
    )
    axes[1].set(
        xlabel="Illustrative packed unit length (mm)",
        ylabel="Units per carton",
        title="Integer packing creates step changes",
    )
    axes[1].text(
        0.03,
        0.03,
        "Hypothetical dimensions; not a market estimate",
        transform=axes[1].transAxes,
        fontsize=7,
        color=COLORS["gray"],
    )
    figure.tight_layout()
    save_figure(figure, "figure_4_straw_and_logistics_boundaries")


def figure_simulations(simulations):
    figure, axes = plt.subplots(1, 3, figsize=(7.5, 3.2), sharey=True)
    labels = {
        "toilet_width": "Narrower fixed width",
        "center_perforation": "Center perforation",
        "straw": "Primary straw shortening",
    }
    colors = [COLORS["blue"], COLORS["green"], COLORS["orange"]]
    for axis, (case, values), color in zip(axes, simulations.items(), colors):
        axis.hist(
            100 * values,
            bins=80,
            density=True,
            color=color,
            alpha=0.82,
        )
        axis.axvline(0, color="black", linewidth=1)
        axis.set(
            xlabel="Material saving (%)",
            title=labels[case],
        )
    axes[0].set_ylabel("Scenario density")
    figure.suptitle(
        "Illustrative uncertainty distributions (not empirical probabilities)",
        fontweight="bold",
    )
    figure.tight_layout()
    save_figure(figure, "figure_5_scenario_uncertainty")


def value_registry(config, width, center, straw, simulations):
    width_primary = width.loc[
        width["candidate_width_mm"]
        == config["toilet_width"]["primary_candidate_width_mm"]
    ].iloc[0]
    simulation_lookup = {
        row["case"]: row for row in simulations.to_dict(orient="records")
    }
    patent = pd.read_csv(PROCESSED / "pg_patent_table2_width_contrasts.csv")
    logistics = pd.read_csv(TABLES / "table_5_logistics_integer_packing.csv")
    logistics_by_length = logistics.set_index("unit_length_mm")
    baseline_length, mid_length, short_length = config["logistics"][
        "illustrative_straw_lengths_mm"
    ]
    straw_boundaries = straw_boundary_values(config, straw)
    values = [
        {
            "value_id": "baseline_width_mm",
            "value": config["toilet_width"]["baseline_width_mm"],
            "unit": "mm",
            "source_file": "config/scenarios.json",
            "method": "configured illustrative baseline",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Abstract; Methods 2.3; Results 3.2",
        },
        {
            "value_id": "primary_candidate_width_mm",
            "value": config["toilet_width"]["primary_candidate_width_mm"],
            "unit": "mm",
            "source_file": "config/scenarios.json",
            "method": "configured illustrative candidate",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Abstract; Methods 2.3; Results 3.2",
        },
        {
            "value_id": "patent_contrast_count",
            "value": len(patent),
            "unit": "contrasts",
            "source_file": "data/processed/pg_patent_table2_width_contrasts.csv",
            "method": "row count",
            "status": "CALCULATED_FROM_PATENT_TABLE",
            "manuscript_location": "Results 3.1",
        },
        {
            "value_id": "patent_positive_contrasts",
            "value": int((patent["material_saving_fraction"] > 0).sum()),
            "unit": "contrasts",
            "source_file": "data/processed/pg_patent_table2_width_contrasts.csv",
            "method": "count material_saving_fraction > 0",
            "status": "CALCULATED_FROM_PATENT_TABLE",
            "manuscript_location": "Results 3.1",
        },
        {
            "value_id": "patent_negative_contrasts",
            "value": int((patent["material_saving_fraction"] < 0).sum()),
            "unit": "contrasts",
            "source_file": "data/processed/pg_patent_table2_width_contrasts.csv",
            "method": "count material_saving_fraction < 0",
            "status": "CALCULATED_FROM_PATENT_TABLE",
            "manuscript_location": "Abstract; Results 3.2",
        },
        {
            "value_id": "patent_saving_min",
            "value": patent["material_saving_fraction"].min(),
            "unit": "fraction",
            "source_file": "data/processed/pg_patent_table2_width_contrasts.csv",
            "method": "minimum",
            "status": "CALCULATED_FROM_PATENT_TABLE",
            "manuscript_location": "Results 3.1",
        },
        {
            "value_id": "patent_saving_max",
            "value": patent["material_saving_fraction"].max(),
            "unit": "fraction",
            "source_file": "data/processed/pg_patent_table2_width_contrasts.csv",
            "method": "maximum",
            "status": "CALCULATED_FROM_PATENT_TABLE",
            "manuscript_location": "Results 3.1",
        },
        {
            "value_id": "primary_width_break_even_longitudinal_ratio",
            "value": width_primary["break_even_longitudinal_ratio"],
            "unit": "ratio",
            "source_file": "tables/table_2_width_scenarios.csv",
            "method": "baseline width / candidate width",
            "status": "ANALYTICAL_BOUNDARY",
            "manuscript_location": "Results 3.2",
        },
        {
            "value_id": "primary_width_zero_compensation_saving",
            "value": width_primary["saving_zero_compensation"],
            "unit": "fraction",
            "source_file": "tables/table_2_width_scenarios.csv",
            "method": "1 - width ratio",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Results 3.2",
        },
        {
            "value_id": "primary_width_break_even_consumption_increase",
            "value": width_primary["break_even_longitudinal_ratio"] - 1.0,
            "unit": "fraction",
            "source_file": "tables/table_2_width_scenarios.csv",
            "method": "break-even longitudinal ratio minus one",
            "status": "ANALYTICAL_BOUNDARY",
            "manuscript_location": "Results 3.2; Discussion 4.3",
        },
        {
            "value_id": "center_low_task_mix_saving",
            "value": center.iloc[0]["material_saving_before_penalties"],
            "unit": "fraction",
            "source_file": "tables/table_3_center_perforation_scenarios.csv",
            "method": "task-mixture expectation",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Results 3.3",
        },
        {
            "value_id": "center_mid_task_mix_saving",
            "value": center.iloc[1]["material_saving_before_penalties"],
            "unit": "fraction",
            "source_file": "tables/table_3_center_perforation_scenarios.csv",
            "method": "task-mixture expectation",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Results 3.3",
        },
        {
            "value_id": "center_high_task_mix_saving",
            "value": center.iloc[2]["material_saving_before_penalties"],
            "unit": "fraction",
            "source_file": "tables/table_3_center_perforation_scenarios.csv",
            "method": "task-mixture expectation",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Results 3.3",
        },
        {
            "value_id": "straw_primary_length_reduction",
            "value": config["straw"]["primary_length_reduction_fraction"],
            "unit": "fraction",
            "source_file": "config/scenarios.json",
            "method": "configured primary straw scenario",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Abstract; Methods 2.7; Results 3.4",
        },
        {
            "value_id": "straw_primary_expected_replacement_rate_break_even",
            "value": straw_boundaries["primary_expected_rate"],
            "unit": "fraction",
            "source_file": "tables/table_4_straw_break_even.csv",
            "method": "1/(1-length reduction)-1 at configured primary reduction",
            "status": "ANALYTICAL_BOUNDARY",
            "manuscript_location": "Abstract; Results 3.4; Results 3.7",
        },
        {
            "value_id": "straw_primary_failure_probability_break_even",
            "value": straw_boundaries["primary_failure_probability"],
            "unit": "fraction",
            "source_file": "tables/table_4_straw_break_even.csv",
            "method": (
                "1 - (1-length reduction)/(1-shifted burden) "
                "at configured primary reduction"
            ),
            "status": "ANALYTICAL_BOUNDARY",
            "manuscript_location": "Abstract; Results 3.4; Results 3.7",
        },
        {
            "value_id": "straw_10pct_length_reduction",
            "value": 0.1,
            "unit": "fraction",
            "source_file": "config/scenarios.json",
            "method": "configured fixed straw comparison row",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Results 3.4",
        },
        {
            "value_id": "straw_20pct_length_reduction",
            "value": 0.2,
            "unit": "fraction",
            "source_file": "config/scenarios.json",
            "method": "configured fixed straw comparison row",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Results 3.4",
        },
        {
            "value_id": "straw_30pct_length_reduction",
            "value": 0.3,
            "unit": "fraction",
            "source_file": "config/scenarios.json",
            "method": "configured fixed straw comparison row",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Results 3.4",
        },
        {
            "value_id": "straw_10pct_expected_replacement_rate_break_even",
            "value": straw_boundaries["fixed_expected_rates"][0.1],
            "unit": "fraction",
            "source_file": "tables/table_4_straw_break_even.csv",
            "method": "1/(1-length reduction)-1",
            "status": "ANALYTICAL_BOUNDARY",
            "manuscript_location": "Results 3.4",
        },
        {
            "value_id": "straw_20pct_expected_replacement_rate_break_even",
            "value": straw_boundaries["fixed_expected_rates"][0.2],
            "unit": "fraction",
            "source_file": "tables/table_4_straw_break_even.csv",
            "method": "1/(1-length reduction)-1",
            "status": "ANALYTICAL_BOUNDARY",
            "manuscript_location": "Results 3.4",
        },
        {
            "value_id": "straw_30pct_expected_replacement_rate_break_even",
            "value": straw_boundaries["fixed_expected_rates"][0.3],
            "unit": "fraction",
            "source_file": "tables/table_4_straw_break_even.csv",
            "method": "1/(1-length reduction)-1",
            "status": "ANALYTICAL_BOUNDARY",
            "manuscript_location": "Results 3.4",
        },
        {
            "value_id": "straw_10pct_failure_probability_break_even",
            "value": straw_boundaries["fixed_failure_probabilities"][0.1],
            "unit": "fraction",
            "source_file": "tables/table_4_straw_break_even.csv",
            "method": "1 - (1-length reduction)/(1-shifted burden)",
            "status": "ANALYTICAL_BOUNDARY",
            "manuscript_location": "Results 3.4",
        },
        {
            "value_id": "straw_20pct_failure_probability_break_even",
            "value": straw_boundaries["fixed_failure_probabilities"][0.2],
            "unit": "fraction",
            "source_file": "tables/table_4_straw_break_even.csv",
            "method": "1 - (1-length reduction)/(1-shifted burden)",
            "status": "ANALYTICAL_BOUNDARY",
            "manuscript_location": "Results 3.4",
        },
        {
            "value_id": "straw_30pct_failure_probability_break_even",
            "value": straw_boundaries["fixed_failure_probabilities"][0.3],
            "unit": "fraction",
            "source_file": "tables/table_4_straw_break_even.csv",
            "method": "1 - (1-length reduction)/(1-shifted burden)",
            "status": "ANALYTICAL_BOUNDARY",
            "manuscript_location": "Results 3.4",
        },
        {
            "value_id": "logistics_baseline_length_mm",
            "value": baseline_length,
            "unit": "mm",
            "source_file": "config/scenarios.json",
            "method": "configured illustrative packed length",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Results 3.5",
        },
        {
            "value_id": "logistics_mid_length_mm",
            "value": mid_length,
            "unit": "mm",
            "source_file": "config/scenarios.json",
            "method": "configured illustrative packed length",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Results 3.5",
        },
        {
            "value_id": "logistics_short_length_mm",
            "value": short_length,
            "unit": "mm",
            "source_file": "config/scenarios.json",
            "method": "configured illustrative packed length",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Results 3.5",
        },
        {
            "value_id": "logistics_baseline_units_per_carton",
            "value": logistics_by_length.loc[baseline_length, "units_per_carton"],
            "unit": "units/carton",
            "source_file": "tables/table_5_logistics_integer_packing.csv",
            "method": "integer orientation packing",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Abstract; Results 3.5",
        },
        {
            "value_id": "logistics_mid_units_per_carton",
            "value": logistics_by_length.loc[mid_length, "units_per_carton"],
            "unit": "units/carton",
            "source_file": "tables/table_5_logistics_integer_packing.csv",
            "method": "integer orientation packing",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Abstract; Results 3.5",
        },
        {
            "value_id": "logistics_short_units_per_carton",
            "value": logistics_by_length.loc[short_length, "units_per_carton"],
            "unit": "units/carton",
            "source_file": "tables/table_5_logistics_integer_packing.csv",
            "method": "integer orientation packing",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Abstract; Results 3.5",
        },
        {
            "value_id": "logistics_mid_capacity_increase",
            "value": (
                logistics_by_length.loc[mid_length, "units_per_carton"]
                / logistics_by_length.loc[baseline_length, "units_per_carton"]
                - 1.0
            ),
            "unit": "fraction",
            "source_file": "tables/table_5_logistics_integer_packing.csv",
            "method": "mid-length capacity / baseline capacity - 1",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Results 3.5",
        },
        {
            "value_id": "logistics_mid_length_reduction",
            "value": 1.0 - mid_length / baseline_length,
            "unit": "fraction",
            "source_file": "config/scenarios.json",
            "method": "1 - mid packed length / baseline packed length",
            "status": "HYPOTHETICAL_SCENARIO",
            "manuscript_location": "Results 3.5",
        },
        {
            "value_id": "monte_carlo_seed",
            "value": config["seed"],
            "unit": "integer",
            "source_file": "config/scenarios.json",
            "method": "configured fixed seed",
            "status": "REPRODUCIBILITY_PARAMETER",
            "manuscript_location": "Methods 2.7",
        },
        {
            "value_id": "monte_carlo_iterations",
            "value": config["monte_carlo_iterations"],
            "unit": "draws",
            "source_file": "config/scenarios.json",
            "method": "configured draw count",
            "status": "REPRODUCIBILITY_PARAMETER",
            "manuscript_location": "Methods 2.7",
        },
    ]
    for case, prefix in [
        ("toilet_width", "width_mc"),
        ("center_perforation", "perforation_mc"),
        ("straw", "straw_mc"),
    ]:
        summary = simulation_lookup[case]
        for field in ("mean", "median", "p2_5", "p97_5", "probability_positive"):
            values.append(
                {
                    "value_id": f"{prefix}_{field}",
                    "value": summary[field],
                    "unit": "fraction",
                    "source_file": "tables/table_6_monte_carlo_summary.csv",
                    "method": f"{field} of configured scenario distribution",
                    "status": "HYPOTHETICAL_SCENARIO_SIMULATION",
                    "manuscript_location": "Results 3.6",
                }
            )
    frame = pd.DataFrame(values)
    frame.to_csv(RESULTS / "manuscript_values.csv", index=False)
    return frame


def source_table():
    toilet = pd.read_csv(PROCESSED / "source_registry.csv")
    straw = pd.read_csv(ROOT / "reports/source_registry.csv")
    patent = pd.read_csv(PROCESSED / "patent_source_registry.csv")
    rows = [
        {
            "evidence_domain": "toilet paper",
            "source_count": len(toilet),
            "observed_or_scenario": "observed source metadata and specifications",
            "principal_limitation": "No controlled population elasticity estimate",
        },
        {
            "evidence_domain": "straw/container",
            "source_count": len(straw),
            "observed_or_scenario": "observed documents and product examples",
            "principal_limitation": "No linked universal minimum functional length",
        },
        {
            "evidence_domain": "prior art",
            "source_count": len(patent),
            "observed_or_scenario": "patent publications",
            "principal_limitation": "Prior art is not proof of market performance",
        },
    ]
    frame = pd.DataFrame(rows)
    frame.to_csv(TABLES / "table_1_evidence_base.csv", index=False)


def method_check(config):
    mass = exact_hollow_cylinder_mass_g(6.0, 0.2, 165.0, 0.92)
    check = {
        "thin_wall_reference_mass_example_g": mass,
        "center_break_even_probability_example": center_perforation_break_even_probability(
            1.2,
            penalty_fraction=0.01,
        ),
        "seed": config["seed"],
        "iterations": config["monte_carlo_iterations"],
    }
    (RESULTS / "method_checks.json").write_text(
        json.dumps(check, indent=2) + "\n",
        encoding="utf-8",
    )


def main():
    setup()
    config = load_config(CONFIG)
    regenerate_patent_contrasts()
    source_table()
    width = width_tables(config)
    center = center_tables(config)
    straw = straw_tables(config)
    logistics = logistics_table(config)
    simulations, simulation_summary = simulation_outputs(config)
    sensitivity_table(config)
    figure_framework()
    figure_width(config)
    figure_patent_and_perforation(config)
    figure_straw_and_logistics(config, logistics)
    figure_simulations(simulations)
    value_registry(config, width, center, straw, simulation_summary)
    method_check(config)
    print(
        "Analysis complete: "
        f"{len(list(FIGURES.glob('*.pdf')))} figures, "
        f"{len(list(TABLES.glob('*.csv')))} tables."
    )


if __name__ == "__main__":
    main()
