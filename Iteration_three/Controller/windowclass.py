from PyQt6.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("test2")
        self.setFixedHeight(600)
        self.setFixedWidth(800)


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
