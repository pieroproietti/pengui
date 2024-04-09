from PySide6.QtCore import QProcess, QObject, Slot
from PySide6.QtWidgets import QWidget, QMessageBox

class Peasy(QWidget):
    def __init__(self):
        super().__init__()

    def run(self, cmd: str):
        self.cmd = cmd
        self.process = QProcess()
        self.process.setProgram("/usr/bin/x-terminal-emulator")
        self.process.setArguments(['-H','-T', f"penGUI: {cmd}",'-e', cmd])
        self.process.finished.connect(self.on_finished_slot) # connect the finished signal to the slot
        self.process.start()

        # Display message before starting the process
        #QMessageBox.information(self, "PenGUI", f"Preparing to execute: {cmd}")

        self.process.waitForStarted()
        self.process.waitForFinished(-1)
        

    @Slot(int)
    def on_finished_slot(self, exit_code):
        if exit_code == 0:
            QMessageBox.information(self, "PenGUI", f"Command {self.cmd} executed successfully")