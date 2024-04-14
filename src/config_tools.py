from PySide6.QtCore import QProcess
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import *
from peasy import Peasy

import webbrowser

# import ui section
from ui.ui_config_tools import Ui_Dialog

import os
import yaml
from utilities import U

class Config_Tools(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.tools_yaml_path = os.path.join(U.conf_path, 'tools.yaml')
        if not os.path.exists(self.tools_yaml_path):
            QMessageBox.warning(self, 'Warning', f"Can't find {self.tools_yaml_path}")
            return

        with open(self.tools_yaml_path, 'r') as file:
            tools = yaml.safe_load(file)

        self.lineEditLocalPathIso.setText(tools["localPathIso"])
        self.lineEditLocalPathDeb.setText(tools["localPathDeb"])
        self.lineEditRemoteHost.setText(tools["remoteHost"])
        self.lineEditRemoteUser.setText(tools["remoteUser"])
        self.lineEditRemotePathIso.setText(tools["remotePathIso"])
        self.lineEditRemotePathDeb.setText(tools["remotePathDeb"])
        self.lineEditFilterDeb.setText(tools["filterDeb"])

        # buttonBox connect
        self.buttonBox.helpRequested.connect(self.help)
        self.buttonBox.rejected.connect(self.close)
        self.buttonBox.accepted.connect(self.save)

        self.show()

    ##
    #
    def help(self):
        webbrowser.open('https://github.com/pieroproietti/penguins-eggs?tab=readme-ov-file#eggs-dad')

    ##
    #
    def save(self):
        tools = {
            "localPathIso": self.lineEditLocalPathIso.text(),
            "localPathDeb": self.lineEditLocalPathDeb.text(),
            "remoteHost": self.lineEditRemoteHost.text(),
            "remoteUser": self.lineEditRemoteUser.text(),
            "remotePathIso": self.lineEditRemotePathIso.text(),
            "remotePathDeb": self.lineEditRemotePathDeb.text(),
            "filterDeb": self.lineEditFilterDeb.text(),
        }

        ##
        #
        with open('/tmp/eggs.yaml', 'w') as object_file:
            yaml.dump(eggs, object_file)

            Peasy().run("sudo mv /tmp/eggs.yaml /etc/penguins-eggs.d/eggs.yaml")

        self.close()
        