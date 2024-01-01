#!/bin/python
import sys
import os
import subprocess

from PySide6 import QtCore
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox

from produce import Produce
from eggs_configuration import EggsConfiguration
from terminal import Terminal

# import from ui
from ui.ui_pengui import Ui_MainWindow

##
# 
class MyMainWindow(Ui_MainWindow, QMainWindow):    
    def __init__ (self):
        super().__init__() # inizializza

        self.setupUi(self) # mandatory

        self.setWindowTitle = "penGUI"

        # check root
        if os.geteuid() != 0:
            button = QPushButton("You MUST be root to configure eggs!")
            button.clicked.connect(self.exit)
            self.setCentralWidget(button)

        # check /etc/penguins-eggs.d/eggs.yaml
        file_eggs='/etc/penguins-eggs.d/eggs.yaml'
        dirname_eggs=os.path.dirname(file_eggs)
        if not os.path.exists(dirname_eggs):
            Terminal.execute('eggs dad --default')
            if not os.path.exists('/etc/penguins-eggs.d'):
                msgBox = QMessageBox(self)
                msgBox.setText("You must to install penguins-eggs, before to configure it")
                msgBox.exec()
                self.exit()
                      
        # Signals are emitted by objects 
        self.action_About.triggered.connect(self.about)
        self.action_Configure.triggered.connect(self.configure)
        self.action_Exit.triggered.connect(self.exit)
        self.action_Kill.triggered.connect(self.kill)
        self.action_Produce.triggered.connect(self.produce)

        # Tools
        self.action_Clean.triggered.connect(self.tools_clean)
        self.action_PPA.triggered.connect(self.tools_ppa)
        self.action_Skel.triggered.connect(self.tools_skel)
        self.action_Yolk.triggered.connect(self.tools_yolk)

        # Wardrobe
        self.actionGet.triggered.connect(self.wardrobe_get)
        self.actionList.triggered.connect(self.wardrobe_list)
        self.actionShow.triggered.connect(self.wardrobe_show)
        self.actionWear.triggered.connect(self.wardrobe_wear)

        # in init prima di show, inizializziamo tutto
        self.show()

    ##
    #
    @QtCore.Slot()
    def about(self):
        msgBox = QMessageBox(self)
        msgBox.setText("penGUI take cure about eggs!")
        msgBox.exec()

    ##
    #
    @QtCore.Slot()
    def configure(self):
        self.setCentralWidget(EggsConfiguration())
        
    ##
    #
    @QtCore.Slot()
    def exit(self):
        sys.exit()

    ##
    #
    @QtCore.Slot()
    def kill(self):
        Terminal.execute(self, 'eggs kill')
        
    @Slot()
    def produce(self):
        self.setCentralWidget(Produce())

    ## tools
    @QtCore.Slot()
    def tools_clean(self):
        Terminal.execute(self, 'eggs tools clean')

    ##
    #
    @QtCore.Slot()
    def tools_ppa(self):
        Terminal.execute(self, 'eggs tools ppa')
    
    ##
    #
    @QtCore.Slot()
    def tools_skel(self):
        Terminal.execute(self, 'eggs tools skel')

    ##
    #
    @QtCore.Slot()
    def tools_yolk(self):
        Terminal.execute(self, 'eggs tools yolk')

    ## wardrobe
    @QtCore.Slot()
    def wardrobe_get(self):
        Terminal.execute(self, 'eggs wardrobe get')

    @QtCore.Slot()
    def wardrobe_list(self):
        Terminal.execute(self, 'eggs wardrobe list')

    @QtCore.Slot()
    def wardrobe_show(self):
        Terminal.execute(self, 'eggs wardrobe show')

    @QtCore.Slot()
    def wardrobe_wear(self):
        Terminal.execute(self, 'eggs wardrobe wear')

##
# real main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    sys.exit(app.exec())