from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import *

# import ui section
from ui.ui_eggs_configuration import Ui_Dialog

import sys
import os
import yaml
import subprocess 

##
#
class EggsConfiguration(Ui_Dialog, QDialog):    

    def __init__ (self):
        super().__init__() # inizializza

        self.setupUi(self) # mandatory

        # check root
        if os.geteuid() != 0:
            button = QPushButton("You need to be root, to configure eggs")
            button.clicked.connect(self.exit)
            self.setCentralWidget(button)

        self.file_eggs='/etc/penguins-eggs.d/eggs.yaml'
        if os.path.exists('/etc/penguins-eggs.d'):
            try:
                subprocess.run(['/usr/bin/eggs', 'dad', '--default'], check=True)
            except subprocess.CalledProcessError as e:
                print(f'Command {e.cmd} failed with error {e.returncode}')

        if not os.path.isfile(self.file_eggs):
            os.popen('cp assets/eggs.yaml /etc/penguins-eggs.d/') 
        
        with open('/etc/penguins-eggs.d/eggs.yaml', 'r') as file:
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

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        self.show()

    ##
    #
    @QtCore.Slot()
    def accept(self):
        
        with open(self.file_eggs, 'r') as file:
            eggs = yaml.safe_load(file)

        eggs["snapshot_dir"]=self.lineEditSnapshotDir.text()
        eggs['snapshot_prefix']=self.lineEditSnapshotPrefix.text()
        eggs['snapshot_basename']=self.lineEditSnapshotBasename.text()

        eggs['user_opt']=self.lineEditUserOpt.text()
        eggs['user_opt_passwd']=self.lineEditUserOptPasswd.text()
        eggs['root_passwd']=self.lineEditRootPasswd.text()

        eggs['make_isohybrid']=self.checkBoxMakeIsohybrid.isChecked()
        eggs['make_md5sum']=self.checkBoxMakeMd5sum.isChecked()

        with open(self.file_eggs, 'w') as object_file:
            yaml.dump(eggs, object_file)


    ##
    #
    @QtCore.Slot()
    def reject(self):
        print('Reject')
            
        
    ##
    #
    @QtCore.Slot()
    def exit(self):
        print ("Exit")
        quit()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = EggsConfiguration()
    sys.exit(app.exec())