import sys
import os

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
        self.form.show()
        #print ("Configure")


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
        print ("Kill")

    ##
    #
    @QtCore.Slot()
    def produce(self):
        print ("Produce")

    ##
    #
    @QtCore.Slot()
    def clean(self):
        print ("Clean")

    ##
    #
    @QtCore.Slot()
    def Ppa(self):
        print ("PPA")

    ##
    #
    @QtCore.Slot()
    def Skel(self):
        print ("Skel")

    ##
    #
    @QtCore.Slot()
    def Yolk(self):
        print ("Yolk")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = MyMainWindow() # ricorda ()

    sys.exit(app.exec()) # ricorda ()