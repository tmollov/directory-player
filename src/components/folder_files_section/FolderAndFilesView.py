from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from src.components.folder_files_section.FavoriteFoldersTreeView import FavoriteFoldersTreeView
from src.components.folder_files_section.FilesInFolderTable import FilesInFolderTable
from src.components.folder_files_section.FoldersTreeView import FoldersTreeView


class FolderAndFilesView(qtw.QSplitter):
    def __init__(self, user_dir, data):
        super().__init__()
        self.setOrientation(qtc.Qt.Horizontal)

        view_folders = FoldersTreeView(user_dir)
        view_favorite_folders = FavoriteFoldersTreeView()
        view_files_in_folder = FilesInFolderTable(data, 4, 4)
        # Arrange views

        splitter1 = qtw.QSplitter(qtc.Qt.Vertical)
        splitter1.addWidget(view_folders)
        splitter1.addWidget(view_favorite_folders)

        self.addWidget(splitter1)
        self.addWidget(view_files_in_folder)
