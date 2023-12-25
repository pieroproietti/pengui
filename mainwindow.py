import sys
import os

# Import QtWidgets, QtCore
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QPushButton

# Questo è l'import cruciale
from ui.ui_mainwindow import Ui_MainWindow


##
# QtWidgets.QWidget serve per customizzare
class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):    
    def __init__ (self):
        super().__init__() # inizializza

        self.setupUi(self) # mandatory

        # Signals are emitted by objects 
        self.action_About.triggered.connect(self.about)
        self.action_Configure.triggered.connect(self.configure)
        self.action_Exit.triggered.connect(self.exit)
        self.action_Kill.triggered.connect(self.kill)
        self.action_Produce.triggered.connect(self.produce)

        #self.setCentralWidget(b)

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
        print ("Configure")


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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = MyMainWindow() # ricorda ()

    sys.exit(app.exec()) # ricorda ()