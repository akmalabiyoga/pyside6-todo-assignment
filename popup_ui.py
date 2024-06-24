# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(462, 475)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"images/detail_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(7)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.time_label = QLabel(self.centralwidget)
        self.time_label.setObjectName(u"time_label")
        font1 = QFont()
        font1.setPointSize(12)
        self.time_label.setFont(font1)

        self.gridLayout_2.addWidget(self.time_label, 4, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 7, 0, 1, 1)

        self.back_btn = QPushButton(self.centralwidget)
        self.back_btn.setObjectName(u"back_btn")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.back_btn.setFont(font2)
        self.back_btn.setStyleSheet(u"background-color: rgb(121, 85, 72);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.back_btn, 8, 1, 1, 1)

        self.id_label = QLabel(self.centralwidget)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setFont(font1)

        self.gridLayout_2.addWidget(self.id_label, 0, 1, 1, 1)

        self.description_label = QLabel(self.centralwidget)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setFont(font1)

        self.gridLayout_2.addWidget(self.description_label, 2, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.gridLayout_2.addLayout(self.horizontalLayout, 8, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setFont(font1)

        self.gridLayout_2.addWidget(self.title_label, 1, 1, 1, 1)

        self.done_label = QLabel(self.centralwidget)
        self.done_label.setObjectName(u"done_label")
        self.done_label.setFont(font1)

        self.gridLayout_2.addWidget(self.done_label, 7, 1, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setMouseTracking(False)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.course_label = QLabel(self.centralwidget)
        self.course_label.setObjectName(u"course_label")
        self.course_label.setFont(font1)

        self.gridLayout_2.addWidget(self.course_label, 3, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 462, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Detail", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ID : ", None))
        self.time_label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Done : ", None))
        self.back_btn.setText(QCoreApplication.translate("MainWindow", u"Back to Tasks >>", None))
        self.id_label.setText("")
        self.description_label.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Title : ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Time : ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Description : ", None))
        self.title_label.setText("")
        self.done_label.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Course : ", None))
        self.course_label.setText("")
    # retranslateUi

