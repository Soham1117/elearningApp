from PySide6 import QtWidgets

from ui.faculty.faculty_landing_window import Ui_FacultyLandingWindow

# from ui.faculty.faculty_goToActiveCourse_logic import GoToActiveCourseLogic
# from ui.faculty.faculty_goToEvaluationCourse_logic import GoToEvaluationCourseLogic
# from ui.faculty.faculty_viewCourses_logic import ViewCoursesLogic
from ui.faculty.faculty_changePassword_logic import FacultyChangePasswordLogic

class FacultyLandingLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyLandingWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.faculty_id = args[1]

        # self.ui.pushButton.clicked.connect(self.go_to_active_courses)
        # self.ui.pushButton_2.clicked.connect(self.go_to_evaluation_courses)
        # self.ui.pushButton_3.clicked.connect(self.view_courses)
        self.ui.pushButton_4.clicked.connect(self.change_password)
        self.ui.pushButton_5.clicked.connect(self.handle_back)

    # def go_to_active_courses(self):
    #     self.ui_go_to_active_course = GoToActiveCourseLogic(self)
    #     self.ui_go_to_active_course.show()
    #     self.close()

    # def go_to_evaluation_courses(self):
    #     self.ui_go_to_evaluation_course = GoToEvaluationCourseLogic(self)
    #     self.ui_go_to_evaluation_course.show()
    #     self.close()

    # def view_courses(self):
    #     self.ui_view_courses = ViewCoursesLogic(self)
    #     self.ui_view_courses.show()
    #     self.close()

    def change_password(self):
        self.ui_change_password = FacultyChangePasswordLogic([self, self.faculty_id])
        self.ui_change_password.show()
        self.close()

    def handle_back(self):
        self.previous_window.show()
        self.close()
