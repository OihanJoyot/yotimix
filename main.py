from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys, time, subprocess

from ui_mainwindow import Ui_MainWindow
from script import Cmd, Decode

class Yotimix(QMainWindow, QWidget, Ui_MainWindow, Cmd):
    def __init__(self, parent=None):
        self.device=0
        self.profile=0
        super(Yotimix, self).__init__(parent)
        self.setupUi(self)
        self.load_devices()
        self._init_buttons()
        self._active = False
        self.setMouseTracking(True)


    def _init_buttons(self):
        self.reloadButton.clicked.connect(self.load_devices)
        self.devList.currentItemChanged.connect(self.load_profiles)
        self.profList.currentItemChanged.connect(self.load_var)
        self.buttonBox.accepted.connect(self.load_cmd)
        self.buttonBox.rejected.connect(self.close)
        self.volumeSlider.sliderMoved.connect(self.volume)

    def load_devices(self):
        _i = 0
        self.devList.clear()
        for _name in self.list_profiles():
            _i += 1
            self.devList.addItem(str(_i)+" - "+str(_name[0]))

    def load_profiles(self):
        if str(self.devList.currentItem()) != "None":
            _i = 0
            self.profList.clear()
            self.device = int(self.devList.currentItem().text()[0])-1
            self.statusBar.showMessage(self.devList.currentItem().text()+" is clicked",2000)
            for _profile in self.list_profiles()[self.device][2]:
                _i += 1
                self.profList.addItem(str(_i)+" - "+str(_profile))
        else:
            pass

    def load_var(self):
        if str(self.profList.currentItem()) != "None":
            self.profile = int(self.profList.currentItem().text()[0])-1
            self.statusBar.showMessage(self.devList.currentItem().text()+" is clicked whith "+self.profList.currentItem().text(), 2000)
        else:
            pass

    def load_cmd(self):
        _cmd =  Cmd(self.device , self.profile)
        # _cmd.set_dev_as_def()
        _cmd.set_profiles()
        self.statusBar.showMessage(_cmd.set_profiles())


    def volume(self, follow = 0):
        # QTimer.singleShot(0, self.runLoop)
        if follow == 1:
            _current_v = str(subprocess.check_output(["bash", "cmdvolume.sh"]))
            _current_v = _current_v.replace("\\n", "")
            _current_v = _current_v.replace("\'", "")
            _current_v = int(_current_v.replace("b", ""))
            self.volumeSlider.setValue(_current_v)
        _v = self.volumeSlider.sliderPosition()
        self.statusBar.showMessage("amixer --quiet -D pulse sset Master "+ str(_v)+"%", 2000)
        subprocess.call(["amixer", "--quiet", "-D", "pulse", "sset", "Master", str(_v)+"%"])


    # def runLoop(self):
    #     from time import sleep
    #     for index in range(100):
    #         sleep(0.5)
    #         self.volume(follow = 1)
    #         qApp.processEvents()



if __name__ =="__main__":
    app = QApplication(sys.argv)
    w =  Yotimix()
    w.show()
    app.installEventFilter(w)
    sys.exit(app.exec_())
