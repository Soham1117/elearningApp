from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.admin.admin_modifyChapter_window import Ui_AdminModifyChapterWindow
from ui.admin.admin_addNewSection_logic import AdminAddNewSectionLogic
from ui.admin.admin_modifySection_logic import AdminModifySectionLogic
from ui.faculty.faculty_delete_activity_window import Ui_FacultyDeleteActivityWindow
from ui.faculty.faculty_delete_chapter_window import Ui_FacultyDeleteChapterWindow
from ui.faculty.faculty_delete_content_block_window import Ui_FacultyDeleteContentBlockWindow
from ui.faculty.faculty_delete_section_window import Ui_FacultyDeleteSectionWindow
from ui.faculty.faculty_hide_section_window import Ui_FacultyHideSectionWindow
from ui.faculty.faculty_modify_chapter_window import Ui_FacultyModifyChapterWindow

class FacultyDeleteActivityLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyDeleteActivityWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id=args[1]
        self.chapter_id=args[2]
        self.section_id=args[3]
        self.block_id=args[4]
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_6.clicked.connect(self.handle_delete_activity)
        
        self.ui.pushButton_7.clicked.connect(self.handle_back)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_delete_activity(self):
        activity_id=self.ui.lineEdit.text()
        if activity_id:
            response,error=self.user_dao.delete_activity(self.textbook_id,self.chapter_id,self.section_id,self.block_id,activity_id)
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", 'Invalid Activity Id')
            return
        
        if response:
           QtWidgets.QMessageBox.information(self,'Information','Section Deleted successfully!!') 
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", str(error))    

        