# GUI FILE
from Login import LoginScreen
from Menu_main import MenuScreen

# MySQL CONNECTOR
import mysql.connector as mc

# QT CLASSES
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMainWindow

# ActiveModel CLASS
from Iteration_three.Model.ActiveModel import ActiveModel


class LoginScreen(QtWidgets.QWidget):
    def __init__(self):
        super(LoginScreen, self).__init__()
        uic.loadUi('.ui', self)
        print("NewEmployeeGUI called")
        print("-" * 30 + "\nGUI: We have the following employees in the active model")
        for e in ActiveModel.get_employee_list():
            print(e)


            # login to database when pushbutton cklicked
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

                result = cursor.fetchone()    #we only want to see one result

                if result == None:
                    self.result.setText("Uni ID eller password findes ikke")

                else:
                    self.result.setText("Du har succesfuldt logget ind")
                    self.window = QtWidgets.QMainWindow()
                    self.ui = MenuScreen()
                    self.ui.setupUi(self.window)
                    self.window.show()

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