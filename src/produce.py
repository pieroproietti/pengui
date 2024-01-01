import sys
import os
import yaml

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QApplication, QMessageBox
from PySide6.QtGui import QClipboard

from ui.ui_produce import Ui_DialogProduce
from terminal import Terminal
from utilies import U


##
#
class Produce(QtWidgets.QWidget, Ui_DialogProduce):
    def __init__ (self):
        super().__init__()
        self.setupUi(self) # mandatory

        self.setWindowTitle = "Produce"

        QApplication.clipboard().dataChanged.connect(self.onClipboardChanged)

        # load eggs.yaml 
        if not U.conf_exists():
            msgBox = QMessageBox(self)
            msgBox.setText("Can't find /etc/penguins-eggs.d/eggs.yaml")
            msgBox.exec()
            quit()

        with open(U.conf_path+'/eggs.yaml', 'r') as file:
            eggs = yaml.safe_load(file)

        self.lineEditPrefix.setText(eggs['snapshot_prefix'])
        self.lineEditBasename.setText(eggs['snapshot_basename'])
        self.comboBoxAddons.addItems(['', 'adapt', 'ichoice', 'pve', 'rsupport'])
        self.comboBoxFilters.addItems(['', 'custom', 'homes', 'usr'])
        self.comboBoxCompression.addItems(['fast', 'standard', 'max'])

        # disable and fill basename and prefix
        self.lineEditBasename.setEnabled(False)
        self.lineEditPrefix.setEnabled(False)

        # checkox connect
        self.checkBoxBasename.stateChanged.connect(self.basename)
        self.checkBoxPrefix.stateChanged.connect(self.prefix)
        self.checkBoxClone.stateChanged.connect(self.clone)
        self.checkBoxCryptedClone.stateChanged.connect(self.crypted_clone)
        self.checkBoxScript.stateChanged.connect(self.script)
        self.checkBoxUnsecure.stateChanged.connect(self.unsecure)

        # buttons connect
        self.pushButtonGenerate.clicked.connect(self.generate)
        self.pushButtonRun.clicked.connect(self.run)

        # recupero i themi da .wardrobe/vendors/
        if os.geteuid() == 0:
            path_themes='/home/' + os.getenv('SUDO_USER')
        else:
            path_themes='/home/' + os.getenv('USER') + '/.wardrobe'

        if os.path.exists(path_themes):
            found_themes= os.listdir(path_themes +'/vendors/')
            sorted_themes=sorted(found_themes)
        else:
            sorted_themes=[]
        
        themes=['eggs']
        themes.extend(sorted_themes)

        self.comboBoxTheme.addItems(themes)

        self.show()

    def onClipboardChanged(self):
        text = QApplication.clipboard().text()


    def generate(self):
        command='sudo eggs produce'
        if (self.comboBoxAddons.currentText() !=''):
            command += ' --addons ' + self.comboBoxAddons.currentText()

        if self.checkBoxPrefix.isChecked():
            command += ' --prefix ' + self.lineEditPrefix.text()

        if self.checkBoxBasename.isChecked():
            command += ' --basename ' + self.lineEditBasename.text()

        if (self.comboBoxFilters.currentText() !=''):
            command += ' --filters ' + self.comboBoxFilters.currentText()

        if (self.comboBoxCompression.currentText() !=''):
            if (self.comboBoxCompression.currentText() !='fast'):
                command += ' --'+ self.comboBoxCompression.currentText()

        if (self.comboBoxTheme.currentText() !=''):
            if (self.comboBoxTheme.currentText() !='eggs'):
                command += ' --theme ' + self.comboBoxTheme.currentText()

        if self.checkBoxClone.isChecked():
            command += ' --clone'

        if self.checkBoxCryptedClone.isChecked():
            command += ' --cryptedclone'

        if self.checkBoxCryptedClone.isChecked():
            command += ' --cryptedclone'

        if self.checkBoxScript.isChecked():
            command += ' --script'

        if self.checkBoxUnsecure.isChecked():
            command += ' --unsecure'

        if self.checkBoxYolk.isChecked():
            command += ' --yolk'

        self.lineEditCommand.setText(command)

    ##
    def run(self):
        command=self.lineEditCommand.text()
        if os.geteuid() != 0:
            QApplication.clipboard().setText(command)
            msgBox = QMessageBox(self)
            msgBox.setText("command was copied on your clipboard")
            msgBox.exec()
        else:
            Terminal.execute(self, command)            

    ##
    #
    def basename(self):
        if self.checkBoxBasename.isChecked():
            self.lineEditBasename.setEnabled(True)
        else:
            self.lineEditBasename.setEnabled(False)

    ##
    #
    def prefix(self):
        if self.checkBoxPrefix.isChecked():
            self.lineEditPrefix.setEnabled(True)
        else:
            self.lineEditPrefix.setEnabled(False)


    ##
    # azzerra cryptedClone, script e setta unsecure
    def clone(self):
        if self.checkBoxClone.isChecked():
            self.checkBoxCryptedClone.setChecked(False)
            self.checkBoxScript.setChecked(False)
            

    ##
    # azzerra clone, script e setta unsecure
    def crypted_clone(self):
        if self.checkBoxCryptedClone.isChecked():
            self.checkBoxClone.setChecked(False)
            self.checkBoxScript.setChecked(False)

    ##
    # azzerra clone e cryptedClone
    def script(self):
        if self.checkBoxScript.isChecked():
            self.checkBoxClone.setChecked(False)
            self.checkBoxCryptedClone.setChecked(False)

    ##
    # azzerra clone e cryptedClone
    def unsecure(self):
        if not self.checkBoxUnsecure.isChecked():
            self.checkBoxClone.setChecked(False)
            self.checkBoxCryptedClone.setChecked(False)

    ##
    #
    @QtCore.Slot()
    def accept(self):
        self.close()

    ##
    #
    @QtCore.Slot()
    def reject(self):
        self.close()



##
# development
if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = Produce() # ricorda ()

    sys.exit(app.exec()) # ricorda ()