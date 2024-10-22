import sys
from PySide6 import QtWidgets
from ui.home_window import Ui_HomeWindow  # Import your generated home window class

from ui.admin_login_logic import AdminLoginLogic
from ui.faculty_login_logic import FacultyLoginLogic
from ui.ta_login_logic import TALoginLogic

class HomeWindowLogic(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomeWindow()  # Create an instance of the generated UI class
        self.ui.setupUi(self)  # Set up the UI

        # Connect the button click event to the login and exit functions
        self.ui.pushButton_6.clicked.connect(self.handle_login)
        self.ui.pushButton_5.clicked.connect(self.handle_exit)

    def handle_login(self):
        # Get the role from the ComboBox
        role = self.ui.comboBox.currentText()

        # Open the corresponding dashboard based on the role
        if role == "Admin":
            self.open_admin_dashboard()
        elif role == "Faculty":
            self.open_faculty_dashboard()
        elif role == "TA":
            self.open_ta_dashboard()
        # elif role == "Student":
        #     self.open_student_dashboard()

    def open_admin_dashboard(self):
        self.ui_admin = AdminLoginLogic(self)
        self.ui_admin.show()
        self.close()
    def open_faculty_dashboard(self):
        self.ui_faculty = FacultyLoginLogic(self)
        self.ui_faculty.show()
        self.close()

    def open_ta_dashboard(self):
        self.ui_ta = TALoginLogic(self)
        self.ui_ta.show()
        self.close()

    # def open_student_dashboard(self):
    #     self.student_dashboard = QtWidgets.QWidget()  # Create a new window for Student
    #     self.ui_student = Ui_StudentDashboard()  # Instance of the Student dashboard UI
    #     self.ui_student.setupUi(self.student_dashboard)  # Set up the Student dashboard
    #     self.student_dashboard.show()  # Show the Student dashboard

    def handle_exit(self):
        sys.exit(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    home_window = HomeWindowLogic()
    home_window.show()
    sys.exit(app.exec())
