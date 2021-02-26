#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
from mtcnn import MTCNN

detector = MTCNN()

# COLOR_BGR2RGB conversion increases success rate
# cv2.cvtColor(cv2.imread("WechatIMG6.jpeg"), cv2.COLOR_BGR2RGB)
image = cv2.imread("WechatIMG6.jpeg") 

faces = detector.detect_faces(image)

# faces is an array with all the bounding boxes detected. We know that for 'ivan.jpg' there is only one.
#bounding_box = faces[0]['box']
#keypoints = faces[0]['keypoints']

for face in faces:
    # (x, y, w, h) = face_coordinates[#]
    (x, y, w, h) = face['box']
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2) # green color box

    keypoints = face['keypoints']
    cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)

# cv2.imwrite("ivan_drawn.jpg", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

print(faces)

WindowName = 'Face Detector'
cv2.namedWindow(WindowName,cv2.WINDOW_NORMAL)
cv2.setWindowProperty(WindowName,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(WindowName,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_NORMAL)
cv2.imshow(WindowName, image)
cv2.waitKey()

print("Ended")
