#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
from mtcnn import MTCNN

detector = MTCNN()

WindowName = 'Face Detector'
cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

webcam = cv2.VideoCapture(0)
# cv2.waitKey(1000)

while True:
    # read current frame
    successful_frame_read, frame = webcam.read()

    # COLOR_BGR2RGB conversion increases success rate
    #color_inverted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # cv2.imshow(WindowName, color_inverted)
    # if cv2.waitKey(10) == ord('q'):
    #     break

    faces = detector.detect_faces(frame)

    for face in faces:
        # (x, y, w, h) = face_coordinates[#]
        (x, y, w, h) = face['box']
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  # green color box

        keypoints = face['keypoints']
        cv2.circle(frame, (keypoints['left_eye']), 2, (0, 155, 255), 2)
        cv2.circle(frame, (keypoints['right_eye']), 2, (0, 155, 255), 2)
        cv2.circle(frame, (keypoints['nose']), 2, (0, 155, 255), 2)
        cv2.circle(frame, (keypoints['mouth_left']), 2, (0, 155, 255), 2)
        cv2.circle(frame, (keypoints['mouth_right']), 2, (0, 155, 255), 2)

    cv2.imshow(WindowName, frame)

    # same as key = cv2.waitKey(1) ## q == 81 or Q = 113
    if cv2.waitKey(10) == ord('q'):
        break

print("Ended")
