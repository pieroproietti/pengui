import sys
import os
import yaml

import webbrowser


from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMessageBox, QDialog, QDialogButtonBox

from ui.ui_produce import Ui_DialogProduce
from utilities import U
from peasy import Peasy

##
#
class Produce(Ui_DialogProduce, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent) # parent
        self.setupUi(self) # mandatory

        QApplication.clipboard().dataChanged.connect(self.onClipboardChanged)

        # load eggs.yaml 
        if not U.conf_exists():
            QMessageBox.critical(self, 'Error', f"Can't find {U.conf_path}")
            quit()

        with open(U.conf_path+'/eggs.yaml', 'r') as file:
            eggs = yaml.safe_load(file)

        self.lineEditPrefix.setText(eggs['snapshot_prefix'])
        self.lineEditBasename.setText(eggs['snapshot_basename'])
        self.comboBoxAddons.addItems(['', 'adapt', 'ichoice', 'pve', 'rsupport'])
        links = ['']
        filesDesktop= os.listdir('/usr/share/applications/')
        links = links + [file[:-8] for file in filesDesktop if file.endswith('.desktop')]
        self.comboBoxLinks.addItems(links)
        self.comboBoxCompression.addItems(['','pendrive', 'max'])

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
        self.checkBoxExcludesStatic.stateChanged.connect(self.static)

        # recupero i temi da .wardrobe/vendors/
        if os.geteuid() == 0:
            path_themes='/home/' + os.getenv('SUDO_USER')
        else:
            path_themes='/home/' + os.getenv('USER') + '/.wardrobe'

        sorted_themes=[]
        if os.path.exists(path_themes):
            path_vendors=path_themes+'/vendors'
            if os.path.exists(path_vendors):    
                found_themes= os.listdir(path_vendors)
                sorted_themes=sorted(found_themes)
        
        themes=['eggs']
        themes.extend(sorted_themes)
        self.comboBoxTheme.addItems(themes)

        # buttonBox connect
        self.buttonBox.helpRequested.connect(self.help)
        self.buttonBox.rejected.connect(self.close_me)
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.generate)
        self.buttonBox.accepted.connect(self.run)

    
    ##
    #    
    def onClipboardChanged(self):
        text = QApplication.clipboard().text()


    ##
    #    
    def generate(self):
        command='sudo eggs produce'
        if self.comboBoxAddons.currentText() !='':
            command += ' --addons ' + self.comboBoxAddons.currentText()

        if self.checkBoxPrefix.isChecked():
            command += ' --prefix ' + self.lineEditPrefix.text()

        if self.checkBoxBasename.isChecked():
            command += ' --basename ' + self.lineEditBasename.text()

        excludes_applied=''
        if self.checkBoxExcludesStatic.isChecked():
            excludes_applied+= "static "

        if self.checkBoxExcludesMine.isChecked():
            excludes_applied+= "mine "

        if self.checkBoxExcludesHome.isChecked():
            excludes_applied+= "home "

        if self.checkBoxExcludesUsr.isChecked():
            excludes_applied+= "usr "

        if self.checkBoxExcludesVar.isChecked():
            excludes_applied+= "var "

        if excludes_applied!="":
            command += ' --excludes ' + excludes_applied

        if self.comboBoxLinks.currentText() !='':
            command += ' --links ' + self.comboBoxLinks.currentText()

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

        if self.checkBoxScript.isChecked():
            command += ' --script'

        if self.checkBoxUnsecure.isChecked():
            command += ' --unsecure'

        if self.checkBoxYolk.isChecked():
            command += ' --yolk'

        self.lineEditCommand.setText(command)

    ##
    #    
    def run(self):
        self.generate()
        command=self.lineEditCommand.text()
        if command.strip() != '':
            Peasy().run(command)
        else:
            QMessageBox.critical(self, 'Error', 'No command to run')

    ##
    #    
    def help(self):
        webbrowser.open('https://github.com/pieroproietti/penguins-eggs#eggs-produce')

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

    def static(self):
        if self.checkBoxExcludesStatic.isChecked():
            self.checkBoxExcludesHome.setChecked(False)
            self.checkBoxExcludesMine.setChecked(False)
            self.checkBoxExcludesUsr.setChecked(False)
            self.checkBoxExcludesVar.setChecked(False)

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
    def close_me(self):
        self.close()
