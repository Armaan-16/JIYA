"""
============================================================
JIYA AI Operating System
Module: Vision Provider (Qwen2.5-VL Vision & OCR)
Purpose: Multimodal visual understanding, screen reading, and document OCR.
Author: Armaan Mishra
============================================================
"""

import os
import base64
from pathlib import Path
from typing import Optional, Dict, Any, List

try:
    import ollama
    OLLAMA_AVAILABLE = True
except ImportError:
    ollama = None  # type: ignore
    OLLAMA_AVAILABLE = False


class VisionProvider:
    """Multimodal vision and OCR processor powered by Qwen2.5-VL via Ollama."""

    def __init__(self, model_name: str = "qwen2.5vl:7b"):
        self.model_name = model_name
        self.is_ready = OLLAMA_AVAILABLE

    @staticmethod
    def encode_image(image_path: str) -> Optional[str]:
        """Encodes an image file on disk to base64 string."""
        path = Path(image_path)
        if not path.is_file():
            print(f"[VISION ERROR] File not found: {image_path}")
            return None
        try:
            with open(path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        except Exception as e:
            print(f"[VISION ERROR] Failed to encode image: {e}")
            return None

    def analyze_image(self, image_path: str, prompt: str = "Describe this image in detail.") -> str:
        """Sends an image and prompt to the Qwen2.5-VL model for visual comprehension."""
        if not self.is_ready or ollama is None:
            return "Vision service is currently unavailable (Ollama client not configured)."

        path = Path(image_path)
        if not path.exists():
            return f"Image path does not exist: {image_path}"

        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                        "images": [str(path.resolve())]
                    }
                ]
            )
            return response.get("message", {}).get("content", "")
        except Exception as e:
            return f"[VISION ERROR] Analysis failed: {e}"

    def extract_text(self, image_path: str) -> str:
        """Performs optical character recognition (OCR) extracting all text from an image."""
        ocr_prompt = (
            "Extract all printed and handwritten text from this image exactly as written. "
            "Output only the extracted text without commentary."
        )
        return self.analyze_image(image_path=image_path, prompt=ocr_prompt)
