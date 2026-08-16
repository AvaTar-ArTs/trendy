#!/usr/bin/env python3
"""Flag hot/rising repositories from a CSV of activity snapshots.

Expected columns:
repo,current,baseline,percentile,signals

- current and baseline are comparable activity values, such as stars/day.
- percentile is 0..100 within a pre-defined comparison cohort.
- signals is the number of independent activity dimensions moving.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass


@dataclass
class Candidate:
    repo: str
    current: float
    baseline: float
    percentile: float
    signals: int

    @property
    def growth_percent(self) -> float:
        if self.baseline <= 0:
            return float("inf") if self.current > 0 else 0.0
        return ((self.current - self.baseline) / self.baseline) * 100

    @property
    def label(self) -> str:
        growth = self.growth_percent
        if self.percentile >= 99 and growth >= 300 and self.signals >= 2:
            return "top-1-breakout"
        if self.percentile >= 95 and growth >= 300 and self.signals >= 2:
            return "top-5-breakout"
        if growth >= 200 and self.signals >= 2:
            return "hot"
        if growth >= 100 and self.signals >= 2:
            return "rising"
        if growth >= 50:
            return "watch"
        return "normal"


def read_rows(path: str) -> list[Candidate]:
    with open(path, newline="", encoding="utf-8") as handle:
        return [
            Candidate(
                repo=row["repo"],
                current=float(row["current"]),
                baseline=float(row["baseline"]),
                percentile=float(row.get("percentile", 0)),
                signals=int(row.get("signals", 1)),
            )
            for row in csv.DictReader(handle)
        ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path")
    args = parser.parse_args()

    for item in sorted(read_rows(args.csv_path), key=lambda x: x.growth_percent, reverse=True):
        growth = "infinite" if item.growth_percent == float("inf") else f"{item.growth_percent:+.1f}%"
        print(f"{item.label:16} {growth:>10} p{item.percentile:>5.1f} signals={item.signals} {item.repo}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
