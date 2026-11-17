"""
============================================================
JIYA AI Operating System
Module: Voice Service (Kokoro TTS Mouth)
Purpose: Text-to-speech synthesis and audio playback.
Author: Armaan Mishra
============================================================
"""

import warnings
from typing import Optional

warnings.filterwarnings("ignore")

try:
    import sounddevice as sd
    SOUNDDEVICE_AVAILABLE = True
except ImportError:
    sd = None  # type: ignore
    SOUNDDEVICE_AVAILABLE = False


class VoiceService:
    """Voice output engine utilizing Kokoro TTS (Bella American English voice profile)."""

    def __init__(self, lang_code: str = 'a', voice_profile: str = 'af_bella'):
        print("\n[SYSTEM] Booting Mouth (Kokoro TTS - Bella)...")
        self.tts_pipeline = None
        self.tts_voice = voice_profile
        self.mouth_ready = False

        try:
            from kokoro import KPipeline
            self.tts_pipeline = KPipeline(lang_code=lang_code)
            self.mouth_ready = True
        except Exception as e:
            print(f"[WARNING] Kokoro TTS mouth failed to boot. Error: {e}")
            self.mouth_ready = False

    def speak(self, text: str) -> None:
        """Converts text to speech and plays it through the system audio device."""
        if not text or not text.strip():
            return

        clean_text = text.strip()

        if self.mouth_ready and self.tts_pipeline is not None and SOUNDDEVICE_AVAILABLE and sd is not None:
            try:
                generator = self.tts_pipeline(clean_text, voice=self.tts_voice)
                for i, (_, _, audio) in enumerate(generator):
                    sd.play(audio, samplerate=24000)
                    sd.wait()
                return
            except Exception as e:
                print(f"\n[TTS Error]: {e}")

        # Platform-native fallback if Kokoro is unavailable
        self._fallback_speak(clean_text)

    def _fallback_speak(self, text: str) -> None:
        """Fallback to Windows SAPI speech synthesis if Kokoro is not available."""
        try:
            import subprocess
            clean_escaped = text.replace('"', '""').replace("'", "''")
            cmd = f"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{clean_escaped}')"
            subprocess.run(["powershell", "-NoProfile", "-Command", cmd], capture_output=True, timeout=10)
        except Exception:
            pass

