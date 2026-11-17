from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class LLMRequest:
    prompt: str
    history: List[Dict[str, str]] = field(default_factory=list)