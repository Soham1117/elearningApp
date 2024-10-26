# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 480)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 40, 161, 31))
        font = QFont()
        font.setPointSize(21)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(170, 150, 311, 151))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #2b2b2b;\n"
"    color: #ffffff;\n"
"    border: 2px solid #3d3d3d;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #3d3d3d;\n"
"    border: 2px solid #5a5a5a;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #5a5a5a;\n"
"    background-color: #2b2b2b;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2b2b2b;\n"
"    border: 1px solid #3d3d3d;\n"
"    selection-background-color: #3d3d3d;\n"
"    color: #ffffff;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Home Menu", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Login Type:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Admin", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Faculty", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"TA", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Student", None))

        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Login", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Exit", None))
    # retranslateUi

