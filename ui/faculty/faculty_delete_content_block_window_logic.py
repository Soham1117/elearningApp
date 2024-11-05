from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.faculty.faculty_delete_content_block_window import Ui_FacultyDeleteContentBlockWindow

class FacultyDeleteContentBlockLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyDeleteContentBlockWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id=args[1]
        self.chapter_id=args[2]
        self.section_id=args[3]
        self.content_block_id=args[4]
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_6.clicked.connect(self.handle_delete_content_block)
        
        self.ui.pushButton_7.clicked.connect(self.handle_back)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_delete_content_block(self):
        response,error=self.user_dao.delete_content_block(self.textbook_id,self.chapter_id,self.section_id,self.content_block_id)
        if response:
           QtWidgets.QMessageBox.information(self,'Information','Block Deleted successfully!!') 
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", str(error))    

        