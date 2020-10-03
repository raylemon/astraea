# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"../astraea.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_CRC = QAction(MainWindow)
        self.action_CRC.setObjectName(u"action_CRC")
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        self.action_ConvertBin = QAction(MainWindow)
        self.action_ConvertBin.setObjectName(u"action_ConvertBin")
        self.action_ConvertDecBin = QAction(MainWindow)
        self.action_ConvertDecBin.setObjectName(u"action_ConvertDecBin")
        self.action_ConvertEso = QAction(MainWindow)
        self.action_ConvertEso.setObjectName(u"action_ConvertEso")
        self.action_Ca2 = QAction(MainWindow)
        self.action_Ca2.setObjectName(u"action_Ca2")
        self.action_ArithPM = QAction(MainWindow)
        self.action_ArithPM.setObjectName(u"action_ArithPM")
        self.action_ArithTD = QAction(MainWindow)
        self.action_ArithTD.setObjectName(u"action_ArithTD")
        self.action_DecFloat = QAction(MainWindow)
        self.action_DecFloat.setObjectName(u"action_DecFloat")
        self.action_FloatDec = QAction(MainWindow)
        self.action_FloatDec.setObjectName(u"action_FloatDec")
        self.action_Hamming = QAction(MainWindow)
        self.action_Hamming.setObjectName(u"action_Hamming")
        self.action_Quitter = QAction(MainWindow)
        self.action_Quitter.setObjectName(u"action_Quitter")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_enonce = QLabel(self.centralwidget)
        self.lbl_enonce.setObjectName(u"lbl_enonce")

        self.horizontalLayout.addWidget(self.lbl_enonce)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMovement(QListView.Free)

        self.verticalLayout.addWidget(self.listWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuExercices = QMenu(self.menubar)
        self.menuExercices.setObjectName(u"menuExercices")
        self.menuConversions = QMenu(self.menuExercices)
        self.menuConversions.setObjectName(u"menuConversions")
        self.menuArith = QMenu(self.menuExercices)
        self.menuArith.setObjectName(u"menuArith")
        self.menuFlottants = QMenu(self.menuExercices)
        self.menuFlottants.setObjectName(u"menuFlottants")
        self.menu_propos = QMenu(self.menubar)
        self.menu_propos.setObjectName(u"menu_propos")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuExercices.menuAction())
        self.menubar.addAction(self.menu_propos.menuAction())
        self.menuExercices.addAction(self.menuConversions.menuAction())
        self.menuExercices.addSeparator()
        self.menuExercices.addAction(self.menuArith.menuAction())
        self.menuExercices.addSeparator()
        self.menuExercices.addAction(self.menuFlottants.menuAction())
        self.menuExercices.addSeparator()
        self.menuExercices.addAction(self.action_CRC)
        self.menuExercices.addSeparator()
        self.menuExercices.addAction(self.action_Hamming)
        self.menuExercices.addSeparator()
        self.menuExercices.addAction(self.action_Quitter)
        self.menuConversions.addAction(self.action_ConvertBin)
        self.menuConversions.addAction(self.action_ConvertDecBin)
        self.menuConversions.addAction(self.action_ConvertEso)
        self.menuArith.addAction(self.action_Ca2)
        self.menuArith.addAction(self.action_ArithPM)
        self.menuArith.addAction(self.action_ArithTD)
        self.menuFlottants.addAction(self.action_DecFloat)
        self.menuFlottants.addAction(self.action_FloatDec)
        self.menu_propos.addAction(self.action_About)

        self.retranslateUi(MainWindow)
        self.action_About.triggered.connect(MainWindow.do_show_about)
        self.action_Quitter.triggered.connect(MainWindow.close)
        self.action_ArithPM.triggered.connect(MainWindow.do_arith_pm)
        self.action_ArithTD.triggered.connect(MainWindow.do_arith_td)
        self.action_CRC.triggered.connect(MainWindow.do_crc)
        self.action_Ca2.triggered.connect(MainWindow.do_arith_ca2)
        self.action_ConvertBin.triggered.connect(MainWindow.do_convert_bin)
        self.action_ConvertDecBin.triggered.connect(MainWindow.do_convert_decbin)
        self.action_ConvertEso.triggered.connect(MainWindow.do_convert_eso)
        self.action_DecFloat.triggered.connect(MainWindow.do_decfloat)
        self.action_FloatDec.triggered.connect(MainWindow.do_floatdec)
        self.action_Hamming.triggered.connect(MainWindow.do_hamming)
        self.pushButton.clicked.connect(MainWindow.do_regen)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Astraea", None))
        self.action_CRC.setText(QCoreApplication.translate("MainWindow", u"CRC", None))
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"\u00c0 propos d\u2019Astraea", None))
        self.action_ConvertBin.setText(QCoreApplication.translate("MainWindow", u"Conversions 2 <-> 8, 16", None))
        self.action_ConvertDecBin.setText(QCoreApplication.translate("MainWindow", u"Conversions 10 <-> 2,8,16", None))
        self.action_ConvertEso.setText(QCoreApplication.translate("MainWindow", u"Conversions toutes bases", None))
        self.action_Ca2.setText(QCoreApplication.translate("MainWindow", u"Compl\u00e9ments \u00e0 2 (C\u00e02)", None))
        self.action_ArithPM.setText(QCoreApplication.translate("MainWindow", u"Arithm\u00e9tique (+,-)", None))
        self.action_ArithTD.setText(QCoreApplication.translate("MainWindow", u"Arithm\u00e9tique (\u00d7,\u00f7)", None))
        self.action_DecFloat.setText(QCoreApplication.translate("MainWindow", u"D\u00e9cimal -> Flottant 16 bits", None))
        self.action_FloatDec.setText(QCoreApplication.translate("MainWindow", u"Flottant 16 bits -> D\u00e9cimal", None))
        self.action_Hamming.setText(QCoreApplication.translate("MainWindow", u"Hamming", None))
        self.action_Quitter.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.lbl_enonce.setText(QCoreApplication.translate("MainWindow", u"\u00c9nonc\u00e9 g\u00e9n\u00e9ral", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"R\u00e9g\u00e9n\u00e9rer", None))
        self.menuExercices.setTitle(QCoreApplication.translate("MainWindow", u"Exercices", None))
        self.menuConversions.setTitle(QCoreApplication.translate("MainWindow", u"Conversions", None))
        self.menuArith.setTitle(QCoreApplication.translate("MainWindow", u"Arithm\u00e9tique Binaire", None))
        self.menuFlottants.setTitle(QCoreApplication.translate("MainWindow", u"Flottants", None))
        self.menu_propos.setTitle(QCoreApplication.translate("MainWindow", u"\u00c0 propos", None))
    # retranslateUi

