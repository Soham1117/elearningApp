import sys
from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection

from ui.student.student_viewParticipationActivityPoint_window import Ui_StudentViewParticipationActivityPointWindow

class StudentViewParticipationActivityPointLogic(QtWidgets.QWidget):

    def __init__(self, args):
        super().__init__()
        self.ui = Ui_StudentViewParticipationActivityPointWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.student_id = args[1]

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)

        self.display_activity_points()

        self.ui.pushButton_5.clicked.connect(self.handle_back)

    def display_activity_points(self):
        student = self.user_dao.get_student_by_student_id(self.student_id)

        if student:
            self.ui.label_2.setText(f"Student ID: {self.student_id}")
            self.ui.label_4.setText(f"Student Name: {student[1]}")

        result = self.user_dao.view_student_participation_activity_points_by_course(self.student_id)

        if not result:
            QtWidgets.QMessageBox.warning(self, "Activity Points Retrieval Failed", "Failed to retrieve Activity Points for your ID. You might not have any activities registered yet.")
            return
        self.ui.tableWidget.setRowCount(len(result))
        self.ui.tableWidget.setColumnCount(3)
        columns = [1, 2, 3]
        # self.ui.tableWidget.setHorizontalHeaderLabels(['Course Name', 'Course Type','Course Start Date', 'Course End Date', 'Course Capacity'])
        for i in range(len(result)):
            for j in range(len(columns)):
                self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][columns[j]])))

        self.ui.tableWidget.resizeColumnsToContents()

    def handle_back(self):
        self.previous_window.show()
        self.close()

