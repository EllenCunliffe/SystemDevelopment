from PyQt6 import QtWidgets, uic
from Iteration_two.Model import SavePreference
from Iteration_two.Model import Preference


class NewPreferenceGUI(QtWidgets.QWidget):
    def __init__(self):
        super(NewPreferenceGUI, self).__init__()
        uic.loadUi('View/NewPreference.ui', self)
        print("NewPreferenceGUI called")
        print("-" * 30 + "\nGUI: We have the following preferences in the saved preferences")
        for p in SavePreference.get_preference_list():
            print(p)

        self.pushButtonOk.clicked.connect(self.save_button_pressed)
        self.pushButtonClear.clicked.connect(self.clear_button_pressed)
        self.pushButtonCancel.clicked.connect(self.cancel_button_pressed)

        self.show()

    def save_button_pressed(self):
        # This is executed when the save button is pressed
        # lets concatenate the values from alle the input fields and write
        # the result in the textEdit field we created:

        print("Save button pressed!")

        # get all the values from the input fields ?

        # Course combobox list --> HELP -> generate list
        course = self.CourseList.list()

        # Start times all days --> should it be saved in list?
        mon_time_start = self.timeEditMonStart.time()
        tues_time_start = self.timeEditTuesStart.time()
        wed_time_start = self.timeEditWedStart.time()
        thur_time_start = self.timeEditThurStart.time()
        fri_time_start = self.timeEditFriStart.time()

        # End times different days
        mon_time_end = self.timeEditMonEnd.time()
        tues_time_end = self.timeEditTuesEnd.time()
        wed_time_end = self.timeEditWedEnd.time()
        thur_time_end = self.timeEditThurEnd.time()
        fri_time_end = self.timeEditFriEnd.time()

        # Weekdays click
        weekday_mon = self.monday.text()
        weekday_tues = self.tuesday.text()
        weekday_wed = self.wednesday.text()
        weekday_thur = self.thursday.text()
        weekday_fri = self.friday.text()

        # Location type as combobox --> preexisting list
        location_type = self.locationType.list()

        # Facilities
        requirements = self.plainTextEditRequirements.text()

        # Try to create preference object with the above parameters
        try:
            preference = Preference()  # can't call it

            print("Preference:", preference)

            # Let us update the list off employees and print it

            SavePreference.save_preference(preference)

        except Exception as p:
            print("Arrgh! Something went wrong!!", p)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Input error")
            msg.setText("Input not valid!")
            msg.setDetailedText(str(p))
            msg.exec()

            # can i clear it if it's not line edits?
            line_edits = self.findChildren(QtWidgets.QLineEdit)
            # Loop over the fields and clear them
            for field in line_edits:
                field.clear()

        print("-" * 30 + "\nThe database has the following preferences")
        for p in SavePreference.get_preference_list():
            print(p)

        print("-" * 30 + "\nThe database did last save this preference")
        print(SavePreference.get_current_preference())

    def clear_button_pressed(self):
        # This method is used in order to clear all input fields.
        # A simple, but naive approach will be to call
        # .clear() for all input fields, e.g. self.firstNameLineEdit.clear()
        # however this will require that we maintain the method if we add
        # more fields. A better approach would probably be to find all fields of type
        # LineEdit and clear them!
        # But first present the user with a warning message by using QMessagebox
        print('Clear button pressed!')

        button = QtWidgets.QMessageBox.question(self, "Clear fields", "All input fields will be cleared")

        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Yes!")
            # Find all fields of type QLineEdit
            line_edits = self.findChildren(QtWidgets.QLineEdit)
            # Loop over the fields and clear them
            for field in line_edits:
                field.clear()
        else:
            print("No!")

    def cancel_button_pressed(self):

        print('Cancel button pressed!')

        button = QtWidgets.QMessageBox.question(self, "Exit form?", "Do you want to save the existing?")

        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Yes!")
            print(type(self.parent()))
            if type(self.parent()) == QtWidgets.QStackedWidget:
                self.parent().setCurrentIndex(0)
            self.close()  # This will close Widget

        else:
            print("No!")

