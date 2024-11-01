from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.student.student_signin_window import Ui_StudentSigninWindow
from ui.student.student_landing_logic import StudentLandingLogic

class StudentSigninLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()
        self.ui = Ui_StudentSigninWindow()
        self.ui.setupUi(self)
        self.previous_window = previous_window

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)
        self.ui.lineEdit.setText("ArMo1024")
        self.ui.lineEdit_2.setText("jwocals")

        self.ui.lineEdit.setText("ErPe1024")
        self.ui.lineEdit_2.setText("qwdmq")

        self.ui.pushButton_6.clicked.connect(self.handle_login)
        self.ui.pushButton_5.clicked.connect(self.handle_back)

    def handle_login(self):
        student_id = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        # check if fields are empty
        if not student_id or not password:
            QtWidgets.QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        if self.user_dao.validate_student_credentials(student_id, password):
            QtWidgets.QMessageBox.information(self, "Login Successful", "Welcome, Student!")
            self.ui_student_landing = StudentLandingLogic([self.previous_window, student_id])
            self.ui_student_landing.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid User ID or password.")

    def handle_back(self):
        self.previous_window.show()
        self.close()

