"""Runtime ledger - append-only JSON Lines."""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any


LEDGER_PATH = Path(__file__).parent.parent.parent / "var" / "ledger.jsonl"


class Ledger:
    def __init__(self, path: Path = LEDGER_PATH):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
    
    def append(self, event_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Append event to ledger (append-only, no edits)."""
        event = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event_type": event_type,
            **data
        }
        with open(self.path, 'a') as f:
            f.write(json.dumps(event) + '\n')
        return event
    
    def read_tail(self, n: int = 10):
        """Read last n events."""
        if not self.path.exists():
            return []
        with open(self.path) as f:
            lines = f.readlines()
        events = []
        for line in lines[-n:]:
            if line.strip():
                events.append(json.loads(line))
        return events
    
    def read_all(self):
        if not self.path.exists():
            return []
        events = []
        with open(self.path) as f:
            for line in f:
                if line.strip():
                    events.append(json.loads(line))
        return events
