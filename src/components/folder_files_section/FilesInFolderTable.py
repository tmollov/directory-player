import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class FilesInFolderTable(qtw.QTableWidget):
    def __init__(self, data, *args):
        super().__init__(*args)
        self.data = data
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.verticalHeader().hide()
        self.horizontalHeader().setStretchLastSection(True)
        self.setSelectionBehavior(qtw.QTableView.SelectRows)
        self.cellClicked.connect(self.row_click)

    def row_click(self, row):
        print(row)

    def setData(self):
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = qtw.QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)
