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
        self.duration = 0

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

        self.button_repeat_track.clicked.connect(self.repeat_media)
        self.audio_player.mediaStatusChanged.connect(self.player_status_change)
        self.audio_player.positionChanged.connect(self.current_position)
        self.audio_player.positionChanged.connect(self.update_slider)
        self.time_slider.valueChanged.connect(self.change_position)
        self.files.clicked.connect(self.play_file)
        self.button_play.clicked.connect(self.play_pause)
        self.button_mute.clicked.connect(self.mute_audio)

    def mute_audio(self):
        if self.button_mute.isChecked():
            self.audio_player.setMuted(True)
        else:
            self.audio_player.setMuted(False)

    def update_slider(self, val):
        self.time_slider.setValue(val)

    def change_position(self, val):
        self.audio_player.setPosition(val)

    def current_position(self, position):
        pos = self.convert_duration_to_str(position)
        self.player_time.setText(f'[{pos} / {self.duration}]')

    def player_status_change(self, status: qt.QMediaPlayer.MediaStatus):
        if status == 6:
            self.duration = self.convert_duration_to_str(self.audio_player.duration())
            self.time_slider.setMaximum(self.audio_player.duration())
            self.player_time.setText(self.duration)
        if status == 7 and self.repeat_audio is True:
            self.audio_player.play()

    def convert_duration_to_str(self, millis):
        seconds = str(int((millis / 1000) % 60)).zfill(2)
        minutes = str(int((millis / (1000 * 60)) % 60)).zfill(2)
        hours = int((millis / (1000 * 60 * 60)) % 24)
        if hours < 1:
            return f'{minutes}:{seconds}'
        return f'{hours}:{minutes}:{seconds}'

    def convert_duration_to_seconds(self, millis):
        seconds = int(millis / 1000)
        return seconds

    def play_pause(self):
        if self.button_play.isChecked():
            self.audio_player.play()
            self.button_play.setText("Pause")
        else:
            self.audio_player.pause()
            self.button_play.setText("Play")

    def repeat_media(self):
        if not self.button_repeat_track.isChecked():
            self.repeat_audio = False
        else:
            self.repeat_audio = True

    def play_file(self, index):
        file_path = self.get_file_path(index, self.files_sm)
        self.audio_player.setMedia(qt.QMediaContent(qt.QUrl.fromLocalFile(file_path)))

        if not self.button_play.isChecked():
            self.button_play.click()

        self.player_filename.setText(self.get_file_name(index, self.files_sm))

        self.audio_player.play()

    def show_files(self, index):
        path = self.sender().model().filePath(index)

        self.files.setRootIndex(self.files_sm.setRootPath(path))
        self.files_sm.setFilter(qt.QDir.Files)
        self.files_sm.setNameFilters(["*.mp3"])
        self.files_sm.setNameFilterDisables(False)

    def get_file_path(self, index, model):
        index_item = model.index(index.row(), 0, index.parent())
        file_path = model.filePath(index_item)
        return file_path

    def get_file_name(self, index, model):
        index_item = model.index(index.row(), 0, index.parent())
        file_name = model.fileName(index_item)
        return file_name

    # SETUP
    def folders_setup(self):
        # Folders props
        self.folders.setModel(self.folders_sm)
        self.folders.setRootIndex(self.folders_sm.index(userDir))
        self.folders.hideColumn(1)
        self.folders.hideColumn(2)
        self.folders.hideColumn(3)

        # Signals
        self.folders.clicked.connect(self.show_files)

    def files_setup(self):
        self.files.setModel(self.files_sm)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setStyle(qtw.QStyleFactory.create('Cleanlooks'))
    window = MainWindow()
    sys.exit(app.exec_())
