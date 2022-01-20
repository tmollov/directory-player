from PyQt5 import QtWidgets as qtw
from PyQt5 import Qt as qt

from .StandardItem import StandardItem
from src.directories import Directories


class FoldersTreeView(qtw.QTreeView):
    def __init__(self, user_directory="/"):
        super().__init__()
        self.setHeaderHidden(True)

        tree_model = qt.QStandardItemModel()
        root_node = tree_model.invisibleRootItem()

        root_item = StandardItem(user_directory)

        ls = Directories().get_standard_items(user_directory)

        for item in ls:
            root_item.appendRow(item)

        root_node.appendRow(root_item)

        self.setModel(tree_model)
        self.expandAll()
        self.clicked.connect(self.get_value)

    def get_value(self, val):
        print(val.data())
