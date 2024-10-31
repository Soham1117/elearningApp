from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.ta.ta_goToActiveCourse_window import Ui_TaGoToActiveCourseWindow
from ui.ta.ta_viewStudents_logic import TAViewStudentsLogic
from ui.ta.ta_addNewChapter_logic import TAAddNewChapterLogic
from ui.ta.ta_modifyChapter_logic import TAModifyChapterLogic

class TAGoToActiveCourseLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_TaGoToActiveCourseWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit_3.setText("NCSUOganCSC440F24")
        self.previous_window = args[0]
        self.ta_id = args[1]
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

       
        self.ui.pushButton.clicked.connect(self.view_students)
        self.ui.pushButton_2.clicked.connect(self.add_new_chapter)
        self.ui.pushButton_3.clicked.connect(self.modify_chapters)
        self.ui.pushButton_back.clicked.connect(self.handle_ta_landing)
        
    # def handle_back(self):    
    #     self.previous_window.show()
    #     self.close()

    def view_students(self):
        course_id = self.ui.lineEdit_3.text()
        if course_id[:4] != "NCSU":
            QtWidgets.QMessageBox.warning(self, "Warning", "CourseID should start with 'NCSU'.")
            return
        self.ta_viewStudents = TAViewStudentsLogic([self, course_id])
        self.ta_viewStudents.show()
        self.close()

    def add_new_chapter(self):
        course_id = self.ui.lineEdit_3.text()
        if course_id[:4] != "NCSU":
            QtWidgets.QMessageBox.warning(self, "Warning", "CourseID should start with 'NCSU'.")
            return
        self.ta_addNewChapter = TAAddNewChapterLogic([self, course_id])
        self.ta_addNewChapter.show()
        self.close()

    def modify_chapters(self):
        course_id = self.ui.lineEdit_3.text()
        if course_id[:4] != "NCSU":
            QtWidgets.QMessageBox.warning(self, "Warning", "CourseID should start with 'NCSU'.")
            return
        self.ta_modifyChapters = TAModifyChapterLogic([self, course_id])
        self.ta_modifyChapters.show()
        self.close()
    
    def handle_ta_landing(self):
        self.previous_window.show()
        self.close()