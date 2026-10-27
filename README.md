# 🎙️ Python Voice Assistant

A modular, intelligent desktop voice assistant developed in Python. It listens to user voice input via speech recognition, responds with clear text-to-speech audio, offers time-sensitive contextual greetings, and integrates with MongoDB for storing reminders and tasks.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Repository](https://img.shields.io/badge/GitHub-rohitchowdhury19%2Fvoice__assistant-181717.svg?logo=github)](https://github.com/rohitchowdhury19/voice_assistant)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📑 Table of Contents

- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Getting Started](#-getting-started)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create & Activate Virtual Environment](#2-create--activate-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Environment Variables Configuration](#4-environment-variables-configuration)
- [Running the Application](#-running-the-application)
- [Modules Overview](#-modules-overview)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- **🗣️ Speech Recognition**: Captures microphone input and converts spoken words into text using Google Speech Recognition (`speech_recognition`).
- **🔊 Text-to-Speech (TTS)**: Delivers clear, offline voice feedback using `pyttsx3` with Windows SAPI5 voice engine.
- **⏰ Contextual Greetings**: Dynamically greets the user based on the time of day (Good Morning, Good Afternoon, or Good Evening).
- **🗄️ MongoDB Integration**: Connects to MongoDB to persist reminders and tasks seamlessly.
- **🧩 Modular Architecture**: Separation of concerns across dedicated packages (`features/` and `utils/`) for effortless extensibility.

---

## 🏗️ Project Architecture

```text
voice_assistant/
│
├── features/
│   ├── __init__.py           # Features package initialization
│   ├── greet.py              # Time-aware greeting logic
│   └── test.py               # Feature testing script
│
├── utils/
│   ├── __init__.py           # Utilities package initialization
│   ├── Recognition.py        # Voice input capture & speech-to-text
│   └── Speak.py              # Speech synthesis / TTS engine wrapper
│
├── .gitignore                # Git ignore patterns
├── main.py                   # Main application entry point
├── mongo.py                  # MongoDB database connection & operations
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🛠️ Tech Stack

- **Language:** [Python 3.8+](https://www.python.org/)
- **Speech Recognition:** [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) (Google Web Speech API)
- **Text-to-Speech:** [pyttsx3](https://pypi.org/project/pyttsx3/) (SAPI5 on Windows)
- **Database:** [MongoDB](https://www.mongodb.com/) via [PyMongo](https://pypi.org/project/pymongo/)
- **Configuration:** [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📋 Prerequisites

Before getting started, make sure you have:

1. **Python 3.8+** installed on your system.
2. A working **Microphone** and **Speakers/Headphones**.
3. **Windows OS** (recommended for SAPI5 TTS engine support).
4. A **MongoDB** instance (local server or [MongoDB Atlas](https://www.mongodb.com/atlas) cloud cluster).

---

## 🚀 Getting Started

### 1. Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/rohitchowdhury19/voice_assistant.git
cd voice_assistant
```

### 2. Create & Activate Virtual Environment

It is recommended to use a virtual environment to manage dependencies:

- **Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```

- **Windows (Command Prompt):**
  ```cmd
  python -m venv venv
  venv\Scripts\activate.bat
  ```

- **Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

> **Note:** If you are running speech recognition and database features, make sure these additional dependencies are installed:
> ```bash
> pip install SpeechRecognition pyaudio pymongo python-dotenv
> ```
> *(On Windows, if `pyaudio` fails to build, install it via pre-built wheels: `pip install pipwin && pipwin install pyaudio` or download the appropriate `.whl` file).*

### 4. Environment Variables Configuration

Create a `.env` file in the root directory for database configuration:

```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority
```

---

## 💻 Running the Application

### Start the Voice Assistant

Run the main application script:

```bash
python main.py
```

The assistant will initialize the speech engine, greet you according to the current time, and begin listening for your voice commands.

### Test MongoDB Reminders

To test the MongoDB database integration for reminders:

```bash
python mongo.py
```

---

## 📦 Modules Overview

| Module | File | Description |
|---|---|---|
| **Entry Point** | `main.py` | Orchestrates the greeting and initiates the voice command loop. |
| **Greeting** | `features/greet.py` | Determines system time and triggers an appropriate vocal greeting. |
| **Speech Recognition** | `utils/Recognition.py` | Listens through the default microphone, adjusts for ambient noise, and returns recognized text. |
| **Text-to-Speech** | `utils/Speak.py` | Initializes the `pyttsx3` voice engine (SAPI5) and vocalizes passed text strings. |
| **Database** | `mongo.py` | Connects to MongoDB, manages collections, and inserts reminder documents. |

---

## 🗺️ Roadmap

- [ ] Add continuous listening and hotword/wake-word detection (e.g., "Hey Assistant").
- [ ] Add web browsing and search capabilities (Wikipedia, Google, YouTube).
- [ ] Add real-time weather and news updates.
- [ ] Add system automation controls (open apps, volume control, shutdown/restart).
- [ ] Implement full conversational CRUD for MongoDB-backed reminders and calendar events.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the Project: [https://github.com/rohitchowdhury19/voice_assistant](https://github.com/rohitchowdhury19/voice_assistant)
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

Made with ❤️ by [Rohit Chowdhury](https://github.com/rohitchowdhury19)