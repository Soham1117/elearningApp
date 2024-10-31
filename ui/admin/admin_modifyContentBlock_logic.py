from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.admin.admin_modifyContentBlock_window import Ui_AdminModifyContentBlockWindow
from ui.admin.admin_addText_logic import AdminAddTextLogic
from ui.admin.admin_addPicture_logic import AdminAddPictureLogic
from ui.admin.admin_addActivity_logic import AdminAddActivityLogic

class AdminModifyContentBlockLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_AdminModifyContentBlockWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id = args[1]
        self.chapter_id = args[2]
        self.section_id = args[3]
        self.admin_landing_window = args[4]
        self.ui.lineEdit_4.setText("Block01")
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_back_2.clicked.connect(self.handle_back)
        self.ui.pushButton_5.clicked.connect(self.handle_add_new_text)
        self.ui.pushButton_6.clicked.connect(self.handle_add_new_picture)
        self.ui.pushButton_7.clicked.connect(self.handle_add_new_activity)
        self.ui.pushButton_8.clicked.connect(self.handle_admin_landing)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_new_text(self):
        block_id = self.ui.lineEdit_4.text()
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_admin_add_new_text = AdminAddTextLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id, self.admin_landing_window])
        self.ui_admin_add_new_text.show()
        self.close()
                
    def handle_add_new_picture(self):
        block_id = self.ui.lineEdit_4.text()        
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_admin_add_new_picture = AdminAddPictureLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id, self.admin_landing_window])
        self.ui_admin_add_new_picture.show()
        self.close()
            
    def handle_add_new_activity(self):
        block_id = self.ui.lineEdit_4.text()        
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_admin_add_new_activity = AdminAddActivityLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id, self.admin_landing_window])
        self.ui_admin_add_new_activity.show()
        self.close()  
    
    def handle_admin_landing(self):
        self.admin_landing_window.show()
        self.close()