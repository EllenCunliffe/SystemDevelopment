import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow


app = QApplication(sys.argv)

window1 = QMainWindow()
window1.show()
sys.exit(app.exec())


