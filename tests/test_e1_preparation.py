"""Negative controls for the E1 preparation publication gate."""

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.check_e1 import REQUIRED, ROOT, preparation_errors


class PreparationGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for relative in REQUIRED:
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def replace(self, relative, old, new):
        path = self.root / relative
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new), encoding="utf-8")

    def test_preparation_can_publish_without_claiming_flight(self):
        self.assertEqual(preparation_errors(self.root), [])

    def test_missing_artifact_fails(self):
        (self.root / "docs/PRD.md").unlink()
        self.assertTrue(preparation_errors(self.root))

    def test_changed_step_budget_fails(self):
        self.replace(REQUIRED[0], "steps: 5", "steps: 50")
        self.assertTrue(any("steps" in e for e in preparation_errors(self.root)))

    def test_malformed_config_fails(self):
        (self.root / "opencode.json").write_text("{", encoding="utf-8")
        self.assertTrue(any("Invalid opencode.json" in e for e in preparation_errors(self.root)))

    def test_missing_owner_approval_fails(self):
        self.replace("docs/PRD.md", "I have reviewed and approve", "Pending approval")
        self.assertTrue(any("approval" in e for e in preparation_errors(self.root)))

    def test_shortened_queue_fails(self):
        path = self.root / "evolution-01/fixtures/review-queue.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(lines[:5]), encoding="utf-8")
        self.assertTrue(any("20 sequential" in e for e in preparation_errors(self.root)))

    def test_removed_falsifier_fails(self):
        self.replace("evolution-01/flight-card.md", "permission was loosened", "permission changed")
        self.assertTrue(any("mandatory falsifier" in e for e in preparation_errors(self.root)))

    def test_unsigned_card_cannot_accompany_flight_claim(self):
        self.replace("evolution-01/flight-log.md", "Status: NOT FLOWN", "Status: PASS")
        self.assertTrue(any("Chase GO" in e for e in preparation_errors(self.root)))

    def test_raw_export_fails_even_with_go(self):
        card = self.root / "evolution-01/flight-card.md"
        with card.open("a", encoding="utf-8") as stream:
            stream.write("\nGO — Test reviewer — 2026-10-21\n")
        (self.root / "evolution-01/evidence/raw.json").write_text("{}", encoding="utf-8")
        self.assertTrue(any("raw exports forbidden" in e for e in preparation_errors(self.root)))


if __name__ == "__main__":
    unittest.main()
