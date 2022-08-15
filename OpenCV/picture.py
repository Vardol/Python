from cgi import test
import cv2

tested_img = cv2.imread('D:/developer/Python/OpenCV/test.jpeg')
tested_img_grey = cv2.cvtColor(tested_img, cv2.COLOR_BGR2GRAY)
face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

faces = face_cascades.detectMultiScale(tested_img_grey)

for (x, y, w, h) in faces:
    cv2.rectangle(tested_img, (x, y), (x + w, y + h), (255 ,0 , 0), 1)

#tested_img = cv2.resize(tested_img, (500,500))
#print(tested_img)

cv2.imshow('result', tested_img)
cv2.waitKey(0)