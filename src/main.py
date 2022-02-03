import os
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import Qt as qt

homeDir = "/home"
userDir = homeDir + "/tmollov/Downloads"

from src.dp_gui import Ui_MainWindow


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.show()
        self.setupUi(self)
        self.audio_player = qt.QMediaPlayer()

        self.repeat_audio = False

        # Model-View
        self.folders_sm = qtw.QFileSystemModel()
        self.folders_sm.setRootPath(userDir)
        self.folders_sm.setNameFilters([""])
        self.folders_sm.setNameFilterDisables(False)

        self.files_sm = qtw.QFileSystemModel()
        self.files_sm.setFilter(qt.QDir.Files)
        self.files_sm.setNameFilters(["*.mp3"])
        self.files_sm.setNameFilterDisables(False)

        # Setup views
        self.folders_setup()
        self.files_setup()

        self.button_repeat.clicked.connect(self.repeat_media)
        self.audio_player.mediaStatusChanged.connect(self.is_repeat_active)

    def is_repeat_active(self, status: qt.QMediaPlayer.MediaStatus):
        print(status)
        if status == 7 and self.repeat_audio is True:
            self.audio_player.play()

    def folders_setup(self):
        # Folders props
        self.folders.setModel(self.folders_sm)
        self.folders.setRootIndex(self.folders_sm.index(userDir))
        self.folders.hideColumn(1)
        self.folders.hideColumn(2)
        self.folders.hideColumn(3)

        # Signals
        self.folders.clicked.connect(self.show_files)
        self.files.clicked.connect(self.play_file)
        self.button_play.clicked.connect(self.play_pause)

    # TODO: Implement auto button checked state switch when files are selected
    def play_pause(self):
        if self.button_play.isChecked():
            self.audio_player.play()
            self.button_play.setText("Pause")
        else:
            self.audio_player.pause()
            self.button_play.setText("Play")

    def repeat_media(self):
        self.repeat_audio = not self.repeat_audio
        print(self.repeat_audio)

    def play_file(self, index):
        file_path = self.get_file_path(index, self.files_sm)
        self.audio_player.setMedia(qt.QMediaContent(qt.QUrl.fromLocalFile(file_path)))

        if self.button_play.isChecked() != True:
            self.button_play.click()

        self.audio_player.play()

    def show_files(self, index):
        path = self.sender().model().filePath(index)
        self.files.setRootIndex(self.files_sm.setRootPath(path))

    def get_file_path(self, index, model):
        indexItem = model.index(index.row(), 0, index.parent())
        filePath = model.filePath(indexItem)
        return filePath

    def files_setup(self):
        self.files.setModel(self.files_sm)
        select_mode = qt.QAbstractItemView.SelectionMode(qt.QAbstractItemView.SelectRows)
        self.files.setSelectionMode(select_mode)

        self.files.hideColumn(1)
        self.files.hideColumn(2)
        self.files.hideColumn(3)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setStyle(qtw.QStyleFactory.create('Cleanlooks'))
    window = MainWindow()
    sys.exit(app.exec_())
