from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QPixmap, QImage
import cv2
import pafy


def show_video():
    face_cascade = cv2.CascadeClassifier('haarcascade/frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade/eye.xml')

    video = pafy.new('https://youtu.be/t67_zAg5vvI')
    play = video.getbest(preftype='mp4')
    capture = cv2.VideoCapture(play.url)
    while True:
        return_val, frame = capture.read()
        if not return_val:
            break

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_coords = face_cascade.detectMultiScale(gray_img)
        for (x, y, w, h) in face_coords:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            roi_gray = gray_img[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w].copy()
            eyes_coords = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes_coords:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + ey), (0, 255, 0), 1)
        cv2.imshow('Video Frame', frame)

        if cv2.waitKey(10) > 0:
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_video()
