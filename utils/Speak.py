"""Text-to-speech wrapper.

Works on Windows (SAPI5), macOS (NSSpeechSynthesizer) and Linux (eSpeak)
through pyttsx3. If no speech engine is available, the assistant keeps
working and simply prints its answers.
"""

_engine = None
_engine_failed = False


def _get_engine():
    global _engine, _engine_failed
    if _engine is not None or _engine_failed:
        return _engine
    try:
        import pyttsx3

        _engine = pyttsx3.init()  # picks the right driver for the OS
        _engine.setProperty("rate", 170)
        voices = _engine.getProperty("voices")
        # Prefer a female/second voice if one exists (original behaviour).
        if voices and len(voices) > 1:
            _engine.setProperty("voice", voices[1].id)
    except Exception:
        _engine_failed = True
        _engine = None
    return _engine


def speech_available() -> bool:
    return _get_engine() is not None


def speak(text: str, voice: bool = True) -> None:
    """Print the assistant's reply and, if possible, say it aloud."""
    print(f"Assistant: {text}")
    if not voice:
        return
    engine = _get_engine()
    if engine is None:
        return
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception:
        pass
