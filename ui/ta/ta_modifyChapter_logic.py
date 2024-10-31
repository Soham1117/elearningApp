from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.ta.ta_modifyChapter_window import Ui_TaModifyChapterWindow
from ui.ta.ta_addNewSection_logic import TAAddNewSectionLogic
from ui.ta.ta_modifySection_logic import TAModifySectionLogic

class TAModifyChapterLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_TaModifyChapterWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.course_id = args[1]
        self.ui.lineEdit_3.setText("chap01")
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton.clicked.connect(self.handle_add_new_section)
        self.ui.pushButton_2.clicked.connect(self.handle_modify_section)
        self.ui.pushButton_back.clicked.connect(self.handle_back)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_new_section(self):
        chapter_id = self.ui.lineEdit_3.text()
        if chapter_id[:4] != "chap":
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID should start with 'chap' followed by 2 digits.")
            return
        textbook_id = self.user_dao.get_textbook_by_course_id(self.course_id)[0]
        if self.user_dao.checkChapter(textbook_id, chapter_id):
            self.ui_ta_addNewSection = TAAddNewSectionLogic([self, textbook_id, chapter_id])
            self.ui_ta_addNewSection.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID does not exist.")

    def handle_modify_section(self):
        chapter_id = self.ui.lineEdit_3.text()
        if chapter_id[:4] != "chap":
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID should start with 'chap' followed by 2 digits.")
            return
        textbook_id = self.user_dao.get_textbook_by_course_id(self.course_id)[0]
        if self.user_dao.checkChapter(textbook_id, chapter_id):
            self.ui_ta_modifySection = TAModifySectionLogic([self, textbook_id, chapter_id])
            self.ui_ta_modifySection.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID does not exist.")