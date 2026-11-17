"""
SKILLS Package
Autonomous desktop control, application launching, and natural intent dispatching.
"""

from SKILLS.automation_service import AutomationService
from SKILLS.intent_engine import IntentEngine, ParsedIntent

__all__ = ["AutomationService", "IntentEngine", "ParsedIntent"]
