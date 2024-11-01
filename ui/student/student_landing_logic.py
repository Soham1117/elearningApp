from PySide6 import QtWidgets
from dao.user_dao import UserDAO
from db.db_connection import get_db_connection
from ui.student.student_landing_window import Ui_StudentLandingWindow
# from ui.student.student_viewSection_logic import StudentViewSectionLogic
from ui.student.student_viewParticipationActivityPoint_logic import StudentViewParticipationActivityPointLogic
from PySide6.QtGui import QStandardItemModel, QStandardItem

class StudentLandingLogic(QtWidgets.QWidget):
    def __init__(self, args):
        super().__init__()
        self.ui = Ui_StudentLandingWindow()
        self.ui.setupUi(self)
        self.previous_window = args[0]
        self.student_id = args[1]

        self.ui.pushButton_2.clicked.connect(self.view_participation_activity_points)
        self.ui.pushButton_5.clicked.connect(self.handle_back)
                
        self.db_connection = get_db_connection()    
        self.user_dao = UserDAO(self.db_connection)
        
        self.courses = self.user_dao.gettreeviewdata(self.student_id)
        self.textbookDict = {}
        self.chapterDict = {}
        self.sectionDict = {}
        self.blockDict = {}
        
        for course in self.courses:
            course_id = course[0]
            textbookDetails = self.user_dao.getTextbookDetails(course_id)
            for textbook_id, textbook_title in textbookDetails:
                self.textbookDict[textbook_id] = textbook_title
                chapterDetails = self.user_dao.getChapterDetails(textbook_id)
                for chapter_id, chapter_title in chapterDetails:
                    self.chapterDict[(textbook_id, chapter_id)] = chapter_title
                    for section_id, section_title in self.user_dao.getSectionDetails(textbook_id, chapter_id):
                        self.sectionDict[(textbook_id, chapter_id, section_id)] = section_title
                        for block_id in self.user_dao.getBlockDetails(textbook_id, chapter_id, section_id):
                            self.blockDict[(textbook_id, chapter_id, section_id, block_id[0])] = block_id[0]
                        
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Textbook ID and Title'])
        self.populate_model()
        self.ui.treeView.setModel(self.model)

    def populate_model(self):
        for textbook_id, textbook_name in self.textbookDict.items():
            # Create textbook item
            textbook_item = QStandardItem(f"{textbook_id} {textbook_name}")
            self.model.appendRow(textbook_item)

            # Add chapters
            chapter_counter = 1  # Counter for chapters starting from 1
            for (tid, chapter_id), chapter_title in self.chapterDict.items():
                if tid == textbook_id:
                    chapter_item = QStandardItem(f"{chapter_counter} {chapter_title}")  # Start chapter numbering from 1
                    textbook_item.appendRow(chapter_item)
                    chapter_counter += 1

                    # Add sections
                    section_counter = 1  # Counter for sections starting from 1
                    for (tid, cid, section_id), section_title in self.sectionDict.items():
                        if (tid, cid) == (textbook_id, chapter_id):
                            section_item = QStandardItem(f"{section_counter} {section_title}")  # Start section numbering from 1
                            chapter_item.appendRow(section_item)
                            section_counter += 1

                            # Add blocks
                            block_counter = 1  # Counter for blocks starting from 1
                            for (tid, cid, sid, block_id), block_title in self.blockDict.items():
                                if (tid, cid, sid) == (textbook_id, chapter_id, section_id):
                                    block_item = QStandardItem(f"{block_counter} {block_title}")  # Start block numbering from 1
                                    section_item.appendRow(block_item)
                                    block_counter += 1
    def view_participation_activity_points(self):
        self.ui_go_to_evaluation_course = StudentViewParticipationActivityPointLogic([self, self.student_id])
        self.ui_go_to_evaluation_course.show()
        self.close()

    def handle_back(self):
        self.previous_window.show()
        self.close()
