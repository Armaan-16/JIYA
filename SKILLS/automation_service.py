"""
============================================================
JIYA AI Operating System
Module: Automation Service (Skills & Desktop Hands)
Purpose: Controls keyboard and mouse actions, launching desktop applications
         via direct Windows paths and PyAutoGUI fallback.
Author: Armaan Mishra
============================================================
"""

import os
import glob
import time
import shutil
import subprocess
from pathlib import Path
from typing import Optional, Dict

try:
    import pyautogui
    PYAUTOGUI_AVAILABLE = True
except ImportError:
    pyautogui = None  # type: ignore
    PYAUTOGUI_AVAILABLE = False


class AutomationService:
    """Desktop automation skills executing keyboard, GUI, and application launches."""

    # Common Windows executable paths for instant, reliable launch
    KNOWN_APP_PATHS: Dict[str, str] = {
        "notepad": "notepad.exe",
        "calc": "calc.exe",
        "calculator": "calc.exe",
        "cmd": "cmd.exe",
        "powershell": "powershell.exe",
        "terminal": "wt.exe",
        "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "code": "code",
        "vscode": "code",
        "vs code": "code",
    }

    def __init__(self):
        print("\n[SYSTEM] Booting Hands (PyAutoGUI Automation & Native Process Launcher)...")
        if PYAUTOGUI_AVAILABLE and pyautogui is not None:
            pyautogui.FAILSAFE = True
            pyautogui.PAUSE = 0.1
            self.is_ready = True
        else:
            print("[WARNING] PyAutoGUI is not installed. GUI automation fallback disabled.")
            self.is_ready = True  # Native process launching remains available!

    def _resolve_kicad_path(self) -> Optional[str]:
        """Locates the installed KiCad executable across Program Files."""
        candidates = [
            r"C:\Program Files\KiCad\10.0\bin\kicad.exe",
            r"C:\Program Files\KiCad\bin\kicad.exe",
            r"C:\Program Files (x86)\KiCad\bin\kicad.exe",
        ]
        for c in candidates:
            if os.path.isfile(c):
                return c

        # Glob search for any KiCad version
        matches = glob.glob(r"C:\Program Files\KiCad\*\bin\kicad.exe")
        if matches:
            return matches[0]

        return None

    def open_application(self, app_name: str) -> str:
        """
        Launches an application using a 2-tier strategy:
        1. Direct Windows execution (Fast, 0ms latency, doesn't interfere with mouse/keyboard)
        2. PyAutoGUI Windows Start Search fallback
        """
        clean_name = app_name.strip().lower()
        print(f"🤖 [JIYA is opening {app_name}...]")

        # Special resolver for KiCad
        if "kicad" in clean_name:
            kicad_exe = self._resolve_kicad_path()
            if kicad_exe:
                try:
                    subprocess.Popen([kicad_exe])
                    return f"Successfully launched KiCad ({kicad_exe})."
                except Exception as e:
                    print(f"[LAUNCH ERROR] Direct KiCad launch failed: {e}")

        # Check known direct executable map
        if clean_name in self.KNOWN_APP_PATHS:
            target = self.KNOWN_APP_PATHS[clean_name]
            try:
                if os.path.isabs(target) and os.path.exists(target):
                    subprocess.Popen([target])
                    return f"Successfully launched {app_name}."
                elif shutil.which(target):
                    subprocess.Popen([target], shell=True)
                    return f"Successfully launched {app_name}."
            except Exception as e:
                print(f"[LAUNCH ERROR] Direct execution failed: {e}")

        # Check if in PATH
        which_path = shutil.which(clean_name)
        if which_path:
            try:
                subprocess.Popen([which_path])
                return f"Successfully launched {app_name}."
            except Exception:
                pass

        # Tier 2: PyAutoGUI Windows Start Menu Automation
        if PYAUTOGUI_AVAILABLE and pyautogui is not None:
            try:
                pyautogui.press('win')
                time.sleep(0.4)
                pyautogui.write(app_name, interval=0.03)
                time.sleep(0.5)
                pyautogui.press('enter')
                return f"Sent command to open {app_name} via Windows Start Menu."
            except Exception as e:
                return f"Failed to open {app_name} via GUI automation: {e}"

        return f"Could not find or launch {app_name} on this system."

    def type_text(self, text: str) -> str:
        """Simulates keyboard keystrokes to type strings into the active window."""
        if not PYAUTOGUI_AVAILABLE or pyautogui is None:
            return "Automation service unavailable. PyAutoGUI is not installed."

        try:
            print("🤖 [JIYA is typing...]")
            pyautogui.write(text, interval=0.02)
            return "Successfully typed the text."
        except Exception as e:
            return f"Failed to type text. Error: {e}"
