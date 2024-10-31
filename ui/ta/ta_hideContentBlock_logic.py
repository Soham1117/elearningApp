from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.ta.ta_hideContentBlock_window import Ui_TaHideContentBlockWindow

class TAHideContentBlockLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_TaHideContentBlockWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id=args[1]
        self.chapter_id=args[2]
        self.section_id=args[3]
        self.ui.lineEdit_3.setText("Block01")
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton.clicked.connect(self.handle_hide_content_block)
        
        self.ui.pushButton_back.clicked.connect(self.handle_back)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_hide_content_block(self):
        content_block_id = self.ui.lineEdit_3.text()
        if content_block_id[:5] != "Block":
            QtWidgets.QMessageBox.warning(self, "Warning", "Block ID should start with 'Block' followed by 2 digits.")
            return
        response,error=self.user_dao.hide_content_block(self.textbook_id,self.chapter_id,self.section_id, content_block_id)
        if response:
           QtWidgets.QMessageBox.information(self,'Information','Block hidden status updated successfully!!')
           self.previous_window.show()
           self.close() 
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", str(error))    