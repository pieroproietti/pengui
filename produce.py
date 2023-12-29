import sys
import os
import yaml

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QPushButton, QVBoxLayout

from ui.ui_produce import Ui_DialogProduce

##
#
class Produce(QtWidgets.QWidget, Ui_DialogProduce):
    def __init__ (self):
        super().__init__()

        self.setupUi(self) # mandatory

        self.setWindowTitle = "Produce"

        # UI
        with open('/etc/penguins-eggs.d/eggs.yaml', 'r') as file:
            eggs = yaml.safe_load(file)

        self.lineEditBasename.setText(eggs['snapshot_basename'])
        self.lineEditPrefix.setText(eggs['snapshot_prefix'])
        self.comboBoxAddons.addItems(['', 'adapt', 'ichoice', 'pve', 'rsupport'])
        self.comboBoxFilters.addItems(['', 'custom', 'homes', 'usr'])
        self.comboBoxCompression.addItems(['fast', 'standard', 'max'])

        # recupero i themi da .wardrobe/vendors/
        if os.geteuid() == 0:
            path='/home/' + os.getenv('SUDO_USER')
        else:
            path='/home/' + os.getenv('USER')

        dirs_themes= os.listdir(path +'/.wardrobe/vendors/')
        sorted_themes=sorted(dirs_themes)
        themes=['eggs']
        themes.extend(sorted_themes)

        self.comboBoxTheme.addItems(themes)

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
