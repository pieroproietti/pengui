import sys
import os
import subprocess

from PySide6 import QtCore
from PySide6.QtCore import QProcess, Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox

class Terminal(QProcess):

    def execute(self, command):
        print("command:" + command)
        if os.geteuid() != 0:
            command='sudo ' + command
        process = QProcess(self)
        process.setProgram("/usr/bin/x-terminal-emulator")

        process.setArguments(["-e", command])
        process.start()
        print(command)

