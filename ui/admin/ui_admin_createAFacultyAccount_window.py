# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_createAFacultyAccount_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 480)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(199, 60, 331, 41))
        font = QFont()
        font.setPointSize(21)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget_2 = QWidget(Form)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(146, 130, 431, 252))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_4.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_5.addWidget(self.lineEdit_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_6.addWidget(self.lineEdit_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit_6.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_7.addWidget(self.lineEdit_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_back = QPushButton(self.layoutWidget_2)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setStyleSheet(u"QPushButton {\n"
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
"		 color: #000000;\n"
"        border: 2px solid #5a5a5a;    \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #1a1a1a;      \n"
"        border: 2px solid #2b2b2b;      \n"
"    }")

        self.horizontalLayout_8.addWidget(self.pushButton_back)

        self.pushButton = QPushButton(self.layoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
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
"		 color: #000000;\n"
"        border: 2px solid #5a5a5a;    \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #1a1a1a;      \n"
"        border: 2px solid #2b2b2b;      \n"
"    }")

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Create a Faculty Account", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"First Name:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Last Name:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.pushButton_back.setText(QCoreApplication.translate("Form", u"Back", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Add User", None))
    # retranslateUi

