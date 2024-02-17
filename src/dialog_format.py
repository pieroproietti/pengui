import sys
from  PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox
import subprocess

class DialogFormat(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Format USB Drive')
        self.layout = QVBoxLayout(self)

        self.label = QLabel('Select USB Drive:')
        self.layout.addWidget(self.label)

        self.usb_drives = self.get_usb_drives()
        self.combo_box = QComboBox(self)
        self.combo_box.addItems(self.usb_drives)
        self.layout.addWidget(self.combo_box)

        self.format_button = QPushButton('Format', self)
        self.format_button.clicked.connect(self.format_drive)
        self.layout.addWidget(self.format_button)

    def get_usb_drives(self):
        drives = subprocess.check_output(['lsblk', '-S', '-d', '-n', '-o', 'NAME,TYPE,TRAN']).decode().split('\n')
        print (drives)
        usb_drives = []
        for drive in drives:
            if 'usb' in drive.lower() and not drive.endswith(')'):
                drive = drive.split()[0]
                usb_drives.append(drive)
        return usb_drives

    def format_drive(self):
        drive = self.combo_box.currentText()
        if drive:
            result = QMessageBox.question(self, 'Confirm', f'Are you sure you want to format {drive}?', QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.Yes:
                subprocess.run(['mkfs.vfat', '-I', drive])
                QMessageBox.information(self, 'Success', f'{drive} has been formatted successfully.')
                self.close()
        else:
            QMessageBox.warning(self, 'Error', 'Please select a USB drive.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogFormat()
    dialog.show()
    sys.exit(app.exec())