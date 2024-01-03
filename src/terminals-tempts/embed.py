# https://stackoverflow.com/questions/66076839/embedding-gnome-terminal-in-qwidget
import os
import re
import shutil
import subprocess
import sys
import time
from PySide6.QtCore import QProcess, Qt
from PySide6.QtGui import QWindow
from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QApplication


class Window(QWidget):
    def __init__(self, program, arguments):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.external = QProcess(self)
        self.external.start(program, arguments)
        time.sleep(1)
        p = subprocess.run(['xprop', '-root'], stdout=subprocess.PIPE)
        for line in p.stdout.decode().splitlines():
            m = re.fullmatch(r'^_NET_ACTIVE_WINDOW.*[)].*window id # (0x[0-9a-f]+)', line)
            if m:
                win = QWindow.fromWinId(int(m.group(1), 16))
                win.setFlag(Qt.ForeignWindow, True)
                win.setFlag(Qt.FramelessWindowHint, True)
                win.setFlag(Qt.BypassGraphicsProxyWidget, True)
                wid = QWidget.createWindowContainer(win, self, Qt.FramelessWindowHint)
                self.layout().addWidget(wid)

                # this is where the magic happens...
                self.external.finished.connect(self.close_maybe)
                break
        else:
            QMessageBox.warning(self, 'Error',  'Could not find WID for curreent Window')

    def close_maybe(self):
        pass

    def closeEvent(self, event):
        self.external.terminate()
        self.external.waitForFinished(1000)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        if shutil.which(sys.argv[1]):
            app = QApplication(sys.argv)
            window = Window(sys.argv[1], sys.argv[2:])
            window.setGeometry(100, 100, 800, 600)
            window.show()
            sys.exit(app.exec_())
        else:
            print('could not find program: %r' % sys.argv[1])
    else:
        print('usage: python %s <external-program-name> [args]' %
              os.path.basename(__file__))
