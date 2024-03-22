from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (QMessageBox)
import os

##
#
class Terminal(QProcess):

    def execute(self, command):
        sudo = False
        if os.geteuid() != 0:

            # sudo for all except:
            if not ("eggs mom" in command or
                'eggs status' in command or
                'eggs wardrobe get' in command or
                'eggs wardrobe list' in command or
                'eggs wardrobe show' in command):

                command='sudo ' + command
                sudo = True

        answer=QMessageBox.question(self, 'PenGUI', 'PenGUI will open a terminal and run the command:\n\n' + command + '\n', QMessageBox.Cancel|QMessageBox.Apply)
        if answer == QMessageBox.Apply:
            # Run the command in the terminal
            process = QProcess(self)
            process.setProgram("/usr/bin/x-terminal-emulator")
            process.setArguments(['-e', command])
            process.start()
            quindici_minuti=900000
            process.waitForFinished(quindici_minuti)
