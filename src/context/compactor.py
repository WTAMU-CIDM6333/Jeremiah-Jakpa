"""Compactor with keep list."""

from typing import List, Dict, Any, Optional
from .ledger import Ledger


class Compactor:
    def __init__(self, keep_list: Optional[List[str]] = None, ledger: Optional[Ledger] = None):
        self.keep_list = keep_list or []
        self.ledger = ledger or Ledger()
    
    def compact(self, content: str, tokens_before: int = None) -> Dict[str, Any]:
        """Compact content keeping items on keep list word for word."""
        if tokens_before is None:
            tokens_before = len(content.split())  # rough estimate
        
        # Extract items from keep list that appear in content - keep them word for word
        kept_items = []
        for item in self.keep_list:
            if item in content:
                kept_items.append(item)
        
        # Simple compaction: keep kept items and summary
        compacted = "\n".join(kept_items) if kept_items else content[:tokens_before // 2]
        tokens_after = len(compacted.split())
        
        event = self.ledger.append("compaction", {
            "tokens_before": tokens_before,
            "tokens_after": tokens_after,
            "kept_items": kept_items,
            "kept_count": len(kept_items)
        })
        
        return {
            "compacted_content": compacted,
            "tokens_before": tokens_before,
            "tokens_after": tokens_after,
            "kept_items": kept_items,
            "event": event
        }
