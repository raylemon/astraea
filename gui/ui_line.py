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
        Line.resize(337, 64)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Line.sizePolicy().hasHeightForWidth())
        Line.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Line)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(Line)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.le_statement = QLineEdit(Line)
        self.le_statement.setObjectName(u"le_statement")

        self.gridLayout.addWidget(self.le_statement, 0, 1, 1, 1)

        self.label_2 = QLabel(Line)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.le_solution = QLineEdit(Line)
        self.le_solution.setObjectName(u"le_solution")

        self.gridLayout.addWidget(self.le_solution, 1, 1, 1, 1)


        self.retranslateUi(Line)
        self.le_solution.textChanged.connect(Line.verify)

        QMetaObject.connectSlotsByName(Line)
    # setupUi

    def retranslateUi(self, Line):
        Line.setWindowTitle(QCoreApplication.translate("Line", u"Form", None))
        self.label.setText(QCoreApplication.translate("Line", u"\u00c9nonc\u00e9", None))
        self.label_2.setText(QCoreApplication.translate("Line", u"Solution", None))
    # retranslateUi

