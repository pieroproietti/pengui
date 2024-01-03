from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import *
import webbrowser
from terminal import Terminal

# import ui section
from ui.ui_config_tools import Ui_Dialog

import os
import yaml
from  utilies import U

##
#
class Config_Tools(Ui_Dialog, QDialog):    

    def __init__(self, parent=None):
        super().__init__(parent) # parent
        self.setupUi(self) # mandatory

        self.tools_yaml_path=U.conf_path+'/tools.yaml'
        if not os.path.isfile(self.tools_yaml_path):
            msgBox = QMessageBox(self)
            msgBox.setText("Can't find " + self.tools)
            msgBox.exec()
            quit()
        
        # now we read tools.yaml
        with open(self.tools_yaml_path, 'r') as file:
            tools = yaml.safe_load(file)

        self.lineEditLocalPathIso.setText(tools["localPathIso"])
        self.lineEditLocalPathDeb.setText(tools["localPathDeb"])
        self.lineEditRemoteHost.setText(tools["remoteHost"])
        self.lineEditRemoteUser.setText(tools["remoteUser"])
        self.lineEditRemotePathIso.setText(tools["remotePathIso"])
        self.lineEditRemotePathDeb.setText(tools["remotePathDeb"])
        self.lineEditFilterDeb.setText(tools["filterDeb"])

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
        with open(self.tools_yaml_path, 'r') as file:
            tools = yaml.safe_load(file)

        tools["localPathIso"]=self.lineEditLocalPathIso.text()
        tools["localPathDeb"]=self.lineEditLocalPathDeb.text()
        tools["remoteHost"]=self.lineEditRemoteHost.text()
        tools["remoteUser"]=self.lineEditRemoteUser.text()
        tools["remotePathIso"]=self.lineEditRemotePathIso.text()
        tools["remotePathDeb"]=self.lineEditRemotePathDeb.text()
        tools["filterDeb"]=self.lineEditFilterDeb.text()

        
        # check root
        if os.geteuid() != 0:
            with open('/tmp/tools.yaml', 'w') as object_file:
                yaml.dump(tools, object_file)
                Terminal.execute(self, 'cp /tmp/tools.yaml /etc/penguins-eggs.d/tools.yaml')
        else:
            with open(self.tools_yaml_path, 'w') as object_file:
                yaml.dump(tools, object_file)



    @QtCore.Slot()
    def close_me(self):
        self.close()
