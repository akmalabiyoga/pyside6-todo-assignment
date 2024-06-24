# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todolist.ui'
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
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 587)
        icon = QIcon()
        icon.addFile(u"images/todolisticon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tasks = QWidget()
        self.tasks.setObjectName(u"tasks")
        self.verticalLayoutWidget = QWidget(self.tasks)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(29, 90, 731, 411))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_title = QLineEdit(self.verticalLayoutWidget)
        self.tb_title.setObjectName(u"tb_title")

        self.horizontalLayout.addWidget(self.tb_title)

        self.tb_description = QLineEdit(self.verticalLayoutWidget)
        self.tb_description.setObjectName(u"tb_description")

        self.horizontalLayout.addWidget(self.tb_description)

        self.tb_course = QLineEdit(self.verticalLayoutWidget)
        self.tb_course.setObjectName(u"tb_course")

        self.horizontalLayout.addWidget(self.tb_course)

        self.tb_time = QLineEdit(self.verticalLayoutWidget)
        self.tb_time.setObjectName(u"tb_time")

        self.horizontalLayout.addWidget(self.tb_time)

        self.add_btn = QPushButton(self.verticalLayoutWidget)
        self.add_btn.setObjectName(u"add_btn")

        self.horizontalLayout.addWidget(self.add_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 1)
        self.label = QLabel(self.tasks)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 721, 61))
        font = QFont()
        font.setFamilies([u"Roboto Condensed"])
        font.setPointSize(33)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tabWidget.addTab(self.tasks, "")
        self.complete = QWidget()
        self.complete.setObjectName(u"complete")
        self.gridLayoutWidget = QWidget(self.complete)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(59, 110, 671, 361))
        self.gridLayout_comp = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_comp.setObjectName(u"gridLayout_comp")
        self.gridLayout_comp.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.complete)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 20, 671, 81))
        font1 = QFont()
        font1.setFamilies([u"Roboto Condensed"])
        font1.setPointSize(33)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tabWidget.addTab(self.complete, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 794, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"To Do List", None))
        self.tb_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex: Do homework", None))
        self.tb_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex: page 14 to16", None))
        self.tb_course.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex: visual programming", None))
        self.tb_time.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex: 11 july at 20 o'clock", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TO DO LIST", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tasks), QCoreApplication.translate("MainWindow", u"tasks", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Completed Tasks", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.complete), QCoreApplication.translate("MainWindow", u"complete", None))
    # retranslateUi

