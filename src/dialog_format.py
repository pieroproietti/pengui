import sys
import psutil
from  PySide6.QtCore import QCoreApplication, QProcess, QThread, Signal
from PySide6.QtWidgets import (
    QApplication, 
    QDialog, 
    QHBoxLayout, 
    QVBoxLayout, 
    QLabel, 
    QComboBox, 
    QPushButton, 
    QMessageBox, 
    QInputDialog, 
    QLineEdit, 
    QProgressBar
)

##
#
class FormatThread(QThread):
    format_done = Signal(int, str)

    def __init__(self, drive, partition_label, password):
        super().__init__()
        self.drive = drive
        self.partition_label = partition_label
        self.password = password


    def run(self):
        print ("formatting device:{} label: {} ".format(self.drive, self.partition_label))
        format_process = QProcess()
        format_process.setProgram("sudo")
        format_process.setArguments(["-S", "mkfs.vfat", "-F", "32", "-n", self.partition_label, self.drive])
        format_process.start()
        format_process.write(self.password.encode())
        format_process.closeWriteChannel()
        format_process.waitForFinished(-1)
        format_stdout = format_process.readAllStandardOutput()
        format_stderr = format_process.readAllStandardError()

        self.format_done.emit(format_process.exitCode(), format_stderr)


class DialogFormat(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Format USB Drive')
        self.layout = QVBoxLayout(self)

        self.label = QLabel('Select USB drive to format:')
        self.layout.addWidget(self.label)

        self.usb_drives = self.get_usb_drives()
        self.combo_box = QComboBox(self)
        self.combo_box.addItems(self.usb_drives)
        self.layout.addWidget(self.combo_box)

        self.usb_partition_label  = QLineEdit(self)
        self.usb_partition_label.setPlaceholderText("insert partition label")
        self.layout.addWidget(self.usb_partition_label)

        # add button_layout to the main layout
        button_layout = QHBoxLayout()

        self.format_button = QPushButton('Format', self)
        self.format_button.clicked.connect(self.format_drive)
        button_layout.addWidget(self.format_button)

        # add button to close the dialog
        self.close_button = QPushButton('Close', self)
        self.close_button.clicked.connect(self.close)
        button_layout.addWidget(self.close_button)

        self.layout.addLayout(button_layout)
        
        self.progress_bar = QProgressBar(self)
        self.layout.addWidget(self.progress_bar)

    ##
    # fine della formattazione    
    def on_format_done(self, exit_code, stderr):
        self.progress_bar.setRange(0, 1)  # Set the progress bar back to determinate mode
        self.close_button.setEnabled(True)
        self.format_button.setEnabled(True)
        if exit_code == 0:
            QMessageBox.information(self, "Success", "Disk was formatted successfully.")
        else:
            QMessageBox.critical(self, "Errore", f"Si è verificato un errore durante la formattazione del dispositivo:\n{stderr}")

    ##
    #
    def get_usb_drives(self):
        process = QProcess()
        process.start("lsblk", ["-S", "-d", "-n", "-o", "NAME,TYPE,TRAN"])
        process.waitForFinished(-1) # Wait until the process finishes
        output = process.readAllStandardOutput().data().decode()
        drives = output.split('\n')
        print(drives)
        #drives = subprocess.check_output(['lsblk', '-S', '-d', '-n', '-o', 'NAME,TYPE,TRAN']).decode().split('\n')
        usb_drives = []
        for drive in drives:
            if 'usb' in drive.lower() and not drive.endswith(')'):
                drive = drive.split()[0]
                usb_drives.append(drive)

        print(usb_drives)

        return usb_drives

    ##
    #
    def format_drive(self):
        self.close_button.setEnabled(False)
        self.format_button.setEnabled(False)
        drive = self.combo_box.currentText()
        if drive:
            drive='/dev/' + drive
            print("format_drive {}".format(drive))
            result = QMessageBox.question(self, 'Confirm', f'Are you sure you want to format {drive}?', QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.Yes:
                # Richiede la password di sudo dall'utente
                password_dialog=QInputDialog()
                password_dialog.setTextValue("evolution")
                password, ok = password_dialog.getText(self, "Password di sudo", "Inserisci la password di sudo:", QLineEdit.Password)
                if not ok:
                    print ("password non inserita")
                    return
                else:
                    print ("password {}".format(password))
            

        if is_device_mounted(drive): 
            print("umount {}".format(drive))
            umount_process = QProcess()
            umount_process.setProgram("sudo")
            umount_process.setArguments(["-S", "umount", drive])
            umount_process.start()
            umount_process.write(password.encode())
            umount_process.closeWriteChannel()
            umount_process.waitForFinished(-1)
            umount_stdout = umount_process.readAllStandardOutput()
            umount_stderr = umount_process.readAllStandardError()

            # Controlla se lo smontaggio ha avuto successo
            if umount_process.exitCode() != 0:
                QMessageBox.critical(self, "Errore", f"Si è verificato un errore durante lo smontaggio del dispositivo:\n{umount_stderr}")
                return

        # Avvia il thread di formattazione
        self.format_thread = FormatThread(drive, self.usb_partition_label.text(), password)
        self.format_thread.format_done.connect(self.on_format_done)
        self.format_thread.start()
        self.progress_bar.setRange(0, 0)  # Set the progress bar to indeterminate mode

##
#
def is_device_mounted(device_path):
    partitions = psutil.disk_partitions(all=True)
    for partition in partitions:
        if partition.device == device_path:
            return True
    return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogFormat()
    dialog.show()
    sys.exit(app.exec())

