"""
============================================================
JIYA AI Operating System
Module: Cortex Router / Provider Manager
Purpose: Routes user prompts between fast conversational models (Qwen)
         and deep reasoning models (DeepSeek-R1).
Author: Armaan Mishra
============================================================
"""

from typing import Tuple, Generator, Any
from BRAIN.providers.ollama_provider import OllamaProvider
from MODELS.llm_request import LLMRequest
from MODELS.llm_response import LLMResponse


class ProviderManager:
    """The Cortex Router directing prompts to specialized neural engines."""

    def __init__(self, fast_model: str = "qwen3:8b", deep_model: str = "deepseek-r1:14b"):
        # Fast conversational brain (Default - Qwen 8B)
        self.fast_brain = OllamaProvider(model=fast_model, think=False)

        # Deep reasoning brain (DeepSeek-R1 14B)
        self.deep_brain = OllamaProvider(model=deep_model, think=True)

    def _route_request(self, prompt: str) -> Tuple[OllamaProvider, str]:
        stripped = prompt.strip()
        if stripped.lower().startswith("/think"):
            print("\n[CORTEX] -> Activating Deep Focus Mode (DeepSeek-R1 14B)...")
            # Strip '/think' command and any separator
            clean_prompt = stripped[6:].strip()
            if clean_prompt.startswith(":") or clean_prompt.startswith("-"):
                clean_prompt = clean_prompt[1:].strip()
            return self.deep_brain, clean_prompt

        return self.fast_brain, prompt

    def generate(self, request: LLMRequest) -> LLMResponse:
        provider, clean_prompt = self._route_request(request.prompt)
        request.prompt = clean_prompt
        return provider.generate(request)

    def generate_stream(self, request: LLMRequest) -> Generator[str, None, None]:
        provider, clean_prompt = self._route_request(request.prompt)
        request.prompt = clean_prompt
        return provider.generate_stream(request)


# Clean alias
CortexRouter = ProviderManager
