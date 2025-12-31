<h1 align="center">
🔥 TerminalFire
</h1>

[![asciicast](https://asciinema.org/a/765109.svg)](https://asciinema.org/a/765109)

A lightweight terminal fire animation written in Python using the built-in `curses` library. Inspired by classic Doom-style fire effects, this script renders an animated ASCII flame simulation directly in your terminal.

---

## 🔍 Overview

`fire.py` creates a real-time fire effect by simulating heat diffusion across a grid mapped to the terminal screen. Intensity is represented using both ASCII characters and terminal colors, producing a smooth, flickering flame animation.

The program runs until any key is pressed.

---

## 🚀 Features

* Real-time animated fire effect
* ASCII character intensity ramp
* Color-based heat visualization
* Automatically adapts to terminal size
* No external dependencies
* Clean exit on keypress

---

## 🧰 Requirements

* Python **3.6+**
* A Unix-like terminal with color support
* `curses` (included with Python on Linux and macOS)

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/DouglasFreshHabian/fire.py.git
cd fire.py
```

Ensure the script is executable (optional):

```bash
chmod +x fire.py
```

---

## ⚙️ Usage

Run the script from a terminal:

```bash
python3 fire.py
```

or, if executable:

```bash
./fire.py
```

Press **any key** to exit.

---

## 🧠 How It Works (Brief)

* The bottom row of the terminal acts as a heat source.
* Heat values diffuse upward using a simple averaging algorithm.
* Each cell’s heat maps to:

  * an ASCII character (density)
  * a color pair (intensity)
* The buffer updates continuously to create motion.

This approach is efficient and well-suited for real-time terminal animation.

---

## ☕ Support This Project

If **TerminalFire™** helps your OSINT, consider supporting continued development:

<p align="center">
  <a href="https://www.buymeacoffee.com/dfreshZ" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
</p>

---

<!-- 
    Fresh Forensics, LLC | Douglas Fresh Habian | 2025
    github.com/DouglasFreshHabian
    freshforensicsllc@tuta.com
-->

