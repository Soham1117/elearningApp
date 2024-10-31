from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.admin.admin_modifyChapter_window import Ui_AdminModifyChapterWindow
from ui.admin.admin_addNewSection_logic import AdminAddNewSectionLogic
from ui.admin.admin_modifySection_logic import AdminModifySectionLogic
from ui.faculty.faculty_add_new_section_window_logic import FacultyAddNewSectionLogic
from ui.faculty.faculty_delete_chapter_window_logic import FacultyDeleteChapterLogic
from ui.faculty.faculty_hide_chapter_window_logic import FacultyHideChapterLogic
from ui.faculty.faculty_modify_chapter_window import Ui_FacultyModifyChapterWindow
from ui.faculty.faculty_modify_section_window_logic import FacultyModifySectionLogic

class FacultyModifyChapterLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyModifyChapterWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.ui.lineEdit_3.setText("chap01")
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton.clicked.connect(self.handle_add_new_section)
        self.ui.pushButton_2.clicked.connect(self.handle_modify_section)
        self.ui.pushButton_3.clicked.connect(self.handle_hide_chapter)
        self.ui.pushButton_back.clicked.connect(self.handle_back)
        self.ui.delete_chapter.clicked.connect(self.handle_delete_chapter)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_new_section(self):
        chapter_id = self.ui.lineEdit_3.text()
        textbook_id=self.ui.lineEdit_4.text()
        if chapter_id[:4] != "chap":
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID should start with 'chap' followed by 2 digits.")
            return
        if self.user_dao.checkChapter(textbook_id, chapter_id):
            self.ui_admin_add_new_section = FacultyAddNewSectionLogic([self, textbook_id, chapter_id])
            self.ui_admin_add_new_section.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID does not exist.")

    def handle_modify_section(self):
        chapter_id = self.ui.lineEdit_3.text()
        textbook_id=self.ui.lineEdit_4.text()
        if chapter_id[:4] != "chap":
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID should start with 'chap' followed by 2 digits.")
            return
        if self.user_dao.checkChapter(textbook_id, chapter_id):
            self.ui_admin_modify_section = FacultyModifySectionLogic([self, textbook_id, chapter_id])
            self.ui_admin_modify_section.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID does not exist.")
    
    def handle_admin_landing(self):
        self.admin_landing_window.show()
        self.close()

    def handle_hide_chapter(self):
        chapter_id = self.ui.lineEdit_3.text()
        textbook_id=self.ui.lineEdit_4.text()
        if chapter_id[:4] != "chap":
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID should start with 'chap' followed by 2 digits.")
            return
        if self.user_dao.checkChapter(textbook_id, chapter_id):
            self.ui_admin_modify_section =FacultyHideChapterLogic([self, textbook_id, chapter_id])
            self.ui_admin_modify_section.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID or TextBook ID does not exist.")    

    def handle_delete_chapter(self):
        chapter_id = self.ui.lineEdit_3.text()
        textbook_id=self.ui.lineEdit_4.text()
        if chapter_id[:4] != "chap":
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID should start with 'chap' followed by 2 digits.")
            return
        if self.user_dao.checkChapter(textbook_id, chapter_id):
            self.ui_admin_modify_section = FacultyDeleteChapterLogic([self, textbook_id, chapter_id])
            self.ui_admin_modify_section.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID or TextBook ID does not exist.")    

