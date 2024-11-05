from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.admin.admin_modifyContentBlock_window import Ui_AdminModifyContentBlockWindow
from ui.faculty.faculty_addActivity_logic import FacultyAddActivityLogic
from ui.faculty.faculty_add_block_image_window_logic import FacultyAddPictureLogic
from ui.faculty.faculty_add_block_text_window_logic import FacultyAddTextLogic
from ui.faculty.faculty_delete_activity_window_logic import FacultyDeleteActivityLogic
from ui.faculty.faculty_delete_content_block_window_logic import FacultyDeleteContentBlockLogic
from ui.faculty.faculty_hide_activity_window_logic import FacultyHideActivityLogic
from ui.faculty.faculty_hide_content_block_window_logic import FacultyHideContentBlockLogic
from ui.faculty.faculty_modify_content_block_window import Ui_FacultyModifyContentBlockWindow

class FacultyModifyContentBlockLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyModifyContentBlockWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id = args[1]
        self.chapter_id = args[2]
        self.section_id = args[3]
        self.ui.lineEdit_4.setText("Block01")
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_5.clicked.connect(self.handle_add_new_text)
        self.ui.pushButton_6.clicked.connect(self.handle_add_new_picture)
        self.ui.pushButton_7.clicked.connect(self.handle_add_new_activity)
        self.ui.pushButton_8.clicked.connect(self.handle_delete_activity)
        self.ui.pushButton_back_2.clicked.connect(self.handle_hide_activity)
        self.ui.pushButton_back_3.clicked.connect(self.handle_hide_content_block)
        self.ui.pushButton_back_4.clicked.connect(self.handle_delete_content_block)
        self.ui.pushButton_back_5.clicked.connect(self.handle_back)

    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_delete_activity(self):
        block_id = self.ui.lineEdit_4.text()
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_faculty_delete_activity = FacultyDeleteActivityLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id])
        self.ui_faculty_delete_activity.show()
        self.close()


    def handle_hide_activity(self):
        block_id = self.ui.lineEdit_4.text()
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_faculty_hide_activity = FacultyHideActivityLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id])
        self.ui_faculty_hide_activity.show()
        self.close()

    def handle_hide_content_block(self):
        block_id = self.ui.lineEdit_4.text()
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_faculty_hide_content_block = FacultyHideContentBlockLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id])
        self.ui_faculty_hide_content_block.show()
        self.close()

    def handle_delete_content_block(self):
        block_id = self.ui.lineEdit_4.text()
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_faculty_delete_content_block = FacultyDeleteContentBlockLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id])
        self.ui_faculty_delete_content_block.show()
        self.close()

    def handle_add_new_text(self):
        block_id = self.ui.lineEdit_4.text()
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_faculty_add_new_text = FacultyAddTextLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id])
        self.ui_faculty_add_new_text.show()
        self.close()
                
    def handle_add_new_picture(self):
        block_id = self.ui.lineEdit_4.text()        
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_faculty_add_new_picture = FacultyAddPictureLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id])
        self.ui_faculty_add_new_picture.show()
        self.close()
            
    def handle_add_new_activity(self):
        block_id = self.ui.lineEdit_4.text()        
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_faculty_add_new_activity = FacultyAddActivityLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id])
        self.ui_faculty_add_new_activity.show()
        self.close()  
    
