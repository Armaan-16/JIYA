"""
============================================================
JIYA AI Operating System
Automated Unit Tests for Natural Intent Engine
============================================================
"""

import unittest
from SKILLS.intent_engine import IntentEngine


class TestIntentEngine(unittest.TestCase):

    def test_direct_open_kicad(self):
        intent = IntentEngine.parse("open kicad")
        self.assertEqual(intent.intent_type, "OPEN_APP")
        self.assertEqual(intent.target_app, "kicad")

    def test_polite_open_kicad(self):
        intent = IntentEngine.parse("can you open kicad")
        self.assertEqual(intent.intent_type, "OPEN_APP")
        self.assertEqual(intent.target_app, "kicad")

    def test_do_open_kicad(self):
        intent = IntentEngine.parse("/do open kicad")
        self.assertEqual(intent.intent_type, "OPEN_APP")
        self.assertEqual(intent.target_app, "kicad")

    def test_contextual_first_open(self):
        # User said "first open" after talking about kicad
        intent = IntentEngine.parse("first open", last_target_app="kicad")
        self.assertEqual(intent.intent_type, "OPEN_APP")
        self.assertEqual(intent.target_app, "kicad")

    def test_contextual_open_it(self):
        intent = IntentEngine.parse("open it", last_target_app="notepad")
        self.assertEqual(intent.intent_type, "OPEN_APP")
        self.assertEqual(intent.target_app, "notepad")

    def test_type_intent(self):
        intent = IntentEngine.parse("type Hello from Armaan")
        self.assertEqual(intent.intent_type, "TYPE_TEXT")
        self.assertEqual(intent.payload, "Hello from Armaan")

    def test_remember_natural_intent(self):
        intent = IntentEngine.parse("remember that my microcontroller is ESP32")
        self.assertEqual(intent.intent_type, "REMEMBER")
        self.assertEqual(intent.payload, "my microcontroller is ESP32")

    def test_remember_slash_intent(self):
        intent = IntentEngine.parse("/remember I am building a PCB")
        self.assertEqual(intent.intent_type, "REMEMBER")
        self.assertEqual(intent.payload, "I am building a PCB")

    def test_reset_memory_intent(self):
        intent = IntentEngine.parse("reset memory")
        self.assertEqual(intent.intent_type, "RESET_MEMORY")

    def test_exit_intent(self):
        intent = IntentEngine.parse("exit")
        self.assertEqual(intent.intent_type, "EXIT")

    def test_chat_fallback(self):
        intent = IntentEngine.parse("What is the difference between a resistor and a capacitor?")
        self.assertEqual(intent.intent_type, "CHAT")

    def test_app_mention_extraction(self):
        app = IntentEngine.extract_app_mention("I want to design a circuit in KiCad today.")
        self.assertEqual(app, "kicad")


if __name__ == "__main__":
    unittest.main()

