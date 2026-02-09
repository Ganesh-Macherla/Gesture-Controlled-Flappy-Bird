import cv2
import mediapipe as mp
# intialize mediapipe hehe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# open webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break



    # conver to rgb for mediapipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    # desture detection
    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            wrist = hand.landmark[0]
            y = wrist.y

            if y < 0.5:
                text = "HAND UP"
                color = (0, 255, 0)
            else:
                text = "HAND DOWN"
                color = (0, 0, 255)
            # draw text
            cv2.putText(frame, text, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            # hand skeleton
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)


    # show frame
    cv2.imshow("Hand Tracking", frame)

    # quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
