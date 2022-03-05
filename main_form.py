# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(193, 243)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_width = QLabel(self.centralwidget)
        self.label_width.setObjectName(u"label_width")

        self.horizontalLayout.addWidget(self.label_width)

        self.lineEdit_width = QLineEdit(self.centralwidget)
        self.lineEdit_width.setObjectName(u"lineEdit_width")

        self.horizontalLayout.addWidget(self.lineEdit_width)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_height = QLabel(self.centralwidget)
        self.label_height.setObjectName(u"label_height")

        self.horizontalLayout_2.addWidget(self.label_height)

        self.lineEdit_height = QLineEdit(self.centralwidget)
        self.lineEdit_height.setObjectName(u"lineEdit_height")

        self.horizontalLayout_2.addWidget(self.lineEdit_height)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_range = QLabel(self.centralwidget)
        self.label_range.setObjectName(u"label_range")

        self.horizontalLayout_3.addWidget(self.label_range)

        self.lineEdit_range = QLineEdit(self.centralwidget)
        self.lineEdit_range.setObjectName(u"lineEdit_range")

        self.horizontalLayout_3.addWidget(self.lineEdit_range)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.btn_ok = QPushButton(self.centralwidget)
        self.btn_ok.setObjectName(u"btn_ok")

        self.verticalLayout.addWidget(self.btn_ok)

        self.label_set_info = QLabel(self.centralwidget)
        self.label_set_info.setObjectName(u"label_set_info")

        self.verticalLayout.addWidget(self.label_set_info)

        self.label_info = QLabel(self.centralwidget)
        self.label_info.setObjectName(u"label_info")

        self.verticalLayout.addWidget(self.label_info)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 193, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"draw_helper_2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9bc \uc790\ub3d9 \uadf8\ub9ac\uae30 \ud504\ub85c\uadf8\ub7a8", None))
        self.label_width.setText(QCoreApplication.translate("MainWindow", u"\ub108\ube44", None))
        self.label_height.setText(QCoreApplication.translate("MainWindow", u"\ub192\uc774", None))
        self.label_range.setText(QCoreApplication.translate("MainWindow", u"\uac04\uaca9", None))
        self.btn_ok.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc778\uc694 ~", None))
        self.label_set_info.setText(QCoreApplication.translate("MainWindow", u"\uc138\ud305 \ub41c \uac12 : ", None))
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"F9 \ub204\ub974\uba74 \uc2dc\uc791", None))
    # retranslateUi

