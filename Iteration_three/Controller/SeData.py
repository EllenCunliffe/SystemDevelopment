from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem
import mysql.connector as mc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(548, 382)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.databasenavn = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.databasenavn.setFont(font)
        self.databasenavn.setObjectName("databasenavn")
        self.horizontalLayout.addWidget(self.databasenavn)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabelnavn = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.tabelnavn.setFont(font)
        self.tabelnavn.setObjectName("tabelnavn")
        self.horizontalLayout_2.addWidget(self.tabelnavn)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        # when clicking the 'Se data' button, show the data
        self.pushButton.clicked.connect(self.show_data)

        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def show_data(self):
        try:
            # make the input from lineedit into variables
            dbname = self.lineEdit.text()
            tablename = self.lineEdit_2.text()

            # Connect to the database that was given in the dbname
            mydb = mc.connect(
                host="127.0.0.1",
                user="root",
                password="Pattefar3638",
                database=dbname


            )
            # in mysql execute "select all from tablename" statement
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM {}".format(tablename))

            # allow us to get all the details
            result = cursor.fetchall()

            # initiate rowcount
            self.tableWidget.setRowCount(0)

            # To present the data in the GUI table we need to iterate through the rows
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)  # and for each row, we insert a row number

                # we are going through the collums to give them a number too
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print("Ups! Der skete en fejl")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.databasenavn.setText(_translate("Form", "Databasenavn:"))
        self.tabelnavn.setText(_translate("Form", "Tabelnavn:"))
        self.pushButton.setText(_translate("Form", "Se data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
