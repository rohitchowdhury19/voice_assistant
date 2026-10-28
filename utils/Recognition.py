"""Voice / text input for the terminal assistant."""

try:
    import speech_recognition as sr
except ImportError:  # SpeechRecognition not installed
    sr = None


def microphone_available() -> bool:
    """True if SpeechRecognition + PyAudio + a working mic are present."""
    if sr is None:
        return False
    try:
        sr.Microphone()  # raises if PyAudio/mic is missing
        return True
    except Exception:
        return False


def takecommand() -> str:
    """Listen on the microphone and return the recognised text.

    Returns "none" if nothing could be understood.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening... (speak now)")
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=8, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("(heard nothing)")
            return "none"
    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language="en-in")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Speech service unreachable (check your internet connection).")
    return "none"


def take_text_command() -> str:
    """Typed fallback input."""
    try:
        return input("\nYou: ").strip() or "none"
    except EOFError:
        return "exit"
