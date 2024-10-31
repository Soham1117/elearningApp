from PySide6 import QtWidgets
from ui.admin.admin_modifyETextbook_window import Ui_AdminModifyETextbookWindow
from ui.admin.admin_addNewChapter_logic import AdminAddNewChapterLogic
from ui.admin.admin_modifyChapter_logic import AdminModifyChapterLogic
from db.db_connection import get_db_connection
from dao.user_dao import UserDAO

class modifyAETextbookLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()

        self.ui = Ui_AdminModifyETextbookWindow()
        self.ui.setupUi(self)
        self.previous_window = previous_window

        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton.clicked.connect(self.handle_add_new_chapter)
        self.ui.pushButton_2.clicked.connect(self.handle_modify_chapter)
        self.ui.pushButton_3.clicked.connect(self.handle_admin_landing)
        self.ui.pushButton_back.clicked.connect(self.handle_back)

    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_modify_chapter(self):
        etextbook_id = self.ui.lineEdit_3.text()
        if self.user_dao.checkTextbook(etextbook_id):
            self.ui_admin_modify_chapter = AdminModifyChapterLogic([self, etextbook_id, self.previous_window])
            self.ui_admin_modify_chapter.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "E Textbook ID does not exist.")
    
    def handle_add_new_chapter(self):
        etextbook_id = self.ui.lineEdit_3.text()
        if self.user_dao.checkTextbook(etextbook_id):
            self.ui_admin_add_new_chapter = AdminAddNewChapterLogic([self, etextbook_id, self.previous_window])
            self.ui_admin_add_new_chapter.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "E Textbook ID does not exist.")
        
    def handle_admin_landing(self):
        self.handle_back()