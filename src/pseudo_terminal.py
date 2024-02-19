import subprocess
from PySide6.QtWidgets import (
    QApplication, 
    QDialog, 
    QHBoxLayout, 
    QInputDialog,
    QLineEdit, 
    QMessageBox, 
    QPushButton, 
    QTextEdit, 
    QVBoxLayout
)
from PySide6.QtCore import QProcess
from PySide6.QtGui import QFont, QFontMetrics

class PseudoTerminal(QDialog):
    process = QProcess() # Create a QProcess object to handle the command

    def __init__(self, command_passed, parent=None):
        super().__init__(parent)

        self.setWindowTitle('PenGUI Terminal')

        self.layout = QVBoxLayout(self)

        # Add a QTextEdit widget to display the terminal
        self.terminal = QTextEdit(self)
        font = QFont("Courier")  # Use a fixed-width font
        font.setPointSize(20)  # Adjust the size as needed
        self.terminal.setFont(font)
        self.terminal.setStyleSheet("background-color: blue; color: white;")  # Set the background to black and the text to white
        self.layout.addWidget(self.terminal)
        # Set the size of the widget to fit 80x24 characters
        metrics = QFontMetrics(font)
        self.terminal.setFixedSize(metrics.horizontalAdvance(' ') * 80, metrics.height() * 24)
        self.layout.addWidget(self.terminal)

        ## Add a QLineEdit widget for command_line
        self.command_line=QLineEdit(self)
        self.command_line.setFont(font)
        self.command_line.setStyleSheet("background-color: blue; color: white;")  # Set the background to black and the text to white
        self.command_line.setText(command_passed)
        self.layout.addWidget(self.command_line)

        # add horizontal layout for buttons
        self.button_layout = QHBoxLayout()

        # add button to run the command
        self.run_button = QPushButton('Run', self)
        self.run_button.clicked.connect(self.run_command)
        self.button_layout.addWidget(self.run_button)

        # add button to clear the terminal
        self.clear_button = QPushButton('Clear', self)
        self.clear_button.clicked.connect(self.clear_terminal)
        self.button_layout.addWidget(self.clear_button)

        # add button to remove the sudo password cache
        self.remove_sudo_cached_password_button = QPushButton('Remove cached password', self)
        self.remove_sudo_cached_password_button.clicked.connect(self.remove_sudo_cached_password)
        self.button_layout.addWidget(self.remove_sudo_cached_password_button)

        # add button to close the terminal
        self.close_button = QPushButton('Close', self)
        self.close_button.clicked.connect(self.close)
        self.button_layout.addWidget(self.close_button)
        # add the button layout to the main layout
        self.layout.addLayout(self.button_layout)

        # Create a QProcess object to handle the command
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)

    ## Clear the sudo password cache
    def remove_sudo_cached_password(self):
        subprocess.run(['sudo', '-k'])
          
    ## Check if the sudo password is cached 
    def is_sudo_password_cached(self):
        try:
            subprocess.check_output('sudo -n true', shell=True, stderr=subprocess.STDOUT)
            return True
        except subprocess.CalledProcessError:
            return False
        
    ## Run the command
    def run_command(self):
        command_line = self.command_line.text()
        command_parts = command_line.split()

        # Split the command into the command and its arguments
        if command_parts:
            command = command_parts[0]
            args = command_parts[1:]

        # Richiesta password
        password = "evolution"
        if command == 'sudo':
            # Add the -S flag to the sudo command to read the password from stdin
            args.insert(0, '-S')
            if not self.is_sudo_password_cached():
                password_dialog=QInputDialog()
                password_dialog.setTextValue("evolution")
                password, ok = password_dialog.getText(self, "sudo", "Inserisci la password di sudo:", QLineEdit.Password)
                if not ok:
                    print ("password non inserita")
                    return

        self.process.setProgram(command)
        self.process.setArguments(args)
        self.process.start()
        self.process.write(password.encode())
        self.process.closeWriteChannel()
        self.process.waitForFinished(-1)

        # Show a message box to inform the user that the command has been executed
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Pseudo Terminal")
        msg.setText("Command:\n\n{}\n\nexecuted".format(self.command_line.text()))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    ## Clear the terminal
    def clear_terminal(self):
        self.terminal.clear()
        self.command_line.clear()
        self.command_line.setFocus()

    ## Handle the standard output
    def handle_stdout(self):
        data = self.process.readAllStandardOutput().data().decode()
        self.terminal.append(data)

    ## Handle the standard error
    def handle_stderr(self):
        data = self.process.readAllStandardError().data().decode()
        self.terminal.append(data)

## Run the application
if __name__ == '__main__':
    app = QApplication([])
    pseudo_terminal = PseudoTerminal("sudo ls -l /")
    pseudo_terminal.show()
    app.exec()