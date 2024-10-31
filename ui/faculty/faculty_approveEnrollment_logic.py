import sys
from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection

from ui.faculty.faculty_approveEnrollment_window import Ui_FacultyApproveEnrollmentWindow

class FacultyApproveEnrollmentLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyApproveEnrollmentWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.course_id = args[1]

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)

        self.display_course_details()

        self.ui.pushButton_6.clicked.connect(self.handle_enrollment)
        self.ui.pushButton_5.clicked.connect(self.handle_back)

    def display_course_details(self):
        course = self.user_dao.get_course_by_course_id(self.course_id)

        if course:
            self.ui.label_3.setText(f"Course ID: {self.course_id}")
            self.ui.label_4.setText(f"Course Name: {course[0]}")

    def handle_enrollment(self):
        student_id = self.ui.lineEdit.text()

        # check if student exists with student id
        student = self.user_dao.get_student_by_student_id(student_id)

        if not student:
            QtWidgets.QMessageBox.warning(self, "Enrollment Failed", "Invalid Student ID")
            return

        # check if enrollment is already approved
        if self.user_dao.get_enrollment_by_student_id_and_course_id(student_id, self.course_id):
            # print("Student already enrolled in the course")
            QtWidgets.QMessageBox.warning(self, "Enrollment Failed", "Student already enrolled in the course")
            return

        # approve enrollment
        if self.user_dao.approve_enrollment(student_id, self.course_id):
            # print("Enrollment approved successfully")
            QtWidgets.QMessageBox.information(self, "Enrollment Approved", "Enrollment approved successfully")
        else:
            QtWidgets.QMessageBox.warning(self, "Enrollment Failed", "Failed to approve enrollment")
        self.handle_back()
    
    def handle_back(self):
        self.previous_window.show()
        self.close()