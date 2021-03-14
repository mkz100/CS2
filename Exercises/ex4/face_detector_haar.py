import cv2

WindowName = 'Face Detector'
cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

# Load some pre-trained data on face from opencv (haar cascade algorithm)
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
# img = cv2.imread('WechatIMG6.jpeg')
# capture video from the default cam or feed in a video clip
webcam = cv2.VideoCapture(0)

while True:
    # read current frame
    successful_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for face_position in face_coordinates:
        # (x, y, w, h) = face_coordinates[#]
        (x, y, w, h) = face_position
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) # green color box

    cv2.imshow(WindowName, frame)

    # same as key = cv2.waitKey(1) ## q == 81 or Q = 113
    if cv2.waitKey(10) == ord('q'):
        break


print("Ended")