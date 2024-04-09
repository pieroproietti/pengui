import sys
import os
import webbrowser
import version

from PySide6.QtCore import QProcess
from PySide6.QtGui import QAction
from PySide6 import QtCore
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QMainWindow, 
    QApplication, 
    QMessageBox, 
    QToolBar, 
    QStatusBar
)

from produce import Produce
from dad import Dad
from config_tools import Config_Tools
from wardrobe_show import WardrobeShow
from utilities import U
from peasy import Peasy

import resources_rc

# import from ui
from ui.ui_pengui import Ui_MainWindow

##
# 
class MyMainWindow(Ui_MainWindow, QMainWindow):
    version=version.APP + "-" + version.VERSION
    def __init__ (self):
        super().__init__() # inizializza

        # don't use penGUI as root
        if os.geteuid() == 0:
            print("Please use penGUI as a normal user.")
            sys.exit(0)

        self.setupUi(self) # mandatory
        
        self.setWindowTitle('penGUI')
        
        # toolbar
        toolbar = QToolBar()

        ## dad
        #dad_icon=QtGui.QIcon(":/pengui/icons/dad.svg")
        dad_action = QAction("DAD", self)
        dad_action.setToolTip("Dad configure eggs")
        dad_action.triggered.connect(self.configure)
        toolbar.addAction(dad_action)

        ## produce
        #produce_icon = QIcon(":/pengui/icons/produce.svg")
        produce_action = QAction("PRODUCE", self)
        produce_action.setToolTip("Produce a new ISO")
        produce_action.triggered.connect(self.produce)
        toolbar.addAction(produce_action)

        ## kill
        #kill_icon = QIcon(":/pengui/icons/kill.svg")
        kill_action = QAction("KILL", self)
        kill_action.setToolTip("Kill generated ISOs")
        kill_action.triggered.connect(self.kill)
        toolbar.addAction(kill_action)
        self.addToolBar(toolbar)

        ## readme
        #readme_icon = QIcon(":/pengui/icons/readme.svg")
        readme_action = QAction("README", self)
        readme_action.setToolTip("read me first!")
        readme_action.triggered.connect(self.readme)
        toolbar.addAction(readme_action)
        self.addToolBar(toolbar)


        # statusBar
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage('Ready', 5000)

        # File
        self.actionCalamaresInstall.triggered.connect(self.calamares_install)
        self.actionCalamaresRemove.triggered.connect(self.calamares_remove)
        self.action_Produce.triggered.connect(self.produce)
        self.action_Kill.triggered.connect(self.kill)
        self.actionStatus.triggered.connect(self.status)
        #self.actionCUckoo.triggered.connect(self.cuckoo)
        self.actionCUckoo.setDisabled(True)
        self.action_Exit.triggered.connect(self.exit)

        # Edit
        self.action_Tools.triggered.connect(self.configure_tools)

        # Tools
        self.action_Clean.triggered.connect(self.tools_clean)
        self.actionIPpaAdd.triggered.connect(self.tools_ppa_add)
        self.actionPpaRemove.triggered.connect(self.tools_ppa_remove)
        self.action_Skel.triggered.connect(self.tools_skel)
        self.action_Yolk.triggered.connect(self.tools_yolk)

        # Wardrobe
        self.actionGet.triggered.connect(self.wardrobe_get)
        self.actionList.triggered.connect(self.wardrobe_list)
        self.actionShow.triggered.connect(self.wardrobe_show)
        self.actionWear.triggered.connect(self.wardrobe_wear)

        # Help
        self.action_About.triggered.connect(self.about)
        self.actionUsersGuide.triggered.connect(self.help_users_guide)
        self.actionBlog.triggered.connect(self.help_blog)
        self.actionRepository.triggered.connect(self.help_repository)
        self.actionTelegram.triggered.connect(self.help_telegram)

        
        # in init prima di show, inizializziamo tutto
        self.showMaximized()
        
        if not U.package_is_installed("eggs"):
            answer=QMessageBox.critical(self, 'PenGUI', 
                                        "Install penguins-eggs before to continue.", 
                                        QMessageBox.Ok)
            webbrowser.open('https://sourceforge.net/projects/penguins-eggs/files/DEBS/')
            self.exit()
        
        # check exists /etc/penguins-eggs.d/
        file_eggs='/etc/penguins-eggs.d/eggs.yaml'
        dirname_eggs=os.path.dirname(file_eggs)
        if not U.conf_exists():
            peasy = Peasy()
            peasy.run('sudo eggs dad --default')

            if not U.eggs_yaml_exists(self):
                QMessageBox.critical(self, "PenGUI", "I was unable to create the configuration file /etc/penguins-eggs.d/eggs.yaml, the process ends")
                self.exit()

    ##
    #
    @QtCore.Slot()
    def about(self):
        QMessageBox.about(self, "PenGUI", "PenGUI is a GUI for penguins-eggs\n\nVersion: " + self.version)

    ##
    #
    @QtCore.Slot()
    
    ##
    #
    @QtCore.Slot()
    def readme(self):
        webbrowser.open('https://github.com/pieroproietti/pengui?tab=readme-ov-file#pengui-take-cure-of-eggs')
        self.statusBar().showMessage('read me', 5000)

    ##
    #
    @QtCore.Slot()
    def configure(self):
        dad=Dad(self)
        dad.setWindowTitle("Dad")
        dad.exec()
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
        Peasy().run("sudo eggs kill")

    @Slot()
    def produce(self):
        dialog = Produce(self)
        dialog.setWindowTitle("Produce")
        answer=dialog.exec()
        if answer== dialog.accept:
            self.statusBar().showMessage('produce', 5000)

    ##
    #
    @Slot()
    def calamares_install(self):
        if Peasy().run('sudo eggs calamares --install'):
            QMessageBox.information(self, "PenGUI", "Calamares installed")
            self.statusBar().showMessage('calamares --install', 5000)

    ##
    #
    @Slot()
    def calamares_remove(self):
        self.statusBar().showMessage('Removing calamares', 5000)
        if Peasy().run("sudo eggs calamares --remove --nointeractive"):
            QMessageBox.information(self, "PenGUI", "Calamares removed")

    ##
    #
    @Slot()
    def status(self):
        self.statusBar().showMessage('status', 5000)
        Peasy().run("eggs status")

    ##
    #
    @Slot()
    def cuckoo(self):
        self.statusBar().showMessage('cuckoo', 5000)
        Peasy().run('sudo eggs cuckoo')

    ## tools
    @QtCore.Slot()
    def tools_clean(self):
        self.statusBar().showMessage('cleaning', 5000)
        if Peasy().run("sudo eggs tools clean"):
            QMessageBox.information(self, "PenGUI", "Cleaned")

    ##
    #
    @QtCore.Slot()
    def tools_ppa_add(self):
        self.statusBar().showMessage('adding penguins-eggs-ppa to yours /etc/apt/sources.list.d', 5000)
        if Peasy().run("sudo eggs tools ppa --add --nointeractive"):
            QMessageBox.information(self, "PenGUI", "Added penguins-eggs-ppa")
    
    ##
    #
    @QtCore.Slot()
    def tools_ppa_remove(self):
        self.statusBar().showMessage('removing penguins-eggs-ppa form yours /etc/apt/sources.list.d', 5000)
        if Peasy().run("sudo eggs tools ppa --remove --nointeractive"):
            QMessageBox.information(self, "PenGUI", "Removed penguins-eggs-ppa")

    ##
    #
    @QtCore.Slot()
    def tools_skel(self):
        self.statusBar().showMessage('copyng your home configuration to /etc/skel', 5000)
        if Peasy().run("sudo eggs tools skel --nointeractive"):
            QMessageBox.information(self, "PenGUI", "Skel done")

    ##
    #
    @QtCore.Slot()
    def tools_yolk(self):
        self.statusBar().showMessage('creating a local repository /var/local/yolk', 5000)
        if Peasy().run("sudo eggs tools yolk --nointeractive"):
            QMessageBox.information(self, "PenGUI", "Yolk done")

    ## wardrobe
    @QtCore.Slot()
    def wardrobe_get(self):
        self.statusBar().showMessage('get a copy of wardrobe on ~/.wardrobe', 5000)
        if Peasy().run("sudo eggs wardrobe get --nointeractive"):
            QMessageBox.information(self, "PenGUI", "Wardrobe get finished")

    @QtCore.Slot()
    def wardrobe_list(self):
        self.statusBar().showMessage('listing wardrobe contents', 5000)
        Peasy().run('eggs wardrobe list')        

    @QtCore.Slot()
    def wardrobe_show(self):
        self.statusBar().showMessage('wardrobe show', 5000)
        dialog = WardrobeShow(self)
        dialog.setWindowTitle("wardrobe show")
        dialog.exec()

    @QtCore.Slot()
    def wardrobe_wear(self):
        self.statusBar().showMessage('wardrobe wear', 5000)
        Peasy().run('sudo eggs wardrobe wear')

    @QtCore.Slot()
    def help(self):
        self.statusBar().showMessage('help', 5000)
        webbrowser.open('https://penguins-eggs.net/docs/Tutorial/eggs-users-guide')

    @QtCore.Slot()
    def help_users_guide(self):
        self.statusBar().showMessage('help user', 5000)
        webbrowser.open('https://penguins-eggs.net/docs/Tutorial/eggs-users-guide')

    @QtCore.Slot()
    def help_blog(self):
        self.statusBar().showMessage('help blog', 5000)
        webbrowser.open('https://penguins-eggs.net')

    @QtCore.Slot()
    def help_repository(self):
        self.statusBar().showMessage('repository', 5000)
        webbrowser.open('https://github.com/pieroproietti/penguins-eggs')

    @QtCore.Slot()
    def help_telegram(self):
        self.statusBar().showMessage('help telegram', 5000)
        webbrowser.open('https://t.me/penguins_eggs')

##
# real main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    sys.exit(app.exec())