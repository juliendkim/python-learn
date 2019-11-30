from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PySide2.QtGui import QPixmap, QImage
import pafy
import cv2
from time import sleep
import threading
import sys


class MainForm(QWidget):

    def __init__(self):
        super().__init__()

        self.video_view = QLabel(self)
        self.video_view.resize(600, 400)
        
        self.resize(800, 600)
        self.setWindowTitle('윈도우 띄우기')

    def show_image(self, img_cv2_bgr):
        img_cv2_rgb = cv2.cvtColor(img_cv2_bgr, cv2.COLOR_BGR2RGB)
        h, w, ch = img_cv2_rgb.shape
        img_qimage = QImage(img_cv2_rgb.data, w, h, QImage.Format_RGB888)
        img_qpixmap = QPixmap(img_qimage)
        img_qpixmap_scaled = img_qpixmap.scaled(600, 400, Qt.IgnoreAspectRatio)
        self.video_view.setPixmap(img_qpixmap_scaled)
        self.video_view.update()

    def show_video(self):
        url = "t67_zAg5vvI"
        video = pafy.new(url)
        video_mp4 = video.getbest(preftype='mp4')
        capture = cv2.VideoCapture(video_mp4.url)
        face_cascade = cv2.CascadeClassifier('haarcascade/frontalface_default.xml')
        while True:
            succeeded, frame = capture.read()
            if not succeeded:
                break
            img_cv2_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(img_cv2_gray)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            self.show_image(frame)
            sleep(0.03)

        capture.release()
        cv2.destroyAllWindows()

    def run_thread(self):
        thread = threading.Thread(target=self.show_video)
        thread.daemon = True
        thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_form = MainForm()
    main_form.show_image(cv2.imread('image/image.jpg', cv2.IMREAD_COLOR))
    main_form.run_thread()
    main_form.show()
    sys.exit(app.exec_())

