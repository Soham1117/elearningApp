from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.student.student_viewSection_window import Ui_StudentViewSectionWindow
from ui.student.student_viewBlock_logic import StudentViewBlockLogic


class StudentViewSectionLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_StudentViewSectionWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.student_id = args[1]

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton.clicked.connect(self.view_block)
        self.ui.pushButton_back.clicked.connect(self.handle_back)

    def view_block(self):
        textbook_id = self.ui.lineEdit.text()
        chapter_id = self.ui.lineEdit_2.text()
        section_id = self.ui.lineEdit_3.text()

        # Check if fields are empty
        if not textbook_id or not chapter_id or not section_id:
            QtWidgets.QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        # go to view block logic
        self.ui_student_view_block = StudentViewBlockLogic([self, self.student_id, textbook_id, chapter_id, section_id, self.previous_window])
        self.ui_student_view_block.show()
        self.close()

    def handle_back(self):
        self.previous_window.show()
        self.close()

