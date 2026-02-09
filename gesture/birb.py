import cv2
import mediapipe as mp
import pygame
import random
import os

ASSET = "assets"
def load(name):
    return pygame.image.load(os.path.join(ASSET, name)).convert_alpha()

pygame.init()
WIDTH, HEIGHT = 288, 512
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bg = random.choice([load("background-day.png"), load("background-night.png")])
base = load("base.png")
gameover_img = load("gameover.png")
message = load("message.png")

bird_frames = [
    load("yellowbird-downflap.png"),
    load("yellowbird-midflap.png"),
    load("yellowbird-upflap.png"),
]

pipe_green = load("pipe-green.png")
pipe_red = load("pipe-red.png")
numbers = [load(f"{i}.png") for i in range(10)]

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
cap = cv2.VideoCapture(0)

gravity = 0.45
thrust = -0.6
pipe_gap = 200
pipe_speed = 1.8
pipe_spacing = 130   # colour spacing
base_x = 0

state = "start"
frame = 0

def draw_score(score):
    digits = list(map(int, str(score)))
    x = WIDTH//2 - len(digits)*12
    for d in digits:
        screen.blit(numbers[d], (x, 40))
        x += 24

def new_pipe():
    color = random.choice(["green", "red"])
    img = pipe_green if color == "green" else pipe_red
    height = random.randint(130, 330)
    value = 10 if color == "green" else 20
    return [WIDTH, height, img, value]

def reset():
    return HEIGHT//2, 0, [new_pipe()], 0

bird_y, velocity, pipes, score = reset()

running = True
while running:

    screen.blit(bg, (0, 0))

    #hand control
    hand_up = False
    ret, cam = cap.read()
    if ret:
        rgb = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        if results.multi_hand_landmarks:
            wrist = results.multi_hand_landmarks[0].landmark[0]
            if wrist.y < 0.5:
                hand_up = True

    keys = pygame.key.get_pressed()
    space = keys[pygame.K_SPACE]

    # start
    if state == "start":
        screen.blit(message, (50, 150))
        if space:   
            state = "play"

    #playyy
    if state == "play":

        if hand_up:
            velocity += thrust

        velocity += gravity
        velocity *= 0.95
        bird_y += velocity

        for pipe in pipes:
            pipe[0] -= pipe_speed

        #spawn next pipe before last leaves
        if pipes[-1][0] < WIDTH - pipe_spacing:
            pipes.append(new_pipe())

        if pipes[0][0] < -60:
            pipes.pop(0)

        for pipe in pipes:
            x, h, img, val = pipe
            flip = pygame.transform.flip(img, False, True)

            screen.blit(flip, (x, h - img.get_height()))
            screen.blit(img, (x, h + pipe_gap))

            if 40 < x < 42:
                score += val

            if 40 < x < 80:
                if bird_y < h or bird_y > h + pipe_gap:
                    state = "gameover"

        if bird_y > HEIGHT - 100 or bird_y < 0:
            state = "gameover"

        draw_score(score)

    #birb
    bird_frame = bird_frames[(frame // 7) % 3]
    screen.blit(bird_frame, (50, int(bird_y)))

    # ground
    base_x -= 2
    if base_x <= -WIDTH:
        base_x = 0
    screen.blit(base, (base_x, HEIGHT - 100))
    screen.blit(base, (base_x + WIDTH, HEIGHT - 100))

    # insert *u died*
    if state == "gameover":
        screen.blit(gameover_img, (50, 200))
        draw_score(score)

        font = pygame.font.SysFont(None, 28)
        txt = font.render("PRESS SPACE", True, (255,255,255))
        screen.blit(txt, (60, 300))

        if space:  
            bird_y, velocity, pipes, score = reset()
            state = "start"

    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)
    frame += 1

cap.release()
pygame.quit()
