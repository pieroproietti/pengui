from PySide6.QtCore import QProcess
from PySide6.QtWidgets import QWidget, QMessageBox, QInputDialog, QLineEdit

##
#
class Peasy(QWidget):
    password = ""

    def __init__(self):
        super().__init__() # inizializza  
        
        
    def run(self, cmd: str): 
        QMessageBox.information(self, "PenGUI", "Pengui will run:\n\n" + cmd)

        cmdArgs = cmd.split()
        if cmdArgs[0] == "sudo":
            # insert -S option to sudo command
            cmdArgs.insert(1, "-S")

        if not self.is_sudo_password_cached():
            password_dialog=QInputDialog()
            password, ok = password_dialog.getText(self, "PenGUI", "Password is not cached, so please insert your password:", QLineEdit.Password)
            if not ok:
                QMessageBox.warning(self, "PenGUI", "Password not inserted, operation aborted")
                return
            else:
                self.password=password
        
        process = QProcess()
        process.setProgram(cmdArgs[0])
        process.setArguments( cmdArgs[1:] )
        process.readyReadStandardError.connect(self.handle_stderr())
        process.start()
        process.waitForStarted()
        process.write(self.password.encode())
        process.closeWriteChannel()
        process.waitForFinished(-1)
        if process.exitStatus() == QProcess.ExitStatus.NormalExit:
            return True
        else:
            QMessageBox.warning(self, "PenGUI", "Error: " + process.errorString())
            return False

    ##
    # Handle stderr
    def handle_stderr(self):
        pass
        #QMessageBox().warning(self, "Warning", self.readAllStandardError().data().decode())
        
    ##
    # Check if the sudo password is cached 
    def is_sudo_password_cached(self):
        cmd = "sudo -n echo 1"
        cmdArgs = cmd.split()
        process = QProcess()
        process.setProgram(cmdArgs[0])
        process.setArguments(cmdArgs[1:])
        process.start()
        process.waitForStarted()
        process.waitForFinished(-1)

        stdOut = process.readAllStandardOutput().data().decode().strip()  # Rimuovi spazi vuoti all'inizio e alla fine
        if stdOut == "1":
            return True
        else:
            return False
