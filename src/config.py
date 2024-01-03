from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import *
import webbrowser
from terminal import Terminal

# import ui section
from ui.ui_config import Ui_DialogConfig

import sys
import os
import yaml
import subprocess 
from  utilies import U

##
#
class Config(Ui_DialogConfig, QDialog):    

    def __init__(self, parent=None):
        super().__init__(parent) # parent
        self.setupUi(self) # mandatory

        self.eggs_yaml_path=U.conf_path+'/eggs.yaml'
        if not os.path.isfile(self.eggs_yaml_path):
            msgBox = QMessageBox(self)
            msgBox.setText("Can't find /etc/penguins-eggs.d/eggs.yaml")
            msgBox.exec()
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

        self.pushButtonHelp.clicked.connect(self.help)
        self.pushButtonSave.clicked.connect(self.save)
        self.pushButtonDiscard.clicked.connect(self.close_me)

        self.buttonBox.accepted.connect(self.close_me)
        self.buttonBox.rejected.connect(self.close_me)
        
        self.show()


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

        
        # check root
        if os.geteuid() != 0:
            with open('/tmp/eggs.yaml', 'w') as object_file:
                yaml.dump(eggs, object_file)
                Terminal.execute(self, 'cp /tmp/eggs.yaml /etc/penguins-eggs.d/eggs.yaml')
        else:
            with open(self.eggs_yaml_path, 'w') as object_file:
                yaml.dump(eggs, object_file)



    @QtCore.Slot()
    def close_me(self):
        self.close()
