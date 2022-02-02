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

    def folders_setup(self):

        # Folders props
        self.folders.setModel(self.folders_sm)
        self.folders.setRootIndex(self.folders_sm.index(userDir))
        self.folders.hideColumn(1)
        self.folders.hideColumn(2)
        self.folders.hideColumn(3)

        # Signals
        self.folders.clicked.connect(self.show_files)
        self.button_play.clicked.connect(self.play_pause)

        self.audio_player.mediaChanged.connect(self.change_audio)

    def change_audio(self, media):
        print(media)

    # TODO: Implement auto button checked state switch when files are selected
    def play_pause(self):
        if (self.audio_player.isAvailable()):
            if (self.button_play.isChecked() == True):
                self.audio_player.play()
                self.button_play.setText("Pause")
            else:
                self.audio_player.pause()
                self.button_play.setText("Play")

    def show_files(self, index):
        indexItem = self.folders_sm.index(index.row(), 0, index.parent())
        # fileName = self.file_system_model.fileName(indexItem)
        filePath = self.folders_sm.filePath(indexItem)

        print(filePath)

        m = self.sender().model()
        path = self.sender().model().filePath(index)

        self.files.setRootIndex(self.files_sm.setRootPath(path))
        # if(os.path.isfile(filePath)):
        #    self.audio_player.setMedia(qt.QMediaContent(qt.QUrl.fromLocalFile(filePath)))
        #    self.button_play.click()

        # print(path)

    # TODO
    def files_setup(self):
        self.files.setModel(self.files_sm)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setStyle(qtw.QStyleFactory.create('Cleanlooks'))
    window = MainWindow()
    sys.exit(app.exec_())
