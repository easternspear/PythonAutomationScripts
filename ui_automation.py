# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'automation.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(417, 394)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 400, 425))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.txt_instructions = QPlainTextEdit(self.centralwidget)
        self.txt_instructions.setObjectName(u"txt_instructions")
        self.txt_instructions.setGeometry(QRect(10, 40, 251, 301))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(270, 40, 136, 301))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_add_click = QPushButton(self.widget)
        self.btn_add_click.setObjectName(u"btn_add_click")

        self.gridLayout_2.addWidget(self.btn_add_click, 0, 0, 1, 1)

        self.btn_add_sleep = QPushButton(self.widget)
        self.btn_add_sleep.setObjectName(u"btn_add_sleep")

        self.gridLayout_2.addWidget(self.btn_add_sleep, 1, 0, 1, 1)

        self.btn_add_press = QPushButton(self.widget)
        self.btn_add_press.setObjectName(u"btn_add_press")

        self.gridLayout_2.addWidget(self.btn_add_press, 2, 0, 1, 1)

        self.btn_add_hotkey = QPushButton(self.widget)
        self.btn_add_hotkey.setObjectName(u"btn_add_hotkey")

        self.gridLayout_2.addWidget(self.btn_add_hotkey, 3, 0, 1, 1)

        self.btn_add_write = QPushButton(self.widget)
        self.btn_add_write.setObjectName(u"btn_add_write")

        self.gridLayout_2.addWidget(self.btn_add_write, 4, 0, 1, 1)

        self.btn_add_wait_image = QPushButton(self.widget)
        self.btn_add_wait_image.setObjectName(u"btn_add_wait_image")

        self.gridLayout_2.addWidget(self.btn_add_wait_image, 5, 0, 1, 1)

        self.btn_add_click_image = QPushButton(self.widget)
        self.btn_add_click_image.setObjectName(u"btn_add_click_image")

        self.gridLayout_2.addWidget(self.btn_add_click_image, 6, 0, 1, 1)

        self.btn_add_click_all_image = QPushButton(self.widget)
        self.btn_add_click_all_image.setObjectName(u"btn_add_click_all_image")

        self.gridLayout_2.addWidget(self.btn_add_click_all_image, 7, 0, 1, 1)

        self.btn_clear_instruction = QPushButton(self.widget)
        self.btn_clear_instruction.setObjectName(u"btn_clear_instruction")

        self.gridLayout_2.addWidget(self.btn_clear_instruction, 8, 0, 1, 1)

        self.btn_save = QPushButton(self.widget)
        self.btn_save.setObjectName(u"btn_save")

        self.gridLayout_2.addWidget(self.btn_save, 9, 0, 1, 1)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(11, 11, 391, 25))
        self.gridLayout_3 = QGridLayout(self.widget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_file = QLabel(self.widget1)
        self.lbl_file.setObjectName(u"lbl_file")

        self.gridLayout_3.addWidget(self.lbl_file, 0, 0, 1, 1)

        self.txt_file = QLineEdit(self.widget1)
        self.txt_file.setObjectName(u"txt_file")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txt_file.sizePolicy().hasHeightForWidth())
        self.txt_file.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.txt_file, 0, 1, 1, 1)

        self.btn_file = QPushButton(self.widget1)
        self.btn_file.setObjectName(u"btn_file")

        self.gridLayout_3.addWidget(self.btn_file, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 417, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Automation GUI", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_add_click.setText(QCoreApplication.translate("MainWindow", u"Mouse Click (alt+q)", None))
        self.btn_add_sleep.setText(QCoreApplication.translate("MainWindow", u"Sleep (alt+w)", None))
        self.btn_add_press.setText(QCoreApplication.translate("MainWindow", u"Press (alt+e)", None))
        self.btn_add_hotkey.setText(QCoreApplication.translate("MainWindow", u"Hotkey (alt+r)", None))
        self.btn_add_write.setText(QCoreApplication.translate("MainWindow", u"Write (alt+a)", None))
        self.btn_add_wait_image.setText(QCoreApplication.translate("MainWindow", u"Wait Image (alt+s)", None))
        self.btn_add_click_image.setText(QCoreApplication.translate("MainWindow", u"Click Image (alt+d)", None))
        self.btn_add_click_all_image.setText(QCoreApplication.translate("MainWindow", u"Click All Image (alt+f)", None))
        self.btn_clear_instruction.setText(QCoreApplication.translate("MainWindow", u"Clear Instruction (alt+x)", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save (ctrl+s)", None))
        self.lbl_file.setText(QCoreApplication.translate("MainWindow", u"File:", None))
        self.btn_file.setText(QCoreApplication.translate("MainWindow", u"Choose File (ctrl+o)", None))
    # retranslateUi

