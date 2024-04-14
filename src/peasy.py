import os
from PySide6.QtCore import QProcess, QObject, Slot
from PySide6.QtWidgets import QWidget, QMessageBox

class Peasy(QWidget):
    def __init__(self):
        super().__init__()

    def run(self, cmd: str):
        self.cmd = cmd

        # Create a script that will run the command and pause
        # This is needed because the terminal emulator will close
        # immediately after the command finishes execution
        # The pause command will keep the terminal open until the user
        # presses a key
        cmdPause = f'{cmd} ; echo ""; read -p "Press enter to close the terminal..."'
        scriptContent = f'#!/bin/bash\n{cmdPause}'
        scriptFile = "/tmp/_pengui-cmd.sh"
        with open(scriptFile, "w") as f:
            f.write(scriptContent)

        # Make the script executable
        os.system(f"chmod +x {scriptFile}")

        term="/usr/bin/x-terminal-emulator"
        if not os.path.exists(term):
            term="/tmp/x-terminal-emulator"
            if not os.path.exists(term):
                # download the terminal emulator
                os.system("wget https://raw.githubusercontent.com/pieroproietti/pengui/main/bin/x-terminal-emulator -O /tmp/x-terminal-emulator")
                os.system("chmod +x /tmp/x-terminal-emulator")
                term="/tmp/x-terminal-emulator"

        # Run the script using the terminal emulator
        # The -H option is used to open a new terminal window
        # The -T option is used to set the title of the terminal window
        # The -e option is used to execute the command
        self.process = QProcess()
        self.process.setProgram(term)
        self.process.setArguments(['-H','-T', f"{cmd}",'-e', 'bash', scriptFile])

        self.process.start()

        self.process.waitForStarted()
        self.process.waitForFinished(-1)

        # remove the script file
        os.system(f"rm {scriptFile}")
