from PySide6.QtCore import QProcess, QByteArray
from PySide6.QtWidgets import QWidget, QMessageBox, QInputDialog, QLineEdit

class Peasy(QWidget):
    password = ""

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self, cmd: str): 
        QMessageBox.information(self, "PenGUI", "Pengui will run:\n\n" + cmd)

        if not self.is_sudo_password_cached():
            password_dialog=QInputDialog()
            password, ok = password_dialog.getText(self, "PenGUI", "Password is not cached, so please insert your password:", QLineEdit.Password)
            if not ok:
                QMessageBox.warning(self, "PenGUI", "Password not inserted, operation aborted")
                return
            else:
                self.password=password

        print(cmd)
        cmd = "echo " + self.password + " | sudo -S " + cmd

        process = QProcess()
        process.readyReadStandardError.connect(self.handle_stderr)
        process.start(cmd)
        process.waitForFinished()

        if process.exitStatus() == QProcess.ExitStatus.NormalExit:
            return True
        else:
            QMessageBox.warning(self, "PenGUI", "Error: " + process.errorString())
            return False

    def handle_stderr(self):
        error = self.sender().readAllStandardError().data().decode()
        QMessageBox().warning(self, "Warning", error)

    def is_sudo_password_cached(self):
        cmd="echo " + self.password + " | sudo -S -n true"
        process = QProcess()
        process.readyReadStandardError.connect(self.handle_stderr)
        process.start(cmd)
        process.waitForFinished()
        return process.exitStatus() == QProcess.ExitStatus.NormalExit