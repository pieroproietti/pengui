import sys
import os

# Import QtWidgets, QtCore
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QPushButton

# Questo è l'import cruciale
from ui.ui_configuration import Ui_Form


##
# QtWidgets.QWidget serve per customizzare
class Configuration(QtWidgets.QMainWindow, Ui_Form):    
    def __init__ (self):
        super().__init__() # inizializza

        self.setupUi(self) # mandatory

