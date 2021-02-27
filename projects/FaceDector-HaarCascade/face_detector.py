import cv2

WindowName = 'Face Detector'
cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

# Load some pre-trained data on face from opencv (haar cascade algorithm)
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
img = cv2.imread('WechatIMG6.jpeg')

# cv2.imshow('Face Detector', img)

grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Face Detector', grayscaled_img)

# detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# print(face_coordinates)
for face_position in face_coordinates:
    # (x, y, w, h) = face_coordinates[#]
    (x, y, w, h) = face_position
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) # green color box

cv2.imshow(WindowName, img)

# wait for any key stroke
cv2.waitKey()

print("Ended")