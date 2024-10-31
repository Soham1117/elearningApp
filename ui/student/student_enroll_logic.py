from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.student.student_enroll_window import Ui_StudentEnrollWindow
from ui.student.student_signup_logic import StudentSignupLogic


class StudentEnrollLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()
        self.ui = Ui_StudentEnrollWindow()
        self.ui.setupUi(self)
        self.previous_window = previous_window

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton.clicked.connect(self.handle_enroll)
        self.ui.pushButton_back.clicked.connect(self.handle_back)

    def handle_enroll(self):
        first_name = self.ui.lineEdit.text()
        last_name = self.ui.lineEdit_2.text()
        email = self.ui.lineEdit_3.text()
        course_token = self.ui.lineEdit_4.text()

        # Check if fields are empty
        if not first_name or not last_name or not email or not course_token:
            QtWidgets.QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return
        
        # Check if email is valid
        if '@' not in email:
            QtWidgets.QMessageBox.warning(self, "Error", "Please enter a valid email.")
            return

        # Check if course token is valid
        if not self.user_dao.is_valid_active_course_token(course_token):
            QtWidgets.QMessageBox.warning(self, "Error", "Please enter a valid Active course token.")
            return
        
        # If student is already registered user
        # Retrieve student details and enroll else go to signup window and then enroll
        result = self.user_dao.check_student_in_enrolls(first_name, last_name, email)
        if result[0] and result[1]:
            # TODO: add error handling
            if self.user_dao.enroll(first_name, last_name, email, course_token):
                QtWidgets.QMessageBox.information(self, "Enrollment Successful", "Enrollment successful!")
                self.handle_back()
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Failed to enroll student.")
                return
        elif result[0] and not result[1]:
            # call signup window
            self.student_signup_logic = StudentSignupLogic([self.previous_window, course_token, first_name, last_name, email])
            self.student_signup_logic.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Enrollment Failed", "Enrollment Failed. Please try again with valid details or after some time.")
            return

    def handle_back(self):
        self.previous_window.show()
        self.close()

