import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import Qt as qt

from components.StandardItem import StandardItem
from directories import Directories

homeDir = "/home"
userDir = homeDir + "/tmollov"

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Directory player")
        self.resize(640, 480)

        treev = qtw.QTreeView()
        treev.setHeaderHidden(True)

        treem = qt.QStandardItemModel()
        rootNode = treem.invisibleRootItem()

        rootItem = StandardItem("tmollov")

        ls = Directories().get_standart_items(userDir)
        
        for item in ls:
             rootItem.appendRow(item)

        rootNode.appendRow(rootItem)

        treev.setModel(treem)
        treev.expandAll()
        treev.clicked.connect(self.getValue)

        self.setCentralWidget(treev)

        self.show()

    def getValue(self, val):
        print(val.data())

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
