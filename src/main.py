import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import Qt as qt

from src.components.folder_files_section.FolderAndFilesView import FolderAndFilesView
from src.components.folder_files_section.StandardItem import StandardItem
from src.directories import Directories

homeDir = "/home"
userDir = homeDir + "/tmollov"

from src.dp_gui import Ui_MainWindow

class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.show()
        self.setupUi(self)
        self.folders_setup()

    def folders_setup(self):
        self.folders.setHeaderHidden(True)
        tree_model = qt.QStandardItemModel()
        root_node = tree_model.invisibleRootItem()

        root_item = StandardItem(userDir)

        ls = Directories().get_standard_items(userDir)

        for item in ls:
            root_item.appendRow(item)

        root_node.appendRow(root_item)

        self.folders.setModel(tree_model)
        self.folders.expandAll()

    def files_setup(self):
        pass

    def old_init(self):
        # Folders / Files section
        data = {'Filename': ['Mascota', 'Miss Moniqueeeeeeeeeeeeeeeeeeeeeeeee', 'NCS', 'NCS Trap'],
                'Size': ['59 123', '60 902', '4 504', '3 321'],
                'Format': ['mp3', 'mp3', 'mp3', 'mp3'],
                'Duration': ['1:11:13', '2:12:03', '4:54', '3:23']}

        folder_and_file_section = FolderAndFilesView(userDir, data)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setStyle(qtw.QStyleFactory.create('Cleanlooks'))
    window = MainWindow()
    sys.exit(app.exec_())
