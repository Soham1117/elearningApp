from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.admin.admin_addNewContentBlock_window import Ui_AdminAddNewContentBlockWindow
from ui.faculty.faculty_addActivity_logic import FacultyAddActivityLogic
from ui.faculty.faculty_add_block_image_window_logic import FacultyAddPictureLogic
from ui.faculty.faculty_add_block_text_window_logic import FacultyAddTextLogic
from ui.faculty.faculty_add_new_content_block_window import Ui_FacultyAddContentBlockWindow

class FacultyAddNewContentBlockLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyAddContentBlockWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id = args[1]
        self.chapter_id = args[2]
        self.section_id = args[3]
        self.ui.lineEdit_3.setText("Block01")
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_back.clicked.connect(self.handle_back)
        self.ui.pushButton.clicked.connect(self.handle_add_new_text)
        self.ui.pushButton_2.clicked.connect(self.handle_add_new_picture)
        self.ui.pushButton_3.clicked.connect(self.handle_add_new_activity)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_new_text(self):
        block_id = self.ui.lineEdit_3.text()
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_admin_add_new_text = FacultyAddTextLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id])
        self.ui_admin_add_new_text.show()
        self.close()
                
    def handle_add_new_picture(self):
        block_id = self.ui.lineEdit_3.text()        
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_admin_add_new_picture = FacultyAddPictureLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id])
        self.ui_admin_add_new_picture.show()
        self.close()
            
    def handle_add_new_activity(self):
        block_id = self.ui.lineEdit_3.text()        
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_admin_add_new_activity = FacultyAddActivityLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id])
        self.ui_admin_add_new_activity.show()
        self.close()  
    
    def handle_admin_landing(self):
        self.admin_landing_window.show()
        self.close()