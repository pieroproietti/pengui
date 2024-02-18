from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QLineEdit, QTextEdit, QInputDialog
from PySide6.QtCore import QProcess
from PySide6.QtGui import QFont, QFontMetrics

## Terminal class
class Terminal(QDialog):

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

    ## Run the command
    def run_command(self):
        command_line = self.command_line.text()
        command_parts = command_line.split()

        # Split the command into the command and its arguments
        if command_parts:
            command = command_parts[0]
            args = command_parts[1:]

        print("command: ", command)
        print("args: ", args)

        # Start the process
        self.process.start(command, args)

        # Richiede la password di sudo dall'utente
        if command == 'sudo':
            password, ok = QInputDialog.getText(self, "Password di sudo", "Inserisci la password di sudo:", QLineEdit.Password)
            if ok:
                print("password: ", password)
                self.process.write(password.encode() + b'\n')
                #self.process.write(password.encode() + b'\n')


    ## Clear the terminal
    def clear_terminal(self):
        self.terminal.clear()
        self.command_line.clear()

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
    terminal = Terminal("ls -l /")
    terminal.show()
    app.exec()