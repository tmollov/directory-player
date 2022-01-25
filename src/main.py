import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from src.components.folder_files_section.FavoriteFoldersTreeView import FavoriteFoldersTreeView
from src.components.folder_files_section.FilesInFolderTable import FilesInFolderTable
from src.components.folder_files_section.FolderAndFilesView import FolderAndFilesView
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
        data = {'Filename': ['Mascota', 'Miss Moniqueeeeeeeeeeeeeeeeeeeeeeeee', 'NCS', 'NCS Trap'],
                'Size': ['59 123', '60 902', '4 504', '3 321'],
                'Format': ['mp3', 'mp3', 'mp3', 'mp3'],
                'Duration': ['1:11:13', '2:12:03', '4:54', '3:23']}

        folder_and_file_section = FolderAndFilesView(userDir, data)

        # Player section
        hbox = qtw.QHBoxLayout()

        image = qtg.QPixmap("../test_img.jpg")
        text_image = qtw.QLabel("image")
        text_image.setPixmap(image)

        hbox.addWidget(text_image)

        vert = qtw.QVBoxLayout()
        vert1 = qtw.QVBoxLayout()
        hbox1 = qtw.QHBoxLayout()
        vert.addLayout(vert1)
        vert.addLayout(hbox1)

        text_name = qtw.QLabel("#FILENAME")
        text_name.setAlignment(qtc.Qt.AlignLeft)

        text_meta = qtw.QLabel("#METADATAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        text_meta.setAlignment(qtc.Qt.AlignLeft)
        vert1.addWidget(text_name)
        vert1.addWidget(text_meta)

        text_time = qtw.QLabel("[ 11:11 / 22:22]")
        text_time.setAlignment(qtc.Qt.AlignLeft)
        repeat_btn = qtw.QPushButton("Repeat")
        widg = qtw.QWidget()
        hbox1.addWidget(text_time)
        hbox1.addWidget(widg)
        hbox1.addWidget(repeat_btn)

        hbox.addLayout(vert)

        # Adding Sections to main layout
        layout_main.addWidget(folder_and_file_section)
        layout_main.addLayout(hbox)

        self.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setStyle(qtw.QStyleFactory.create('Cleanlooks'))
    window = MainWindow()
    sys.exit(app.exec_())
