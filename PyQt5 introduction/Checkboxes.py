import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("How you are doing", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(0, 0, 500, 200)
        self.checkbox.setStyleSheet("font-size:25px;"
                                    "font-family-Arial")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("I'm good")
        else:
            print("I'm not good")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()