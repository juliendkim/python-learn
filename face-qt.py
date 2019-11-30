from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QPixmap, QImage
import pafy
import cv2
from time import sleep
import threading


class MainWindowClass(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")

        self.video_viewer_label = QtWidgets.QLabel(self.centralwidget)
        self.video_viewer_label.setGeometry(QtCore.QRect(10, 10, 400, 300))

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def video_to_frame(self, main_window):
        url = "https://youtu.be/t67_zAg5vvI"
        video = pafy.new(url)

        video_length = video.length / 60
        print(video_length)

        play = video.getbest(preftype="mp4")

        cap = cv2.VideoCapture(play.url)
        face_cascade = cv2.CascadeClassifier('haarcascade/frontalface_default.xml')

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_coords = face_cascade.detectMultiScale(img_gray)
            for (x, y, w, h) in face_coords:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                
            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, channel = img_rgb.shape
            img_qt = QImage(img_rgb.data, w, h, QImage.Format_RGB888)

            pixmap = QPixmap(img_qt)
            p = pixmap.scaled(400, 225, QtCore.Qt.IgnoreAspectRatio)

            self.video_viewer_label.setPixmap(p)
            self.video_viewer_label.update()

            sleep(0.03)
        cap.release()
        cv2.destroyAllWindows()

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))

    # video_to_frame을 쓰레드로 사용
    def video_thread(self, main_window):
        thread = threading.Thread(target=self.video_to_frame, args=(self,))
        thread.daemon = True  # 프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowClass()
    ui.setup_ui(MainWindow)

    ui.video_thread(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())
