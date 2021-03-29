#PC STARTER PACK MINI SCRIPT

version = "2.2"

autoexit = 2

import os
import webbrowser
import sys
import subprocess
import time
from PySide2 import QtWidgets, QtGui
from tendo import singleton



me = singleton.SingleInstance()
class SystemTrayIcon(QtWidgets.QSystemTrayIcon):


    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f"PC STARTER PACK MINI")
        menu = QtWidgets.QMenu(parent)


        open_PSP = menu.addAction("PC STARTER PACK DIRECT LINK")
        open_PSP.triggered.connect(self.open_PSP)
        open_PSP.setIcon(QtGui.QIcon("gd.png"))
        

        open_1 = menu.addAction("ABLETON LIVE 10 SUITE DOWNLOAD")
        open_1.triggered.connect(self.open_1)
        open_1.setIcon(QtGui.QIcon("abltn.png"))



        open_2 = menu.addAction("ADOBE ILLUSTRATOR 2020 DOWNLOAD")
        open_2.triggered.connect(self.open_2)
        open_2.setIcon(QtGui.QIcon("ai.png"))



        open_3 = menu.addAction("ADOBE PHOTOSHOP 2020 DOWNLOAD")
        open_3.triggered.connect(self.open_3)
        open_3.setIcon(QtGui.QIcon("aps.png"))



        open_4 = menu.addAction("ADOBE PREMIERE 2020 DOWNLOAD")
        open_4.triggered.connect(self.open_4)
        open_4.setIcon(QtGui.QIcon("apr.png"))
        
        
        open_4A = menu.addAction("ADOBE ACROBAT PRO DOWNLOAD")
        open_4A.triggered.connect(self.open_4)
        open_4A.setIcon(QtGui.QIcon("aacr.png"))



        open_5 = menu.addAction("MICROSOFT OFFICE INSTALLER DOWNLOAD")
        open_5.triggered.connect(self.open_5)
        open_5.setIcon(QtGui.QIcon("ofce.png"))



        open_7 = menu.addAction("MOVAVI VIDEO EDITOR DOWNLOAD")
        open_7.triggered.connect(self.open_7)
        open_7.setIcon(QtGui.QIcon("mve.png"))
        
        
        open_8 = menu.addAction("AUTODESK AUTOCAD 2021 DOWNLOAD")
        open_8.triggered.connect(self.open_8)
        open_8.setIcon(QtGui.QIcon("acad.png"))
        
        
        
        open_1I = menu.addAction("MINECRAFT TLAUNCHER DOWNLOAD")
        open_1I.triggered.connect(self.open_1I)
        open_1I.setIcon(QtGui.QIcon("tlau.png"))




        open_AE = menu.addAction("AUTO EXIT ON/OFF (ALWAYS ON)")
        open_AE.triggered.connect(self.open_AE)
        open_AE.setIcon(QtGui.QIcon("autoext.png"))



        exit_ = menu.addAction("EXIT PC STARTER PACK MINI")
        exit_.triggered.connect(lambda: sys.exit())
        exit_.setIcon(QtGui.QIcon("exit.png"))


        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        
        if reason == self.DoubleClick:
            self.open_PSP()
        # if reason == self.Trigger:
        #     self.open_PSP()

    def open_PSP(self):
        """
        :return:
        """
        webbrowser.open("https://drive.google.com/drive/folders/1OhHPrYFLYjWt0Ts-4ZEbHy2_HJ4l6B7r?usp=sharing", new=2)
        if autoexit % 2 == 0:
            sys.exit()


    def open_1(self):
        """
        :return:
        """
        webbrowser.open("https://drive.google.com/uc?export=download&id=1pmoCbs18F4v2CfxQYv5Dt-um3x6vPpxV", new=2)
        
        if autoexit % 2 == 0:
            sys.exit()

    def open_2(self):
        """
        :return:
        """
        webbrowser.open("https://drive.google.com/uc?export=download&id=1YMvmh6_sFpKUGPBfZaVoJdhHK0pTUPfa", new=2)

        if autoexit % 2 == 0:
            sys.exit()

    def open_3(self):
        """
        :return:
        """
        webbrowser.open("https://drive.google.com/uc?export=download&id=1ReL2NjifQ7x_TJ5tOafZxZoSq6OQsBpP", new=2)

        if autoexit % 2 == 0:
            sys.exit()

    def open_4(self):
        """
        :return:
        """
        webbrowser.open("https://drive.google.com/uc?export=download&id=1dteT2TYVboLzY0MVVgMcwArs0PT2d3_P", new=2)

        if autoexit % 2 == 0:
            sys.exit()
            
    def open_4A(self):
        """
        :return:
        """
        webbrowser.open("https://drive.google.com/uc?export=download&id=1k5RkNdZgF8hwAjVvANSUKii3Hq1FpZ9y", new=2)

        if autoexit % 2 == 0:
            sys.exit()

    def open_5(self):
        """
        :return:
        """
        webbrowser.open("https://drive.google.com/uc?export=download&id=1Y6lMdEZzMhoeKcw88UBmL4EHUq_qxSHE", new=2)

        if autoexit % 2 == 0:
            sys.exit()
    
    def open_6(self):
        """
        :return:
        """
        webbrowser.open("https://drive.google.com/uc?export=download&id=1oRD1a_Gw5ailbc6Rb_tY3ufJsrqZ1dnk", new=2)
        webbrowser.open("https://drive.google.com/uc?export=download&id=18V2gj1kfcc8nWjInMpBt78UoLZyXnIsA", new=2)

        if autoexit % 2 == 0:
            sys.exit()

    def open_7(self):
        """
        :return:
        """
        webbrowser.open("https://drive.google.com/uc?export=download&id=1tMvVrauCdiL3K1MtFie5JHCIRE4WoN9M", new=2)

        if autoexit % 2 == 0:
            sys.exit()
    
    def open_8(self):
        """
        :return:
        """
        webbrowser.open("https://drive.google.com/uc?export=download&id=1GAKpVgyfsqYjeLGLetFQm04oo5YfqMdj", new=2)

        if autoexit % 2 == 0:
            sys.exit()
        
    def open_1I(self):
        """
        :return:
        """
        webbrowser.open("https://tlauncher.org/installer", new=2)
        
        if autoexit % 2 == 0:
            sys.exit()
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
    tray_icon = SystemTrayIcon(QtGui.QIcon("psp.png"), w)
    tray_icon.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()