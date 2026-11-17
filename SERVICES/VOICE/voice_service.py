"""
Backward-compatibility shim. Canonical location: VOICE.voice_service and EARS.ear_service
"""
from VOICE.voice_service import VoiceService
from EARS.ear_service import EarService

__all__ = ["VoiceService", "EarService"]