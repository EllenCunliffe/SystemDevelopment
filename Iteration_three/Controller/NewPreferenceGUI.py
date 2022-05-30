from PyQt6 import QtWidgets, uic
from Iteration_three.Model import ActiveModel
from Iteration_three.Model import Preference


class NewPreferenceGUI(QtWidgets.QWidget):
    def __init__(self):
        super(NewPreferenceGUI, self).__init__()
        uic.loadUi('View/NewPreference_form.ui', self)
        print("NewPreferenceGUI called")
        print("-" * 30 + "\nGUI: We have the following preferences in the required preference")
        for p in ActiveModel.get_preference_list(self):
            print(p)

        self.pushButtonOk.clicked.connect(self.request_button_pressed)
        self.pushButtonClear.clicked.connect(self.clear_button_pressed)
        self.pushButtonCancel.clicked.connect(self.cancel_button_pressed)

        self.show()



