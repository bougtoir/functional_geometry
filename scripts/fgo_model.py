import itertools
import json
import math
from pathlib import Path

import numpy as np


def load_config(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def toilet_width_material_ratio(width_new, width_old, elasticity):
    width_ratio = np.asarray(width_new, dtype=float) / float(width_old)
    return np.power(width_ratio, 1.0 + np.asarray(elasticity, dtype=float))


def toilet_width_saving(width_new, width_old, elasticity):
    return 1.0 - toilet_width_material_ratio(width_new, width_old, elasticity)


def longitudinal_break_even_ratio(width_new, width_old):
    return float(width_old) / float(width_new)


def center_perforation_material_ratio(
    half_suitable_probability,
    half_task_unit_multiplier,
    full_task_unit_multiplier=1.0,
):
    probability = np.asarray(half_suitable_probability, dtype=float)
    return (
        (1.0 - probability) * full_task_unit_multiplier
        + probability * 0.5 * half_task_unit_multiplier
    )


def center_perforation_break_even_probability(
    half_task_unit_multiplier,
    full_task_unit_multiplier=1.0,
    penalty_fraction=0.0,
):
    half_ratio = 0.5 * half_task_unit_multiplier
    target = 1.0 / (1.0 + penalty_fraction)
    denominator = full_task_unit_multiplier - half_ratio
    if denominator <= 0:
        return math.inf
    return max(0.0, (full_task_unit_multiplier - target) / denominator)


def straw_material_ratio_expected_rate(
    length_reduction_fraction,
    expected_additional_replacement_rate=0.0,
    shifted_container_burden=0.0,
):
    return (
        (1.0 - np.asarray(length_reduction_fraction, dtype=float))
        * (1.0 + np.asarray(expected_additional_replacement_rate, dtype=float))
        + np.asarray(shifted_container_burden, dtype=float)
    )


def straw_expected_replacement_rate_break_even(
    length_reduction_fraction,
    shifted_burden=0.0,
):
    retained = 1.0 - float(length_reduction_fraction)
    return (1.0 - float(shifted_burden)) / retained - 1.0


def straw_material_ratio_failure_probability(
    length_reduction_fraction,
    independent_failure_probability=0.0,
    shifted_container_burden=0.0,
):
    retained = 1.0 - np.asarray(length_reduction_fraction, dtype=float)
    success_probability = 1.0 - np.asarray(
        independent_failure_probability,
        dtype=float,
    )
    return (
        retained / success_probability
        + np.asarray(shifted_container_burden, dtype=float)
    )


def straw_failure_probability_break_even(
    length_reduction_fraction,
    shifted_burden=0.0,
):
    retained = 1.0 - float(length_reduction_fraction)
    burden_remaining = 1.0 - float(shifted_burden)
    return 1.0 - retained / burden_remaining


def exact_hollow_cylinder_mass_g(
    outer_diameter_mm,
    wall_thickness_mm,
    length_mm,
    density_g_cm3,
):
    outer_radius_cm = float(outer_diameter_mm) / 20.0
    inner_radius_cm = (float(outer_diameter_mm) - 2.0 * float(wall_thickness_mm)) / 20.0
    length_cm = float(length_mm) / 10.0
    volume_cm3 = math.pi * length_cm * (outer_radius_cm**2 - inner_radius_cm**2)
    return float(density_g_cm3) * volume_cm3


def max_integer_pack(carton_dimensions_mm, unit_dimensions_mm):
    best = 0
    best_orientation = None
    for orientation in set(itertools.permutations(unit_dimensions_mm)):
        count = math.prod(
            int(carton / unit)
            for carton, unit in zip(carton_dimensions_mm, orientation)
        )
        if count > best:
            best = count
            best_orientation = orientation
    return best, best_orientation


def run_monte_carlo(config):
    rng = np.random.default_rng(config["seed"])
    count = int(config["monte_carlo_iterations"])

    width = config["toilet_width"]
    elasticity = rng.triangular(*width["elasticity_triangular"], size=count)
    success = rng.triangular(*width["success_ratio_triangular"], size=count)
    penalty = rng.uniform(*width["manufacturing_penalty_uniform"], size=count)
    width_ratio = toilet_width_material_ratio(
        width["primary_candidate_width_mm"],
        width["baseline_width_mm"],
        elasticity,
    )
    width_saving = 1.0 - width_ratio * (1.0 + penalty) / success

    perforation = config["center_perforation"]
    probability = rng.beta(
        *perforation["half_suitable_probability_beta"],
        size=count,
    )
    half_multiplier = rng.triangular(
        *perforation["half_task_unit_multiplier_triangular"],
        size=count,
    )
    success = rng.triangular(*perforation["success_ratio_triangular"], size=count)
    penalty = rng.uniform(*perforation["manufacturing_penalty_uniform"], size=count)
    perforation_ratio = center_perforation_material_ratio(
        probability,
        half_multiplier,
    )
    perforation_saving = 1.0 - perforation_ratio * (1.0 + penalty) / success

    straw = config["straw"]
    expected_replacement_rate = rng.triangular(
        *straw["expected_additional_replacement_rate_triangular"],
        size=count,
    )
    shifted = rng.uniform(*straw["shifted_container_burden_uniform"], size=count)
    straw_saving = 1.0 - straw_material_ratio_expected_rate(
        straw["primary_length_reduction_fraction"],
        expected_replacement_rate,
        shifted,
    )

    return {
        "toilet_width": width_saving,
        "center_perforation": perforation_saving,
        "straw": straw_saving,
    }


def summarize_simulation(values):
    values = np.asarray(values, dtype=float)
    return {
        "mean": float(np.mean(values)),
        "median": float(np.median(values)),
        "p2_5": float(np.quantile(values, 0.025)),
        "p97_5": float(np.quantile(values, 0.975)),
        "probability_positive": float(np.mean(values > 0.0)),
    }


def convergence_diagnostics(values, sample_sizes):
    rows = []
    values = np.asarray(values, dtype=float)
    for size in sample_sizes:
        subset = values[: min(size, values.size)]
        summary = summarize_simulation(subset)
        rows.append(
            {
                "iterations": subset.size,
                "mean": summary["mean"],
                "median": summary["median"],
                "probability_positive": summary["probability_positive"],
            }
        )
    return rows
