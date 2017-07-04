[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Breezeicons-devices-64-audio-card.svg/64px-Breezeicons-devices-64-audio-card.svg.png)](https://nodesource.com/products/nsolid)

# Yotimix
(just to learn pyqt)
Yotimix is a python software used to select the default audio device and its profile. It should be compatible with bluetooth devices even if other mixers don't work. Actually, in addition to set the audio card as default device, the program desactivate the 
others.

[![N|Solid](https://image.noelshack.com/fichiers/2017/27/2/1499167273-yotimix.png)](https://nodesource.com/products/nsolid)

# Requirements and credits
| Requirement | URL |
| ------ | ------ |
| Python3 | https://www.python.org/ |
| amixer| https://www.alsa-project.org/main/index.php/Main_Page (may be installed)|
| PulseAudio (pacmd) | https://www.freedesktop.org/wiki/Software/PulseAudio/ (may be installed)|
| pyQt5 | https://www.riverbankcomputing.com/software/pyqt/ |
| python_subprocess | https://docs.python.org/3.6/library/subprocess.html#module-subprocess |

With shell:
```sh
$ apt-get install python3
$ apt-get install alsa-base
$ apt-get install pulseaudio
$ apt-get install pyqt5-dev
$ apt-get install python3-ptyprocess
```

| Credits | URL |
| ------ | ------ |
| QT creator | https://www.qt.io/download-open-source/?hsCtaTracking=f977210e-de67-475f-a32b-65cec207fd03%7Cd62710cd-e1db-46aa-8d4d-2f1c1ffdacea|
| pyuic5 | http://pyqt.sourceforge.net/Docs/PyQt4/designer.html|
| Breeze (plasma) | https://github.com/KDE/breeze (in the ressources folder)|

# Files
| Name | Target |
| ------ | ------ |
| main.py | Main program: To run the sofware execute ```$ python3 main.py``` |
| script.py | Library of the essential fonctions of the program|
| ui_mainwindow | Libray to build the QWidgets in the window (generate by QtCreator and pyuic)|
| cmdolume.sh | Storage of a bash command executed by subprocess |

