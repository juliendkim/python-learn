import cv2
import pafy
import dlib


def show_video():
    face_detector = dlib.get_frontal_face_detector()
    eye_cascade = cv2.CascadeClassifier('haarcascade/eye.xml')

    video = pafy.new('https://youtu.be/t67_zAg5vvI')
    play = video.getbest(preftype='mp4')
    capture = cv2.VideoCapture(play.url)
    while True:
        return_val, frame = capture.read()
        if not return_val:
            break

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_coords = face_detector(frame)
        for f in face_coords:
            cv2.rectangle(frame, (f.left(), f.top()), (f.right(), f.bottom()), (0, 0, 255), 1)
            roi_gray = gray_img[f.top():f.bottom(), f.left():f.right()]
            roi_color = frame[f.top():f.bottom(), f.left():f.right()].copy()
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
