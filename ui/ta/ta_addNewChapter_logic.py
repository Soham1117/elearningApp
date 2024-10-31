from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.ta.ta_addNewChapter_window import Ui_TaAddNewChapterWindow
from ui.ta.ta_addNewSection_logic import TAAddNewSectionLogic

class TAAddNewChapterLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_TaAddNewChapterWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.course_id = args[1]
        self.ui.lineEdit_3.setText("chap01")
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_back.clicked.connect(self.handle_back)
        self.ui.pushButton.clicked.connect(self.handle_add_new_section)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_new_section(self):
        chapter_id = self.ui.lineEdit_3.text()
        chapter_title = self.ui.lineEdit_4.text()
        if chapter_id[:4] != "chap":
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID should start with 'chap' followed by 2 digits.")
            return
        textbook_id = self.user_dao.get_textbook_by_course_id(self.course_id)[0]
        response, error = self.user_dao.add_new_chapter(textbook_id, chapter_id, chapter_title)
        if response:
            QtWidgets.QMessageBox.information(self, "Message", "Chapter added successfully.")
            self.ui_ta_addNewSection = TAAddNewSectionLogic([self, textbook_id, chapter_id])
            self.ui_ta_addNewSection.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", str(error))    