#!/bin/python
import sys
import os
import webbrowser

from PySide6 import QtGui
from PySide6.QtGui import QAction, QIcon, QPixmap, QImage
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
        toolbar = QToolBar()

        ## dad
        dad_icon=QtGui.QIcon(":/pengui/icons/dad.svg")
        dad_action = QAction(dad_icon , "", self)
        dad_action.setToolTip("Dad configure eggs")
        dad_action.triggered.connect(self.configure)
        toolbar.addAction(dad_action)

        ## produce
        produce_icon = QIcon(":/pengui/icons/produce.svg")
        produce_action = QAction(produce_icon, "", self)
        produce_action.setToolTip("Produce a new ISO")
        produce_action.triggered.connect(self.produce)
        toolbar.addAction(produce_action)

        ## kill
        kill_icon = QIcon(":/pengui/icons/kill.svg")
        kill_action = QAction(kill_icon, "", self)
        kill_action.setToolTip("Kill generated ISOs")
        kill_action.triggered.connect(self.kill)
        toolbar.addAction(kill_action)
        self.addToolBar(toolbar)

        # statusBar
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage('Ready', 5000)


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
        if not U.package_is_installed("eggs"):
            msgBox = QMessageBox()
            msgBox.setText("You must install penguins-eggs, before to continue.")
            msgBox.setInformativeText("""download it from https://sourceforge.net/projects/penguins-eggs/files/DEBS/and install with dkkg -i eggs-9.6.24.deb""")
            msgBox.setStandardButtons(QMessageBox.Cancel)
            msgBox.exec()
        
        # check exists /etc/penguins-eggs.d/eggs.yaml
        file_eggs='/etc/penguins-eggs.d/eggs.yaml'
        dirname_eggs=os.path.dirname(file_eggs)
        if not U.conf_exists():
            Terminal('eggs dad --default')
            if not U.eggs_yaml_exists():
                msgBox = QMessageBox(self)
                msgBox.setText("I was unable to reconfigure eggs, the process ends")
                msgBox.exec()
                self.exit()
                      
    ##
    #
    @QtCore.Slot()
    def about(self):
        msgBox = QMessageBox(self)
        msgBox.setText("penGUI take cure about eggs!")
        msgBox.exec()
        self.statusBar().showMessage('dad', 5000)


    ##
    #
    @QtCore.Slot()
    def read_me(self):
        webbrowser.open('https://github.com/pieroproietti/pengui?tab=readme-ov-file#pengui-take-cure-of-eggs')
        self.statusBar().showMessage('read me', 5000)

    ##
    #
    @QtCore.Slot()
    def configure(self):
        dialog_config=Config(self)
        dialog_config.setWindowTitle("Dad")
        dialog_config.exec()
        self.statusBar().showMessage('dad', 5000)

    @QtCore.Slot()
    def configure_tools(self):
        dialog=Config_Tools(self)
        dialog.setWindowTitle("Config tools")
        dialog.exec()
        self.statusBar().showMessage('tools configuration', 5000)

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
        self.statusBar().showMessage('kill', 5000)
        
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

        self.statusBar().showMessage('produce', 5000)


    ## tools
    @QtCore.Slot()
    def tools_clean(self):
        Terminal.execute(self, 'eggs tools clean')
        self.statusBar().showMessage('cleaning cache, logs, etc', 5000)


    ##
    #
    @QtCore.Slot()
    def tools_ppa(self):
        Terminal.execute(self, 'eggs tools ppa')
        self.statusBar().showMessage('adding penguins-eggs-ppa to yours /etc/apt/sources.list.d', 5000)
    
    ##
    #
    @QtCore.Slot()
    def tools_skel(self):
        Terminal.execute(self, 'eggs tools skel')
        self.statusBar().showMessage('copyng your home configuration to /etc/skel', 5000)

    ##
    #
    @QtCore.Slot()
    def tools_yolk(self):
        Terminal.execute(self, 'eggs tools yolk')
        self.statusBar().showMessage('creating a local repository /var/local/yolk', 5000)

    ## wardrobe
    @QtCore.Slot()
    def wardrobe_get(self):
        Terminal.execute(self, 'eggs wardrobe get')
        self.statusBar().showMessage('gettina a copy of wardrobe on ~/.wardrobe', 5000)

    @QtCore.Slot()
    def wardrobe_list(self):
        Terminal.execute(self, 'eggs wardrobe list')
        self.statusBar().showMessage('listing wardrobe contents', 5000)

    @QtCore.Slot()
    def wardrobe_show(self):
        Terminal.execute(self, 'eggs wardrobe show')
        self.statusBar().showMessage('show wardrpve content', 5000)

    @QtCore.Slot()
    def wardrobe_wear(self):
        Terminal.execute(self, 'eggs wardrobe wear')
        self.statusBar().showMessage('wardrobe wear', 5000)

    def help(self):
        webbrowser.open('https://penguins-eggs.net/docs/Tutorial/eggs-users-guide')
        self.statusBar().showMessage('help', 5000)

    def help_users_guide(self):
        webbrowser.open('https://penguins-eggs.net/docs/Tutorial/eggs-users-guide')
        self.statusBar().showMessage('help user', 5000)

    def help_blog(self):
        webbrowser.open('https://penguins-eggs.net')
        self.statusBar().showMessage('help blog', 5000)

    def help_repository(self):
        webbrowser.open('https://github.com/pieroproietti/penguins-eggs')
        self.statusBar().showMessage('repository', 5000)

    def help_telegram(self):
        webbrowser.open('https://t.me/penguins_eggs')
        self.statusBar().showMessage('help telegram', 5000)

##
# real main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    sys.exit(app.exec())