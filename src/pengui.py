#!/bin/python
import sys
import os
import subprocess

from PySide6 import QtCore
from PySide6.QtCore import QProcess, Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox

from produce import Produce
from eggs_configuration import EggsConfiguration

# Questo è l'import cruciale
from ui.ui_penGUI import Ui_MainWindow

##
# QtWidgets.QWidget serve per customizzare
class MyMainWindow(Ui_MainWindow, QMainWindow):    
    def __init__ (self):
        super().__init__() # inizializza

        self.setupUi(self) # mandatory

        self.setWindowTitle = "penGUI"

        # check root
        if os.geteuid() != 0:
            button = QPushButton("You MUST be root!")
            button.clicked.connect(self.exit)
            self.setCentralWidget(button)

        # check /etc/penguins-eggs.d/eggs.yaml
        file_eggs='/etc/penguins-eggs.d/eggs.yaml'
        dirname_eggs=os.path.dirname(file_eggs)
        # basename_eggs=os.path.basename(file_eggs)
        if os.path.exists(dirname_eggs):
            if not os.path.isfile(file_eggs):
                try:
                    subprocess.run(['/usr/bin/eggs', 'dad', '--default'], check=True)
                except subprocess.CalledProcessError as e:
                    print(f'Command {e.cmd} failed with error {e.returncode}')
                print('eggs dad --default')
                      
        # Signals are emitted by objects 
        self.action_About.triggered.connect(self.about)
        self.action_Configure.triggered.connect(self.configure)
        self.action_Exit.triggered.connect(self.exit)
        self.action_Kill.triggered.connect(self.kill)
        self.action_Produce.triggered.connect(self.produce)

        # Tools
        self.action_Clean.triggered.connect(self.clean)
        self.action_PPA.triggered.connect(self.Ppa)
        self.action_Skel.triggered.connect(self.Skel)
        self.action_Yolk.triggered.connect(self.Yolk)

        #self.setCentralWidget(Terminal())

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
        self.Terminal('eggs kill')
        
    @Slot()
    def produce(self):
        self.setCentralWidget(Produce())

    ##
    #
    @QtCore.Slot()
    def clean(self):
        self.Terminal('eggs tools clean')

    ##
    #
    @QtCore.Slot()
    def Ppa(self):
        self.Terminal('eggs tools ppa')
    
    ##
    #
    @QtCore.Slot()
    def Skel(self):
        self.Terminal('eggs tools skel')

    ##
    #
    @QtCore.Slot()
    def Yolk(self):
        self.Terminal('eggs tools yolk')

    ##
    #
    def Terminal(self, command):
        if os.geteuid() != 0:
            command='sudo ' + command
        process = QProcess(self)
        process.setProgram("/usr/bin/x-terminal-emulator")

        process.setArguments(["-e", command])
        process.start()
        print(command)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = MyMainWindow() # ricorda ()

    sys.exit(app.exec()) # ricorda ()