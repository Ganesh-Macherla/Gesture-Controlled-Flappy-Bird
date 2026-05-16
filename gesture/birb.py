import cv2
import mediapipe as mp
import pygame
import random
import os

# assets

ASSET = "assets"

def load(name):
    return pygame.image.load(
        os.path.join(ASSET, name)
    ).convert_alpha()

pygame.init()

# game dimensions

GAME_WIDTH = 288
CAM_WIDTH = 320

WIDTH = GAME_WIDTH + CAM_WIDTH
HEIGHT = 512

# bird constants
BIRD_X = 50
BIRD_WIDTH = 34
BIRD_HEIGHT = 24

# ground
GROUND_HEIGHT = 100

# display

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_surface = pygame.Surface((GAME_WIDTH, HEIGHT))

clock = pygame.time.Clock()

# load sprites

bg = random.choice([
    load("background-day.png"),
    load("background-night.png")
])

base = pygame.transform.scale(
    load("base.png"),
    (GAME_WIDTH, 112)
)

gameover_img = load("gameover.png")
message = load("message.png")

bird_frames = [
    load("yellowbird-downflap.png"),
    load("yellowbird-midflap.png"),
    load("yellowbird-upflap.png"),
]

# pipes
pipe_green = load("pipe-green.png")
pipe_red = load("pipe-red.png")

# precomputed flipped pipes (optimization)
pipe_green_flip = pygame.transform.flip(
    pipe_green,
    False,
    True
)

pipe_red_flip = pygame.transform.flip(
    pipe_red,
    False,
    True
)

# score numbers
numbers = [load(f"{i}.png") for i in range(10)]

# mediapipe

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# webcam
cap = cv2.VideoCapture(0)

# fisics

gravity = 0.35
thrust = -5

pipe_gap = 180
pipe_speed = 2
pipe_spacing = 160

# variables

base_x = 0
frame = 0

state = "start"

# draw score

def draw_score(score):

    digits = list(map(int, str(score)))

    x = GAME_WIDTH // 2 - len(digits) * 12

    for d in digits:

        game_surface.blit(numbers[d], (x, 40))

        x += 24

# create pipe

def new_pipe():

    color = random.choice(["green", "red"])

    if color == "green":

        img = pipe_green
        flip = pipe_green_flip
        value = 10

    else:

        img = pipe_red
        flip = pipe_red_flip
        value = 20

    height = random.randint(
        80,
        HEIGHT - pipe_gap - 80
    )

    return {

        "x": GAME_WIDTH,

        "height": height,

        "img": img,

        "flip": flip,

        "value": value,

        "passed": False
    }

# reset game

def reset():

    return (
        HEIGHT // 2,
        0,
        [new_pipe()],
        0
    )

# initial values
bird_y, velocity, pipes, score = reset()

cam_surface = None

running = True

# da main loop

while running:

    # draw background
    game_surface.blit(bg, (0, 0))

    # cam

    hand_up = False

    ret, cam = cap.read()

    if ret:

        # mirror camera
        cam = cv2.flip(cam, 1)

        # convert for mediapipe
        rgb = cv2.cvtColor(
            cam,
            cv2.COLOR_BGR2RGB
        )

        results = hands.process(rgb)

        # detect hand
        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                # draw landmarks
                mp_draw.draw_landmarks(
                    cam,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

                wrist = hand_landmarks.landmark[0]

                # if hand is upper half
                if wrist.y < 0.5:
                    hand_up = True

        # resize camera
        cam = cv2.resize(
            cam,
            (CAM_WIDTH, HEIGHT)
        )

        # divider line
        mid = HEIGHT // 2

        cv2.line(
            cam,
            (0, mid),
            (CAM_WIDTH, mid),
            (255, 255, 255),
            2
        )

        # labels
        cv2.putText(
            cam,
            "UP",
            (CAM_WIDTH // 2 - 25, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 255, 255),
            2
        )

        cv2.putText(
            cam,
            "DOWN",
            (CAM_WIDTH // 2 - 45, HEIGHT - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 255, 255),
            2
        )

        # convert for pygame
        cam = cv2.cvtColor(
            cam,
            cv2.COLOR_BGR2RGB
        )

        cam_surface = pygame.surfarray.make_surface(
            cam.swapaxes(0, 1)
        )

    # input

    keys = pygame.key.get_pressed()

    space = keys[pygame.K_SPACE]

    # start screen

    if state == "start":

        game_surface.blit(message, (50, 150))

        if space:
            state = "play"

    # gameplay

    if state == "play":

        # bird jump
        if hand_up and velocity > -2:
            velocity = thrust

        # gravity
        velocity += gravity

        bird_y += velocity

        # move pipes
        for pipe in pipes:
            pipe["x"] -= pipe_speed

        # create new pipes
        if pipes[-1]["x"] < GAME_WIDTH - pipe_spacing:
            pipes.append(new_pipe())

        # remove offscreen pipes
        if pipes and pipes[0]["x"] < -100:
            pipes.pop(0)

        # bird hitbox
        bird_rect = pygame.Rect(
            BIRD_X,
            bird_y,
            BIRD_WIDTH,
            BIRD_HEIGHT
        )

        # draw+collision
        for pipe in pipes:

            x = pipe["x"]

            h = pipe["height"]

            img = pipe["img"]

            flip = pipe["flip"]

            val = pipe["value"]

            # top pipe
            game_surface.blit(
                flip,
                (x, h - img.get_height())
            )

            # bottom pipe
            game_surface.blit(
                img,
                (x, h + pipe_gap)
            )

            # score
            if (
                not pipe["passed"]
                and x + img.get_width() < BIRD_X
            ):

                score += val

                pipe["passed"] = True

            # hitboxes
            top_pipe = pygame.Rect(
                x,
                h - img.get_height(),
                img.get_width(),
                img.get_height()
            )

            bottom_pipe = pygame.Rect(
                x,
                h + pipe_gap,
                img.get_width(),
                img.get_height()
            )

            # collision
            if (
                bird_rect.colliderect(top_pipe)
                or bird_rect.colliderect(bottom_pipe)
            ):

                state = "gameover"

        # ground / ceiling collision
        if (
            bird_y > HEIGHT - GROUND_HEIGHT
            or bird_y < 0
        ):

            state = "gameover"

        draw_score(score)

    # bird

    bird_frame = bird_frames[(frame // 7) % 3]

    game_surface.blit(
        bird_frame,
        (BIRD_X, int(bird_y))
    )

    # ground

    base_x -= 2

    if base_x <= -GAME_WIDTH:
        base_x = 0

    game_surface.blit(
        base,
        (base_x, HEIGHT - 100)
    )

    game_surface.blit(
        base,
        (base_x + GAME_WIDTH, HEIGHT - 100)
    )

    # womp womp

    if state == "gameover":

        game_surface.blit(
            gameover_img,
            (50, 200)
        )

        draw_score(score)

        font = pygame.font.SysFont(None, 28)

        txt = font.render(
            "PRESS SPACE",
            True,
            (255, 255, 255)
        )

        game_surface.blit(txt, (60, 300))

        # restart
        if space:

            bird_y, velocity, pipes, score = reset()

            state = "start"

    # rendering

    screen.fill((0, 0, 0))

    # game screen
    screen.blit(game_surface, (0, 0))

    # camera screen
    if ret and cam_surface is not None:

        screen.blit(
            cam_surface,
            (GAME_WIDTH, 0)
        )

    # divider line
    pygame.draw.line(
        screen,
        (255, 255, 255),
        (GAME_WIDTH, 0),
        (GAME_WIDTH, HEIGHT),
        3
    )

    # events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

    clock.tick(60)

    frame += 1



cap.release()

pygame.quit()
