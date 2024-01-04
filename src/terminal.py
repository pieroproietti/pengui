from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (QMessageBox)

import sys
import os
import subprocess

##
#
class Terminal(QProcess):

    def on_process_finished(exit_code, exit_status):
        msgBox = QMessageBox()
        msgBox.setText("Command end: exit code " + 
                       str(exit_code)+ 
                       " " + str(exit_status))
        msgBox.exec()



    def execute(self, command):
        title=command
        if os.geteuid() != 0:
            if (command !='eggs wardrobe get' and 
                command !='eggs wardrobe list' and
                command !='eggs wardrobe show'):
                command='sudo ' + command

        if False:
            # method1
            p = QProcess()
            p.setProgram("/usr/bin/x-terminal-emulator")
            p.setArguments(['-e', command])
            p.start()        
            p.waitForFinished(100000)

        # Run the command in the terminal
        process = QProcess(self)
        process.setProgram("/usr/bin/x-terminal-emulator")
        process.setArguments(['-e', command])
        #process.finished.connect(Terminal.on_process_finished)
        process.start()
        process.waitForFinished(100000)
        
