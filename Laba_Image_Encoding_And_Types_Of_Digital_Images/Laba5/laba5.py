import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread("matrix.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.1, minNeighbors = 5)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("found_faces", image)
cv2.waitKey(0)