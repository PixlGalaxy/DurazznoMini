#GALAXY APP SCRIPT

version = "5.9"
Notif = ""

import os
import urllib.request 
import webbrowser
import sys
import subprocess
from PySide2 import QtWidgets, QtGui
from tkinter import *
from tendo import singleton

for line in urllib.request.urlopen("https://drive.google.com/uc?export=download&id=1O2ZLaoNrkjv1fcc072Y5oagHaeSX28sB"):
    global versiononline
    versiononline = (line.decode('utf-8')) 

if version != versiononline:
        Notif = "Durazzno Mini Update Avialable"
    
    

me = singleton.SingleInstance()
class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f"Galaxy")
        menu = QtWidgets.QMenu(parent)



        open_DMSCU = menu.addAction("DURAZZNO MINI UPDATE")
        open_DMSCU.triggered.connect(self.open_DMSCU)
        open_DMSCU.setIcon(QtGui.QIcon("update.png"))
        

        open_PSP = menu.addAction("PC STARTER PACK")
        open_PSP.triggered.connect(self.open_PSP)
        open_PSP.setIcon(QtGui.QIcon("psp.png"))
        
        
        open_PAP = menu.addAction("PYTHON APPS")
        open_PAP.triggered.connect(self.open_PAP)
        open_PAP.setIcon(QtGui.QIcon("papp.png"))


        open_CDI = menu.addAction("CRYSTAL DISK INFO")
        open_CDI.triggered.connect(self.open_CDI)
        open_CDI.setIcon(QtGui.QIcon("cdi.png"))



        open_CDM = menu.addAction("CRYSTAL DISK MARK")
        open_CDM.triggered.connect(self.open_CDM)
        open_CDM.setIcon(QtGui.QIcon("cdm.png"))



        open_SDS = menu.addAction("SHUTDOWN SCHEDULER")
        open_SDS.triggered.connect(self.open_SDS)
        open_SDS.setIcon(QtGui.QIcon("sds.png"))



        open_KMS = menu.addAction("KMS AUTO DOWNLOAD")
        open_KMS.triggered.connect(self.open_KMS)
        open_KMS.setIcon(QtGui.QIcon("win.png"))



        exit_ = menu.addAction("EXIT APPLICATION")
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

    
    def open_DMSCU(self):
        """
        :return:
        """
        for line in urllib.request.urlopen("https://drive.google.com/uc?export=download&id=1O2ZLaoNrkjv1fcc072Y5oagHaeSX28sB"):
            global versiononline
            versiononline = (line.decode('utf-8')) 

        if version != versiononline:
            os.startfile("updatestart.pyw")
            sys.exit()
        elif version == versiononline:
            root = Tk()
            root.title("Durazzno Mini Update Client")
            root.iconbitmap(r"update.ico")

            text = Label(root, text="DURAZZNO MINI IS UP TO DATE!")
            text.pack() 

            photo = PhotoImage(file="Durazzno.png")
            labelphoto = Label(root, image = photo)
            labelphoto.pack() 

            root.mainloop()

 

    def open_PSP(self):
        """
        :return:
        """
        os.startfile("psp.pyw")
        
    def open_PAP(self):
        """
        :return:
        """
        os.startfile("papp.pyw")

    def open_CDI(self):
        """
        :return:
        """
        os.startfile("cdi.exe")

    def open_CDM(self):
        """
        :return:
        """
        os.startfile("cdm.exe")

    def open_SDS(self):
        """
        :return:
        """
        os.system('Sds.py')

    def open_KMS(self):
        """
        :return:
        """
        os.startfile('kms.bat')

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icon.png"), w)
    tray_icon.show()
    tray_icon.showMessage(Notif, '')
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
