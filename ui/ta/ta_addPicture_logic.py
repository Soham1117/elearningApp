from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.ta.ta_addPicture_window import Ui_TaAddPictureWindow

class TAAddPictureLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_TaAddPictureWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id = args[1]
        self.chapter_id = args[2]
        self.section_id = args[3]
        self.block_id = args[4]
        self.ui.lineEdit_3.setText("Add Picture Here")
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_back.clicked.connect(self.handle_back)
        self.ui.pushButton.clicked.connect(self.handle_add_new_picture)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_new_picture(self):
        content = self.ui.lineEdit_3.text()        
        response, error = self.user_dao.add_new_picture(self.textbook_id, self.chapter_id, self.section_id, self.block_id, content)
        if response:
            QtWidgets.QMessageBox.information(self, "Message", "Picture added successfully.")
            self.previous_window.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", str(error))   