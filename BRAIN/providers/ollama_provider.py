"""
============================================================
JIYA AI Operating System
Module: Ollama Provider (Resilient Multi-Model Engine)
Purpose: Implements BaseProvider for local Ollama instances with
         automatic CUDA-to-CPU self-healing failover.
Author: Armaan Mishra
============================================================
"""

from typing import Generator, Any, Dict, List, Optional
import sys
import ollama

from MODELS.base_provider import BaseProvider
from MODELS.llm_request import LLMRequest
from MODELS.llm_response import LLMResponse
from PERSONALITY.jiya_character import JIYACharacter


class OllamaProvider(BaseProvider):
    """Local Ollama inference backend with automatic VRAM-safe layer offloading and CPU failover."""

    def __init__(self, model: str = "qwen3:8b", think: bool = False):
        self.model_name = model
        self.think_enabled = think

        # 14B models need safe layer bounds on 6GB VRAM GPUs (e.g. RTX 4050)
        # 20 layers offloaded to GPU allows fast hybrid inference without buffer overrun
        self.default_num_gpu: Optional[int] = 20 if "14b" in model.lower() else None

    def get_system_prompt(self) -> str:
        """Dynamically generates system prompt with live timestamp per request."""
        return JIYACharacter.system_prompt(
            current_project="JIYA Architecture & OS Build",
            location="Burla, Odisha"
        )

    def _build_options(self, num_gpu: Optional[int] = None) -> Dict[str, Any]:
        """Constructs Ollama runtime options with GPU layer controls."""
        opts: Dict[str, Any] = {
            "temperature": 0.6,
            "num_predict": 4096,
        }
        target_gpu = num_gpu if num_gpu is not None else self.default_num_gpu
        if target_gpu is not None:
            opts["num_gpu"] = target_gpu
        return opts

    def _is_cuda_or_memory_error(self, err_msg: str) -> bool:
        """Detects whether an error is caused by CUDA, VRAM exhaustion, or llama-server crash."""
        lower_err = err_msg.lower()
        return any(indicator in lower_err for indicator in [
            "cuda",
            "llama-server",
            "0xc0000409",
            "status code: 500",
            "out of memory",
            "shared object initialization failed",
            "buffer overrun",
            "terminated",
        ])

    def generate(self, request: LLMRequest) -> LLMResponse:
        system_prompt = self.get_system_prompt()
        messages = [{"role": "system", "content": system_prompt}]
        if request.history:
            messages.extend(request.history)
        messages.append({"role": "user", "content": request.prompt})

        # Attempt 1: Standard or partial GPU offload
        options = self._build_options()
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=messages,
                think=self.think_enabled,
                options=options
            )
            return LLMResponse(
                success=True,
                text=response["message"]["content"],
                provider="Ollama",
                model=self.model_name
            )
        except Exception as e:
            err_str = str(e)
            if self._is_cuda_or_memory_error(err_str):
                print(f"\n[SYSTEM] ⚠️ GPU memory limit reached on '{self.model_name}'. Rerouting to CPU mode...")
                try:
                    cpu_options = self._build_options(num_gpu=0)
                    response = ollama.chat(
                        model=self.model_name,
                        messages=messages,
                        think=self.think_enabled,
                        options=cpu_options
                    )
                    return LLMResponse(
                        success=True,
                        text=response["message"]["content"],
                        provider="Ollama (CPU Fallback)",
                        model=self.model_name
                    )
                except Exception as cpu_err:
                    err_str = str(cpu_err)

            return LLMResponse(
                success=False,
                text="",
                provider="Ollama",
                model=self.model_name,
                error=err_str
            )

    def generate_stream(self, request: LLMRequest) -> Generator[str, None, None]:
        system_prompt = self.get_system_prompt()
        messages = [{"role": "system", "content": system_prompt}]
        if request.history:
            messages.extend(request.history)
        messages.append({"role": "user", "content": request.prompt})

        options = self._build_options()

        # Generator initiation with automated CPU failover
        try:
            response_stream = ollama.chat(
                model=self.model_name,
                messages=messages,
                stream=True,
                think=self.think_enabled,
                options=options
            )
            # Pull first chunk to verify connection without failing midway
            first_chunk = next(response_stream)
            yield first_chunk["message"]["content"]

            for chunk in response_stream:
                yield chunk["message"]["content"]

        except Exception as e:
            err_str = str(e)
            if self._is_cuda_or_memory_error(err_str):
                sys.stdout.write(f"\n[SYSTEM] ⚠️ GPU memory limit reached on '{self.model_name}'. Rerouting to CPU mode...\n")
                sys.stdout.flush()
                try:
                    cpu_options = self._build_options(num_gpu=0)
                    cpu_stream = ollama.chat(
                        model=self.model_name,
                        messages=messages,
                        stream=True,
                        think=self.think_enabled,
                        options=cpu_options
                    )
                    for chunk in cpu_stream:
                        yield chunk["message"]["content"]
                    return
                except Exception as cpu_err:
                    err_str = str(cpu_err)

            yield f"\n❌ Error: {err_str}"
