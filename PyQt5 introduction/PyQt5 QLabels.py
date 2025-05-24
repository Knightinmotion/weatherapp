import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProjectGUI one")
        self.setGeometry(700, 30, 500, 500)  #(x, y, width) for positioning of the interface(UI)
        self.setWindowIcon(QIcon("bugatti.jpg"))

        label = QLabel("Hello", self )
        label.setFont(QFont("Arial", 10))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color:#292929;"
                            "Background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "text-decoration: underline;"
                            "font-style: italic;")

        label.setAlignment(Qt.AlignTop) # VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom)  # VERTICALLY BOTTOM
        # label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER
        #
        # label.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignLeft) # HORIZONTALLY LEFT
        # label.setAlignment(Qt.AlignCenter) # HORIZONTALLY CENTER
        #
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER & CENTER


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


