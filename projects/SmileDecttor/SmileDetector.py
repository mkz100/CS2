import cv2

WindowName = 'Face Detector'
cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

face_detector = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

webcam = cv2.VideoCapture(0)

while True:

    successful_read, frame = webcam.read()

    if not successful_read:
        break

    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(grey_frame)

    # fine tune the parameters for more accurate detection
    #smiles = smile_detector.detectMultiScale(grey_frame)
    #smiles = smile_detector.detectMultiScale(grey_frame, scaleFactor=1.7)
    #smiles = smile_detector.detectMultiScale(grey_frame, scaleFactor=1.7, minNeighbors=20)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (0, 255, 0), 2)  # green color box

        face = frame[y:(y+h), x:(x+w)]
        grey_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        smiles = smile_detector.detectMultiScale(grey_face, scaleFactor=1.7, minNeighbors=20)

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(face, (sx, sy), (sx+sw, sy+sh),
                          (0, 255, 255), 2)
        if (len(smiles) > 0):
            cv2.putText(frame, 'smiling!', (x, y+h+40), fontScale=3, fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))

    cv2.imshow(WindowName, frame)

    # same as key = cv2.waitKey(1) ## q == 81 or Q = 113
    if cv2.waitKey(10) == ord('q'):
        break
