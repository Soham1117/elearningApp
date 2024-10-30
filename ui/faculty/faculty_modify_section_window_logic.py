from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.admin.admin_modifySection_window import Ui_AdminSectionWindow
from ui.admin.admin_addNewContentBlock_logic import AdminAddNewContentBlockLogic
from ui.admin.admin_modifyContentBlock_logic import AdminModifyContentBlockLogic
from ui.faculty.faculty_add_new_content_block_window_logic import FacultyAddNewContentBlockLogic
from ui.faculty.faculty_delete_section_window_logic import FacultyDeleteSectionLogic
from ui.faculty.faculty_hide_section_window_logic import FacultyHideSectionLogic
from ui.faculty.faculty_modify_content_block_window_logic import FacultyModifyContentBlockLogic
from ui.faculty.faculty_modify_section_window import Ui_FacutyModifySectionWindow

class FacultyModifySectionLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacutyModifySectionWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id = args[1]
        self.chapter_id = args[2]
        self.ui.lineEdit_3.setText("Sec01")
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton.clicked.connect(self.handle_add_new_block)
        self.ui.pushButton_3.clicked.connect(self.handle_hide_section)
        self.ui.pushButton_2.clicked.connect(self.handle_modify_block)
        self.ui.pushButton_back.clicked.connect(self.handle_delete_section)
        self.ui.pushButton_back_2.clicked.connect(self.handle_back)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()
    
    def handle_delete_section(self):
        section_id = self.ui.lineEdit_3.text()
        if section_id[:3] != "Sec":
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID should start with 'Sec' followed by 2 digits.")
            return
        if self.user_dao.checkSection(self.textbook_id, self.chapter_id, section_id):
            self.ui_admin_add_new_block = FacultyDeleteSectionLogic([self, self.textbook_id, self.chapter_id, section_id])
            self.ui_admin_add_new_block.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID does not exist.")

    def handle_hide_section(self):
        section_id = self.ui.lineEdit_3.text()
        if section_id[:3] != "Sec":
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID should start with 'Sec' followed by 2 digits.")
            return
        if self.user_dao.checkSection(self.textbook_id, self.chapter_id, section_id):
            self.ui_admin_add_new_block = FacultyHideSectionLogic([self, self.textbook_id, self.chapter_id, section_id])
            self.ui_admin_add_new_block.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID does not exist.")

    def handle_add_new_block(self):
        section_id = self.ui.lineEdit_3.text()
        if section_id[:3] != "Sec":
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID should start with 'Sec' followed by 2 digits.")
            return
        if self.user_dao.checkSection(self.textbook_id, self.chapter_id, section_id):
            self.ui_admin_add_new_block = FacultyAddNewContentBlockLogic([self, self.textbook_id, self.chapter_id, section_id])
            self.ui_admin_add_new_block.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID does not exist.")
    
    def handle_modify_block(self):
        section_id = self.ui.lineEdit_3.text()
        if section_id[:3] != "Sec":
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID should start with 'Sec' followed by 2 digits.")
            return
        if self.user_dao.checkSection(self.textbook_id, self.chapter_id, section_id):
            self.ui_admin_modify_block = FacultyModifyContentBlockLogic([self, self.textbook_id, self.chapter_id, section_id])
            self.ui_admin_modify_block.show()
            self.close()
        else: 
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID does not exist.")
            
    def handle_admin_landing(self):
        self.admin_landing_window.show()
        self.close()