import sys
from enum import Enum

from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem

from gui.lines import QBean
from gui.ui_main import Ui_MainWindow
from lib.beans import *

class Types(Enum):
    CONV2 = 1,
    CONV10 = 2,
    CONVESO = 3,
    AR_CA2 = 4,
    AR_PM = 5,
    AR_TD = 6,
    CRC = 7,
    HAM_ENC = 8,
    HAM_DEC = 9

class Gui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.setupUi(self)
        self.beanType: Types = None

    def do_show_about(self):
        pass

    def do_arith_pm(self):
        pass

    def do_arith_td(self):
        pass

    def do_crc(self):
        pass

    def do_hamming(self):
        pass

    def do_arith_ca2(self):
        pass

    def do_convert_bin(self):
        self.beanType = Types.CONV2
        self.lbl_enonce.setText("Pensez à préfixer votre réponse par b, 0, 0x !\nIndiquez votre réponse sur 8 bits (b.... ....) si elle est en binaire.")
        for i in range(10):
            line = QBean(Convert(base_src=choose_bin_base(), base_dst=choose_bin_base()))
            item = QListWidgetItem(self.listWidget)
            item.setSizeHint(line.minimumSizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item,line)

    def do_convert_decbin(self):
        pass

    def do_convert_eso(self):
        pass

    def do_decfloat(self):
        pass

    def do_floatdec(self):
        pass

    def do_regen(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    gui.show()
    app.exec_()
