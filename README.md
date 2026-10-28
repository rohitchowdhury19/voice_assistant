# Terminal Voice Assistant (predefined answers)

A terminal-based voice assistant in Python. It listens through your microphone,
answers out loud and in the terminal, and **only answers questions from a
predefined list**. Anything else gets a polite "I don't know".

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

PyAudio notes: Windows `pip install pyaudio` usually works; macOS
`brew install portaudio` first; Linux `sudo apt install portaudio19-dev espeak`.

## Run

```bash
python main.py          # voice mode (auto-falls back to typing if no mic)
python main.py --text   # type commands
python main.py --mute   # print answers only, no speech
```

Say or type `help` to list questions, and `exit` / `bye` to quit.
Speech recognition uses Google's free service, so voice input needs internet.

## Add your own answers

Edit `features/responses.py` and add an entry to `RESPONSES`:

```python
("your favourite colour", "favorite colour"): "I like blue.",
```

A value can also be a function returning a string (like the time/date answers).

## Structure

```
main.py                  # terminal loop
features/greet.py        # time-aware greeting
features/responses.py    # predefined Q&A + matching logic
utils/Recognition.py     # microphone / typed input
utils/Speak.py           # text-to-speech (cross-platform, optional)
```
