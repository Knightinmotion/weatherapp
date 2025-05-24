# tryin' to put CSS and Checkboxes

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class MyClock(QWidget):
	def __init__(self):
		super().__init__()
		self.time_label = QLabel()
