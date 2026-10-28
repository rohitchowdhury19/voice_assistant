
import difflib
import random
import re
from datetime import datetime

ASSISTANT_NAME = "Jarvis"


def _time():
    return "It is " + datetime.now().strftime("%I:%M %p").lstrip("0") + "."


def _date():
    return "Today is " + datetime.now().strftime("%A, %d %B %Y") + "."


def _day():
    return "Today is " + datetime.now().strftime("%A") + "."


def _joke():
    return random.choice([
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "I would tell you a UDP joke, but you might not get it.",
        "There are 10 kinds of people: those who understand binary and those who don't.",
    ])


RESPONSES = {
    ("hello", "hi", "hey", "hii"):
        "Hello! Nice to hear from you.",
    ("how are you", "how are you doing", "how do you do"):
        "I'm doing great, thank you for asking!",
    ("your name", "who are you", "what are you"):
        f"I'm {ASSISTANT_NAME}, a simple voice assistant that answers predefined questions.",
    ("who made you", "who created you", "who is your creator"):
        "I was created by Rohit Chowdhury in Python.",
    ("what can you do", "what do you do", "your features", "your abilities"):
        "I can tell you the time and date, share a joke, and answer a few "
        "predefined questions. Say 'help' to hear them all.",
    ("what time", "current time", "time now", "tell me the time", "time is it"):
        _time,
    ("what date", "today's date", "todays date", "current date", "date today"):
        _date,
    ("what day", "which day", "day today"):
        _day,
    ("joke", "make me laugh", "something funny"):
        _joke,
    ("thank you", "thanks"):
        "You're welcome!",
    ("good morning",):
        "Good morning! I hope you have a wonderful day.",
    ("good night",):
        "Good night! Sleep well.",
    ("what is python", "tell me about python"):
        "Python is a high-level, general-purpose programming language known for its readable syntax.",
    ("what is ai", "what is artificial intelligence"):
        "Artificial intelligence is the ability of machines to perform tasks that normally need human intelligence.",
    ("where do you live", "where are you from"):
        "I live inside your computer's terminal.",
    ("are you human", "are you a robot"):
        "I'm a program, not a human, but I try to be friendly.",
}

HELP_TEXT = (
    "You can ask me things like: hello, how are you, what is your name, "
    "what time is it, what is today's date, what day is it, tell me a joke, "
    "what is Python, what is AI, who made you. Say 'exit' or 'bye' to quit."
)

EXIT_WORDS = ("exit", "quit", "bye", "goodbye", "stop", "see you")
FALLBACK = "Sorry, I don't know the answer to that. Say 'help' to hear what I can answer."


def _normalize(text: str) -> str:
    text = text.lower().replace("'", "")
    return re.sub(r"[^a-z0-9 ]+", " ", text).strip()


def _phrase_in(phrase: str, text: str) -> bool:
    return re.search(rf"\b{re.escape(_normalize(phrase))}\b", text) is not None


def is_exit(command: str) -> bool:
    text = _normalize(command)
    return any(_phrase_in(w, text) for w in EXIT_WORDS)


def get_response(command: str) -> str:
   
    text = _normalize(command)
    if not text or text == "none":
        return FALLBACK

    if _phrase_in("help", text):
        return HELP_TEXT

   
    best, best_len = None, 0
    for phrases, answer in RESPONSES.items():
        for p in phrases:
            if _phrase_in(p, text) and len(p) > best_len:
                best, best_len = answer, len(p)

    
    if best is None:
        all_phrases = {p: a for ps, a in RESPONSES.items() for p in ps}
        close = difflib.get_close_matches(text, all_phrases.keys(), n=1, cutoff=0.75)
        if close:
            best = all_phrases[close[0]]

    if best is None:
        return FALLBACK
    return best() if callable(best) else best
