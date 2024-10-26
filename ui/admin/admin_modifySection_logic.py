from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.admin.admin_modifySection_window import Ui_AdminSectionWindow
from ui.admin.admin_addNewContentBlock_logic import AdminAddNewContentBlockLogic
from ui.admin.admin_modifyContentBlock_logic import AdminModifyContentBlockLogic

class AdminModifySectionLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_AdminSectionWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id = args[1]
        self.chapter_id = args[2]
        self.admin_landing_window = args[3]
        self.ui.lineEdit_3.setText(self.textbook_id)
        self.ui.lineEdit_4.setText(self.chapter_id)
        self.ui.lineEdit_5.setText("Sec01")
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton.clicked.connect(self.handle_add_new_block)
        self.ui.pushButton_2.clicked.connect(self.handle_admin_landing)
        self.ui.pushButton_3.clicked.connect(self.handle_modify_block)
        self.ui.pushButton_back.clicked.connect(self.handle_back)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_new_block(self):
        section_id = self.ui.lineEdit_5.text()
        if section_id[:3] != "Sec":
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID should start with 'Sec' followed by 2 digits.")
            return
        if self.user_dao.checkSection(self.textbook_id, self.chapter_id, section_id):
            self.ui_admin_add_new_block = AdminAddNewContentBlockLogic([self, self.textbook_id, self.chapter_id, section_id, self.admin_landing_window])
            self.ui_admin_add_new_block.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID does not exist.")
    
    def handle_modify_block(self):
        section_id = self.ui.lineEdit_5.text()
        if section_id[:3] != "Sec":
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID should start with 'Sec' followed by 2 digits.")
            return
        if self.user_dao.checkSection(self.textbook_id, self.chapter_id, section_id):
            self.ui_admin_modify_block = AdminModifyContentBlockLogic([self, self.textbook_id, self.chapter_id, section_id, self.admin_landing_window])
            self.ui_admin_modify_block.show()
            self.close()
        else: 
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID does not exist.")
            
    def handle_admin_landing(self):
        self.admin_landing_window.show()
        self.close()