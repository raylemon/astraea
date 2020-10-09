# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'line.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Line(object):
    def setupUi(self, Line):
        if not Line.objectName():
            Line.setObjectName(u"Line")
        Line.resize(337, 90)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Line.sizePolicy().hasHeightForWidth())
        Line.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Line)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_2 = QLabel(Line)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(Line)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.le_solution = QLineEdit(Line)
        self.le_solution.setObjectName(u"le_solution")

        self.gridLayout.addWidget(self.le_solution, 1, 1, 1, 1)

        self.le_statement = QLineEdit(Line)
        self.le_statement.setObjectName(u"le_statement")

        self.gridLayout.addWidget(self.le_statement, 0, 1, 1, 1)

        self.label_3 = QLabel(Line)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.le_correction = QLineEdit(Line)
        self.le_correction.setObjectName(u"le_correction")
        self.le_correction.setEnabled(False)
        self.le_correction.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.le_correction, 2, 1, 1, 1)

        self.btn_correct = QPushButton(Line)
        self.btn_correct.setObjectName(u"btn_correct")

        self.gridLayout.addWidget(self.btn_correct, 0, 2, 3, 1)


        self.retranslateUi(Line)
        self.le_solution.textChanged.connect(Line.verify)
        self.btn_correct.clicked.connect(Line.show_correct)

        QMetaObject.connectSlotsByName(Line)
    # setupUi

    def retranslateUi(self, Line):
        Line.setWindowTitle(QCoreApplication.translate("Line", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Line", u"Solution", None))
        self.label.setText(QCoreApplication.translate("Line", u"\u00c9nonc\u00e9", None))
        self.le_solution.setPlaceholderText(QCoreApplication.translate("Line", u"Entrez votre solution ici", None))
        self.label_3.setText(QCoreApplication.translate("Line", u"Correction", None))
        self.le_correction.setPlaceholderText("")
        self.btn_correct.setText(QCoreApplication.translate("Line", u"Corriger", None))
    # retranslateUi

