# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fline.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FLine(object):
    def setupUi(self, FLine):
        if not FLine.objectName():
            FLine.setObjectName(u"FLine")
        FLine.resize(351, 112)
        self.gridLayout = QGridLayout(FLine)
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_statement = QLineEdit(FLine)
        self.le_statement.setObjectName(u"le_statement")

        self.gridLayout.addWidget(self.le_statement, 0, 1, 1, 3)

        self.label_2 = QLabel(FLine)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.le_solution = QLineEdit(FLine)
        self.le_solution.setObjectName(u"le_solution")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_solution.sizePolicy().hasHeightForWidth())
        self.le_solution.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_solution, 1, 3, 1, 1)

        self.label = QLabel(FLine)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(FLine)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.le_polynom = QLineEdit(FLine)
        self.le_polynom.setObjectName(u"le_polynom")

        self.gridLayout.addWidget(self.le_polynom, 1, 1, 1, 1)


        self.retranslateUi(FLine)
        self.le_polynom.textChanged.connect(FLine.verify)
        self.le_solution.textChanged.connect(FLine.verify)

        QMetaObject.connectSlotsByName(FLine)
    # setupUi

    def retranslateUi(self, FLine):
        FLine.setWindowTitle(QCoreApplication.translate("FLine", u"Form", None))
        self.le_statement.setText("")
        self.label_2.setText(QCoreApplication.translate("FLine", u"Solution", None))
        self.label.setText(QCoreApplication.translate("FLine", u"\u00c9nonc\u00e9", None))
        self.label_3.setText(QCoreApplication.translate("FLine", u"Polyn\u00f4me", None))
    # retranslateUi

