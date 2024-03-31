from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import *
import webbrowser
from terminal import Terminal
from pseudo_terminal import PseudoTerminal

# import ui section
from ui.ui_config_tools import Ui_Dialog

import os
import yaml
from utilies import U

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
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.save)
        self.buttonBox.rejected.connect(self.close_me)
        self.buttonBox.accepted.connect(self.close_me)

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

        if os.geteuid() != 0:
            with open('/tmp/tools.yaml', 'w') as object_file:
                yaml.dump(tools, object_file)
                # cp /tmp/tools.yaml /etc/penguins-eggs.d/tools.yaml
                pseudo_terminal = PseudoTerminal('sudo cp /tmp/tools.yaml /etc/penguins-eggs.d/tools.yaml', self)
                pseudo_terminal.show()
        else:
            with open(self.tools_yaml_path, 'w') as object_file:
                yaml.dump(tools, object_file)
