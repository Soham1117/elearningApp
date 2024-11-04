from ui.queries_window import Ui_QueriesWindow
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from PySide6 import QtWidgets

class QueriesLogic(QtWidgets.QWidget):
    def __init__(self, previous_window):
        super().__init__()
        self.ui = Ui_QueriesWindow()
        self.ui.setupUi(self)
        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)
        self.previous_window = previous_window
        self.ui.lineEdit.setPlaceholderText("Textbook ID")
        
        self.ui.pushButton.clicked.connect(self.handle_1)
        self.ui.pushButton_2.clicked.connect(self.handle_2)
        self.ui.pushButton_3.clicked.connect(self.handle_3)
        self.ui.pushButton_4.clicked.connect(self.handle_4)
        self.ui.pushButton_5.clicked.connect(self.handle_5)
        self.ui.pushButton_6.clicked.connect(self.handle_6)
        self.ui.pushButton_7.clicked.connect(self.handle_7)
        self.ui.pushButton_back.clicked.connect(self.handle_back)

    def handle_1(self):
        textbook_id = self.ui.lineEdit.text()
        if textbook_id == "":
            QtWidgets.QMessageBox.warning(self, "Error", "Textbook ID cannot be empty")
            return
        response, result = self.user_dao.excute_query_1(textbook_id)
        if response:
            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(5)
            columns = [0, 1, 2, 3, 4]
            self.ui.tableWidget.setHorizontalHeaderLabels(['Textbook ID', 'Textbook Title', 'Chapter ID', 'Chapter Title', 'Section Count'])
            for i in range(len(result)):
                for j in range(len(columns)):
                    self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][columns[j]])))
            self.ui.tableWidget.resizeColumnsToContents()
        else:
            QtWidgets.QMessageBox.warning(self, "Query 1 Failed", str(result))
            
    def handle_2(self):
        response, result = self.user_dao.excute_query_2()
        if response:
            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(4)
            columns = [0, 1, 2, 3]
            self.ui.tableWidget.setHorizontalHeaderLabels(['Course ID', 'Course Name', 'Name', 'Role'])
            for i in range(len(result)):
                for j in range(len(columns)):
                    self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][columns[j]])))
            self.ui.tableWidget.resizeColumnsToContents()
        else:
            QtWidgets.QMessageBox.warning(self, "Query 2 Failed", str(result))
        

    def handle_3(self):
        response, result = self.user_dao.excute_query_3()
        if response:
            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(4)
            columns = [0, 1, 2, 3]
            self.ui.tableWidget.setHorizontalHeaderLabels(['Course ID', 'First Name', 'Last Name', 'Total'])
            for i in range(len(result)):
                for j in range(len(columns)):
                    self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][columns[j]])))
            self.ui.tableWidget.resizeColumnsToContents()
        else:
            QtWidgets.QMessageBox.warning(self, "Query 3 Failed", str(result))

    def handle_4(self):
        response, result = self.user_dao.excute_query_4()
        if response:
            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(2)
            columns = [0, 1]
            self.ui.tableWidget.setHorizontalHeaderLabels(['Course ID', 'Total Waitlist'])
            for i in range(len(result)):
                for j in range(len(columns)):
                    self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][columns[j]])))
            self.ui.tableWidget.resizeColumnsToContents()
        else:
            QtWidgets.QMessageBox.warning(self, "Query 4 Failed", str(result))

    def handle_5(self):
        response, result = self.user_dao.excute_query_5()
        if response:
            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(2)
            columns = [0, 1]
            self.ui.tableWidget.setHorizontalHeaderLabels(['Course ID', 'Total Waitlist'])
            for i in range(len(result)):
                for j in range(len(columns)):
                    self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][columns[j]])))
            self.ui.tableWidget.resizeColumnsToContents()
        else:
            QtWidgets.QMessageBox.warning(self, "Query 5 Failed", str(result))
    
    def handle_6(self):
        response, result = self.user_dao.excute_query_6()
        if response:
            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(3)
            columns = [0, 1, 2]
            self.ui.tableWidget.setHorizontalHeaderLabels(['Option Number', 'Option Text', 'Explanation'])
            for i in range(len(result)):
                for j in range(len(columns)):
                    self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][columns[j]])))
            self.ui.tableWidget.resizeColumnsToContents()
        else:
            QtWidgets.QMessageBox.warning(self, "Query 6 Failed", str(result))        

    def handle_7(self):
        response, result = self.user_dao.excute_query_7()
        if response:
            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(4)
            columns = [0, 1, 2, 3]
            self.ui.tableWidget.setHorizontalHeaderLabels(['Textbook ID', 'Title', 'Active Faculty', 'Evaluation Faculty'])
            for i in range(len(result)):
                for j in range(len(columns)):
                    self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][columns[j]])))
            self.ui.tableWidget.resizeColumnsToContents()
        else:
            QtWidgets.QMessageBox.warning(self, "Query 7 Failed", str(result))      
        
    def handle_back(self):
        self.previous_window.show()
        self.close()
    
    