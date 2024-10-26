from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.admin.admin_addNewSection_window import Ui_AdminAddNewSectionWindow
from ui.admin.admin_addNewContentBlock_logic import AdminAddNewContentBlockLogic

class AdminAddNewSectionLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_AdminAddNewSectionWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id = args[1]
        self.chapter_id = args[2]
        self.admin_landing_window = args[3]
        self.ui.lineEdit_3.setText("Sec01")
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_back.clicked.connect(self.handle_back)
        self.ui.pushButton.clicked.connect(self.handle_add_new_block)
        self.ui.pushButton_2.clicked.connect(self.handle_admin_landing)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_new_block(self):
        section_id = self.ui.lineEdit_3.text()
        section_title = self.ui.lineEdit_4.text()
        if section_id[:3] != "Sec":
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID should start with 'Sec' followed by 2 digits.")
            return
        response, error = self.user_dao.add_new_content_block(self.textbook_id, self.chapter_id, section_id, section_title)
        if response:
            QtWidgets.QMessageBox.information(self, "Message", "Section added successfully.")
            self.ui_admin_add_new_block = AdminAddNewContentBlockLogic([self, self.textbook_id, self.chapter_id, section_id, self.admin_landing_window])
            self.ui_admin_add_new_block.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", str(error))    
    
    def handle_admin_landing(self):
        self.admin_landing_window.show()
        self.close()