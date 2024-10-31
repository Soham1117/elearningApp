from PySide6 import QtWidgets
from ui.admin.admin_createNewActiveCourse_window import Ui_AdminCreateNewActiveCourseWindow
from db.db_connection import get_db_connection
from dao.user_dao import UserDAO

class createNewActiveCourseLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()

        self.ui = Ui_AdminCreateNewActiveCourseWindow()
        self.ui.setupUi(self)
        self.previous_window = previous_window

        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_back.clicked.connect(self.handle_back)
        self.ui.pushButton.clicked.connect(self.handle_add_active_course)
        self.ui.pushButton_2.clicked.connect(self.handle_admin_landing)
    
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_active_course(self):
        course_id = self.ui.lineEdit_3.text()
        course_name = self.ui.lineEdit_4.text()
        etextbook_id = self.ui.lineEdit_5.text()
        course_start_date = self.ui.lineEdit_6.text()
        course_end_date = self.ui.lineEdit_7.text()
        unique_token = self.ui.lineEdit_8.text()
        course_capacity = self.ui.lineEdit_9.text()
        faculty_id = self.ui.lineEdit_10.text()
        if self.user_dao.checkTextbook(etextbook_id) == False:
            QtWidgets.QMessageBox.warning(self, "Warning", "E Textbook ID does not exist.")
            return
        if self.user_dao.checkFaculty(faculty_id) == False:
            QtWidgets.QMessageBox.warning(self, "Warning", "Faculty ID does not exist.")
            return
        
        response, error = self.user_dao.add_active_course(course_id, course_name, etextbook_id, course_start_date, course_end_date, unique_token, course_capacity, faculty_id)
        if response:
            QtWidgets.QMessageBox.information(self, "Message", "Active Course added successfully.")
            self.previous_window.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", str(error))    
    
    def handle_admin_landing(self):
        self.handle_back()
        self.close()