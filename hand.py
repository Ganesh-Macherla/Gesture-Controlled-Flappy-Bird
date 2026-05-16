import cv2
import mediapipe as mp

# initialize mediapipe hands
mp_hands = mp.solutions.hands

hands = mp_hands.Hands()

# drawing utilities
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # convert BGR to RGB for mediapipe
    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    results = hands.process(rgb)

    # detect them hands
    if results.multi_hand_landmarks:

        for hand in results.multi_hand_landmarks:

            # wrist landmark
            wrist = hand.landmark[0]

            y = wrist.y

            # determine hand position
            if y < 0.5:

                text = "HAND UP"
                color = (0, 255, 0)

            else:

                text = "HAND DOWN"
                color = (0, 0, 255)

            # display text
            cv2.putText(
                frame,
                text,
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color,
                2
            )

            # draw hand skeleton
            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

    # display frame
    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
