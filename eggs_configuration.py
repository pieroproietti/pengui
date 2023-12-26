import sys
import os
import yaml
import subprocess

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

        # check root
        if os.geteuid() != 0:
            button = QPushButton("You MUST be root!")
            button.clicked.connect(self.exit)
            #self.setCentralWidget(button)
            #sys.exit(0)

        self.file_eggs='/etc/penguins-eggs.d/eggs.yaml'
        if os.path.exists('/etc/penguins-eggs.d'):
            if not os.path.isfile(self.file_eggs):
                os.popen('cp eggs.yaml /etc/penguins-eggs.d/') 
        else:
            os.mkdir('/etc/penguins-eggs.d')    
            os.popen('cp eggs.yaml /etc/penguins-eggs.d/') 

        print('file_eggs:' + self.file_eggs)
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

        eggs['make_md5sum']=self.checkBoxMakeMd5sum.checkState

        with open(self.file_eggs, 'w') as object_file:
            yaml.dump(eggs, object_file)

        print('Accept')

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