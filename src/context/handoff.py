"""Handoff writer and resume loader."""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional

from .ledger import Ledger


class HandoffWriter:
    def __init__(self, ledger: Optional[Ledger] = None):
        self.ledger = ledger or Ledger()
    
    def write_handoff(self, handoff_path: Path, sections: Dict[str, Any]) -> Dict[str, Any]:
        """Write handoff with seven sections. next step 1 must be one action."""
        # Ensure seven sections
        required_sections = ["intent", "current_state", "key_decisions", 
                           "constraints", "next_steps", "open_questions", "references"]
        # Fill in provided sections
        handoff_content = []
        handoff_content.append(f"# Handoff - {datetime.utcnow().isoformat()}Z\n")
        
        for section in required_sections:
            if section in sections:
                handoff_content.append(f"## {section.replace('_', ' ').title()}\n")
                content = sections[section]
                if isinstance(content, list):
                    for item in content:
                        if section == "next_steps" and content.index(item) == 0:
                            # next step 1 is one action
                            handoff_content.append(f"1. {item}\n")
                        elif section == "next_steps":
                            handoff_content.append(f"{content.index(item)+1}. {item}\n")
                        else:
                            handoff_content.append(f"- {item}\n")
                else:
                    handoff_content.append(f"{content}\n")
                handoff_content.append("\n")
        
        handoff_path.parent.mkdir(parents=True, exist_ok=True)
        with open(handoff_path, 'w') as f:
            f.writelines(handoff_content)
        
        event = self.ledger.append("handoff_written", {
            "path": str(handoff_path),
            "sections": required_sections
        })
        
        return {"path": handoff_path, "event": event}


class ResumeLoader:
    def __init__(self, ledger: Optional[Ledger] = None):
        self.ledger = ledger or Ledger()
    
    def resume_from_handoff(self, handoff_path: Path, l1_files: List[Path] = None, 
                           include_ledger_tail: bool = True) -> Dict[str, Any]:
        """Start a session from the handoff, L1 files, and the ledger tail, with no transcript."""
        l1_files = l1_files or []
        loaded = {
            "handoff": None,
            "l1_files": [],
            "ledger_tail": []
        }
        
        if handoff_path.exists():
            with open(handoff_path) as f:
                loaded["handoff"] = f.read()
        
        for l1_file in l1_files:
            if l1_file.exists():
                with open(l1_file) as f:
                    loaded["l1_files"].append({
                        "path": str(l1_file),
                        "content": f.read()
                    })
        
        if include_ledger_tail:
            loaded["ledger_tail"] = self.ledger.read_tail(10)
        
        event = self.ledger.append("session_resumed", {
            "handoff_path": str(handoff_path),
            "l1_files": [str(f) for f in l1_files],
            "ledger_tail_count": len(loaded["ledger_tail"]),
            "no_transcript": True
        })
        
        loaded["event"] = event
        return loaded
