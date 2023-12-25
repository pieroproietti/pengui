import sys
import os

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

        if (self.lineEditSnapshotDir == ''):
            self.lineEditSnapshotDir.setText('/home/eggs')

        if self.lineEditSnapshotPrefix.text == '':           
            self.lineEditSnapshotPrefix.setText('egg-of_debian-bookworm-')

        if self.lineEditUserOpt.text == '':
            self.lineEditUserOpt.setText('live')

        if self.lineEditUserOptPasswd.text == '':
            self.lineEditUserOptPasswd.setText('evolution')
            
        if self.lineEditSnapshotBasename.text == '':
            self.lineEditSnapshotBasename.setText('colibri')


        if self.lineEditRootPasswd.text == '':
            self.lineEditRootPasswd.setText('evolution')

        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = Configuration() # ricorda ()

    sys.exit(app.exec()) # ricorda ()