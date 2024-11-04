from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.faculty.faculty_add_new_chapter_window import Ui_FacultyAddNewChapterWindow
from ui.faculty.faculty_add_new_section_window_logic import FacultyAddNewSectionLogic

class FacultyAddNewChapterLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyAddNewChapterWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.faculty_id=args[1]
        self.course_id=args[2]
        self.ui.lineEdit_5.setText("chap01")
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_back_2.clicked.connect(self.handle_back)
        self.ui.pushButton_4.clicked.connect(self.handle_add_new_section)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_new_section(self):
        
        textbook_id=self.get_textbook_id_from_course_id()
        if textbook_id is None:
            return

        chapter_id = self.ui.lineEdit_5.text()
        chapter_title = self.ui.lineEdit_6.text()
        if chapter_id[:4] != "chap":
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID should start with 'chap' followed by 2 digits.")
            return
        response, error = self.user_dao.add_new_chapter(textbook_id, chapter_id, chapter_title)
        if response:
            QtWidgets.QMessageBox.information(self, "Message", "Chapter added successfully.")
            self.ui_admin_add_new_section = FacultyAddNewSectionLogic([self, textbook_id, chapter_id])
            self.ui_admin_add_new_section.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", str(error))    
    
    def handle_admin_landing(self):
        self.admin_landing_window.show()
        self.close()


    def get_textbook_id_from_course_id(self):
        response,id=self.user_dao.get_textbook_id_from_course_id(self.course_id)
        print(response,id)
        if response:
            return id
        else:
            QtWidgets.QMessageBox.warning(self, "Warning",str(id))
            return None    

