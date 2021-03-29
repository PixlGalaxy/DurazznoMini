#PYTHON APPS SCRIPT

version = "1.4"

autoexit = 2

import os
import webbrowser
import sys
import subprocess
import urllib.request 
import requests
import time
from PySide2 import QtWidgets, QtGui
from tendo import singleton



me = singleton.SingleInstance()
class SystemTrayIcon(QtWidgets.QSystemTrayIcon):


    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f"PYTHON APPS")
        menu = QtWidgets.QMenu(parent)

        open_LIU = menu.addAction("PYTHON LIBRARY UPDATER")
        open_LIU.triggered.connect(self.open_LIU)
        open_LIU.setIcon(QtGui.QIcon("liu.png"))


        open_0 = menu.addAction("BATTERY CHARGING SOUND")
        open_0.triggered.connect(self.open_0)
        open_0.setIcon(QtGui.QIcon("bat.png"))



        open_AE = menu.addAction("AUTO EXIT ON/OFF (ALWAYS ON)")
        open_AE.triggered.connect(self.open_AE)
        open_AE.setIcon(QtGui.QIcon("autoext.png"))



        exit_ = menu.addAction("EXIT PYTHON APPS")
        exit_.triggered.connect(lambda: sys.exit())
        exit_.setIcon(QtGui.QIcon("exit.png"))


        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        
        if reason == self.DoubleClick:
            self.open_LIU()
        # if reason == self.Trigger:
        #     self.open_LIU()
    
    def open_LIU(self):
        """
        :return:
        """
        os.system("Lib_Update.py")

    def open_0(self):
        """
        :return:
        """
        url = 'https://drive.google.com/uc?export=download&id=1Ot8w6AhFg2SYGkyphxVdncMXfQRu3zY6'
        r = requests.get(url, allow_redirects=True)

        open('BatterySC-windows-installer.exe', 'wb').write(r.content)

        time.sleep(5)

        os.startfile("BatterySC-windows-installer.exe")

        
        if autoexit % 2 == 0:
            sys.exit()
        


    def open_1(self):
        """
        :return:
        """
        
        if autoexit % 2 == 0:
            sys.exit()

    def open_2(self):
        """
        :return:
        """

        if autoexit % 2 == 0:
            sys.exit()

    def open_3(self):
        """
        :return:
        """

        if autoexit % 2 == 0:
            sys.exit()

    def open_4(self):
        """
        :return:
        """

        if autoexit % 2 == 0:
            sys.exit()

    def open_5(self):
        """
        :return:
        """

        if autoexit % 2 == 0:
            sys.exit()
    
    def open_6(self):
        """
        :return:
        """

        if autoexit % 2 == 0:
            sys.exit()

    def open_7(self):
        """
        :return:
        """
    
        if autoexit % 2 == 0:
            sys.exit()

    def open_AE(self):
        """
        :return:
        """
        global autoexit 
        autoexit = autoexit + 1


           
    


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("papp.png"), w)
    tray_icon.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()