from PySide6.QtCore import QProcess
import sys
import os

##
#
class Terminal(QProcess):

    def execute(self, command):
        if os.geteuid() != 0:
            if command !='eggs wardrobe get':
                command='sudo ' + command

        # process start
        process = QProcess(self)
        process.setProgram("/usr/bin/x-terminal-emulator")
        # can not run without dbus-launch, so we need:
        # sudo apt-get install dbus-x11
        # sudo service dbus restart
        process.setArguments(["-e", command])
        process.start()

