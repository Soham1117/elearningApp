from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.admin.admin_login_window import Ui_AdminLoginWindow
from ui.admin.admin_landing_logic import AdminLandingLogic

class AdminLoginLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()
        self.ui = Ui_AdminLoginWindow()
        self.ui.setupUi(self)
        self.previous_window = previous_window

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)

        self.ui.lineEdit.setText("1")
        self.ui.lineEdit_2.setText("1")
        self.ui.pushButton_6.clicked.connect(self.handle_login)
        self.ui.pushButton_5.clicked.connect(self.handle_back)

    def handle_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        
        if self.user_dao.validate_credentials(username, password):
            self.ui_admin_landing = AdminLandingLogic(self.previous_window)
            self.ui_admin_landing.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def handle_back(self):
        self.previous_window.show()
        self.close()    
        
