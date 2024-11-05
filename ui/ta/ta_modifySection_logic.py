from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.ta.ta_modifySection_window import Ui_TaModifySectionWindow
from ui.ta.ta_addNewContentBlock_logic import TAAddNewContentBlockLogic
from ui.ta.ta_modifyContentBlock_logic import TAModifyContentBlockLogic
from ui.ta.ta_deleteContentBlock_logic import TADeleteContentBlockLogic
from ui.ta.ta_hideContentBlock_logic import TAHideContentBlockLogic

class TAModifySectionLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_TaModifySectionWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id = args[1]
        self.chapter_id = args[2]
        self.ui.lineEdit_3.setText(str(self.textbook_id))
        self.ui.lineEdit_6.setText(str(self.chapter_id))
        self.ui.lineEdit_5.setText("Sec01")
        self.ui.lineEdit_4.setText("Title")
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton.clicked.connect(self.handle_add_new_block)
        self.ui.pushButton_2.clicked.connect(self.handle_modify_block)
        self.ui.pushButton_3.clicked.connect(self.handle_delete_block)
        self.ui.pushButton_4.clicked.connect(self.handle_hide_block)
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
            self.ui_ta_addNewBlock = TAAddNewContentBlockLogic([self, self.textbook_id, self.chapter_id, section_id])
            self.ui_ta_addNewBlock.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID does not exist.")
    
    def handle_modify_block(self):
        section_id = self.ui.lineEdit_5.text()
        if section_id[:3] != "Sec":
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID should start with 'Sec' followed by 2 digits.")
            return
        if self.user_dao.checkSection(self.textbook_id, self.chapter_id, section_id):
            self.ui_ta_modifyBlock = TAModifyContentBlockLogic([self, self.textbook_id, self.chapter_id, section_id])
            self.ui_ta_modifyBlock.show()
            self.close()
        else: 
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID does not exist.")

    def handle_delete_block(self):
        section_id = self.ui.lineEdit_5.text()
        if section_id[:3] != "Sec":
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID should start with 'Sec' followed by 2 digits.")
            return
        textbook_id = self.ui.lineEdit_3.text()
        if not self.user_dao.checkTextbook(textbook_id):
            QtWidgets.QMessageBox.warning(self, "Warning", "Textbook ID does not exist.")
            return
        if self.user_dao.checkSection(textbook_id, self.chapter_id, section_id):
            self.ui_ta_deleteBlock = TADeleteContentBlockLogic([self, textbook_id, self.chapter_id, section_id])
            self.ui_ta_deleteBlock.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID does not exist.")
    
    def handle_hide_block(self):
        section_id = self.ui.lineEdit_5.text()
        if section_id[:3] != "Sec":
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID should start with 'Sec' followed by 2 digits.")
            return
        if self.user_dao.checkSection(self.textbook_id, self.chapter_id, section_id):
            self.ui_ta_hideBlock = TAHideContentBlockLogic([self, self.textbook_id, self.chapter_id, section_id])
            self.ui_ta_hideBlock.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Section ID does not exist.")