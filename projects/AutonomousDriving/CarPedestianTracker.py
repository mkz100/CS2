import cv2

WindowName = 'Car Detector'
cv2.namedWindow(WindowName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN,
                      cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

img_file = ''

classifier_file = 'car_detector.xml'

img = cv2.imread(img_file)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

car_tracker = cv2.CascadeClassifier(classifier_file)

cv2.imshow(WindowName, gray_img)

# same as key = cv2.waitKey(1) ## q == 81 or Q = 113
cv2.waitKey()

# if cv2.waitKey(1) == ord('q'):
#     break
