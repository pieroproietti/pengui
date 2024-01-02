#!/bin/python
import sys
import os
import subprocess

from PySide6.QtGui import QAction, QIcon
from PySide6 import QtCore
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QMainWindow, 
    QApplication, 
    QPushButton, 
    QMessageBox, 
    QToolBar, 
    QStatusBar
)

from produce import Produce
from config import Config
from terminal import Terminal
from utilies import U

# import from ui
from ui.ui_pengui import Ui_MainWindow

##
# 
class MyMainWindow(Ui_MainWindow, QMainWindow):    
    def __init__ (self):
        super().__init__() # inizializza

        self.setupUi(self) # mandatory

        self.setWindowTitle = "penGUI"

        # toolbar
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        ## configure
        tb_configure_action = QAction("Configure", self)
        tb_configure_action.setToolTip("Configure eggs")
        tb_configure_action.triggered.connect(self.configure)
        toolbar.addAction(tb_configure_action)
        ## produce
        tb_produce_action = QAction("Produce", self)
        tb_produce_action.setToolTip("Produce a new ISO")
        tb_produce_action.triggered.connect(self.produce)
        toolbar.addAction(tb_produce_action)
        ## kill
        tb_kill_action = QAction("Kill", self)
        tb_kill_action.setToolTip("Kill generated ISOs")
        tb_kill_action.triggered.connect(self.kill)
        toolbar.addAction(tb_kill_action)
        ## exit
        tb_quit_action = QAction("Exit", self)
        tb_quit_action.setToolTip("Exit from penGUI")
        tb_quit_action.triggered.connect(self.exit)
        toolbar.addAction(tb_quit_action)

        # statusBar
        self.setStatusBar(QStatusBar(self))

        # check root
        if os.geteuid() != 0:
            button = QPushButton("You MUST be root to configure eggs!")
            button.clicked.connect(self.exit)
            self.setCentralWidget(button)

        # check exists /etc/penguins-eggs.d/eggs.yaml
        file_eggs='/etc/penguins-eggs.d/eggs.yaml'
        dirname_eggs=os.path.dirname(file_eggs)
        if not U.conf_exists():
            Terminal.execute('eggs dad --default')
            if not U.eggs_yaml_exists():
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
        dialog_config=Config(self)
        dialog_config.setWindowTitle("Configuration")
        dialog_config.exec()
        #self.setCentralWidget()
        
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
        dialog_produce = Produce(self)
        dialog_produce.setWindowTitle("Produce")
        dialog_produce.exec()

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