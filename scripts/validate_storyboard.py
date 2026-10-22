#!/usr/bin/env python3
"""Lightweight, dependency-free structural checks for storyboard and H3 prompt files.

This script checks deterministic formatting only. It does not replace semantic review
of action causality, spatial continuity, or whether the choreography matches user intent.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

H3_FIELDS = [
    "subject_definitions",
    "summary",
    "retention_analysis",
    "detailed_description",
    "overall_soundscape",
    "non_diegetic_music",
]
H3_SHOT_RE = re.compile(
    r"(?m)^\s*\[Shot\s+(\d+)\](?:\s+At\s+(\d{2}):(\d{2})\.(\d{3}))?"
)
CN_SHOT_RE = re.compile(r"(?m)^\s*(?:#{1,4}\s*)?镜头\s*(\d+)\s*[：:]")
CJK_RE = re.compile(r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af]")
FIELD_RE = re.compile(r"(?m)^\s*([a-z_]+)\s*:")
CN_REQUIRED_MARKERS = {
    "参考图说明": re.compile(r"参考图说明"),
    "质感词语": re.compile(r"质感词语"),
    "声音设计": re.compile(r"声音设计"),
    "场景轴线声明": re.compile(r"场景.{0,12}轴线声明|轴线声明"),
}


def issue(level: str, code: str, message: str) -> dict[str, str]:
    return {"level": level, "code": code, "message": message}


def check_numbering(numbers: list[int], label: str, issues: list[dict[str, str]]) -> None:
    if not numbers:
        issues.append(issue("error", "no_shots", f"No numbered shots found for {label}."))
        return
    expected = list(range(1, len(numbers) + 1))
    if numbers != expected:
        issues.append(
            issue(
                "error",
                "shot_numbering",
                f"{label} shot numbers must be continuous from 1; found {numbers}.",
            )
        )


def validate_h3(text: str, max_chars: int, issues: list[dict[str, str]]) -> None:
    nonempty = [line.strip() for line in text.splitlines() if line.strip()]
    if not nonempty:
        issues.append(issue("error", "empty_file", "The file is empty."))
        return

    if nonempty[0] != "subject_definitions:":
        issues.append(
            issue("error", "h3_first_line", "The first non-empty line must be subject_definitions:.")
        )
    if nonempty[-1] != "N/A":
        issues.append(issue("error", "h3_last_line", "The last non-empty line must be N/A."))

    if len(text) > max_chars:
        issues.append(
            issue(
                "error",
                "h3_char_limit",
                f"Prompt has {len(text)} Unicode code points including whitespace/newlines; limit is {max_chars}.",
            )
        )

    cjk = list(CJK_RE.finditer(text))
    if cjk:
        line_no = text.count("\n", 0, cjk[0].start()) + 1
        issues.append(
            issue(
                "error",
                "h3_cjk",
                f"Found {len(cjk)} CJK/Kana/Hangul character(s); first occurrence is on line {line_no}. H3 prompt must be English-only.",
            )
        )

    positions: dict[str, int] = {}
    for match in FIELD_RE.finditer(text):
        field = match.group(1)
        if field in H3_FIELDS and field not in positions:
            positions[field] = match.start()

    missing = [field for field in H3_FIELDS if field not in positions]
    if missing:
        issues.append(
            issue("error", "h3_fields_missing", "Missing required H3 field(s): " + ", ".join(missing) + ".")
        )
    else:
        ordered = [positions[field] for field in H3_FIELDS]
        if ordered != sorted(ordered):
            issues.append(
                issue("error", "h3_field_order", "H3 fields must appear in the required six-field order.")
            )

    shot_matches = list(H3_SHOT_RE.finditer(text))
    numbers = [int(match.group(1)) for match in shot_matches]
    check_numbering(numbers, "H3", issues)

    times: list[tuple[int, float]] = []
    for match in shot_matches:
        shot_no = int(match.group(1))
        minute, second, millis = match.group(2), match.group(3), match.group(4)
        newline = text.find("\n", match.start())
        header_line = text[match.start(): newline if newline >= 0 else len(text)]
        has_at = re.search(r"\bAt\b", header_line) is not None
        if shot_no == 1 and minute is not None:
            issues.append(
                issue("error", "h3_first_shot_timestamp", "Shot 1 must not carry a timestamp in the H3 format.")
            )
        if shot_no > 1 and minute is None:
            if has_at:
                message = f"Shot {shot_no} has an invalid timestamp; expected At MM:SS.mmm."
            else:
                message = f"Shot {shot_no} is missing its At MM:SS.mmm timestamp."
            issues.append(issue("error", "h3_timestamp_missing", message))
        if minute is not None:
            seconds_value = int(minute) * 60 + int(second) + int(millis) / 1000
            times.append((shot_no, seconds_value))
            if "CUT TO:" not in header_line:
                issues.append(
                    issue("warning", "h3_cut_marker", f"Shot {shot_no} timestamp header does not contain CUT TO:.")
                )

    for previous, current in zip(times, times[1:]):
        if current[1] <= previous[1]:
            issues.append(
                issue(
                    "error",
                    "h3_timestamp_order",
                    f"Timestamps must increase strictly; Shot {current[0]} is not later than Shot {previous[0]}.",
                )
            )


def validate_storyboard(text: str, issues: list[dict[str, str]]) -> None:
    nonempty = [line.strip() for line in text.splitlines() if line.strip()]
    if not nonempty:
        issues.append(issue("error", "empty_file", "The file is empty."))
        return

    shot_matches = list(CN_SHOT_RE.finditer(text))
    numbers = [int(match.group(1)) for match in shot_matches]
    check_numbering(numbers, "Storyboard", issues)

    if not shot_matches:
        issues.append(
            issue("warning", "shot_format_unrecognized", "No Chinese '镜头 N：' headings found; confirm this is a complete storyboard file.")
        )

    for label, pattern in CN_REQUIRED_MARKERS.items():
        if not pattern.search(text):
            issues.append(
                issue("warning", "storyboard_section_missing", f"Expected section marker not found: {label}.")
            )

    # A storyboard template may express duration as seconds rather than timecodes,
    # so this script does not invent or require a timecode format for Chinese drafts.
    if shot_matches and "场景" not in text:
        issues.append(
            issue("warning", "scene_context_missing", "No scene heading/context marker found; verify spatial context manually.")
        )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run deterministic structure checks on a Chinese storyboard or H3 prompt."
    )
    parser.add_argument("file", help="Path to the storyboard .md or H3 prompt .txt")
    parser.add_argument(
        "--mode",
        choices=("auto", "h3", "storyboard"),
        default="auto",
        help="Input format; auto detects H3 from extension or subject_definitions: (default: auto)",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=7000,
        help="H3 maximum character count, counting Unicode code points including whitespace/newlines (default: 7000)",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    try:
        text = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        print(f"ERROR: unable to decode as UTF-8: {exc}", file=sys.stderr)
        return 2

    mode = args.mode
    if mode == "auto":
        mode = "h3" if path.suffix.lower() == ".txt" or re.search(
            r"(?m)^\s*subject_definitions\s*:", text
        ) else "storyboard"

    issues: list[dict[str, str]] = []
    if mode == "h3":
        validate_h3(text, args.max_chars, issues)
    else:
        validate_storyboard(text, issues)

    errors = sum(item["level"] == "error" for item in issues)
    warnings = sum(item["level"] == "warning" for item in issues)
    result: dict[str, Any] = {
        "file": str(path),
        "mode": mode,
        "characters": len(text),
        "character_count_definition": "Python Unicode code points, including whitespace and newlines",
        "errors": errors,
        "warnings": warnings,
        "issues": issues,
        "semantic_review_required": True,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"File: {path}")
        print(f"Mode: {mode}")
        print(f"Characters: {len(text)} (Unicode code points, including whitespace/newlines)")
        print(f"Result: {errors} error(s), {warnings} warning(s)")
        for item in issues:
            print(f"[{item['level'].upper()}] {item['code']}: {item['message']}")
        print("Note: structural checks do not replace semantic review of action causality or spatial continuity.")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
