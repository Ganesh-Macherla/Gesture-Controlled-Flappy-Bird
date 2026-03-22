#  Gesture-Controlled Flappy Bird

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-green?style=for-the-badge)

An interactive computer-vision-based reimagining of the classic Flappy Bird game.

This project integrates **MediaPipe hand tracking** with a physics-driven Pygame engine to replace traditional keyboard input with real-time gesture recognition. It demonstrates practical applications of **Human-Computer Interaction (HCI)** and real-time vision systems in gaming.

---

##  Key Features

-  Real-time hand tracking using MediaPipe’s 21-point landmark model  
-  Webcam frame processing via OpenCV  
-  Physics-based movement system (gravity + velocity damping)  
-  Animated sprite rendering using Pygame  
-  Dual pipe system with variable scoring  
-  Game state management (Start / Play / Game Over)  
-  Spacebar fallback control  

---

## Core Technologies

| Component        | Technology     | Purpose |
|------------------|---------------|----------|
| Vision Engine    | OpenCV        | Frame capture & preprocessing |
| Tracking Model   | MediaPipe     | Hand landmark detection |
| Game Engine      | Pygame        | Rendering & physics |
| Environment      | Python 3.11   | Stable compatibility for CV libraries |

---

## Project Structure

```
project/
│
├── birb.py            # Main game file
├── camera.py          # Webcam test
├── hand.py            # Hand detection test
├── test_mp.py         # MediaPipe verification
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

## Version Compatibility

This project officially supports **Python 3.11**.

While newer Python versions exist, MediaPipe and OpenCV currently provide the most stable experience within Python 3.9–3.11.

If you encounter:

```
No matching distribution found
```

Ensure you are using Python 3.11 inside a virtual environment.

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/hand-flappy-bird.git
cd hand-flappy-bird
```

### Create a virtual environment

```bash
python3.11 -m venv venv
```

### Activate the environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install opencv-python mediapipe pygame numpy
```

### Run the game

```bash
python birb.py
```

Ensure:
- Webcam is connected
- `assets` folder is in the root directory

---

##  How to Play

- Launch the game with `python birb.py`
- Position your hand clearly in front of the webcam
- Raise your hand upward to make the bird flap
- Avoid colliding with pipes or the ground
- Survive as long as possible to increase your score

---

##  Gesture Control Logic

- MediaPipe detects 21 hand landmarks.
- The **wrist landmark (index 0)** is monitored.
- If the wrist’s normalized Y-coordinate is above the midpoint (y < 0.5), upward thrust is applied.
- Otherwise, gravity pulls the bird downward.

```python
wrist = results.multi_hand_landmarks[0].landmark[0]
if wrist.y < 0.5:
    velocity += thrust
```

This creates a natural mapping between physical hand elevation and in-game movement.

---

##  Technical Implementation

The game loop continuously:

1. Captures webcam frames  
2. Processes landmarks using MediaPipe  
3. Applies physics updates (gravity + velocity decay)  
4. Updates pipe positions  
5. Performs collision detection  
6. Renders sprites and score  

Physics model:

- Constant gravity acceleration  
- Velocity damping factor  
- Collision bounds checking  
- Procedural pipe generation  

---

##  Scoring System

-  Green Pipe → +10 points  
-  Red Pipe → +20 points  

Score increments when the bird successfully passes a pipe.

---

## Game States

- `"start"` → Waiting for user input  
- `"play"` → Active gameplay  
- `"gameover"` → Display score + restart prompt  

---

## Testing Modules

Run components independently:

### Test Camera
```bash
python camera.py
```

### Test Hand Tracking
```bash
python hand.py
```

### Test MediaPipe Installation
```bash
python test_mp.py
```

---

## Concepts Demonstrated

- Real-time computer vision
- Gesture-based interaction systems
- Game loop architecture
- Physics simulation
- Sprite animation
- Collision detection
- Procedural obstacle spawning

---

## Why This Project Matters

This project demonstrates the integration of:

- Computer Vision  
- Real-time physics simulation  
- Human-Computer Interaction  
- Game development principles  

It showcases how machine perception can replace traditional input devices in interactive systems.

---

## Gameplay Demo

(add photo/video thingy here)

---

## Future Improvements

- Add sound effects  
- Adaptive difficulty scaling  
- High score persistence  
- More advanced gesture controls  
- Performance optimization  

---

## Takeaway

I saw many applicaitons of hand tracking everywhere and i was like, "Cooool i wanna do that too"...and decided to combine it with Python-based game development to build a gesture controlled version of the classic game of flappy bird. Why? Because I have free will and i thought it would be cool to explore my boundaries with this one. Safe to say it helped me build confidence in building cross domain systems and improved my understanding of real-time system designs in general.
