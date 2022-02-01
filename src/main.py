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
        self.file_system_model = qtw.QFileSystemModel()
        self.file_system_model.setRootPath(userDir)
        self.file_system_model.setNameFilters(["*.mp3"])
        self.file_system_model.setNameFilterDisables(False)

        # Setup views
        self.folders_setup()

    def folders_setup(self):

        # Folders props
        self.folders.setModel(self.file_system_model)
        self.folders.setRootIndex(self.file_system_model.index(userDir))
        self.folders.hideColumn(2)
        self.folders.hideColumn(3)

        # Signals
        self.folders.clicked.connect(self.show_files)
        self.button_play.clicked.connect(self.play_pause)

    # TODO: Implement auto button checked state switch when files are selected
    def play_pause(self):
        if(self.audio_player.isAvailable()):
            if (self.button_play.isChecked() == True):
                self.audio_player.play()
                self.button_play.setText("Pause")
            else:
                self.audio_player.pause()
                self.button_play.setText("Play")



    def show_files(self, index):
        indexItem = self.file_system_model.index(index.row(), 0, index.parent())
        #fileName = self.file_system_model.fileName(indexItem)
        filePath = self.file_system_model.filePath(indexItem)

        #print(fileName)
        print(filePath)

        m = self.sender().model()
        path = self.sender().model().filePath(index)

        if(os.path.isfile(filePath)):
            self.audio_player.setMedia(qt.QMediaContent(qt.QUrl.fromLocalFile(filePath)))
            self.play_pause()

        print(path)

    # TODO
    def files_setup(self):
        pass


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setStyle(qtw.QStyleFactory.create('Cleanlooks'))
    window = MainWindow()
    sys.exit(app.exec_())
