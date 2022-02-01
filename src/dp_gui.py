# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dp.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.button_mute = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_mute.sizePolicy().hasHeightForWidth())
        self.button_mute.setSizePolicy(sizePolicy)
        self.button_mute.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_mute.setObjectName("button_mute")
        self.gridLayout.addWidget(self.button_mute, 2, 8, 1, 1)
        self.button_next = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_next.sizePolicy().hasHeightForWidth())
        self.button_next.setSizePolicy(sizePolicy)
        self.button_next.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_next.setObjectName("button_next")
        self.gridLayout.addWidget(self.button_next, 2, 7, 1, 1)
        self.player_section = QtWidgets.QHBoxLayout()
        self.player_section.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.player_section.setObjectName("player_section")
        self.artwork = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.artwork.sizePolicy().hasHeightForWidth())
        self.artwork.setSizePolicy(sizePolicy)
        self.artwork.setMaximumSize(QtCore.QSize(208, 117))
        self.artwork.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.artwork.setText("")
        self.artwork.setTextFormat(QtCore.Qt.PlainText)
        self.artwork.setPixmap(QtGui.QPixmap(":/artwork/sample.jpg"))
        self.artwork.setScaledContents(True)
        self.artwork.setAlignment(QtCore.Qt.AlignCenter)
        self.artwork.setWordWrap(False)
        self.artwork.setOpenExternalLinks(False)
        self.artwork.setObjectName("artwork")
        self.player_section.addWidget(self.artwork)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.player_filename = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_filename.sizePolicy().hasHeightForWidth())
        self.player_filename.setSizePolicy(sizePolicy)
        self.player_filename.setMaximumSize(QtCore.QSize(16777215, 50))
        self.player_filename.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.player_filename.setObjectName("player_filename")
        self.verticalLayout_2.addWidget(self.player_filename)
        self.player_metadata = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_metadata.sizePolicy().hasHeightForWidth())
        self.player_metadata.setSizePolicy(sizePolicy)
        self.player_metadata.setMaximumSize(QtCore.QSize(16777215, 50))
        self.player_metadata.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.player_metadata.setObjectName("player_metadata")
        self.verticalLayout_2.addWidget(self.player_metadata)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.player_time = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_time.sizePolicy().hasHeightForWidth())
        self.player_time.setSizePolicy(sizePolicy)
        self.player_time.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.player_time.setObjectName("player_time")
        self.horizontalLayout_2.addWidget(self.player_time)
        self.player_empty_space = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_empty_space.sizePolicy().hasHeightForWidth())
        self.player_empty_space.setSizePolicy(sizePolicy)
        self.player_empty_space.setObjectName("player_empty_space")
        self.horizontalLayout_2.addWidget(self.player_empty_space)
        self.button_repeat = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_repeat.sizePolicy().hasHeightForWidth())
        self.button_repeat.setSizePolicy(sizePolicy)
        self.button_repeat.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_repeat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_repeat.setAutoDefault(False)
        self.button_repeat.setDefault(False)
        self.button_repeat.setFlat(False)
        self.button_repeat.setObjectName("button_repeat")
        self.horizontalLayout_2.addWidget(self.button_repeat)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.player_section.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.player_section, 1, 0, 1, 9)
        self.files_section = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.files_section.sizePolicy().hasHeightForWidth())
        self.files_section.setSizePolicy(sizePolicy)
        self.files_section.setOrientation(QtCore.Qt.Horizontal)
        self.files_section.setObjectName("files_section")
        self.splitter_1 = QtWidgets.QSplitter(self.files_section)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_1.sizePolicy().hasHeightForWidth())
        self.splitter_1.setSizePolicy(sizePolicy)
        self.splitter_1.setBaseSize(QtCore.QSize(0, 0))
        self.splitter_1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.splitter_1.setOrientation(QtCore.Qt.Vertical)
        self.splitter_1.setObjectName("splitter_1")
        self.folders = QtWidgets.QTreeView(self.splitter_1)
        self.folders.setObjectName("folders")
        self.favorites = QtWidgets.QTreeView(self.splitter_1)
        self.favorites.setObjectName("favorites")
        self.files = QtWidgets.QTableWidget(self.files_section)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.files.sizePolicy().hasHeightForWidth())
        self.files.setSizePolicy(sizePolicy)
        self.files.setMinimumSize(QtCore.QSize(0, 0))
        self.files.setObjectName("files")
        self.files.setColumnCount(2)
        self.files.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.files.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.files.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.files_section, 0, 0, 1, 9)
        self.button_settings = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_settings.sizePolicy().hasHeightForWidth())
        self.button_settings.setSizePolicy(sizePolicy)
        self.button_settings.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_settings.setObjectName("button_settings")
        self.gridLayout.addWidget(self.button_settings, 2, 1, 1, 1)
        self.button_prev = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_prev.sizePolicy().hasHeightForWidth())
        self.button_prev.setSizePolicy(sizePolicy)
        self.button_prev.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_prev.setObjectName("button_prev")
        self.gridLayout.addWidget(self.button_prev, 2, 3, 1, 1)
        self.button_play = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_play.sizePolicy().hasHeightForWidth())
        self.button_play.setSizePolicy(sizePolicy)
        self.button_play.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_play.setCheckable(True)
        self.button_play.setChecked(False)
        self.button_play.setObjectName("button_play")
        self.gridLayout.addWidget(self.button_play, 2, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Directory Player"))
        self.button_mute.setText(_translate("MainWindow", "Mute"))
        self.button_next.setText(_translate("MainWindow", "next"))
        self.player_filename.setText(_translate("MainWindow", "Filename"))
        self.player_metadata.setText(_translate("MainWindow", "Metadata"))
        self.player_time.setText(_translate("MainWindow", "[ 212:131 / 1231:231]"))
        self.button_repeat.setText(_translate("MainWindow", "Repeat"))
        item = self.files.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Filename"))
        item = self.files.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Duration"))
        self.button_settings.setText(_translate("MainWindow", "Settings"))
        self.button_prev.setText(_translate("MainWindow", "prev"))
        self.button_play.setText(_translate("MainWindow", "Play"))
