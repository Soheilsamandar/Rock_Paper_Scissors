import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier

import numpy as np
import math
import random
import time

# -----------------------------

cap = cv.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
labels = ["rock", "paper", "scissors"]
offset = 20
imgSize = 300
player_score = 0
computer_score = 0


# -----------------------------
def check_winner(player, computer):
    if player == computer:
        return "Draw"
    if player == "rock" and computer == "scissors":
        return "Player"
    if player == "paper" and computer == "rock":
        return "Player"
    if player == "scissors" and computer == "paper":
        return "Player"
    return "Computer"


# -----------------------------
while True:
    start_time = time.time()
    while time.time() - start_time < 3:
        success, img = cap.read()
        img = cv.flip(img, 1)
        count = 3 - int(time.time() - start_time)
        cv.putText(
            img, str(count), (300, 200), cv.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 10
        )
        cv.putText(
            img,
            "Show your hand",
            (150, 400),
            cv.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
        )
        cv.imshow("Rock Paper Scissors AI", img)
        if cv.waitKey(1) == 27:
            cap.release()
            cv.destroyAllWindows()
            exit()
    success, img = cap.read()
    imgOutput = img.copy()
    img = cv.flip(img, 1)
    hands, img = detector.findHands(img)
    player_move = None
    confidence = 0
    if hands:
        hand = hands[0]
        x, y, w, h = hand["bbox"]
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        x1 = max(0, x - offset)
        y1 = max(0, y - offset)
        x2 = min(img.shape[1], x + w + offset)
        y2 = min(img.shape[0], y + h + offset)
        imgCrop = img[y1:y2, x1:x2]
        aspectRatio = h / w
        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv.resize(imgCrop, (wCal, imgSize))
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap : wCal + wGap] = imgResize
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv.resize(imgCrop, (imgSize, hCal))
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap : hCal + hGap, :] = imgResize
        prediction, index = classifier.getPrediction(imgWhite, draw=False)
        player_move = labels[index]
        confidence = max(prediction)
    else:
        player_move = "unknown"
    computer_move = random.choice(labels)
    result = check_winner(player_move, computer_move)
    if result == "Player":
        player_score += 1
    elif result == "Computer":
        computer_score += 1
    cv.putText(
        imgOutput,
        f"You : {player_move}",
        (20, 50),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2,
    )
    cv.putText(
        imgOutput,
        f"AI : {computer_move}",
        (20, 100),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2,
    )
    cv.putText(
        imgOutput,
        f"Result : {result}",
        (20, 150),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2,
    )
    cv.putText(
        imgOutput,
        f"Confidence : {confidence*100:.1f}%",
        (20, 200),
        cv.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2,
    )
    cv.putText(
        imgOutput,
        f"You {player_score}  -  AI {computer_score}",
        (20, 260),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2,
    )
    cv.putText(
        imgOutput,
        "SPACE = Next Round",
        (20, 430),
        cv.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2,
    )
    cv.imshow("Rock Paper Scissors AI", imgOutput)
    while True:
        key = cv.waitKey(1)
        if key == 32:
            break
        if key == 27:
            cap.release()
            cv.destroyAllWindows()
            exit()
