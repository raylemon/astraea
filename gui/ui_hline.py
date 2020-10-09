# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hline.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_HLine(object):
    def setupUi(self, HLine):
        if not HLine.objectName():
            HLine.setObjectName(u"HLine")
        HLine.resize(400, 67)
        self.gridLayout = QGridLayout(HLine)
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_error = QLineEdit(HLine)
        self.le_error.setObjectName(u"le_error")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_error.sizePolicy().hasHeightForWidth())
        self.le_error.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.le_error, 1, 3, 1, 1)

        self.label_3 = QLabel(HLine)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label = QLabel(HLine)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.le_statement = QLineEdit(HLine)
        self.le_statement.setObjectName(u"le_statement")

        self.gridLayout.addWidget(self.le_statement, 0, 1, 1, 3)

        self.le_solution = QLineEdit(HLine)
        self.le_solution.setObjectName(u"le_solution")

        self.gridLayout.addWidget(self.le_solution, 1, 1, 1, 1)

        self.label_2 = QLabel(HLine)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)


        self.retranslateUi(HLine)
        self.le_solution.textEdited.connect(HLine.verify)
        self.le_error.textEdited.connect(HLine.verify)

        QMetaObject.connectSlotsByName(HLine)
    # setupUi

    def retranslateUi(self, HLine):
        HLine.setWindowTitle(QCoreApplication.translate("HLine", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("HLine", u"Solution", None))
        self.label.setText(QCoreApplication.translate("HLine", u"\u00c9nonc\u00e9", None))
        self.le_statement.setText("")
        self.label_2.setText(QCoreApplication.translate("HLine", u"Erreur", None))
    # retranslateUi

