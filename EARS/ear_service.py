"""
============================================================
JIYA AI Operating System
Module: Ear Service (Faster-Whisper STT)
Purpose: Audio recording and speech-to-text transcription.
Author: Armaan Mishra
============================================================
"""

import warnings
from typing import Optional

warnings.filterwarnings("ignore")

try:
    import numpy as np
    import sounddevice as sd
    from faster_whisper import WhisperModel
    EARS_DEPENDENCIES_AVAILABLE = True
except ImportError:
    np = None  # type: ignore
    sd = None  # type: ignore
    WhisperModel = None  # type: ignore
    EARS_DEPENDENCIES_AVAILABLE = False


class EarService:
    """Listens through the microphone and transcribes speech using Faster-Whisper."""

    def __init__(self, model_size: str = "base.en", device: str = "cpu", compute_type: str = "int8"):
        print("\n[SYSTEM] Booting Ears (Faster-Whisper)...")
        self.stt_model = None
        self.ears_ready = False

        if not EARS_DEPENDENCIES_AVAILABLE:
            print("[WARNING] Audio or Faster-Whisper dependencies not installed. Ears disabled.")
            return

        try:
            self.stt_model = WhisperModel(model_size, device=device, compute_type=compute_type)
            self.ears_ready = True
        except Exception as e:
            print(f"[WARNING] Ears failed to boot. Error: {e}")
            self.ears_ready = False

    def listen(self, duration: int = 6) -> str:
        """Records audio from the microphone for the specified duration and returns transcribed text."""
        if not self.ears_ready or self.stt_model is None or sd is None or np is None:
            print("\n[Ears Error]: Speech recognition is not active.")
            return ""

        fs = 16000  # 16kHz sample rate for Whisper
        print(f"\n🎤 [JIYA is Listening for {duration} seconds... Speak now!]")

        try:
            myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
            sd.wait()

            print("⏳ [Processing audio...]")
            audio_data = np.squeeze(myrecording)

            segments, _ = self.stt_model.transcribe(audio_data, beam_size=5)
            text = " ".join([segment.text for segment in segments]).strip()
            return text

        except Exception as e:
            print(f"\n[Microphone Error]: Make sure your mic is enabled! {e}")
            return ""

