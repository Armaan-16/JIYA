"""
============================================================
JIYA AI Operating System
Automated Architectural Verification Suite
============================================================
"""

import unittest
from MODELS.llm_request import LLMRequest
from MODELS.llm_response import LLMResponse
from PERSONALITY.jiya_character import JIYACharacter
from BRAIN.cortex_router import ProviderManager
from SKILLS.automation_service import AutomationService
from VISION.vision_provider import VisionProvider


class TestArchitecture(unittest.TestCase):

    def test_models_dataclasses(self):
        req = LLMRequest(prompt="Hello JIYA", history=[{"role": "user", "content": "Hi"}])
        self.assertEqual(req.prompt, "Hello JIYA")
        self.assertEqual(len(req.history), 1)

        res = LLMResponse(success=True, text="Hi Armaan", provider="Ollama", model="qwen3:8b", latency=0.15)
        self.assertTrue(res.success)
        self.assertEqual(res.text, "Hi Armaan")

    def test_personality_system_prompt(self):
        prompt = JIYACharacter.system_prompt(current_project="Testing", location="Burla")
        self.assertIn("JIYA", prompt)
        self.assertIn("Armaan Mishra", prompt)
        self.assertIn("Armaan", prompt)
        self.assertIn("Testing", prompt)

    def test_cortex_router_logic(self):
        router = ProviderManager()
        # Normal prompt routes to fast brain
        provider, clean_prompt = router._route_request("Hello there")
        self.assertEqual(provider.model_name, "qwen3:8b")
        self.assertEqual(clean_prompt, "Hello there")

        # /think prompt routes to deep brain
        deep_provider, deep_prompt = router._route_request("/think What is consciousness?")
        self.assertEqual(deep_provider.model_name, "deepseek-r1:14b")
        self.assertEqual(deep_prompt, "What is consciousness?")

    def test_vision_provider_encode_image(self):
        # Non-existent file returns None safely without raising an unhandled exception
        result = VisionProvider.encode_image("non_existent_file.png")
        self.assertIsNone(result)

    def test_skills_safe_methods(self):
        skills = AutomationService()
        self.assertIsNotNone(skills)


if __name__ == "__main__":
    unittest.main()

