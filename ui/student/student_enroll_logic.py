from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.student.student_enroll_window import Ui_StudentEnrollWindow


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

        if self.user_dao.enroll(first_name, last_name, email, course_token):
            QtWidgets.QMessageBox.information(self, "Message", "Enrollment Successful!")
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid User ID or password.")

    def handle_back(self):
        self.previous_window.show()
        self.close()

