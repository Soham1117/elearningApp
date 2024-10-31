from PySide6 import QtWidgets

from ui.student.student_landing_window import Ui_StudentLandingWindow

# from ui.student.student_viewSection_logic import StudentViewSectionLogic
# from ui.student.student_viewParticipationActivityPoints_logic import StudentViewParticipationActivityPointsLogic

class StudentLandingLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_StudentLandingWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.student_id = args[1]

        # self.ui.pushButton.clicked.connect(self.view_section)
        # self.ui.pushButton_2.clicked.connect(self.view_participation_activity_points)
        self.ui.pushButton_5.clicked.connect(self.handle_back)

    # def view_section(self):
    #     self.ui_go_to_active_course = StudentViewSectionLogic([self, self.student_id])
    #     self.ui_go_to_active_course.show()
    #     self.close()

    # def view_participation_activity_points(self):
    #     self.ui_go_to_evaluation_course = StudentViewParticipationActivityPointsLogic([self, self.student_id])
    #     self.ui_go_to_evaluation_course.show()
    #     self.close()

    def handle_back(self):
        self.previous_window.show()
        self.close()
