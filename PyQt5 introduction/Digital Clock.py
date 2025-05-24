
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("10:00:00", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
         self.setGeometry(450, 100, 300, 150)
         self.setWindowTitle("Clock")
         self.setWindowIcon(QIcon('watch.jpg'))

         vbox = QVBoxLayout()
         vbox.addWidget(self.time_label)
         self.setLayout(vbox)

         self.time_label.setAlignment(Qt.AlignCenter)
 
         self.time_label.setStyleSheet("font-size: 75px;"
                                       "font-family: Times New Roman;"
                                       "color: hsl(111, 100%, 35%;)")

         self.setStyleSheet("background-color: black;")

         self.timer.timeout.connect(self.update_time)
         self.timer.start(1000)

         self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())