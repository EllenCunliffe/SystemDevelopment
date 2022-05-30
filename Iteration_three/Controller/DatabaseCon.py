

from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(554, 243)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dbCreate = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dbCreate.setFont(font)
        self.dbCreate.setObjectName("dbCreate")

        # Create a database when 'create database' button is clicked
        self.dbCreate.clicked.connect(self.create_database)

        self.horizontalLayout_2.addWidget(self.dbCreate)
        self.dbConnect = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dbConnect.setFont(font)
        self.dbConnect.setObjectName("dbConnect")

        # Connect to a database when 'connect to database' button is clicked
        self.dbConnect.clicked.connect(self.db_connect)

        self.horizontalLayout_2.addWidget(self.dbConnect)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def create_database(self):
        try:
            mydb = mc.connect(
                host="127.0.0.1",
                user="root",
                password="Pattefar3638"
            )
            cursor = mydb.cursor()
            dbname = self.lineEdit.text()
            cursor.execute("CREATE DATABASE {}".format(dbname))
            self.label_2.setText("Databasen {} blev succesfuldt oprettet".format(dbname))
        except mc.Error as e:
            self.label_2.setText("Databasen blev ikke oprettet")

    def db_connect(self):
            try:
                mydb = mc.connect(
                    host="127.0.0.1",
                    user="root",
                    password="Pattefar3638",
                    database="mydb"
                )
                self.label_2.setText("Du har succesfuldt oprettet forbindelse")
            except mc.Error as e:
                self.label_2.setText("Kunne ikke oprette forbindelse")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Database Navn:"))
        self.dbCreate.setText(_translate("Form", "Opret Database"))
        self.dbConnect.setText(_translate("Form", "Connect til Database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
