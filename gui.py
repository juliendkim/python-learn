from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PySide2.QtGui import QPixmap, QImage
import pafy
import cv2
from time import sleep
import threading
import sys


class MainForm(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.video_view = QLabel(self)
        self.video_view.resize(600, 400)
        
        self.setWindowTitle('윈도우 띄우기')
        self.resize(800, 600)

        self.show_image()
    
    def show_image(self):
        img_cv2_bgr = cv2.imread('image/image.jpg', cv2.IMREAD_COLOR)
        img_cv2_rgb = cv2.cvtColor(img_cv2_bgr, cv2.COLOR_BGR2RGB)
        h, w, ch = img_cv2_rgb.shape
        img_qimage = QImage(img_cv2_rgb.data, w, h, QImage.Format_RGB888)
        img_qpixmap = QPixmap(img_qimage)
        self.video_view.setPixmap(img_qpixmap)
        self.video_view.update()
    
    def show_video(self):
        url = "https://youtu.be/t67_zAg5vvI"
        video = pafy.new(url)
        video_mp4 = video.getbest(preftype='mp4')
        capture = cv2.VideoCapture(video_mp4.url)

        while True:
            succeeded, frame = capture.read()
            if not succeeded:
                break

            img_cv2_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = img_cv2_rgb.shape
            img_qimage = QImage(img_cv2_rgb, w, h, QImage.Format_RGB888)
            img_qpixmap = QPixmap(img_qimage)
            self.video_view.setPixmap(img_qpixmap)
            self.video_view.update()

            if cv2.waitKey(1) > 0:
                break
        
        capture.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_form = MainForm()
    main_form.show()
    app.exec_()

