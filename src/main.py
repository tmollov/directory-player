import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from src.components.folder_files_section.FavoriteFoldersTreeView import FavoriteFoldersTreeView
from src.components.folder_files_section.FilesInFolderTable import FilesInFolderTable
from src.components.folder_files_section.FoldersTreeView import FoldersTreeView

homeDir = "/home"
userDir = homeDir + "/tmollov"


class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Directory player")
        self.setMinimumSize(400, 300)

        # Main Layout - VBox
        layout_main = qtw.QVBoxLayout()
        self.setLayout(layout_main)

        # Folders / Files section
        layout_selection = qtw.QGridLayout()
        view_folders = FoldersTreeView(userDir)
        view_favorite_folders = FavoriteFoldersTreeView()

        data = {'Filename': ['Mascota', 'Miss Monique', 'NCS', 'NCS Trap'],
                'Size': ['59 123', '60 902', '4 504', '3 321'],
                'Format': ['mp3', 'mp3', 'mp3', 'mp3'],
                'Duration': ['1:11:13', '2:12:03', '4:54', '3:23']}

        view_files_in_folder = FilesInFolderTable(data, 4, 4)
        # Arrange views
        layout_selection.addWidget(view_folders, 0, 0)
        layout_selection.addWidget(view_favorite_folders, 1, 0)
        layout_selection.addWidget(view_files_in_folder, 0, 1)

        splitter1 = qtw.QSplitter(qtc.Qt.Vertical)
        splitter1.addWidget(view_folders)
        splitter1.addWidget(view_favorite_folders)

        splitter2 = qtw.QSplitter(qtc.Qt.Horizontal)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(view_files_in_folder)

        layout_main.addWidget(splitter2)

        # Adding Section to main layout
        #layout_main.addLayout(layout_selection)

        self.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setStyle(qtw.QStyleFactory.create('Cleanlooks'))
    window = MainWindow()
    sys.exit(app.exec_())
