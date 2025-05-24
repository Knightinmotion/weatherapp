
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProjectGUI one")
        self.setGeometry(700, 30, 500, 500)  #(x, y, width, height) for positioning of the interface(UI)
        self.setWindowIcon(QIcon("bugatti.jpg"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


