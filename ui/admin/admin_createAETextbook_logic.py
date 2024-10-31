from PySide6 import QtWidgets
from ui.admin.admin_createAETextbook_window import Ui_AdminCreateAETextbookWindow
from ui.admin.admin_addNewChapter_logic import AdminAddNewChapterLogic
from db.db_connection import get_db_connection
from dao.user_dao import UserDAO

class createAETexbookLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()

        self.ui = Ui_AdminCreateAETextbookWindow()
        self.ui.setupUi(self)
        self.previous_window = previous_window

        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_back.clicked.connect(self.handle_back)
        self.ui.pushButton.clicked.connect(self.handle_add_new_chapter)

    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_new_chapter(self):
        title = self.ui.lineEdit_3.text()
        etextbook_id = self.ui.lineEdit_4.text()
        
        response, error = self.user_dao.add_new_etextbook(title, etextbook_id)
        if response:
            QtWidgets.QMessageBox.information(self, "Message", "E Textbook added successfully.")
            self.ui_admin_add_new_chapter = AdminAddNewChapterLogic([self, etextbook_id, self.previous_window])
            self.ui_admin_add_new_chapter.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", str(error))    