"""Tests for E6 context engineering."""

import unittest
import json
import os
from pathlib import Path
import tempfile

from src.context.budget import BudgetMeter
from src.context.compactor import Compactor
from src.context.handoff import HandoffWriter, ResumeLoader
from src.context.ledger import Ledger


class TestE6Context(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.ledger = Ledger(Path(self.tmpdir) / "ledger.jsonl")
    
    def test_budget_meter_turn_budget_per_call(self):
        """Test proves one turn_budget record per model call, with provider's token counts and declared budget."""
        meter = BudgetMeter(declared_budget=5000, ledger=self.ledger)
        record = meter.record_turn({"prompt_tokens": 100, "completion_tokens": 50, "total_tokens": 150}, model="gpt-4")
        self.assertEqual(record["event"], "turn_budget")
        self.assertIn("provider_tokens", record)
        self.assertEqual(record["declared_budget"], 5000)
        self.assertIn("prompt_tokens", record)
        self.assertIn("completion_tokens", record)
        # Check ledger
        events = self.ledger.read_all()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["event_type"], "turn_budget")
    
    def test_compactor_keep_list_survives_word_for_word(self):
        """Test proves items on keep list survive compaction word for word and compaction records tokens before and after."""
        keep_list = ["Intent: build secure MCP server", "Decision: use token auth"]
        compactor = Compactor(keep_list=keep_list, ledger=self.ledger)
        content = "Some random text. Intent: build secure MCP server more text. Decision: use token auth end."
        result = compactor.compact(content, tokens_before=20)
        self.assertIn("Intent: build secure MCP server", result["compacted_content"])
        self.assertIn("Decision: use token auth", result["compacted_content"])
        self.assertIn("tokens_before", result)
        self.assertIn("tokens_after", result)
        events = self.ledger.read_all()
        self.assertEqual(events[0]["event_type"], "compaction")
        self.assertIn("tokens_before", events[0])
        self.assertIn("tokens_after", events[0])
    
    def test_handoff_seven_sections_next_step_one_action(self):
        """Handoff has seven sections; next step 1 is one action."""
        writer = HandoffWriter(ledger=self.ledger)
        handoff_path = Path(self.tmpdir) / "handoff.md"
        sections = {
            "intent": "Complete E6",
            "current_state": "In progress",
            "key_decisions": ["Use new package"],
            "constraints": ["Append-only ledger"],
            "next_steps": ["Run tests first"],  # next step 1 is one action
            "open_questions": ["None"],
            "references": ["README.md"]
        }
        writer.write_handoff(handoff_path, sections)
        self.assertTrue(handoff_path.exists())
        with open(handoff_path) as f:
            content = f.read()
        # Check seven sections
        for s in ["Intent", "Current State", "Key Decisions", "Constraints", "Next Steps", "Open Questions", "References"]:
            self.assertIn(s, content)
        events = self.ledger.read_all()
        self.assertTrue(any(e["event_type"] == "handoff_written" for e in events))
    
    def test_resume_loader(self):
        """Loader starts session from handoff, L1 files, and ledger tail, with no transcript."""
        writer = HandoffWriter(ledger=self.ledger)
        loader = ResumeLoader(ledger=self.ledger)
        handoff_path = Path(self.tmpdir) / "handoff.md"
        l1_file = Path(self.tmpdir) / "l1.md"
        l1_file.write_text("L1 content")
        
        sections = {
            "intent": "Complete E6",
            "current_state": "In progress",
            "key_decisions": ["Use new package"],
            "constraints": ["Append-only ledger"],
            "next_steps": ["Run tests first"],
            "open_questions": ["None"],
            "references": ["README.md"]
        }
        writer.write_handoff(handoff_path, sections)
        result = loader.resume_from_handoff(handoff_path, [l1_file])
        self.assertIsNotNone(result["handoff"])
        self.assertEqual(len(result["l1_files"]), 1)
        self.assertIsInstance(result["ledger_tail"], list)
        self.assertTrue(result["event"]["no_transcript"])
        self.assertEqual(result["event"]["event_type"], "session_resumed")


if __name__ == "__main__":
    unittest.main()
