from PySide6.QtCore import QProcess
import sys
import os

##
#
class Terminal(QProcess):

    def execute(self, command):
        print("command:" + command)
        if os.geteuid() != 0:
            if command !='eggs wardrobe get':
                command='sudo ' + command

        # process start
        process = QProcess(self)
        process.setProgram("/usr/bin/x-terminal-emulator")
        process.setArguments(["-e", command])
        process.start()

