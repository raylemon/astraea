from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QGridLayout


class QBean(QWidget):
    def __init__(self,bean, parent=None):
        super(QBean, self).__init__(parent)
        self.bean = bean
        self.statement = QLabel(self.bean.statement)
        self.le_solution = QLineEdit()
        self.le_solution.textChanged[str].connect(self.verify)
        self.le_solution.setToolTip(self.bean.solution)
        self.row = QGridLayout()
        self.row.addWidget(self.statement,row=0,column=1)
        self.row.addWidget(self.le_solution,row=0,column=1)
        self.setLayout(self.row)

    def verify(self,text):
        if text == self.bean.solution:
            self.le_solution.setStyleSheet("background-color:green")
        else:
            self.le_solution.setStyleSheet("background-color:red")
