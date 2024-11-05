from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection

from ui.faculty.faculty_goToActiveCourse_window import Ui_FacultyGoToActiveCourseWindow

from ui.faculty.faculty_viewWorklist_logic import FacultyViewWorklistLogic
from ui.faculty.faculty_approveEnrollment_logic import FacultyApproveEnrollmentLogic
from ui.faculty.faculty_viewStudents_logic import FacultyViewStudentsLogic
from ui.faculty.faculty_add_new_chapter_window_logic import FacultyAddNewChapterLogic
from ui.faculty.faculty_modify_chapter_window_logic import FacultyModifyChapterLogic
from ui.faculty.faculty_addTA_logic import FacultyAddTALogic

class FacultyGoToActiveCourseLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyGoToActiveCourseWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.faculty_id = args[1]

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)

        # handle input
        self.ui.lineEdit_3.setText("NCSUOganCSC540F24")
        # course_id = self.ui.lineEdit_3.text()

        # handle button clicks
        self.ui.pushButton.clicked.connect(self.view_worklist)
        self.ui.pushButton_2.clicked.connect(self.approve_enrollment)
        self.ui.pushButton_3.clicked.connect(self.view_students)
        self.ui.pushButton_4.clicked.connect(self.add_new_chapter)
        self.ui.pushButton_5.clicked.connect(self.add_ta)
        self.ui.pushButton_6.clicked.connect(self.modify_chapters)
        self.ui.pushButton_back.clicked.connect(self.handle_back)

    def view_worklist(self):
        if not self.check_faculty_course_match():
            QtWidgets.QMessageBox.warning(self, "Warning", "You are not a faculty of this course! Please check your course ID and try again. Or this is not valid Active course ID. Please try again.")
            return
        course_id = self.ui.lineEdit_3.text()

        self.faculty_viewWorklist_logic = FacultyViewWorklistLogic([self, course_id])
        self.faculty_viewWorklist_logic.show()
        self.close()

    def approve_enrollment(self):
        if not self.check_faculty_course_match():
            QtWidgets.QMessageBox.warning(self, "Warning", "You are not a faculty of this course! Please check your course ID and try again. Or this is not valid Active course ID. Please try again.")
            return
        course_id = self.ui.lineEdit_3.text()

        self.faculty_approveEnrollment_logic = FacultyApproveEnrollmentLogic([self, course_id])
        self.faculty_approveEnrollment_logic.show()
        self.close()

    def view_students(self):
        if not self.check_faculty_course_match():
            QtWidgets.QMessageBox.warning(self, "Warning", "You are not a faculty of this course! Please check your course ID and try again. Or this is not valid Active course ID. Please try again.")
            return
        course_id = self.ui.lineEdit_3.text()

        self.faculty_viewStudents_logic = FacultyViewStudentsLogic([self, course_id])
        self.faculty_viewStudents_logic.show()
        self.close()

    def add_new_chapter(self):
        if not self.check_faculty_course_match():
            QtWidgets.QMessageBox.warning(self, "Warning", "You are not a faculty of this course! Please check your course ID and try again. Or this is not valid Active course ID. Please try again.")
            return
        course_id = self.ui.lineEdit_3.text()

        self.faculty_addNewChapter_logic = FacultyAddNewChapterLogic([self, self.faculty_id, course_id])
        self.faculty_addNewChapter_logic.show()
        self.close()

    def modify_chapters(self):
        if not self.check_faculty_course_match():
            QtWidgets.QMessageBox.warning(self, "Warning", "You are not a faculty of this course! Please check your course ID and try again. Or this is not valid Active course ID. Please try again.")
            return
        course_id = self.ui.lineEdit_3.text()

        self.faculty_modifyChapters_logic = FacultyModifyChapterLogic([self, self.faculty_id, course_id])
        self.faculty_modifyChapters_logic.show()
        self.close()

    def add_ta(self):
        if not self.check_faculty_course_match():
            QtWidgets.QMessageBox.warning(self, "Warning", "You are not a faculty of this course! Please check your course ID and try again. Or this is not valid Active course ID. Please try again.")
            return
        course_id = self.ui.lineEdit_3.text()

        self.faculty_addTa_logic = FacultyAddTALogic([self, course_id, self.faculty_id])
        self.faculty_addTa_logic.show()
        self.close()

    def handle_back(self):
        self.previous_window.show()
        self.close()

    def check_faculty_course_match(self):
        course_id = self.ui.lineEdit_3.text()

        return self.user_dao.check_faculty_course_match(course_id, self.faculty_id, "Active")
