from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.uic import loadUi
import mysql.connector as mc
from PyQt6.QtWidgets import QDialog, QApplication, QStackedWidget
from Menu_main import MenuGUI


class LoginScreen(object):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("LogInd_main.ui", self)

        # login to database when pushbutton clicked
        self.pushButton.clicked.connect(self.login)

    def login(self):
        try:
            # First we take the input for the lineedit and save it into a string
            uniID = self.lineEdit.text()
            password = self.lineEdit_2.text()

            mydb = mc.connect(
                host="127.0.0.1",
                user="root",
                password="Pattefar3638",
                database="mydb"
            )

            # Im mysql database we are selecting a user only if it matches our input variables
            cursor = mydb.cursor()
            query = "SELECT UniID, Password FROM bruger WHERE UniID like '" + uniID + "'and Password like'" + password + "'"

            # Execute the query
            cursor.execute(query)

            result = cursor.fetchone()  # we only want to see one result

            if result == None:
                self.result.setText("Uni ID eller password findes ikke")

            else:
                self.result.setText("Du har succesfuldt logget ind")
                mymain = QDialog()
                mymain.setModal(True)  # try setmywindowmodality if doesent work
                mymain.exec()  # in pyqt5 'exec' is 'exec_'

        except mc.Error as e:
            self.result.setText("Ups! Der skete en fejl")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
