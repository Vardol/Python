import cv2

my_video = cv2.VideoCapture('D:/developer/Python/OpenCV/test.avi')
#cap = cv2.VideoCapture(0) #для захвата видео с веб-камеры

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


while True:
    success, frame = my_video.read()
    frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(frame_grey)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255 ,0 , 0), 1)

    cv2.imshow('result', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break