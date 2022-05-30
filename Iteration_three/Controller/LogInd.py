from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PyQt6 import uic
import sys


class LogIndGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("LogInd_main.ui", self)


app = QApplication(sys.argv)
window = LogIndGUI()
window.show()
sys.exit(app.exec())
