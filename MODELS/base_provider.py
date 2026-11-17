"""
============================================================
JIYA AI Operating System
Module: Base Provider (Abstract Contract)
Purpose: Defines the abstract interface every AI model provider must implement.
Author: Armaan Mishra
============================================================
"""

from abc import ABC, abstractmethod
from typing import Generator, Any
from MODELS.llm_request import LLMRequest
from MODELS.llm_response import LLMResponse


class BaseProvider(ABC):
    """Abstract base class that all LLM provider backends must implement."""

    @abstractmethod
    def generate(self, request: LLMRequest) -> LLMResponse:
        """
        Generate a complete synchronous response from the model.
        """
        pass

    @abstractmethod
    def generate_stream(self, request: LLMRequest) -> Generator[str, None, None]:
        """
        Stream response tokens chunk-by-chunk from the model.
        """
        pass

