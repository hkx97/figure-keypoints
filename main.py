import cv2
import mediapipe as mp
import time

mp_hand = mp.solutions.hands
hands = mp_hand.Hands()
mp_draw = mp.solutions.drawing_utils
s, e = time.time(), time.time()
cap = cv2.VideoCapture(0)
while True:
    res, img = cap.read()
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img)
    print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for _ in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, _, mp_hand.HAND_CONNECTIONS)
    e = time.time()
    cv2.putText(img, "FPS:{}".format(int(1 / (e - s))), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (232, 0, 255))
    s = time.time()
    cv2.imshow("img", img)
    if cv2.waitKey(1) == ord("q"):
        break
