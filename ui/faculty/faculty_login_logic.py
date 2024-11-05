from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.faculty.faculty_login_window import Ui_FacultyLoginWindow
from ui.faculty.faculty_landing_logic import FacultyLandingLogic

class FacultyLoginLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()
        self.ui = Ui_FacultyLoginWindow()
        self.ui.setupUi(self)
        self.previous_window = previous_window

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)

        self.ui.lineEdit.setText("KeOg1024")
        self.ui.lineEdit_2.setText("Ko2024!rpc")
        self.ui.pushButton_6.clicked.connect(self.handle_login)
        self.ui.pushButton_5.clicked.connect(self.handle_back)

    def handle_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        
        if self.user_dao.validate_faculty_credentials(username, password):
            self.ui_faculty_landing = FacultyLandingLogic([self.previous_window, username])
            self.ui_faculty_landing.show()
            self.close()
            QtWidgets.QMessageBox.information(self, "Login Successful", "Welcome, Faculty!")
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid User ID or password.")

    def handle_back(self):
        self.previous_window.show()
        self.close()

