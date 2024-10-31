import sys
from PySide6 import QtWidgets
from ui.MainWindow_window import Ui_MainWindow
from ui.admin.admin_login_logic import AdminLoginLogic
from ui.faculty.faculty_login_logic import FacultyLoginLogic
from ui.ta.ta_login_logic import TALoginLogic
from ui.student.student_login_logic import StudentLoginLogic

class MainWindowLogic(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_6.clicked.connect(self.handle_login)
        self.ui.pushButton_5.clicked.connect(self.handle_exit)

    def handle_login(self):
        # Get the role from the ComboBox
        role = self.ui.comboBox.currentText()

        if role == "Admin":
            self.open_admin_dashboard()
        elif role == "Faculty":
            self.open_faculty_dashboard()
        elif role == "TA":
            self.open_ta_dashboard()
        elif role == "Student":
            self.open_student_dashboard()

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
    def open_student_dashboard(self):
        self.ui_student = StudentLoginLogic(self)
        self.ui_student.show()
        self.close()

    def handle_exit(self):
        sys.exit(0)

