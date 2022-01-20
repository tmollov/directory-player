from PyQt5 import QtWidgets as qtw
from PyQt5 import Qt as qt

from src.components.folder_files_section.StandardItem import StandardItem


class FavoriteFoldersTreeView(qtw.QTreeView):
    def __init__(self):
        super().__init__()
        self.setHeaderHidden(True)

        tree_model = qt.QStandardItemModel()
        root_node = tree_model.invisibleRootItem()

        root_item = StandardItem("/home/tmollov/Music")

        root_node.appendRow(root_item)

        self.setModel(tree_model)

