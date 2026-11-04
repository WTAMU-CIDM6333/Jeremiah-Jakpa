"""Budget meter for model calls."""

from typing import Dict, Any, Optional
from .ledger import Ledger


class BudgetMeter:
    def __init__(self, declared_budget: int = 10000, ledger: Optional[Ledger] = None):
        self.declared_budget = declared_budget
        self.ledger = ledger or Ledger()
        self.total_tokens = 0
    
    def record_turn(self, provider_tokens: Dict[str, int], model: str = "unknown") -> Dict[str, Any]:
        """Record one turn_budget event per model call with provider's token counts and declared budget."""
        prompt_tokens = provider_tokens.get('prompt_tokens', provider_tokens.get('input_tokens', 0))
        completion_tokens = provider_tokens.get('completion_tokens', provider_tokens.get('output_tokens', 0))
        total = provider_tokens.get('total_tokens', prompt_tokens + completion_tokens)
        
        self.total_tokens += total
        
        record = {
            "event": "turn_budget",
            "model": model,
            "provider_tokens": provider_tokens,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": total,
            "declared_budget": self.declared_budget,
            "remaining": self.declared_budget - self.total_tokens
        }
        
        self.ledger.append("turn_budget", record)
        return record
