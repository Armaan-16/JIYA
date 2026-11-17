"""
JIYA Subsystem & Dependency Import Test
"""
import sys
import unittest


class TestImports(unittest.TestCase):

    def test_internal_architecture_imports(self):
        """Verifies that all new modular paths can be imported cleanly."""
        from BRAIN.cortex_router import ProviderManager
        from BRAIN.MEMORY.memory_service import MemoryService
        from PERSONALITY.jiya_character import JIYACharacter
        from SKILLS.automation_service import AutomationService
        from EARS.ear_service import EarService
        from VOICE.voice_service import VoiceService
        from VISION.vision_provider import VisionProvider
        from MODELS.llm_request import LLMRequest
        from MODELS.llm_response import LLMResponse
        from MODELS.base_provider import BaseProvider

        self.assertIsNotNone(ProviderManager)
        self.assertIsNotNone(MemoryService)
        self.assertIsNotNone(JIYACharacter)
        self.assertIsNotNone(AutomationService)
        self.assertIsNotNone(EarService)
        self.assertIsNotNone(VoiceService)
        self.assertIsNotNone(VisionProvider)
        self.assertIsNotNone(LLMRequest)
        self.assertIsNotNone(LLMResponse)
        self.assertIsNotNone(BaseProvider)


if __name__ == "__main__":
    unittest.main()

