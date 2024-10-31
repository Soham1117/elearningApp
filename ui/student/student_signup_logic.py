from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.student.student_signup_window import Ui_StudentSignupWindow

class StudentSignupLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_StudentSignupWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.course_token = args[1]
        self.first_name = args[2]
        self.last_name = args[3]
        self.email = args[4]

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_6.clicked.connect(self.handle_login)
        self.ui.pushButton_5.clicked.connect(self.handle_back)

    def handle_login(self):
        password = self.ui.lineEdit.text()
        confirm_password = self.ui.lineEdit_2.text()
        if not password == confirm_password:
            QtWidgets.QMessageBox.warning(self, "Error", "Passwords do not match. Retype password.")
            return
        
        # Check if fields are empty
        if not password or not confirm_password:
            QtWidgets.QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        # signup/create student account
        if self.user_dao.create_student(self.first_name, self.last_name, self.email, password):
            if self.user_dao.enroll(self.first_name, self.last_name, self.email, self.course_token):
                QtWidgets.QMessageBox.information(self, "Enrollment Successful", "Sign up and enrollment successful!")
                self.handle_back()
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Failed to enroll student.")
                return
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to create student account.")
            return

    def handle_back(self):
        self.previous_window.show()
        self.close()
