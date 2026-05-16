# Gesture-Controlled Flappy Bird

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-green?style=for-the-badge)

A computer-vision-based recreation of the classic Flappy Bird game using real-time hand gesture controls.

This project combines **MediaPipe hand tracking**, **OpenCV webcam processing**, and a **Pygame-based physics engine** to replace traditional keyboard controls with gesture-driven interaction.

The project demonstrates practical applications of:

- Human-Computer Interaction (HCI)
- Real-time Computer Vision
- Gesture Recognition
- Physics-based Game Development

---

# Features

- Real-time hand tracking using MediaPipe
- Webcam frame processing with OpenCV
- Gesture-controlled bird movement
- Physics-based gameplay
- Animated bird sprites
- Randomized pipe generation
- Dual scoring system
- Start / Play / Game Over states
- Spacebar fallback controls
- Live webcam preview integrated into the game window

---

# Technologies Used

| Component | Technology | Purpose |
|---|---|---|
| Programming Language | Python 3.11 | Core development |
| Computer Vision | OpenCV | Webcam capture and frame processing |
| Hand Tracking | MediaPipe | Real-time hand landmark detection |
| Game Engine | Pygame | Rendering, animation, and physics |

---

# Project Structure

```text
project/
│
├── birb.py            # Main game file
├── camera.py          # Webcam testing script
├── hand.py            # Hand tracking test
├── test_mp.py         # MediaPipe verification script
│
└── assets/
    ├── background-day.png
    ├── background-night.png
    ├── base.png
    ├── gameover.png
    ├── message.png
    ├── pipe-green.png
    ├── pipe-red.png
    ├── yellowbird-downflap.png
    ├── yellowbird-midflap.png
    ├── yellowbird-upflap.png
    ├── 0.png - 9.png
```

---

# Python Version

This project is tested on:

```text
Python 3.11
```

MediaPipe currently works most reliably on Python 3.9 - 3.11.

If you face installation errors such as:

```text
No matching distribution found
```

make sure you are using Python 3.11 inside a virtual environment.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/gesture-flappy-bird.git
cd gesture-flappy-bird
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

### Mac/Linux

```bash
python3.11 -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install pygame opencv-python mediapipe numpy
```

---

# Running the Project

## Start the Game

```bash
python birb.py
```

Ensure:
- Webcam is connected
- `assets` folder is in the project root directory

---

# Controls

| Action | Control |
|---|---|
| Bird Flap | Raise hand upward |
| Start Game | SPACE |
| Restart Game | SPACE |
| Quit Testing Scripts | Q |

---

# How Gesture Control Works

MediaPipe detects 21 hand landmarks in real time.

The project tracks the:

```text
Wrist Landmark (Index 0)
```

Logic used:

```python
wrist = hand_landmarks.landmark[0]

if wrist.y < 0.5:
    hand_up = True
```

If the wrist moves above the midpoint of the camera frame:
- upward thrust is applied
- the bird flaps upward

Otherwise:
- gravity pulls the bird downward

This creates a natural gesture-based control system.

---

# Game Mechanics

The game loop continuously performs:

1. Webcam frame capture
2. Hand landmark detection
3. Physics updates
4. Pipe generation
5. Collision detection
6. Score updates
7. Sprite rendering

---

# Physics System

The game uses a simple physics model:

- Constant gravity
- Upward thrust force
- Velocity-based movement
- Collision bounds checking

Physics constants:

```python
gravity = 0.35
thrust = -5
```

---

# Scoring System

| Pipe Type | Score |
|---|---|
| Green Pipe | +10 |
| Red Pipe | +20 |

Score increases when the bird successfully passes a pipe.

---

# Game States

| State | Description |
|---|---|
| `"start"` | Waiting for player input |
| `"play"` | Active gameplay |
| `"gameover"` | Collision detected |

---

# Optimization Improvements

The project includes several optimizations:

- Precomputed flipped pipe sprites
- Reusable collision objects
- Modular helper functions
- Cleaner constant management
- Reduced repeated computations

Example optimization:

```python
pipe_green_flip = pygame.transform.flip(
    pipe_green,
    False,
    True
)
```

instead of flipping images every frame.

---

# Testing Scripts

## Test Webcam

```bash
python camera.py
```

Tests whether OpenCV can access the webcam correctly.

---

## Test MediaPipe Installation

```bash
python test_mp.py
```

Verifies MediaPipe installation and version.

---

## Test Hand Tracking

```bash
python hand.py
```

Displays hand tracking and gesture detection independently from the game.

---

# Concepts Demonstrated

- Computer Vision
- Hand Tracking
- Human-Computer Interaction
- Physics Simulation
- Real-Time Rendering
- Collision Detection
- Sprite Animation
- Procedural Obstacle Generation

---

# Future Improvements

Potential future upgrades:

- Sound effects and background music
- Difficulty scaling
- High score saving
- Additional gestures
- Multiple bird skins
- Better performance optimization
- Mobile camera support

---

# Gameplay Preview

(Add gameplay screenshots or video here)

---

# Takeaway

This project started as an experiment after seeing various hand-tracking applications online and wondering how gesture recognition could be integrated into game development.

The idea evolved into combining:
- computer vision
- real-time interaction
- physics simulation
- game programming

into a single interactive system.

Building this project helped improve understanding of:
- real-time processing
- gesture-based interaction systems
- game loop architecture
- cross-domain software integration

while also making the learning process genuinely fun.
