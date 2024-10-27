from PySide6 import QtWidgets

from ui.faculty.faculty_landing_window import Ui_FacultyLandingWindow

# add button related classes here
# from ui.admin.admin_createAFacultyAccount_logic import createAFacultyAccountLogic
# from ui.admin.admin_createAETextbook_logic import createAETexbookLogic
# from ui.admin.admin_modifyETextbook_logic import modifyAETextbookLogic
# from ui.admin.admin_createNewActiveCourse_logic import createNewActiveCourseLogic
# from ui.admin.admin_createNewEvaluationCourse_logic import createNewEvaluationCourseLogic

class FacultyLandingLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()
        self.ui = Ui_FacultyLandingWindow()
        self.ui.setupUi(self)
        self.previous_window = previous_window

        # self.ui.pushButton.clicked.connect(self.go_to_active_courses)
        # self.ui.pushButton_2.clicked.connect(self.go_to_evaluation_courses)
        # self.ui.pushButton_3.clicked.connect(self.view_courses)
        # self.ui.pushButton_4.clicked.connect(self.change_password)
        self.ui.pushButton_5.clicked.connect(self.handle_back)

    # def go_to_active_courses(self):
    #     self.ui_create_faculty_account = createAFacultyAccountLogic(self)
    #     self.ui_create_faculty_account.show()
    #     self.close()

    # def go_to_evaluation_courses(self):
    #     self.ui_create_etextbook = createAETexbookLogic(self)
    #     self.ui_create_etextbook.show()
    #     self.close()

    # def view_courses(self):
    #     self.ui_modify_etextbook = modifyAETextbookLogic(self)
    #     self.ui_modify_etextbook.show()
    #     self.close()

    # def change_password(self):
    #     self.ui_create_new_active_course = createNewActiveCourseLogic(self)
    #     self.ui_create_new_active_course.show()
    #     self.close()

    def handle_back(self):
        self.previous_window.show()
        self.close()