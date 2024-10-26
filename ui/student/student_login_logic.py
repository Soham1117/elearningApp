from PySide6 import QtWidgets
from ui.student.student_login_window import Ui_StudentLoginWindow
from ui.student.student_enroll_logic import StudentEnrollLogic
from ui.student.student_signin_logic import StudentSigninLogic

class StudentLoginLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()
        self.ui = Ui_StudentLoginWindow()
        self.ui.setupUi(self)
        self.previous_window = previous_window

        self.ui.pushButton_7.clicked.connect(self.handle_signin)
        self.ui.pushButton_6.clicked.connect(self.handle_enroll)
        self.ui.pushButton_5.clicked.connect(self.handle_back)

    def handle_signin(self):
        self.ui_student_signin = StudentSigninLogic(self)
        self.ui_student_signin.show()
        self.close()

    def handle_enroll(self):
        self.ui_student_enroll = StudentEnrollLogic(self)
        self.ui_student_enroll.show()
        self.close()

    def handle_back(self):
        self.previous_window.show()
        self.close()

