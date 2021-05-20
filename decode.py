# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'decodeZWpAze.ui'
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
        MainWindow.resize(676, 524)
        MainWindow.setWindowIcon(QIcon('mona-l.jpg')) 
        MainWindow.setMinimumSize(QSize(300, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.drop_shadow_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Roboto Condensed Light")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_title2 = QLabel(self.frame_title)
        self.label_title2.setObjectName(u"label_title2")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        self.label_title2.setFont(font1)
        self.label_title2.setStyleSheet(u"color: rgb(60, 231, 195);")

        self.verticalLayout_2.addWidget(self.label_title2)
        
        self.back = QPushButton(self.frame_title)
        self.back.setObjectName(u"back")
        self.back.setCursor(QCursor(Qt.OpenHandCursor))
        self.back.setGeometry(QRect(5, 20, 55, 16))
        self.back.setIcon(QIcon('back_to_24px.png'))

        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(85, 255, 127, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_maximize)

        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.gridLayout.addWidget(self.title_bar, 0, 0, 1, 1)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_bar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: none;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_5 = QVBoxLayout(self.page_home)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.page_home)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content_home)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_infos = QFrame(self.frame_content_home)
        self.frame_infos.setObjectName(u"frame_infos")
        self.frame_infos.setFrameShape(QFrame.StyledPanel)
        self.frame_infos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_infos)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_circle_1 = QFrame(self.frame_infos)
        self.frame_circle_1.setObjectName(u"frame_circle_1")
        self.frame_circle_1.setMinimumSize(QSize(250, 250))
        self.frame_circle_1.setMaximumSize(QSize(250, 250))
        self.frame_circle_1.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(60, 231, 195);\n"
"	border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_circle_1.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_circle_1)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 50, 10, 50)
        self.pushButton = QPushButton(self.frame_circle_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.pushButton)


        self.horizontalLayout_4.addWidget(self.frame_circle_1)


        self.verticalLayout_9.addWidget(self.frame_infos)

        self.frame_texts = QFrame(self.frame_content_home)
        self.frame_texts.setObjectName(u"frame_texts")
        self.frame_texts.setMinimumSize(QSize(600, 0))
        self.frame_texts.setMaximumSize(QSize(16777215, 100))
        self.frame_texts.setFrameShape(QFrame.StyledPanel)
        self.frame_texts.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_texts)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_13 = QLabel(self.frame_texts)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(600, 50))
        font2 = QFont()
        font2.setFamily(u"Roboto Light")
        font2.setPointSize(14)
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(33, 33, 75);\n"
"border-radius: 10px;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_13)


        self.verticalLayout_9.addWidget(self.frame_texts)


        self.verticalLayout_5.addWidget(self.frame_content_home)

        self.stackedWidget.addWidget(self.page_home)
        self.page_credits = QWidget()
        self.page_credits.setObjectName(u"page_credits")
        self.frame_content_credits = QFrame(self.page_credits)
        self.frame_content_credits.setObjectName(u"frame_content_credits")
        self.frame_content_credits.setGeometry(QRect(90, 70, 120, 80))
        self.frame_content_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_content_credits.setFrameShadow(QFrame.Raised)
        self.stackedWidget.addWidget(self.page_credits)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.content_bar, 1, 0, 1, 1)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: rgb(33, 33, 75);")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.bmw = QPushButton(self.frame_label_credits)
        self.bmw.setObjectName(u"bmw")
        self.bmw.setCursor(QCursor(Qt.OpenHandCursor))
        self.bmw.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"font:14px;")
         
        self.verticalLayout_3.addWidget(self.bmw)

        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        font3 = QFont()
        font3.setFamily(u"Roboto")
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: rgb(128, 102, 168);")

        self.verticalLayout_3.addWidget(self.label_credits)


        self.horizontalLayout_2.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_grip)


        self.gridLayout.addWidget(self.credits_bar, 2, 0, 1, 1)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"STEGANOREX-DECODER", None))
        self.label_title2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;STEGANOREX-Decode</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
#if QT_CONFIG(statustip)
        self.pushButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Choose the cover image", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton.setWhatsThis(QCoreApplication.translate("MainWindow", u"Choose the cover image", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Main Image", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\"If you control the code, you control the world.\"", None))
        self.bmw.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"By: AA", None))
    # retranslateUi

