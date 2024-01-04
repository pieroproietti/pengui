from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (QMessageBox)

import sys
import os
import subprocess

##
#
class Terminal(QProcess):

    def execute(self, command):
        title=command

        sudo = False
        if os.geteuid() != 0:
            if (command !='eggs wardrobe get' and 
                command !='eggs wardrobe list' and
                command !='eggs wardrobe show'):
                command='sudo ' + command
                sudo = True

        msgBox = QMessageBox()
        msgBox.setStandardButtons(QMessageBox.Cancel|QMessageBox.Apply)
        msgBox.setText("PenGUI will open a terminal and run:\n\n" + command + "\n")
        ret=msgBox.exec()
        if ret == QMessageBox.Apply:
            # Run the command in the terminal
            process = QProcess(self)
            process.setProgram("/usr/bin/x-terminal-emulator")
            process.setArguments(['-e', command])
            process.start()
            process.waitForFinished(100000)
      
