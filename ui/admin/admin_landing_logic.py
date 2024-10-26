from PySide6 import QtWidgets
from ui.admin.admin_landing_window import Ui_AdminLandingWindow
from ui.admin.admin_createAFacultyAccount_logic import createAFacultyAccountLogic
from ui.admin.admin_createAETextbook_logic import createAETexbookLogic
from ui.admin.admin_modifyETextbook_logic import modifyAETextbookLogic
from ui.admin.admin_createNewActiveCourse_logic import createNewActiveCourseLogic
from ui.admin.admin_createNewEvaluationCourse_logic import createNewEvaluationCourseLogic

class AdminLandingLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()
        self.ui = Ui_AdminLandingWindow()
        self.ui.setupUi(self)
        self.previous_window = previous_window

        self.ui.pushButton.clicked.connect(self.handle_create_faculty_account)
        self.ui.pushButton_2.clicked.connect(self.handle_create_etextbook)
        self.ui.pushButton_3.clicked.connect(self.handle_modify_etextbooks)
        self.ui.pushButton_4.clicked.connect(self.handle_create_new_active_course)
        self.ui.pushButton_5.clicked.connect(self.handle_back)
        self.ui.pushButton_6.clicked.connect(self.handle_create_new_evaluation_course)

    def handle_create_faculty_account(self):
        self.ui_create_faculty_account = createAFacultyAccountLogic(self)
        self.ui_create_faculty_account.show()
        self.close()

    def handle_create_etextbook(self):
        self.ui_create_etextbook = createAETexbookLogic(self)
        self.ui_create_etextbook.show()
        self.close()    

    def handle_modify_etextbooks(self):
        self.ui_modify_etextbook = modifyAETextbookLogic(self)
        self.ui_modify_etextbook.show()  
        self.close()

    def handle_create_new_active_course(self):
        self.ui_create_new_active_course = createNewActiveCourseLogic(self)
        self.ui_create_new_active_course.show()
        self.close()   

    def handle_create_new_evaluation_course(self):
        self.ui_create_new_evaluation_course = createNewEvaluationCourseLogic(self)
        self.ui_create_new_evaluation_course.show()
        self.close()    

    def handle_back(self):
        self.previous_window.show()
        self.close()
