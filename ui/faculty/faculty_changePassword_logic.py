import sys
from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection

from ui.faculty.faculty_changePassword_window import Ui_FacultyChangePasswordWindow

class FacultyChangePasswordLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyChangePasswordWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.faculty_id = args[1]

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_6.clicked.connect(self.change_password)
        self.ui.pushButton_5.clicked.connect(self.handle_back)

    def change_password(self):
        current_password = self.ui.lineEdit.text()
        new_password = self.ui.lineEdit_2.text()
        confirm_new_password = self.ui.lineEdit_3.text()

        if new_password == confirm_new_password:
            if self.user_dao.change_faculty_password(self.faculty_id, current_password, new_password):
                self.previous_window.show()
                QtWidgets.QMessageBox.information(self, "Password Changed", "Password changed successfully.")
                self.close()
            else:
                QtWidgets.QMessageBox.warning(self, "Password Change Failed", "Failed to change password.")
        else:
            QtWidgets.QMessageBox.warning(self, "Password Change Failed", "New Password and Confirm New Password do not match.")

    def handle_back(self):
        self.previous_window.show()
        self.close()
