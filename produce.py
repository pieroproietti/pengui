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

        self.checkBoxClone.stateChanged.connect(self.clone)
        self.checkBoxCryptedClone.stateChanged.connect(self.crypted_clone)
        self.checkBoxScript.stateChanged.connect(self.script)

        # recupero i themi da .wardrobe/vendors/
        if os.geteuid() == 0:
            path_themes='/home/' + os.getenv('SUDO_USER')
        else:
            path_themes='/home/' + os.getenv('USER')

        if os.path.exists(path_themes):
            found_themes= os.listdir(path_themes +'/.wardrobe/vendors/')
        else:
            found_themes=["To get theme, execute: eggs wardobe get"]

        sorted_themes=sorted(found_themes)
        themes=['eggs']
        themes.extend(sorted_themes)

        self.comboBoxTheme.addItems(themes)

        self.show()


    ##
    # azzerra cryptedClone, script e setta unsecure
    def clone(self):
        if self.checkBoxClone.checkState():
            self.checkBoxCryptedClone.setChecked(False)
            self.checkBoxScript.setChecked(False)
            self.checkBoxUnsecure.setChecked(True)

    ##
    # azzerra clone, script e setta unsecure
    def crypted_clone(self):
        if self.checkBoxCryptedClone.checkState():
            self.checkBoxClone.setChecked(False)
            self.checkBoxScript.setChecked(False)
            self.checkBoxUnsecure.setChecked(True)

    ##
    # azzerra clone e cryptedClone
    def script(self):
        if self.checkBoxScript.checkState():
            self.checkBoxClone.setChecked(False)
            self.checkBoxCryptedClone.setChecked(False)
           

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
