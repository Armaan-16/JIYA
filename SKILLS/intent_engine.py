"""
============================================================
JIYA AI Operating System
Module: Intent Engine (Natural Language Action Dispatcher)
Purpose: Parses user prompts to recognize natural action commands
         (open apps, type text, memory, reasoning, voice) without
         requiring rigid slash prefixes.
Author: Armaan Mishra
============================================================
"""

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class ParsedIntent:
    """Structured representation of a recognized user intent."""
    intent_type: str  # 'OPEN_APP', 'TYPE_TEXT', 'REMEMBER', 'RESET_MEMORY', 'VOICE', 'THINK', 'EXIT', 'CHAT'
    payload: str = ""
    target_app: Optional[str] = None


class IntentEngine:
    """Parses natural language commands for the JIYA Operating System."""

    # Regex patterns for opening applications
    OPEN_PATTERNS = [
        # "/do open kicad", "open kicad", "launch kicad", "start kicad", "run kicad"
        re.compile(r"^(?:/do\s+)?(?:please\s+|can\s+you\s+|could\s+you\s+|jiya[,\s]+)?(?:open|launch|start|run)\s+([a-zA-Z0-9_\-\.\s]+)$", re.IGNORECASE),
        # "open up kicad"
        re.compile(r"^(?:please\s+|can\s+you\s+)?open\s+up\s+([a-zA-Z0-9_\-\.\s]+)$", re.IGNORECASE),
        # "first open kicad"
        re.compile(r"^first\s+(?:open|launch|start)\s+([a-zA-Z0-9_\-\.\s]+)$", re.IGNORECASE),
    ]

    # Patterns for context-dependent follow-up open ("first open", "open it", "open that")
    CONTEXT_OPEN_PATTERNS = [
        re.compile(r"^first\s+open(?:\s+it|\s+that)?$", re.IGNORECASE),
        re.compile(r"^open\s+(?:it|that)$", re.IGNORECASE),
        re.compile(r"^just\s+open(?:\s+it|\s+that)?$", re.IGNORECASE),
        re.compile(r"^first\s+launch(?:\s+it|\s+that)?$", re.IGNORECASE),
    ]

    # Regex patterns for typing text
    TYPE_PATTERNS = [
        re.compile(r"^(?:/do\s+)?(?:please\s+|can\s+you\s+|jiya[,\s]+)?(?:type|write)\s+(?:out\s+)?(.+)$", re.IGNORECASE),
    ]

    # Patterns for memory
    REMEMBER_PATTERNS = [
        re.compile(r"^/remember\s+(.+)$", re.IGNORECASE),
        re.compile(r"^(?:please\s+|jiya[,\s]+)?remember\s+(?:that\s+)?(.+)$", re.IGNORECASE),
    ]

    # Patterns for memory reset
    RESET_PATTERNS = [
        re.compile(r"^/reset$", re.IGNORECASE),
        re.compile(r"^(?:reset|wipe|clear)\s+(?:all\s+)?(?:my\s+)?(?:vector\s+)?memory$", re.IGNORECASE),
    ]

    # Patterns for deep reasoning
    THINK_PATTERNS = [
        re.compile(r"^/think(?:\s*[:\-]?\s*)(.+)$", re.IGNORECASE),
        re.compile(r"^(?:deep\s+think|reason\s+through|think\s+deeply\s+about)\s+(.+)$", re.IGNORECASE),
    ]

    # Patterns for voice mode
    VOICE_PATTERNS = [
        re.compile(r"^/voice$", re.IGNORECASE),
        re.compile(r"^(?:voice|voice\s+mode|listen\s+to\s+me|start\s+listening)$", re.IGNORECASE),
    ]

    # Patterns for exiting
    EXIT_PATTERNS = [
        re.compile(r"^(?:exit|quit|bye|goodbye|close\s+os|shutdown)$", re.IGNORECASE),
    ]

    @classmethod
    def parse(cls, prompt: str, last_target_app: Optional[str] = None) -> ParsedIntent:
        """Parses a user string into a structured intent."""
        cleaned = prompt.strip()
        if not cleaned:
            return ParsedIntent(intent_type="EMPTY")

        # 1. Exit check
        for pattern in cls.EXIT_PATTERNS:
            if pattern.match(cleaned):
                return ParsedIntent(intent_type="EXIT")

        # 2. Reset check
        for pattern in cls.RESET_PATTERNS:
            if pattern.match(cleaned):
                return ParsedIntent(intent_type="RESET_MEMORY")

        # 3. Voice mode check
        for pattern in cls.VOICE_PATTERNS:
            if pattern.match(cleaned):
                return ParsedIntent(intent_type="VOICE")

        # 4. Remember check
        for pattern in cls.REMEMBER_PATTERNS:
            m = pattern.match(cleaned)
            if m:
                fact = m.group(1).strip()
                return ParsedIntent(intent_type="REMEMBER", payload=fact)

        # 5. Think / Deep reasoning check
        for pattern in cls.THINK_PATTERNS:
            m = pattern.match(cleaned)
            if m:
                query = m.group(1).strip()
                return ParsedIntent(intent_type="THINK", payload=query)

        # 6. Contextual open ("first open", "open it")
        for pattern in cls.CONTEXT_OPEN_PATTERNS:
            if pattern.match(cleaned):
                app = last_target_app if last_target_app else "kicad"
                return ParsedIntent(intent_type="OPEN_APP", target_app=app, payload=cleaned)

        # 7. Direct open application check ("open kicad", "can you open brave")
        for pattern in cls.OPEN_PATTERNS:
            m = pattern.match(cleaned)
            if m:
                app = m.group(1).strip()
                # Exclude purely conversational words like "a discussion", "your mind", etc.
                if app.lower() not in ["a discussion", "up", "your mind", "a question"]:
                    return ParsedIntent(intent_type="OPEN_APP", target_app=app, payload=cleaned)

        # 8. Type text check
        for pattern in cls.TYPE_PATTERNS:
            m = pattern.match(cleaned)
            if m:
                text = m.group(1).strip()
                return ParsedIntent(intent_type="TYPE_TEXT", payload=text)

        # 9. Fallback to conversation / chat
        return ParsedIntent(intent_type="CHAT", payload=cleaned)

    @classmethod
    def extract_app_mention(cls, text: str) -> Optional[str]:
        """Extracts any mentioned desktop application in conversational text to track context."""
        lowered = text.lower()
        known_apps = [
            "kicad", "notepad", "calculator", "calc", "brave", "chrome",
            "vs code", "vscode", "spotify", "discord", "terminal", "powershell"
        ]
        for app in known_apps:
            if re.search(rf"\b{re.escape(app)}\b", lowered):
                return app
        return None
