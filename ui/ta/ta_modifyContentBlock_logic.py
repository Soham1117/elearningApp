from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.ta.ta_modifyContentBlock_window import Ui_TaModifyContentBlockWindow
from ui.ta.ta_addText_logic import TAAddTextLogic
from ui.ta.ta_addPicture_logic import TAAddPictureLogic
from ui.ta.ta_addActivity_logic import TAAddActivityLogic

class TAModifyContentBlockLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_TaModifyContentBlockWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id = args[1]
        self.chapter_id = args[2]
        self.section_id = args[3]
        # self.ta_landing_window = args[4]
        self.ui.lineEdit_4.setText("Block01")
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_back_2.clicked.connect(self.handle_back)
        self.ui.pushButton_5.clicked.connect(self.handle_add_new_text)
        self.ui.pushButton_6.clicked.connect(self.handle_add_new_picture)
        self.ui.pushButton_7.clicked.connect(self.handle_add_new_activity)
        # self.ui.pushButton_8.clicked.connect(self.handle_ta_landing)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_new_text(self):
        block_id = self.ui.lineEdit_4.text()
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_ta_addNewText = TAAddTextLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id])
        self.ui_ta_addNewText.show()
        self.close()
                
    def handle_add_new_picture(self):
        block_id = self.ui.lineEdit_4.text()        
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_ta_addNewPicture = TAAddPictureLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id])
        self.ui_ta_addNewPicture.show()
        self.close()
            
    def handle_add_new_activity(self):
        block_id = self.ui.lineEdit_4.text()        
        if block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block'.")
            return
        self.ui_ta_addNewActivity = TAAddActivityLogic([self, self.textbook_id, self.chapter_id, self.section_id, block_id])
        self.ui_ta_addNewActivity.show()
        self.close()  