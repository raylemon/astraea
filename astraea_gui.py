import sys
from enum import Enum

from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem

from gui.lines import QBean
from gui.ui_main import Ui_MainWindow
from lib.beans import *


class Types(Enum):
    NONE = 0,
    CONV2 = 1,
    CONV10 = 2,
    CONVESO = 3,
    AR_CA2 = 4,
    AR_PM = 5,
    AR_TD = 6,
    DEC_FLOAT = 7,
    FLOAT_DEC = 8,
    CRC = 9,
    HAM_ENC = 10,
    HAM_DEC = 11


class Gui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.setupUi(self)
        self.beanType = Types.NONE

    def do_show_about(self):
        pass

    def do_arith_pm(self):
        pass

    def do_arith_td(self):
        pass

    def do_crc(self):
        pass

    def do_hamming_decode(self):
        pass

    def do_hamming_encode(self):
        pass

    def do_arith_ca2(self):
        pass

    def do_convert_bin(self):
        enonce = "Conversions 2<->8,16\nPensez à préfixer votre réponse par b, 0, 0x !\nIndiquez votre réponse sur 8 " \
                 "bits (b.... ....) si elle est en binaire. "
        self.select(Types.CONV2,enonce)

    def do_convert_decbin(self):
        enonce = "Conversion 10 <-> 2,8,16\nPensez à préfixer votre réponse par b, 0, 0x !\nIndiquez votre réponse " \
                 "sur 8 bits (b.... ....) si elle est en binaire. "
        self.select(Types.CONV10,enonce)

    def do_convert_eso(self):
        enonce = "Conversions toutes bases\nPensez à préfixer votre réponse par b, 0, 0x pour les bases " \
                 "binaires\nPensez à suffixer votre réponse par () pour les autres bases\nIndiquez votre réponse sur " \
                 "8 bits (b.... ....) si elle est en binaire "
        self.select(Types.CONVESO,enonce)

    def do_decfloat(self):
        pass

    def do_floatdec(self):
        pass

    def select(self,typ:Types,enonce:str):
        self.listWidget.clear()
        self.beanType = typ
        self.lbl_enonce.setText(enonce)
        self.do_regen()

    def do_regen(self):
        beans = []
        for i in range(10):
            if self.beanType == Types.CONV2:
                bs = choose_bin_base()
                bd = choose_bin_base()
                while bd == bs:
                    bd = choose_bin_base()
                beans.append(Convert(base_src=bs, base_dst=bd))
            elif self.beanType == Types.CONV10:
                bs = get_base()
                bd = get_base()
                while bd == bs:
                    bd = get_base()
                beans.append(Convert(base_src=bs,base_dst=bd))
            elif self.beanType == Types.CONVESO:
                beans.append(Convert())
            elif self.beanType == Types.AR_CA2:
                pass
            elif self.beanType == Types.AR_PM:
                pass
            elif self.beanType == Types.AR_TD:
                pass
            elif self.beanType == Types.DEC_FLOAT:
                pass
            elif self.beanType == Types.FLOAT_DEC:
                pass
            elif self.beanType == Types.CRC:
                pass
            elif self.beanType == Types.HAM_ENC:
                pass
            elif self.beanType == Types.HAM_DEC:
                pass
            else:
                pass
        self.append_to_list(beans)

    def append_to_list(self, beans: list):
        for bean in beans:
            line = QBean(bean)
            item = QListWidgetItem(self.listWidget)
            item.setSizeHint(line.minimumSizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, line)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    gui.show()
    app.exec_()
