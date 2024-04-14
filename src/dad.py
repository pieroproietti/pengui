from PySide6.QtCore import QProcess
from PySide6 import QtCore
from PySide6.QtWidgets import *
import webbrowser

# import ui section
from ui.ui_dad import Ui_DialogDad

import sys
import os
import yaml
import subprocess 
from  utilities import U
from peasy import Peasy

##
#
class Dad(Ui_DialogDad, QDialog):    

    def __init__(self, parent=None):
        super().__init__(parent) # parent
        self.setupUi(self) # mandatory

        self.eggs_yaml_path=U.conf_path+'/eggs.yaml'
        if not os.path.isfile(self.eggs_yaml_path):
            QMessageBox.critical(self, 'Error', f"Can't find {self.eggs_yaml_path}")
            quit()
        
        # now we read eggs.yaml
        with open(self.eggs_yaml_path, 'r') as file:
            eggs = yaml.safe_load(file)

        self.lineEditSnapshotDir.setText(eggs["snapshot_dir"])
        self.lineEditSnapshotPrefix.setText(eggs['snapshot_prefix'])
        self.lineEditSnapshotBasename.setText(eggs['snapshot_basename'])
        self.lineEditUserOpt.setText(eggs['user_opt'])

        self.lineEditUserOptPasswd.setText(eggs['user_opt_passwd'])
        self.lineEditRootPasswd.setText(eggs['root_passwd'])
        self.checkBoxMakeIsohybrid.setEnabled(False)
        self.checkBoxMakeIsohybrid.setChecked(eggs['make_isohybrid'])
        self.checkBoxMakeMd5sum.setEnabled(True) 
        self.checkBoxMakeMd5sum.setChecked(eggs['make_md5sum'])

       
        # buttonBox connect
        self.buttonBox.helpRequested.connect(self.help)
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.dad_d)
        self.buttonBox.rejected.connect(self.close)
        self.buttonBox.accepted.connect(self.save)
        self.showMaximized()

    ##
    #
    def help(self):
        webbrowser.open('https://github.com/pieroproietti/penguins-eggs?tab=readme-ov-file#eggs-dad')

    ##
    #
    @QtCore.Slot()
    def save(self):
        with open(self.eggs_yaml_path, 'r') as file:
            eggs = yaml.safe_load(file)

        eggs["snapshot_dir"]=self.lineEditSnapshotDir.text()
        eggs['snapshot_prefix']=self.lineEditSnapshotPrefix.text()
        eggs['snapshot_basename']=self.lineEditSnapshotBasename.text()

        eggs['user_opt']=self.lineEditUserOpt.text()
        eggs['user_opt_passwd']=self.lineEditUserOptPasswd.text()
        eggs['root_passwd']=self.lineEditRootPasswd.text()

        eggs['make_isohybrid']=self.checkBoxMakeIsohybrid.isChecked()
        eggs['make_md5sum']=self.checkBoxMakeMd5sum.isChecked()
        
        ##
        #
        with open('/tmp/eggs.yaml', 'w') as object_file:
            yaml.dump(eggs, object_file)

            Peasy().run("sudo mv /tmp/eggs.yaml /etc/penguins-eggs.d/eggs.yaml")

        self.close()

    @QtCore.Slot()
    def dad_d(self):
        Peasy().run("sudo eggs dad -d")
        self.close()
