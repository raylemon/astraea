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
        FLine.resize(396, 93)
        self.gridLayout = QGridLayout(FLine)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(FLine)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.le_solution = QLineEdit(FLine)
        self.le_solution.setObjectName(u"le_solution")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_solution.sizePolicy().hasHeightForWidth())
        self.le_solution.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_solution, 1, 3, 1, 1)

        self.le_statement = QLineEdit(FLine)
        self.le_statement.setObjectName(u"le_statement")

        self.gridLayout.addWidget(self.le_statement, 0, 1, 1, 3)

        self.le_corr_poly = QLineEdit(FLine)
        self.le_corr_poly.setObjectName(u"le_corr_poly")
        self.le_corr_poly.setEnabled(False)

        self.gridLayout.addWidget(self.le_corr_poly, 2, 1, 1, 2)

        self.label_2 = QLabel(FLine)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.le_polynom = QLineEdit(FLine)
        self.le_polynom.setObjectName(u"le_polynom")

        self.gridLayout.addWidget(self.le_polynom, 1, 1, 1, 1)

        self.label_4 = QLabel(FLine)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label = QLabel(FLine)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.le_correction = QLineEdit(FLine)
        self.le_correction.setObjectName(u"le_correction")
        self.le_correction.setEnabled(False)

        self.gridLayout.addWidget(self.le_correction, 2, 3, 1, 1)

        self.btn_correct = QPushButton(FLine)
        self.btn_correct.setObjectName(u"btn_correct")

        self.gridLayout.addWidget(self.btn_correct, 1, 4, 1, 1)


        self.retranslateUi(FLine)
        self.le_polynom.textChanged.connect(FLine.verify)
        self.le_solution.textChanged.connect(FLine.verify)
        self.btn_correct.pressed.connect(FLine.show_correct)

        QMetaObject.connectSlotsByName(FLine)
    # setupUi

    def retranslateUi(self, FLine):
        FLine.setWindowTitle(QCoreApplication.translate("FLine", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("FLine", u"Polyn\u00f4me", None))
        self.le_statement.setText("")
        self.label_2.setText(QCoreApplication.translate("FLine", u"Solution", None))
        self.label_4.setText(QCoreApplication.translate("FLine", u"Correction", None))
        self.label.setText(QCoreApplication.translate("FLine", u"\u00c9nonc\u00e9", None))
        self.btn_correct.setText(QCoreApplication.translate("FLine", u"Corriger", None))
    # retranslateUi

