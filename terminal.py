import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QPushButton, QVBoxLayout

from ui.ui_terminal import Ui_Dialog as Ui_terminal

##
#
class Terminal(QtWidgets.QWidget, Ui_terminal):
    def __init__ (self):
        super().__init__()

        self.setupUi(self) # mandatory

        self.setWindowTitle = "Terminal"
    
        self.show()


    ##
    #
    @QtCore.Slot()
    def accept(self):
        pass

    ##
    #
    @QtCore.Slot()
    def reject(self):
        print('Reject')
