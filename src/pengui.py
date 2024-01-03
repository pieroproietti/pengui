#!/bin/python
import sys
import os
import webbrowser

from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6 import QtCore
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QMainWindow, 
    QApplication, 
    QPushButton, 
    QMessageBox, 
    QToolBar, 
    QStatusBar,
    # Dialog
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QLabel
)

from produce import Produce
from config import Config
from config_tools import Config_Tools
from terminal import Terminal
from utilies import U

import resources_rc 


# import from ui
from ui.ui_pengui import Ui_MainWindow

##
# 
class MyMainWindow(Ui_MainWindow, QMainWindow):    
    def __init__ (self):
        super().__init__() # inizializza

        self.setupUi(self) # mandatory
        self.setWindowTitle = "penGUI"

        button = QPushButton("README")
        button.clicked.connect(self.read_me)
        self.setCentralWidget(button)

        # toolbar
        toolbar = QToolBar("My main toolbar")

        ## configure
        dad_icon = QIcon(QPixmap(":/icons/dad.svg"))
        dad_action = QAction("Dad", self)
        dad_action.setToolTip("Dad configure eggs")
        dad_action.triggered.connect(self.configure)
        #toolbar.addAction(dad_icon, dad_action)
        toolbar.addAction(dad_action)
        ## produce
        produce_action = QAction("Produce", self)
        produce_action.setToolTip("Produce a new ISO")
        produce_action.triggered.connect(self.produce)
        produce_icon = QIcon(QPixmap(":/icons/produce.svg"))
        #toolbar.addAction(produce_icon, produce_action)
        toolbar.addAction(produce_action)
        ## kill
        kill_action = QAction("Kill", self)
        kill_action.setToolTip("Kill generated ISOs")
        kill_action.triggered.connect(self.kill)
        kill_icon = QIcon(QPixmap(":/icons/kill.svg"))
        #toolbar.addAction(kill_icon, kill_action)
        toolbar.addAction(kill_action)

        self.addToolBar(toolbar)

        # statusBar
        self.setStatusBar(QStatusBar(self))

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
        self.actionConfigureTools.triggered.connect(self.configure_tools)
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

        self.actionUsersGuide.triggered.connect(self.help_users_guide)
        self.actionBlog.triggered.connect(self.help_blog)
        self.actionRepository.triggered.connect(self.help_repository)
        self.actionTelegram.triggered.connect(self.help_telegram)

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
    def read_me(self):
        webbrowser.open('https://github.com/pieroproietti/pengui?tab=readme-ov-file#pengui-take-cure-of-eggs')

    ##
    #
    @QtCore.Slot()
    def configure(self):
        dialog_config=Config(self)
        dialog_config.setWindowTitle("Dad")
        dialog_config.exec()
        #self.setCentralWidget()

    @QtCore.Slot()
    def configure_tools(self):
        dialog=Config_Tools(self)
        dialog.setWindowTitle("Config tools")
        dialog.exec()

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
        dialog = Produce(self)
        dialog.setWindowTitle("Produce")
        answer=dialog.exec()
        print(answer)
        if answer== dialog.accept:
            print("produce") 
        
        if answer ==dialog.reject:
            print("non produce")

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

    def help(self):
        webbrowser.open('https://penguins-eggs.net/docs/Tutorial/eggs-users-guide')

    def help_users_guide(self):
        webbrowser.open('https://penguins-eggs.net/docs/Tutorial/eggs-users-guide')

    def help_blog(self):
        webbrowser.open('https://penguins-eggs.net')

    def help_repository(self):
        webbrowser.open('https://github.com/pieroproietti/penguins-eggs')

    def help_telegram(self):
        webbrowser.open('https://t.me/penguins_eggs')

##
# real main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    sys.exit(app.exec())