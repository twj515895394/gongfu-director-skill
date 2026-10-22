"""Regression tests for scripts/validate_storyboard.py; standard library only."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_storyboard.py"

GOOD_H3 = """subject_definitions:
<Subject 1> is character A.

summary:
Two fighters face each other.

retention_analysis:
Preserve the references.

detailed_description:
[Shot 1] Two fighters square up.
[Shot 2] At 00:01.000, CUT TO: A steps forward.
[Shot 3] At 00:02.000, CUT TO: B blocks.

overall_soundscape:
Footsteps and impact sounds.

non_diegetic_music:
N/A
"""

GOOD_STORYBOARD = """【参考图说明】

图1：人物A
图2：场景

【质感词语】3DCG，冷色调

【声音设计】纯音效

【场景一 · 轴线声明】A 面朝画右

镜头1：中景，A 左侧平拍，A 出拳，固定，2秒

镜头2：近景，B 右侧平拍，B 格挡，手持，2秒
"""


class ValidateStoryboardTests(unittest.TestCase):
    def run_validator(self, content: str, suffix: str, *args: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = Path(temp_dir) / f"sample{suffix}"
            input_path.write_text(content, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(SCRIPT), str(input_path), *args],
                capture_output=True,
                text=True,
                check=False,
            )

    def test_valid_h3_passes(self) -> None:
        result = self.run_validator(GOOD_H3, ".txt")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("0 error(s)", result.stdout)

    def test_h3_timestamp_order_and_chinese_are_detected(self) -> None:
        bad = GOOD_H3.replace("At 00:02.000", "At 00:01.000").replace("N/A\n", "无配乐\n")
        result = self.run_validator(bad, ".txt")
        self.assertEqual(result.returncode, 1)
        self.assertIn("h3_timestamp_order", result.stdout)
        self.assertIn("h3_cjk", result.stdout)
        self.assertIn("h3_last_line", result.stdout)

    def test_h3_character_limit_is_enforced(self) -> None:
        result = self.run_validator(GOOD_H3, ".txt", "--max-chars", "100")
        self.assertEqual(result.returncode, 1)
        self.assertIn("h3_char_limit", result.stdout)

    def test_valid_chinese_storyboard_passes(self) -> None:
        result = self.run_validator(GOOD_STORYBOARD, ".md")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_json_output_is_machine_readable(self) -> None:
        result = self.run_validator(GOOD_H3, ".txt", "--json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["mode"], "h3")
        self.assertEqual(payload["errors"], 0)
        self.assertTrue(payload["semantic_review_required"])


if __name__ == "__main__":
    unittest.main()
