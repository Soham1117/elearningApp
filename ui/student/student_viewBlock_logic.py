from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.student.student_viewBlock_window import Ui_StudentViewBlockWindow

class StudentViewBlockLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_StudentViewBlockWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.student_id = args[1]
        self.textbook_id = args[2]
        self.chapter_id = args[3]
        self.section_id = args[4]
        self.landing_page = args[5]
        
        self.block_type = None
        self.displaying_answer = False
        self.score = 0

        self.db_connection = get_db_connection()
        self.user_dao = UserDAO(self.db_connection)

        self.get_block()

        self.ui.pushButton.clicked.connect(self.submit) 
        self.ui.pushButton_back.clicked.connect(self.handle_back)

    def get_block(self):
        self.blocks = self.user_dao.get_blocks(self.textbook_id, self.chapter_id, self.section_id)
        if self.blocks:
            self.display_block()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "No blocks found.")
            return
    
    def display_block(self):
        block = self.blocks[0]
        if block[4] == 'text':
            self.block_type = 'text'
            self.ui.frame.show()
            self.ui.frame_2.hide()
            self.ui.label_2.setText(str(block[5]))
        elif block[4] == 'picture':
            self.block_type = 'picture'
            self.ui.frame.show()
            self.ui.frame_2.hide()
            self.ui.label_2.setText(str(block[5]))
        else:   
            self.block_type = 'activity'
            self.ui.frame.hide()
            self.ui.frame_2.show()
            self.view_questions(block)

    def view_questions(self, block):
        self.questions = self.user_dao.get_questions(self.textbook_id, self.chapter_id, self.section_id, block[5])
        if self.questions:
            self.question_number = 0
            self.view_question(self.questions[self.question_number])
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "No questions found.")

    def view_question(self, question):
        self.ui.frame.hide()
        self.ui.frame_2.show()
        
        self.ui.lineEdit.clear()
        self.ui.label_3.setText(str(question[6]))
        self.ui.label_4.setText(str(question[7]))
        self.ui.label_5.setText(str(question[9]))
        self.ui.label_6.setText(str(question[11]))
        self.ui.label_7.setText(str(question[13]))
    
    def view_answer(self, question, answer):
        self.ui.frame.show()
        self.ui.frame_2.hide()
        score = 0

        text = 'Score: 1' if int(answer) == question[-2] else 'Score: 0'
        if int(answer) == question[-2]:
            score = 1

        self.score += score
        # add score to database
        self.add_score_to_database(question, score)

        col = [8, 10, 12, 14] # column numbers for option 1, 2, 3, and 4 explanations
        text += '\n' + question[col[int(answer) - 1]]

        self.ui.label_2.setText(text)

    def add_score_to_database(self, question, score):
        # check if entry already exists
        if self.user_dao.check_question_score_entry(self.student_id, question):
            if self.user_dao.update_question_score_entry(self.student_id, question, score):
                return
            else:
                QtWidgets.QMessageBox.warning(self, "Warning", "Failed to update score.")
                return
        else:
            course_id = self.user_dao.get_course_id_from_textbook_id(self.textbook_id)
            if course_id:
                for id in course_id:
                    if self.user_dao.insert_question_score_entry(self.student_id, id[0], question, score):
                        pass
                    else:
                        QtWidgets.QMessageBox.warning(self, "Warning", "Failed to insert score.")
                        return
            else:
                QtWidgets.QMessageBox.warning(self, "Warning", "Failed to get course id to insert score.")
                return
    
    def submit(self):
        if self.block_type == 'activity':
            if self.question_number == len(self.questions) - 1 and self.displaying_answer:
                self.landing_page.show()
                self.close()
            else:
                if self.displaying_answer:
                    self.question_number += 1
                    self.displaying_answer = False
                    self.view_question(self.questions[self.question_number])
                else:
                    # get answer input in line edit
                    answer = self.ui.lineEdit.text()
                    if not answer:
                        QtWidgets.QMessageBox.warning(self, "Warning", "Please enter an answer.")
                        return
                    if answer not in ['1', '2', '3', '4']:
                        QtWidgets.QMessageBox.warning(self, "Warning", "Please enter a valid answer(1/2/3/4).")
                        return
                    
                    self.displaying_answer = True
                    self.view_answer(self.questions[self.question_number], answer)
        else:
            self.landing_page.show()
            self.close()

    def handle_back(self):
        self.previous_window.show()
        self.close()