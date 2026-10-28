

import argparse

from features import greet, get_response, is_exit
from utils import (
    speak,
    speech_available,
    takecommand,
    take_text_command,
    microphone_available,
)


def main():
    parser = argparse.ArgumentParser(description="Terminal voice assistant")
    parser.add_argument("--text", action="store_true", help="type instead of speaking")
    parser.add_argument("--mute", action="store_true", help="print answers without speaking")
    args = parser.parse_args()

    use_voice_out = not args.mute and speech_available()
    say = lambda t: speak(t, voice=use_voice_out)

    use_mic = not args.text and microphone_available()
    if not args.text and not use_mic:
        print("[!] Microphone not available - switching to typed input.")
    if not args.mute and not use_voice_out:
        print("[!] Text-to-speech not available - answers will be printed only.")

    print("=" * 50)
    print(" Voice Assistant  |  say/type 'help' for commands")
    print(" Say/type 'exit' to quit")
    print("=" * 50)

    greet(say)

    try:
        while True:
            command = takecommand() if use_mic else take_text_command()
            if command == "none":
                continue
            if is_exit(command):
                say("Goodbye! Have a nice day.")
                break
            say(get_response(command))
    except KeyboardInterrupt:
        print()
        say("Goodbye!")


if __name__ == "__main__":
    main()
