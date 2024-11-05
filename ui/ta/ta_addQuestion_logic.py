from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.ta.ta_addQuestion_window import Ui_TaAddQuestionWindow

class TAAddQuestionLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_TaAddQuestionWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.textbook_id = args[1]
        self.chapter_id = args[2]
        self.section_id = args[3]
        self.block_id = args[4]
        self.unique_activity_id = args[5]
        self.ui.lineEdit_3.setText("Q1")
        self.ui.lineEdit_4.setText("Question Text")
        self.ui.lineEdit_6.setText("Option 1")
        self.ui.lineEdit_5.setText("Option 1 Explanation")
        self.ui.lineEdit_8.setText("Option 2")
        self.ui.lineEdit_9.setText("Option 2 Explanation")
        self.ui.lineEdit_14.setText("Option 3")
        self.ui.lineEdit_10.setText("Option 3 Explanation")
        self.ui.lineEdit_12.setText("Option 4")
        self.ui.lineEdit_13.setText("Option 4 Explanation")
        
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)

        self.ui.pushButton_back.clicked.connect(self.handle_back)
        self.ui.pushButton.clicked.connect(self.handle_add_question)
        
    def handle_back(self):    
        self.previous_window.show()
        self.close()

    def handle_add_question(self):
        qa = []
        question_id = self.ui.lineEdit_3.text()
        if question_id[:1] != "Q":
            QtWidgets.QMessageBox.warning(self, "Warning", "Question ID should start with 'Q'.")
            return
        question_text = self.ui.lineEdit_4.text()
        option1_text = self.ui.lineEdit_6.text()
        option1_explanation = self.ui.lineEdit_5.text()
        option2_text = self.ui.lineEdit_8.text()
        option2_explanation = self.ui.lineEdit_9.text()
        option3_text = self.ui.lineEdit_14.text()
        option3_explanation = self.ui.lineEdit_10.text()
        option4_text = self.ui.lineEdit_12.text()
        option4_explanation = self.ui.lineEdit_13.text()
        answer = self.ui.lineEdit_17.text()
        
        qa.append(question_id)
        qa.append(question_text)
        qa.append(option1_text)
        qa.append(option1_explanation)
        qa.append(option2_text)
        qa.append(option2_explanation)
        qa.append(option3_text)
        qa.append(option3_explanation)
        qa.append(option4_text)
        qa.append(option4_explanation)
        qa.append(answer)
        
        response, error = self.user_dao.add_question(self.textbook_id, self.chapter_id, self.section_id, self.block_id, self.unique_activity_id, qa, "ta")
        if response:
            QtWidgets.QMessageBox.information(self, "Message", "Question added successfully.")
            self.previous_window.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", str(error))    