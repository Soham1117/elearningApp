from PySide6 import QtWidgets
from dao.user_dao import UserDAO    
from db.db_connection import get_db_connection 
from ui.admin.admin_createAFacultyAccount_window import Ui_AdminCreateAFacultyAccountWindow

class createAFacultyAccountLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()
        self.ui = Ui_AdminCreateAFacultyAccountWindow()
        self.ui.setupUi(self)
        self.previous_window = previous_window
        
        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)
        
        self.ui.pushButton_back.clicked.connect(self.handle_back)
        self.ui.pushButton.clicked.connect(self.handle_add_user)
        
    def handle_back(self):
        self.previous_window.show()
        self.close()
        
    def handle_add_user(self):
        first_name = self.ui.lineEdit_3.text()
        last_name = self.ui.lineEdit_4.text()
        email = self.ui.lineEdit_5.text()
        password = self.ui.lineEdit_6.text()
        
        self.user_dao.create_faculty(first_name, last_name, email, password)
        QtWidgets.QMessageBox.information(self, "User Created", "User created successfully.")
        self.handle_back()
        
    
        