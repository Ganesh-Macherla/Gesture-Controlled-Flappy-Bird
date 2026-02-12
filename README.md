# 🐦 Gesture-Controlled Flappy Bird

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-green?style=for-the-badge)

This project is an interactive, computer-vision-based reimagining of the classic Flappy Bird game.

By integrating **MediaPipe’s hand-tracking** with a physics-based game engine, it replaces traditional keyboard inputs with real-time gesture recognition. The tool serves as a practical demonstration of how **Human-Computer Interaction (HCI)** can be applied to gaming.

---

## 🚀 Key Features

* 🖐️ Neural Gesture Mapping: Uses MediaPipe's 21-point hand landmark model to track movements with sub-millisecond latency.
* ⚡ Real-time Control Pipeline: Processes webcam frames via OpenCV to trigger the "jump" mechanism instantly.
* 🎮 Dynamic Physics Engine: Features simulated gravity and collision masks that respond to your physical movement.
* 📈 Live Performance Overlay: Displays a diagnostic HUD showing hand tracking confidence and connection points.

---

## 🧠 Core Technologies

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Vision Engine** | **OpenCV** | Frame acquisition and image processing |
| **Tracking Model**| **MediaPipe** | 3D Hand Landmark detection |
| **Game Logic** | **Pygame** | Sprite management and physics |
| **Environment** | **Python 3.11** | Optimized compatibility for ML libraries |

---

## ⚠️ Version Compatibility Note

> **Important:** This project officially supports **Python 3.11**.

## ❓ Why Python 3.11?

As of early 2026, while Python 3.13 and 3.14 are out, many heavy-duty AI libraries like MediaPipe still recommend **3.9 to 3.11** for the most stable experience.

This is because they rely on specific C++ bindings that take time to update for every new Python release.


If you encounter a `No matching distribution found` error, please ensure you are using a Python 3.11 virtual environment.

---

## ⚙️ Installation

### Why use a virtual environment?

A virtual environment is a **private sandbox Python installation** just for this project.

It prevents package conflicts and keeps your system Python clean.  
If anything breaks, you can simply delete the environment and recreate it.

---

### 1. Create the environment

```bash
python3.11 -m venv venv
```

This creates a folder named `venv` containing an isolated Python setup.

---

### 2. Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

After activation, your terminal will show:

```
(venv)
```

That means all installs now go inside the sandbox.

---

### 3. Install dependencies

```bash
pip install opencv-python mediapipe pygame numpy
```

---

## 🎮 How to Play

- Launch: Run `python main.py`
- Setup: Position your hand clearly in the webcam view
- Control: Move your hand or index finger upward to make the bird flap
- Goal: Survive as long as possible by navigating through the pipes

---

## 🛠️ Technical Implementation

The system monitors the **y-coordinate of the Index Finger Tip (Landmark 8)**. When a sudden upward velocity is detected:

```
Δy > threshold
```

the bird's vertical velocity is reset to a jump value, counteracting the constant gravity **g** applied in the game loop.

---





