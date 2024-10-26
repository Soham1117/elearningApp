from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.admin.admin_addActivity_window import Ui_AdminAddActivityWindow
from ui.admin.admin_addQuestion_logic import AdminAddQuestionLogic

class AdminAddActivityLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_AdminAddActivityWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id = args[1]
        self.chapter_id = args[2]
        self.section_id = args[3]
        self.block_id = args[4]
        self.admin_landing_window = args[5]
        self.ui.lineEdit_3.setText("ACT0")
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_back.clicked.connect(self.handle_back)
        self.ui.pushButton.clicked.connect(self.handle_add_new_activity)
        self.ui.pushButton_5.clicked.connect(self.handle_admin_landing)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_new_activity(self):
        unique_activity_id = self.ui.lineEdit_3.text()   
        if unique_activity_id[:3] != "ACT":
            QtWidgets.QMessageBox.warning(self, "Warning", "Activity ID should start with 'ACT'.")
            return
        response, error = self.user_dao.add_activityBlock(self.textbook_id, self.chapter_id, self.section_id, self.block_id, unique_activity_id)
        if response:
            response_2, error_2 = self.user_dao.add_activity(self.textbook_id, self.chapter_id, self.section_id, self.block_id, unique_activity_id)    
            if response_2:
                QtWidgets.QMessageBox.information(self, "Message", "Activity added successfully.")
                self.ui_admin_add_new_question = AdminAddQuestionLogic([self, self.textbook_id, self.chapter_id, self.section_id, self.block_id, unique_activity_id, self.admin_landing_window])
                self.ui_admin_add_new_question.show()
            else:
                QtWidgets.QMessageBox.warning(self, "Warning", str(error_2))
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", str(error))     
        self.close()

    def handle_admin_landing(self):
        self.admin_landing_window.show()
        self.close()