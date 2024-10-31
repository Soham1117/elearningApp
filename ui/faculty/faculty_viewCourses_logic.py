import sys
from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection

from ui.faculty.faculty_viewCourses_window import Ui_FacultyViewCoursesWindow

class FacultyViewCoursesLogic(QtWidgets.QWidget):

    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyViewCoursesWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.faculty_id = args[1]

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)

        self.display_courses()

        self.ui.pushButton_5.clicked.connect(self.handle_back)

    def display_courses(self):
        result = self.user_dao.view_faculty_courses(self.faculty_id)
        if not result[1]:
            QtWidgets.QMessageBox.warning(self, "Courses Retrieval Failed", "Failed to retrieve courses for your ID.")
            return
        self.ui.tableWidget.setRowCount(len(result[0]))
        self.ui.tableWidget.setColumnCount(6)
        columns = [0, 1, 3, 6, 7, 9]
        # self.ui.tableWidget.setHorizontalHeaderLabels(['Course Name', 'Course Type','Course Start Date', 'Course End Date', 'Course Capacity'])
        for i in range(len(result[0])):
            for j in range(len(columns)):
                self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[0][i][columns[j]])))

        self.ui.tableWidget.resizeColumnsToContents()

    def handle_back(self):
        self.previous_window.show()
        self.close()

