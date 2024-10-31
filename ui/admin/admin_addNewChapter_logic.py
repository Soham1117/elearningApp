from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.admin.admin_addNewChapter_window import Ui_AdminAddNewChapterWindow
from ui.admin.admin_addNewSection_logic import AdminAddNewSectionLogic

class AdminAddNewChapterLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_AdminAddNewChapterWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id = args[1]
        self.admin_landing_window = args[2]
        self.ui.lineEdit_3.setText("chap01")
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_back.clicked.connect(self.handle_back)
        self.ui.pushButton.clicked.connect(self.handle_add_new_section)
        self.ui.pushButton_2.clicked.connect(self.handle_admin_landing)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_new_section(self):
        chapter_id = self.ui.lineEdit_3.text()
        chapter_title = self.ui.lineEdit_4.text()
        if chapter_id[:4] != "chap":
            QtWidgets.QMessageBox.warning(self, "Warning", "Chapter ID should start with 'chap' followed by 2 digits.")
            return
        response, error = self.user_dao.add_new_chapter(self.textbook_id, chapter_id, chapter_title)
        if response:
            QtWidgets.QMessageBox.information(self, "Message", "Chapter added successfully.")
            self.ui_admin_add_new_section = AdminAddNewSectionLogic([self, self.textbook_id, chapter_id, self.admin_landing_window])
            self.ui_admin_add_new_section.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", str(error))    
    
    def handle_admin_landing(self):
        self.admin_landing_window.show()
        self.close()