#!/usr/bin/env python3

import csv
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/processed/pg_patent_table2_observed.csv"
OUTPUT = ROOT / "data/processed/pg_patent_table2_width_contrasts.csv"


def load_rows():
    with INPUT.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        for field in (
            "basis_weight_lb_per_3000ft2",
            "width_in",
            "sheet_area_ft2",
            "sheets_per_task",
            "total_usage_lb_per_task",
        ):
            row[field] = float(row[field])
    return rows


def build_contrasts(rows):
    contrasts = []
    for basis_weight in sorted({row["basis_weight_lb_per_3000ft2"] for row in rows}):
        group = sorted(
            (row for row in rows if row["basis_weight_lb_per_3000ft2"] == basis_weight),
            key=lambda row: row["width_in"],
        )
        for narrow, wide in combinations(group, 2):
            width_ratio = narrow["width_in"] / wide["width_in"]
            longitudinal_ratio = narrow["sheets_per_task"] / wide["sheets_per_task"]
            area_ratio_from_reported_sheet_area = (
                narrow["sheet_area_ft2"] * narrow["sheets_per_task"]
            ) / (wide["sheet_area_ft2"] * wide["sheets_per_task"])
            reported_total_usage_ratio = (
                narrow["total_usage_lb_per_task"]
                / wide["total_usage_lb_per_task"]
            )
            finite_elasticity = math.log(longitudinal_ratio) / math.log(width_ratio)
            contrasts.append(
                {
                    "source_id": "pg_patent_us6458450",
                    "basis_weight_lb_per_3000ft2": f"{basis_weight:g}",
                    "narrow_width_in": f'{narrow["width_in"]:g}',
                    "wide_width_in": f'{wide["width_in"]:g}',
                    "width_ratio": f"{width_ratio:.6f}",
                    "longitudinal_consumption_ratio": f"{longitudinal_ratio:.6f}",
                    "break_even_longitudinal_ratio": f"{1 / width_ratio:.6f}",
                    "reported_total_usage_ratio": (
                        f"{reported_total_usage_ratio:.6f}"
                    ),
                    "geometry_implied_area_ratio": (
                        f"{area_ratio_from_reported_sheet_area:.6f}"
                    ),
                    "rounding_difference_fraction": (
                        f"{reported_total_usage_ratio - area_ratio_from_reported_sheet_area:.6f}"
                    ),
                    "material_saving_fraction": (
                        f"{1 - reported_total_usage_ratio:.6f}"
                    ),
                    "finite_epsilon_LW": f"{finite_elasticity:.6f}",
                    "value_status": "CALCULATED_FROM_PATENT_TABLE_2",
                }
            )
    return contrasts


def write_contrasts(contrasts, output=OUTPUT):
    fields = list(contrasts[0])
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(contrasts)


def main():
    write_contrasts(build_contrasts(load_rows()))


if __name__ == "__main__":
    main()
