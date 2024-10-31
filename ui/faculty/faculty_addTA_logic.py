import sys
from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection

from ui.faculty.faculty_addTA_window import Ui_FacultyAddTAWindow

class FacultyAddTALogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyAddTAWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.course_id = args[1]
        self.faculty_id = args[2]

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)

        self.display_course_details()

        self.ui.pushButton_6.clicked.connect(self.add_ta)
        self.ui.pushButton_5.clicked.connect(self.handle_back)

    def display_course_details(self):
        course = self.user_dao.get_course_by_course_id(self.course_id)

        if course:
            self.ui.label_3.setText(f"Course ID: {self.course_id}")
            self.ui.label_4.setText(f"Course Name: {course[0]}")

    def add_ta(self):
        first_name = self.ui.lineEdit.text()
        last_name = self.ui.lineEdit_2.text()
        email = self.ui.lineEdit_3.text()
        default_password = self.ui.lineEdit_4.text()

        # check if all fields are filled
        if not first_name or not last_name or not email or not default_password:
            QtWidgets.QMessageBox.warning(self, "Enrollment Failed", "Please fill in all fields")
            return

        # check if email is valid
        if not email.endswith("@ncsu.edu"):
            QtWidgets.QMessageBox.warning(self, "Enrollment Failed", "Please enter a valid email address")
            return
        
        # create new TA
        if self.user_dao.create_ta(first_name, last_name, email, default_password, self.course_id, self.faculty_id):
            QtWidgets.QMessageBox.information(self, "Enrollment Successful", "TA added successfully")
        else:
            QtWidgets.QMessageBox.warning(self, "Enrollment Failed", "Failed to add a TA")
            return
        self.handle_back()
    
    def handle_back(self):
        self.previous_window.show()
        self.close()