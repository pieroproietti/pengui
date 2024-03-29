from PySide6.QtWidgets import QApplication, QProgressDialog
from PySide6.QtCore import QProcess, Signal, Slot, Qt
import sys

class DialogGetEggs(QProgressDialog):
    download_started = Signal()
    download_finished = Signal()

    def __init__(self, url, destination):
        super().__init__()

        self.setWindowTitle("Download in progress")
        self.setLabelText("Downloading eggs_9.6.30_amd64.deb from SourceForge...")
        self.setRange(0, 100)
        self.setAutoClose(True)

        self.process = QProcess()
        self.process.setProgram("wget")
        self.process.setArguments(["--progress=dot", url, "-O", destination])
        self.process.readyReadStandardError.connect(self.handle_stderr)

        self.download_started.connect(self.process.start)
        self.download_finished.connect(self.close)

    def handle_stderr(self):
        data = self.process.readAllStandardError().data().decode()
        if "%" in data:
            progress = int(data.split('%')[0].split()[-1])
            self.setValue(progress)

    def start_download(self):
        self.download_started.emit()

    def finish_download(self):
        self.download_finished.emit()

    def close(self):
        self.process.close()
        super().close()


# Example usage
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = DialogGetEggs("https://sourceforge.net/projects/penguins-eggs/files/DEBS/eggs_9.6.30_amd64.deb", "/tmp/eggs_9.6.30_amd64.deb")
    dialog.show()
    dialog.start_download()
    dialog.download_started.connect(dialog.show)
    dialog.download_finished.connect(dialog.close)
    sys.exit(app.exec())