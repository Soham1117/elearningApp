# Form implementation generated from reading ui file 'faculty_hide_chapter_window.ui'
#
# Created by: PySide6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_FacultyHideChapterWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 480)
        self.pushButton_6 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_6.setGeometry(QtCore.QRect(160, 200, 151, 42))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"        background-color: #2b2b2b;  \n"
"        color: #fcba03;              \n"
"        border: 2px solid #3d3d3d;      \n"
"        border-radius: 8px;          \n"
"        padding: 8px 16px;            \n"
"        font-size: 16px;            \n"
"        font-weight: bold;\n"
"    \n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        background-color: #fcba03;\n"
"         color: #000000;\n"
"        border: 2px solid #5a5a5a;    \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #1a1a1a;      \n"
"        border: 2px solid #2b2b2b;      \n"
"    }")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 200, 151, 42))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"        background-color: #2b2b2b;  \n"
"        color: #fcba03;              \n"
"        border: 2px solid #3d3d3d;      \n"
"        border-radius: 8px;          \n"
"        padding: 8px 16px;            \n"
"        font-size: 16px;            \n"
"        font-weight: bold;\n"
"    \n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        background-color: #fcba03;\n"
"         color: #000000;\n"
"        border: 2px solid #5a5a5a;    \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #1a1a1a;      \n"
"        border: 2px solid #2b2b2b;      \n"
"    }")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(240, 110, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_6.setText(_translate("Form", "Save"))
        self.pushButton_7.setText(_translate("Form", "Cancel"))
        self.label_2.setText(_translate("Form", "Hide Chapter"))
