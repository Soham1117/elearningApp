from PySide6 import QtWidgets
from ui.admin.admin_createNewEvaluationCourse_window import Ui_AdminCreateNewEvaluationCourseWindow
from db.db_connection import get_db_connection
from dao.user_dao import UserDAO

class createNewEvaluationCourseLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()

        self.ui = Ui_AdminCreateNewEvaluationCourseWindow()
        self.ui.setupUi(self)
        self.previous_window = previous_window

        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_back.clicked.connect(self.handle_back)
        self.ui.pushButton.clicked.connect(self.handle_add_evaluation_course)
        self.ui.pushButton_2.clicked.connect(self.handle_admin_landing)
    
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_evaluation_course(self):
        course_id = self.ui.lineEdit_3.text()
        course_name = self.ui.lineEdit_4.text()
        etextbook_id = self.ui.lineEdit_5.text()
        faculty_id = self.ui.lineEdit_6.text()
        course_start_date = self.ui.lineEdit_7.text()
        course_end_date = self.ui.lineEdit_8.text()
        
        if self.user_dao.checkTextbook(etextbook_id) == False:
            QtWidgets.QMessageBox.warning(self, "Warning", "E Textbook ID does not exist.")
            return
        if self.user_dao.checkFaculty(faculty_id) == False:
            QtWidgets.QMessageBox.warning(self, "Warning", "Faculty ID does not exist.")
            return
        
        response, error = self.user_dao.add_evaluation_course(course_id, course_name, etextbook_id, course_start_date, course_end_date, faculty_id)
        if response:
            QtWidgets.QMessageBox.information(self, "Message", "Evaluation Course added successfully.")
            self.previous_window.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", str(error))    
    
    def handle_admin_landing(self):
        self.handle_back()
        self.close()