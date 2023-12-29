#!/bin/python
import sys
import os
import subprocess

from PySide6 import QtCore
from PySide6.QtCore import QProcess, Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton

from produce import Produce
from terminal import Terminal
from eggs_configuration import EggsConfiguration

# Questo è l'import cruciale
from ui.ui_mainwindow import Ui_MainWindow

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
        #self.setCentralWidget(EggsConfiguration())
        #self.setCentralWidget(Produce())


        # in init prima di show, inizializziamo tutto
        self.show()

    ##
    #
    @QtCore.Slot()
    def about(self):
        print ("About")

    ##
    #
    @QtCore.Slot()
    def configure(self):
        EggsConfiguration.show(self)
        
    ##
    #
    @QtCore.Slot()
    def exit(self):
        print ("Exit")
        quit()

    ##
    #
    @QtCore.Slot()
    def kill(self):
        #try:
        #    subprocess.run(['/usr/bin/eggs', 'kill'], check=True)
        #except subprocess.CalledProcessError as e:
        #    print(f'Command {e.cmd} failed with error {e.returncode}')

        # https://stackoverflow.com/questions/803265/getting-realtime-output-using-subprocess
        cmd=['/usr/bin/eggs', 'kill',]
        process = subprocess.run(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        while True:
            out = process.stdout.read(1)
            if out == '' and process.poll() != None:
                break
            if out != '':
                sys.stdout.write(out)
                sys.stdout.flush()
        #result=subprocess.run(['/usr/bin/eggs', 'kill', '--nointeractive'], stdout=subprocess.PIPE)
        #print(result.stdout.decode())

    @Slot()
    def produce(self):
        self.setCentralWidget(Produce())
        #terminal_process = QProcess()
        #terminal_program = "/usr/bin/x-terminal-emulator"  
        #command = "/usr/bin/eggs produce"

        #terminal_process.start(terminal_program, [command])

        #if terminal_process.waitForStarted():
            #terminal_process.waitForFinished(-1)
            #output = terminal_process.readAllStandardOutput().data().decode()
            #print(output)
        #else:
            #print("Failed to open the terminal.")

    ##
    #
    @QtCore.Slot()
    def clean(self):
        try:
            subprocess.run(['/usr/bin/eggs', 'tools', 'clean'], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Command {e.cmd} failed with error {e.returncode}')
        print ("Clean end")

    ##
    #
    @QtCore.Slot()
    def Ppa(self):
        try:
            subprocess.run(['/usr/bin/eggs', 'tools', 'ppa'], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Command {e.cmd} failed with error {e.returncode}')
        print ("PPA end")

    ##
    #
    @QtCore.Slot()
    def Skel(self):
        try:
            subprocess.run(['/usr/bin/eggs', 'tools', 'skel'], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Command {e.cmd} failed with error {e.returncode}')
        print ("Skel end")

    ##
    #
    @QtCore.Slot()
    def Yolk(self):
        print ("Yolk")


    ########################################################
    ###############    eggs_configuration    ###############


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = MyMainWindow() # ricorda ()

    sys.exit(app.exec()) # ricorda ()