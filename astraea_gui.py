import sys
from enum import Enum

from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem

from gui.lines import QLine, QFLine, QCLine,QHLine
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
        title= "Arithmétique: Additions et Soustraction"
        enonce = "Pensez à préfixer votre réponse par b, 0, 0x !\nIndiquez votre réponse sur 8 bits (b.... ....) si elle est en binaire. "
        self.select(Types.AR_PM,title, enonce)

    def do_arith_td(self):
        title = "Arithmétique: Multiplications et Divisions"
        enonce = "Pensez à préfixer votre réponse par b, 0, 0x !\nIndiquez votre réponse sur 8 bits (b.... ....) si elle est en binaire. "
        self.select(Types.AR_TD, title,enonce)

    def do_crc(self):
        title = "Encodage et Décodage de CRC"
        enonce = "Encodez ou Décodez le CRC. Pensez à préfixer votre réponse par b, 0, 0x !\nIndiquez votre réponse sur 8 bits (b.... ....) si elle est en binaire. "
        self.select(Types.CRC, title,enonce)

    def do_hamming_decode(self):
        title = "Décodage de Hamming"
        enonce = "Décodez le message de Hamming"
        self.select(Types.HAM_DEC, title,enonce)

    def do_hamming_encode(self):
        title = "Encodage de Hamming"
        enonce = "Encodez le message de Hamming et notez le message encodé. Pensez à préfixer votre réponse par b, 0, 0x !\nIndiquez votre réponse sur 8 bits (b.... ....) si elle est en binaire. "
        self.select(Types.HAM_ENC, title,enonce)

    def do_arith_ca2(self):
        title = "Compléments à 2"
        enonce = "Calculez le complément à 2. Pensez à préfixer votre réponse par b, 0, 0x !\nIndiquez votre réponse sur 8 bits (b.... ....) si elle est en binaire. "
        self.select(Types.AR_CA2, title, enonce)

    def do_convert_bin(self):
        title = "Conversions 2<->8,16"
        enonce = "Pensez à préfixer votre réponse par b, 0, 0x !\nIndiquez votre réponse sur 8 " \
                 "bits (b.... ....) si elle est en binaire. "
        self.select(Types.CONV2,title, enonce)

    def do_convert_decbin(self):
        title = "Conversion 10 <-> 2,8,16"
        enonce = "Pensez à préfixer votre réponse par b, 0, 0x !\nIndiquez votre réponse " \
                 "sur 8 bits (b.... ....) si elle est en binaire. "
        self.select(Types.CONV10, title, enonce)

    def do_convert_eso(self):
        title= "Conversions toutes bases"
        enonce = "Pensez à préfixer votre réponse par b, 0, 0x pour les bases " \
                 "binaires\nPensez à suffixer votre réponse par () pour les autres bases\nIndiquez votre réponse sur " \
                 "8 bits (b.... ....) si elle est en binaire "
        self.select(Types.CONVESO, title,enonce)

    def do_decfloat(self):
        title = "Conversion Décimal en Float16"
        enonce = "Convertissez le nombre décimal en flottant 16 bits"
        self.select(Types.DEC_FLOAT, title,enonce)

    def do_floatdec(self):
        title = "Conversion Float16 en Décimal"
        enonce = "Convertissez le nombre flottant en décimal"
        self.select(Types.FLOAT_DEC,title, enonce)

    def select(self, typ: Types, title:str,enonce: str):
        self.listWidget.clear()
        self.lbl_title.setText(title)
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
                beans.append(Convert(base_src=bs, base_dst=bd))

            elif self.beanType == Types.CONVESO:
                beans.append(Convert())

            elif self.beanType == Types.AR_CA2:
                bs = choose_bin_base()
                bd = choose_bin_base()
                while bd == bs:
                    bd = choose_bin_base()
                beans.append(Ca2(base_src=bs, base_dst=bd))

            elif self.beanType == Types.AR_PM:
                bs1 = choose_bin_base()
                bs2 = choose_bin_base()
                bd = choose_bin_base()
                beans.append(Arith(base_src1=bs1, base_src2=bs2, base_dst=bd, op=npr.choice(('+', '-'))))

            elif self.beanType == Types.AR_TD:
                bs1 = choose_bin_base()
                bs2 = choose_bin_base()
                bd = choose_bin_base()
                beans.append(Arith(base_src1=bs1, base_src2=bs2, base_dst=bd, op=npr.choice(('×', '÷'))))

            elif self.beanType == Types.DEC_FLOAT:
                beans.append(DecimalToFloat16(base_dst=choose_bin_base()))

            elif self.beanType == Types.FLOAT_DEC:
                beans.append(Float16ToDecimal(base_src=choose_bin_base()))

            elif self.beanType == Types.CRC:
                bs = choose_bin_base()
                bd = choose_bin_base()
                while bs == bd:
                    bd = choose_bin_base()
                beans.append(Crc(base_src=bs, base_dst=bd))

            elif self.beanType == Types.HAM_ENC:
                bs = choose_bin_base()
                bd = choose_bin_base()
                while bs == bd:
                    bd = choose_bin_base()
                beans.append(HammingMessage(base_src=bs, base_dst=bd, encoded=True))

            elif self.beanType == Types.HAM_DEC:
                bs = choose_bin_base()
                bd = choose_bin_base()
                while bs == bd:
                    bd = choose_bin_base()
                beans.append(HammingMessage(base_src=bs, base_dst=bd, encoded=False))

            else:
                pass
        self.append_to_list(beans)

    def append_to_list(self, beans: list):
        for bean in beans:
            if self.beanType == Types.FLOAT_DEC:
                line = QFLine(bean)
            elif self.beanType == Types.HAM_DEC:
                line = QHLine(bean)
            elif self.beanType == Types.CRC:
                line = QCLine(bean)
            else:
                line = QLine(bean)
            item = QListWidgetItem(self.listWidget)
            item.setSizeHint(line.minimumSizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, line)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    gui.show()
    app.exec_()
