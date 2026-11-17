"""
============================================================
JIYA AI Operating System
Main Entry Point (v1.1 - Natural Intent & Action Engine)
============================================================
"""
import sys
import time
import re
from typing import Optional

# Ensure Windows PowerShell/cmd console handles UTF-8 (emojis, unicode) cleanly
if sys.platform == "win32":
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

from BRAIN.cortex_router import ProviderManager
from BRAIN.MEMORY.memory_service import MemoryService
from EARS.ear_service import EarService
from VOICE.voice_service import VoiceService
from SKILLS.automation_service import AutomationService
from SKILLS.intent_engine import IntentEngine, ParsedIntent
from MODELS.llm_request import LLMRequest


def main():
    # Initialize all active modular subsystems
    llm = ProviderManager() 
    memory = MemoryService()
    ears = EarService()
    voice = VoiceService()  
    automation = AutomationService()
    
    conversation_history = []
    MAX_HISTORY = 10
    last_target_app: Optional[str] = None

    print("=" * 60)
    print("      JIYA (AI Operating System - Natural Actions & Voice)")
    print("=" * 60)
    print("\nHi Armaan 😊")
    print("What you can do:")
    print("  • Talk / Chat freely    - (e.g., 'What are we building today?')")
    print("  • Open Applications     - (e.g., 'open kicad', 'open notepad', 'launch brave')")
    print("  • Type for you          - (e.g., 'type Hello world')")
    print("  • Voice Mode            - (e.g., '/voice' to speak into microphone)")
    print("  • Deep Focus Reasoning  - (e.g., '/think solve this algorithm')")
    print("  • Permanent Memory      - (e.g., 'remember my board operates at 3.3V')")
    print("  • Memory Reset          - (e.g., '/reset' to clear memories)")
    print("  • Exit                  - ('exit' to quit)\n")

    while True:
        try:
            raw_prompt = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nJIYA: Goodbye, Armaan! 👋")
            break

        if not raw_prompt:
            continue

        # ==========================================
        # NATURAL INTENT DISPATCHER
        # ==========================================
        intent = IntentEngine.parse(raw_prompt, last_target_app=last_target_app)

        # 1. Exit Intent
        if intent.intent_type == "EXIT":
            print("\nJIYA: Goodbye, Armaan! 👋")
            break

        # 2. Reset Memory Intent
        if intent.intent_type == "RESET_MEMORY":
            memory.clear_all()
            conversation_history.clear()
            print("JIYA: Memory reset! My mind is totally blank.")
            continue

        # 3. Permanent Memory Intent
        if intent.intent_type == "REMEMBER":
            fact = intent.payload
            memory.save_memory(f"Armaan instructed me to remember this fact: {fact}")
            print("JIYA: Got it. I've saved this to my permanent vector memory. 🧠")
            continue

        # 4. Open / Launch Application Intent
        if intent.intent_type == "OPEN_APP":
            target_app = intent.target_app or last_target_app or "kicad"
            last_target_app = target_app

            result = automation.open_application(target_app)
            print(f"JIYA: 🚀 {result}")
            voice.speak(f"Opening {target_app} now.")

            conversation_history.append({"role": "user", "content": raw_prompt})
            conversation_history.append({"role": "assistant", "content": f"Opened {target_app} for you."})
            continue

        # 5. Type Text Intent
        if intent.intent_type == "TYPE_TEXT":
            text_to_type = intent.payload
            print("JIYA: Move your cursor to the text box. I will start typing in 3 seconds...")
            voice.speak("Move your cursor to the text box. I will start typing in 3 seconds.")
            time.sleep(3)
            automation.type_text(text_to_type)
            conversation_history.append({"role": "user", "content": raw_prompt})
            conversation_history.append({"role": "assistant", "content": f"Typed text: {text_to_type}"})
            continue

        # 6. Voice Mode Input Trigger
        is_voice_mode = False
        if intent.intent_type == "VOICE":
            raw_prompt = ears.listen(duration=6)
            if not raw_prompt:
                print("JIYA: I didn't catch that. Try again.")
                continue
            print(f"You (Spoken): {raw_prompt}")
            is_voice_mode = True

            # If spoken input was an action (e.g. "open kicad"), dispatch it immediately!
            spoken_intent = IntentEngine.parse(raw_prompt, last_target_app=last_target_app)
            if spoken_intent.intent_type == "OPEN_APP":
                target_app = spoken_intent.target_app or last_target_app or "kicad"
                last_target_app = target_app
                result = automation.open_application(target_app)
                print(f"JIYA: 🚀 {result}")
                voice.speak(f"Opening {target_app} now.")
                conversation_history.append({"role": "user", "content": raw_prompt})
                conversation_history.append({"role": "assistant", "content": f"Opened {target_app} for you."})
                continue

        # Check if conversation mentions an application to track contextual state
        app_mention = IntentEngine.extract_app_mention(raw_prompt)
        if app_mention:
            last_target_app = app_mention

        # ==========================================
        # RETRIEVE PAST MEMORIES (BRAIN/MEMORY)
        # ==========================================
        search_query = intent.payload if intent.intent_type == "THINK" else raw_prompt
        relevant_memories = memory.recall(search_query) if search_query else []
        
        augmented_prompt = raw_prompt
        if relevant_memories:
            context_block = "\n\n[SYSTEM NOTE: Relevant past memories for context:]\n"
            if isinstance(relevant_memories, list):
                for mem in relevant_memories:
                    context_block += f"- {mem}\n"
            else:
                context_block += f"- {relevant_memories}\n"
            augmented_prompt = raw_prompt + context_block

        # ==========================================
        # GENERATE RESPONSE (BRAIN / CORTEX ROUTER)
        # ==========================================
        request = LLMRequest(prompt=augmented_prompt, history=conversation_history)

        print("\nJIYA: ", end="", flush=True)
        full_response_text = ""
        
        for token in llm.generate_stream(request):
            sys.stdout.write(token)
            sys.stdout.flush()
            full_response_text += token
        print("\n")

        # If voice mode was used, speak back using Bella voice (VOICE)
        if is_voice_mode:
            print("🔊 [JIYA is speaking...]")
            spoken_text = full_response_text.split("</think>")[-1].strip()
            if spoken_text:
                voice.speak(spoken_text)

        # ==========================================
        # SAVE TO SHORT-TERM MEMORY (SLIDING WINDOW)
        # ==========================================
        clean_assistant_reply = re.sub(r'<think>.*?</think>', '', full_response_text, flags=re.DOTALL).strip()
        if not clean_assistant_reply:
            clean_assistant_reply = full_response_text

        conversation_history.append({"role": "user", "content": raw_prompt})
        conversation_history.append({"role": "assistant", "content": clean_assistant_reply})

        if len(conversation_history) > MAX_HISTORY:
            conversation_history = conversation_history[-MAX_HISTORY:]


if __name__ == "__main__":
    main()