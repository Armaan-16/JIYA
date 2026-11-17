"""
============================================================
JIYA AI Operating System

Module:
LLM Response Model

Purpose:
Represents a response returned by a language model.

Author:
Armaan Mishra

Version:
0.2.0
============================================================
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class LLMResponse:

    success: bool

    text: str

    provider: str

    model: str

    error: Optional[str] = None

    latency: float = 0.0