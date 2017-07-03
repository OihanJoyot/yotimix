from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
import sys, subprocess

from template import Ui_MainWindow
from script import Cmd, Decode

class Yotimix(QWidget, Cmd):
    def __init__(self):
        self.device=0
        self.profile=0
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_devices()
        self._init_buttons()
        self.ui.centralWidget.installEventFilter(self)

    def eventFilter(self, object, event = None):
        self.volume(follow = 1)

    def _init_buttons(self):
        self.ui.reloadButton.clicked.connect(self.load_devices)
        self.ui.devList.currentItemChanged.connect(self.load_profiles)
        self.ui.profList.currentItemChanged.connect(self.load_var)
        self.ui.buttonBox.accepted.connect(self.load_cmd)
        self.ui.buttonBox.rejected.connect(self.close)
        self.ui.volumeSlider.sliderMoved.connect(self.volume)

    def load_devices(self):
        _i = 0
        self.ui.devList.clear()
        for _name in self.list_profiles():
            _i += 1
            self.ui.devList.addItem(str(_i)+" - "+str(_name[0]))

    def load_profiles(self):
        _i = 0
        self.ui.profList.clear()
        self.device = int(self.ui.devList.currentItem().text()[0])-1
        for _profile in self.list_profiles()[self.device][2]:
            _i += 1
            self.ui.profList.addItem(str(_i)+" - "+str(_profile))

    def load_var(self):
        if str(self.ui.profList.currentItem()) != "None":
            self.profile = int(self.ui.profList.currentItem().text()[0])-1
        else:
            pass

    def load_cmd(self):
        _cmd =  Cmd(self.device , self.profile)
        # _cmd.set_dev_as_def()
        _cmd.set_profiles()


    def volume(self, follow = 0):
        if follow == 1:
            _current_v = str(subprocess.check_output(["bash", "cmdvolume.sh"]))
            _current_v = _current_v.replace("\\n", "")
            _current_v = _current_v.replace("\'", "")
            _current_v = int(_current_v.replace("b", ""))
            self.ui.volumeSlider.setValue(_current_v)
        _v = self.ui.volumeSlider.sliderPosition()
        subprocess.call(["amixer", "--quiet", "-D", "pulse", "sset", "Master", str(_v)+"%"])


if __name__ =="__main__":
    app = QApplication(sys.argv)
    w =  Yotimix()
    w.show()
    sys.exit(app.exec_())
