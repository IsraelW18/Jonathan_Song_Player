# Jonathan Song Player 🎵

A simple yet educational Python project that plays a familiar children's melody  
using the PC speaker (`winsound`) while displaying real-time visual progress in the terminal.

This project combines **sound, terminal output, and modular architecture** – ideal for beginners who want to explore creative Python applications beyond basic scripts.

---

## 🎯 Project Purpose

This script demonstrates how to:
- Play melodies using terminal-based Python
- Structure a small-scale Python project with reusable modules
- Combine sound logic with a basic text-based UI (progress bar per note)

---

## 🎥 Demo

![Console demo of melody playback](./jonathan_song_demo.gif)

---

## 🗂 Project Structure

```bash
jonathan_song_player/
├── main.py                  # Entry point – runs the full melody
├── README.md                # Project documentation
├── requirements.txt         # Dependencies (winsound is built-in on Windows)
└── player/
    ├── __init__.py
    ├── melody.py            # Note data and melody definitions
    ├── playback.py          # Plays the melody and prints progress
    └── utils.py             # Utility: clears the screen
```

---

## 🧠 Educational Value

- Teaches how to work with **winsound** and sound duration logic
- Reinforces modular thinking in Python
- Shows how to build a clean, documented project structure
- Encourages creative use of basic terminal output

---

## 🚀 Requirements

- Python 3.x  
- Windows OS (uses built-in `winsound` module – not supported on Linux/macOS)

---

## ▶️ Run

```bash
python main.py
```

---

## 🤝 Contributing

Pull requests and ideas are welcome!  
Feel free to fork this repo or open an issue to suggest improvements.

---

## 👨‍💻 Developer

**Israel Wasserman**  
[LinkedIn Profile](https://www.linkedin.com/in/israel-wasserman)