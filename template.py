# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(450, 450)
        MainWindow.setMinimumSize(QtCore.QSize(450, 450))
        MainWindow.setMaximumSize(QtCore.QSize(450, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/share/icons/breeze/devices/64/audio-card.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        # MainWindow.setDocumentMode(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralWidget)
        self.buttonBox.setGeometry(QtCore.QRect(270, 400, 174, 41))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.volumeSlider = QtWidgets.QSlider(self.centralWidget)
        self.volumeSlider.setGeometry(QtCore.QRect(130, 410, 131, 21))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.devList = QtWidgets.QListWidget(self.centralWidget)
        self.devList.setGeometry(QtCore.QRect(10, 10, 201, 381))
        self.devList.setObjectName("devList")
        self.profList = QtWidgets.QListWidget(self.centralWidget)
        self.profList.setGeometry(QtCore.QRect(220, 10, 221, 381))
        self.profList.setObjectName("profList")
        self.reloadButton = QtWidgets.QPushButton(self.centralWidget)
        self.reloadButton.setGeometry(QtCore.QRect(10, 400, 51, 41))
        self.reloadButton.setText("")
        icon = QtGui.QIcon.fromTheme("/usr/share/icons/breeze/actions/16/chronometer-reset.svg")
        self.reloadButton.setIcon(icon)
        self.reloadButton.setIconSize(QtCore.QSize(32, 32))
        self.reloadButton.setObjectName("reloadButton")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(70, 410, 59, 18))
        self.label.setObjectName("label")
        self.buttonBox.raise_()
        self.volumeSlider.raise_()
        self.devList.raise_()
        self.profList.raise_()
        self.reloadButton.raise_()
        self.label.raise_()
        # MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yotimix - Select device card"))
        self.label.setText(_translate("MainWindow", "Volume:"))
