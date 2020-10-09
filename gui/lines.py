from PySide2.QtWidgets import QWidget

from gui.ui_fline import Ui_FLine
from gui.ui_hline import Ui_HLine
from gui.ui_line import Ui_Line
from lib.beans import *


class QLine(QWidget, Ui_Line):
    def __init__(self, bean:Convert or Arith or Ca2 or DecimalToFloat16):
        super(QLine, self).__init__()
        self.bean = bean
        self.setupUi(self)
        self.le_statement.setText(self.bean.statement)

    def verify(self, text: str):
        self.le_solution.setStyleSheet(f"background-color:{'green' if text == self.bean.solution else 'red'} ")

    def show_correct(self):
        self.le_correction.setEnabled(True)
        self.le_correction.setText(self.bean.solution)


class QFLine(QWidget, Ui_FLine):
    def __init__(self, bean:Float16ToDecimal):
        super(QFLine, self).__init__()
        self.bean = bean
        self.setupUi(self)
        self.le_statement.setText(self.bean.statement)

    def verify(self, text: str):
        self.le_solution.setStyleSheet(f"background-color:{'green' if text == self.bean.solution else 'red'} ")
        self.le_polynom.setStyleSheet(f"background-color:{'green' if text == self.bean.polynom else 'red'} ")

    def show_correct(self):
        self.le_correction.setEnabled(True)
        self.le_corr_poly.setEnabled(True)
        self.le_correction.setText(self.bean.solution)
        self.le_corr_poly.setText(self.bean.polynom)


class QHLine(QWidget,Ui_HLine):
    def __init__(self,bean:HammingMessage):
        super(QHLine, self).__init__()
        self.bean = bean
        self.setupUi(self)
        self.le_statement.setText(self.bean.statement)

    def verify(self,text:str):
        self.le_solution.setStyleSheet(f"background-color:{'green' if text == self.bean.solution else 'red'} ")
        self.le_error.setStyleSheet(f"background-color:{'green' if text == self.bean.error_pos else 'red'} ")

    def show_correct(self):
        self.le_correction.setEnabled(True)
        self.le_error_pos.setEnabled(True)
        self.le_correction.setText(self.bean.solution)
        self.le_error_pos.setText(str(self.bean.error_pos))
