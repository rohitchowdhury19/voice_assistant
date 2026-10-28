from datetime import datetime


def greeting_text() -> str:
    hour = datetime.now().hour
    if hour < 12:
        part = "Good Morning"
    elif hour < 17:
        part = "Good Afternoon"
    else:
        part = "Good Evening"
    return f"{part}! I'm your voice assistant. How may I help you?"


def greet(speak):
    speak(greeting_text())
