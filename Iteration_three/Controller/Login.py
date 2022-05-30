from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from Menu_main import MenuScreen


class LoginScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 70, 241, 111))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(260, 230, 251, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uniID_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.uniID_2.setFont(font)
        self.uniID_2.setObjectName("uniID_2")
        self.verticalLayout.addWidget(self.uniID_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.password = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        # login when pushbutton clicked
        self.pushButton.clicked.connect(self.login)

        self.verticalLayout.addWidget(self.pushButton)
        self.result = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        self.verticalLayout.addWidget(self.result)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:700;\">Log ind</span></p></body></html>"))
        self.uniID_2.setText(_translate("MainWindow", "Uni ID"))
        self.password.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Log Ind"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
