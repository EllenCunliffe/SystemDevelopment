from PyQt6 import QtWidgets, uic
from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc



class PreferenceScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 279)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.overskrift = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.overskrift.setFont(font)
        self.overskrift.setObjectName("overskrift")
        self.verticalLayout.addWidget(self.overskrift)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ugedag = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ugedag.setFont(font)
        self.ugedag.setObjectName("ugedag")
        self.verticalLayout.addWidget(self.ugedag)
        self.lineEdit_ugedag = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_ugedag.setFont(font)
        self.lineEdit_ugedag.setObjectName("lineEdit_ugedag")
        self.verticalLayout.addWidget(self.lineEdit_ugedag)
        self.tidsrum = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tidsrum.setFont(font)
        self.tidsrum.setObjectName("tidsrum")
        self.verticalLayout.addWidget(self.tidsrum)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_2.addWidget(self.timeEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.horizontalLayout_2.addWidget(self.timeEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setText("")
        self.result.setObjectName("result")
        self.verticalLayout.addWidget(self.result)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonClear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout.addWidget(self.pushButtonClear)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setObjectName("pushButtonSave")

        # save a new preference when pushbutton save is clicked
        self.pushButtonSave.clicked.connect(self.save_preference)

        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.horizontalLayout.addWidget(self.pushButtonBack)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.overskrift.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Tilføj Præference</p></body></html>"))
        self.ugedag.setText(_translate("MainWindow", "Ugedag (fx. Mandag)"))
        self.tidsrum.setText(_translate("MainWindow", "Tidsrum"))
        self.label_4.setText(_translate("MainWindow", "Fra kl."))
        self.label_5.setText(_translate("MainWindow", "Til kl."))
        self.pushButtonClear.setText(_translate("MainWindow", "Nulstil"))
        self.pushButtonSave.setText(_translate("MainWindow", "Gem"))
        self.pushButtonBack.setText(_translate("MainWindow", "Annuler"))

    def save_preference(self):
        try:
            mydb = mc.connect(
                host="127.0.0.1",
                user="root",
                password="Pattefar3638",
                database="mydb"
            )
            cursor = mydb.cursor()
            # We save the inserted text from the GUI lineedit into variables
            # In the real world uniID is properly autogenerated.
            weekday = self.lineEdit_ugedag.text()
            time_start = self.timeEdit.text()
            time_end = self.timeEdit_2.text()
            kursus_id = "101"

            # Insert into the 'præferencer' table in the weekday, timeslot and courseID fields.
            # Using a string placeholder, we can insert values from python variables
            query = "INSERT INTO præferencer (Ugedag, TidStart, TidSlut, KursusID) VALUES (%s, %s, %s, %s)"
            value = (weekday, time_start, time_end, kursus_id)

            # Now we have to execute the query we made
            cursor.execute(query, value)
            mydb.commit()

            # If all this is going well, we want the result to be visible in the Gui
            self.result.setText("Du har tilføjet en dag til dine pæferencer")

        # If all this is going wrong, we want the result to be visible in the Gui
        except mc.Error as e:
            self.result.setText("Noget gik galt!" + str(e.errno) + e.msg)

#     def clear_button_pressed(self):
#         # This method is used in order to clear all input fields.
#         # A simple, but naive approach will be to call
#         # .clear() for all input fields, e.g. self.firstNameLineEdit.clear()
#         # however this will require that we maintain the method if we add
#         # more fields. A better approach would probably be to find all fields of type
#         # LineEdit and clear them!
#         # But first present the user with a warning message by using QMessagebox
#         print('Clear button pressed!')
#
#         button = QtWidgets.QMessageBox.question(self, "Clear fields", "All input fields will be cleared")
#
#         if button == QtWidgets.QMessageBox.StandardButton.Yes:
#             print("Yes!")
#             # Find all fields of type QLineEdit
#             line_edits = self.findChildren(QtWidgets.QLineEdit)
#             # Loop over the fields and clear them
#             for field in line_edits:
#                 field.clear()
#         else:
#             print("No!")
#
#     def cancel_button_pressed(self):
#
#         print('Cancel button pressed!')
#
#         button = QtWidgets.QMessageBox.question(self, "Exit form?", "Do you want to save the existing?")
#
#         if button == QtWidgets.QMessageBox.StandardButton.Yes:
#             print("Yes!")
#             print(type(self.parent()))
#             if type(self.parent()) == QtWidgets.QStackedWidget:
#                 self.parent().setCurrentIndex(0)
#             self.close()  # This will close Widget
#
#         else:
#             print("No!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PreferenceScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
