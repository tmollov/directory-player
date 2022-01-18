from PyQt5 import Qt as qt
from PyQt5 import QtGui as qtg

class StandardItem(qt.QStandardItem):
    def __init__(self, txt="", font_size=12, set_bold=False, color=qtg.QColor(0, 0, 0)):
        super().__init__()

        fnt = qtg.QFont("Open Sans", font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)