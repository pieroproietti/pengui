import sys
import os
import subprocess

# Import QtWidgets, QtCore
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QPushButton

from eggs_configuration import Ui_Form

# Questo è l'import cruciale
from ui.ui_mainwindow import Ui_MainWindow


##
# QtWidgets.QWidget serve per customizzare
class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):    
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
        
        self.form = Ui_Form

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
        # visualizza form
        pass
        
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
        try:
            subprocess.run(['/usr/bin/eggs', 'kill'], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Command {e.cmd} failed with error {e.returncode}')

        #result=subprocess.run(['/usr/bin/eggs', 'kill', '--nointeractive'], stdout=subprocess.PIPE)
        #print(result.stdout.decode())

    ##
    #
    @QtCore.Slot()
    def produce(self):
        try:
            subprocess.run(['/usr/bin/eggs', 'produce'], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Command {e.cmd} failed with error {e.returncode}')
        print ("Produce end")

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = MyMainWindow() # ricorda ()

    sys.exit(app.exec()) # ricorda ()