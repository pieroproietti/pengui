from PySide6 import QtCore
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QApplication, QMessageBox, QDialog
from PySide6.QtGui import QClipboard

from ui.ui_text_editor import Ui_DialogTextEditor
from terminal import Terminal
from utilies import U


##
#
class TextEditor(Ui_DialogTextEditor, QDialog):

    filename=''

    def __init__(self, parent=None):
        super().__init__(parent) # parent
        self.setupUi(self) # mandatory

    #
    def setFilename(self, filename=""):
        self.filename=filename

    def open(self):
        if self.filename!='':
            f = open(self.filename, 'r')
            with f:
                data = f.read()
                self.plainTextEdit.setPlainText(data)
