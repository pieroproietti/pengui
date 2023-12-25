import sys
import os
import json 
import yaml

# Import QtWidgets, QtCore
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QPushButton

# Questo è l'import cruciale
from ui.ui_configuration import Ui_Form

##
# QtWidgets.QWidget serve per customizzare
class Configuration(QtWidgets.QWidget, Ui_Form):    
    def __init__ (self):
        super().__init__() # inizializza

        self.setupUi(self) # mandatory

        with open('eggs.yaml', 'r') as file:
            eggs = yaml.safe_load(file)

        self.lineEditSnapshotDir.setText(eggs["snapshot_dir"])
        self.lineEditSnapshotPrefix.setText(eggs['snapshot_prefix'])
        self.lineEditSnapshotBasename.setText(eggs['snapshot_basename'])
        self.lineEditUserOpt.setText(eggs['user_opt'])
        self.lineEditUserOptPasswd.setText(eggs['user_opt_passwd'])
        self.lineEditRootPasswd.setText(eggs['root_passwd'])
        self.checkBoxMakeMd5sum.setEnabled(eggs['make_md5sum'])

        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = Configuration() # ricorda ()

    sys.exit(app.exec()) # ricorda ()