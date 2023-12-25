import sys
#import os
#import json 
import yaml

# Import QtWidgets, QtCore
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QPushButton

# Questo è l'import cruciale
from ui.ui_configuration import Ui_Form

##
# QtWidgets.QWidget serve per customizzare
class EggsConfiguration(QtWidgets.QWidget, Ui_Form):    
    def __init__ (self):
        super().__init__() # inizializza

        self.setupUi(self) # mandatory

        with open('/etc/penguins-eggs.d/eggs.yaml', 'r') as file:
            eggs = yaml.safe_load(file)

        self.lineEditSnapshotDir.setText(eggs["snapshot_dir"])
        self.lineEditSnapshotPrefix.setText(eggs['snapshot_prefix'])
        self.lineEditSnapshotBasename.setText(eggs['snapshot_basename'])
        self.lineEditUserOpt.setText(eggs['user_opt'])
        self.lineEditUserOptPasswd.setText(eggs['user_opt_passwd'])
        self.lineEditRootPasswd.setText(eggs['root_passwd'])
        self.checkBoxMakeMd5sum.setEnabled(True) 
        self.checkBoxMakeMd5sum.setChecked(eggs['make_md5sum'])

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        self.show()

    ##
    #
    def accept(self):
        print('Accept')

    ##
    #
    def reject(self):
        print('Reject')
            
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = EggsConfiguration()
    sys.exit(app.exec())