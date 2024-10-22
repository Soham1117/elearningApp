import sys
from PySide6 import QtWidgets
from ui.signup_window import Ui_Form  # Import your generated signup window class
from dao.user_dao import UserDAO  # Import your UserDAO
from db.db_connection import get_db_connection  # Import your database connection

class SignupWindowLogic(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  # Create an instance of the generated UI class
        self.ui.setupUi(self)  # Set up the UI

        # Initialize UserDAO
        self.db_connection = get_db_connection()  # Use the imported db connection
        self.user_dao = UserDAO(self.db_connection)

        # Connect the button click event to the signup function
        self.ui.pushButton.clicked.connect(self.handle_signup)

    def handle_signup(self):
        user_id = self.ui.lineEdit.text().strip()  # Changed to QLineEdit
        first_name = self.ui.lineEdit_2.text().strip()  # Changed to QLineEdit
        last_name = self.ui.lineEdit_3.text().strip()  # Changed to QLineEdit
        email = self.ui.lineEdit_4.text().strip()  # Changed to QLineEdit
        password = self.ui.lineEdit_5.text().strip()  # Changed to QLineEdit
        role = self.ui.comboBox.currentText()

        # Validate input fields
        if not all([user_id, first_name, last_name, email, password, role]):
            QtWidgets.QMessageBox.warning(self, "Error", "All fields are required!")
            return

        # Call the DAO method to create the user
        if self.user_dao.create_user(user_id, first_name, last_name, email, password, role):
            QtWidgets.QMessageBox.information(self, "Success", "User registered successfully!")
            self.clear_inputs()  # Clear input fields after successful registration
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "User registration failed!")

    def clear_inputs(self):
        self.ui.lineEdit.clear()       # Clear the QLineEdit
        self.ui.lineEdit_2.clear()     # Clear the QLineEdit
        self.ui.lineEdit_3.clear()     # Clear the QLineEdit
        self.ui.lineEdit_4.clear()     # Clear the QLineEdit
        self.ui.lineEdit_5.clear()     # Clear the QLineEdit
        self.ui.comboBox.setCurrentIndex(0)  # Reset to the first item in the combo box

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    signup_window = SignupWindowLogic()
    signup_window.show()
    sys.exit(app.exec())
