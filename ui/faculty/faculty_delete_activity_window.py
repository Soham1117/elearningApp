# Form implementation generated from reading ui file '.\faculty_delete_activity_window.ui'
#
# Created by: PySide6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_FacultyDeleteActivityWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 480)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(250, 70, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(parent=Form)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 160, 241, 97))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"        background-color: #2b2b2b;  /* Dark background */\n"
"        color: #fcba03;  /* Text color */\n"
"        border: 2px solid #3d3d3d;  /* Border color */\n"
"        border-radius: 8px;  /* Rounded corners */\n"
"        padding: 8px;  /* Padding inside the input field */\n"
"        font-size: 16px;  /* Font size */\n"
"        font-weight: bold;  /* Bold font */\n"
"    }\n"
"\n"
"    QLineEdit:hover {\n"
"        background-color: #3d3d3d;  /* Background when hovered */\n"
"        border: 2px solid #fcba03;  /* Border color when hovered */\n"
"    }\n"
"\n"
"    QLineEdit:focus {\n"
"        background-color: #1a1a1a;  /* Background when focused */\n"
"        border: 2px solid #fcba03;  /* Border color when focused */\n"
"        color: #ffffff;  /* Text color when focused */\n"
"    }")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.layoutWidget)
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
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.layoutWidget)
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
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Delete Activity"))
        self.label_2.setText(_translate("Form", "Activity ID"))
        self.pushButton_6.setText(_translate("Form", "Delete"))
        self.pushButton_7.setText(_translate("Form", "Back"))
