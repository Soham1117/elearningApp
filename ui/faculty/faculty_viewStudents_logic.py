import sys
from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.faculty.faculty_viewStudents_window import Ui_FacultyViewStudentsWindow

class FacultyViewStudentsLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_FacultyViewStudentsWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.course_id = args[1]

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)

        self.display_students()

        self.ui.pushButton_5.clicked.connect(self.handle_back)

    def display_students(self):
        course = self.user_dao.get_course_by_course_id(self.course_id)

        if course:
            self.ui.label_2.setText(f"Course ID: {self.course_id}")
            self.ui.label_4.setText(f"Course Name: {course[0]}")
        
        students = self.user_dao.get_students_by_course_id(self.course_id)

        if students:
            self.ui.tableWidget.setRowCount(len(students))
            self.ui.tableWidget.setColumnCount(3)
            columns = [0, 1, 2]
            # self.ui.tableWidget.setHorizontalHeaderLabels(['Student ID', 'Full Name', 'Email'])
            for i in range(len(students)):
                for j in range(len(columns)):
                    self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(students[i][columns[j]])))

            self.ui.tableWidget.resizeColumnsToContents()
        else:
            QtWidgets.QMessageBox.warning(self, "Students Retrieval Failed", "Failed to retrieve students for your course ID.")
    
    def handle_back(self):
        self.previous_window.show()
        self.close()
