import sys
import os

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QApplication, QMessageBox, QDialog
from PySide6.QtGui import QClipboard, QScreen

from utilities import U
from text_editor import TextEditor
from terminal import Terminal

from ui.ui_wardrobe_show import Ui_DialogWardrobeShow

##
#
class WardrobeShow(Ui_DialogWardrobeShow, QDialog):
    path_costumes=os.path.expanduser('~')+"/.wardrobe/costumes"
    path_accessories=os.path.expanduser('~')+"/.wardrobe/accessories"
    path_servers=os.path.expanduser('~')+"/.wardrobe/servers"

    def __init__(self, parent=None):
        super().__init__(parent) # parent
        self.setupUi(self) # mandatory

        if not U.wardrobe_exists():
            QMessageBox.information(self, 'PenGUI', "I will import wardrobe before.\nUse:\n\neggs wardrobe get")
            Terminal.execute(self, 'eggs wardrobe get')
        
        # recupero i costumes da .wardrobe/costumes/
        #self.path_costumes=os.path.expanduser('~')+"/.wardrobe/costumes"

        costumes=[]
        if os.path.exists(self.path_costumes):
            if os.path.exists(self.path_costumes):    
                found_costumes= os.listdir(self.path_costumes)
                costumes=sorted(found_costumes)
        
        # recupero gli accessories da .wardrobe/accessories/
        #self.path_accessories=os.path.expanduser('~')+"/.wardrobe/accessories"

        accessories=[]
        if os.path.exists(self.path_accessories):
            if os.path.exists(self.path_accessories):    
                found_accessories= os.listdir(self.path_accessories)
                accessories=sorted(found_accessories)

        servers=[]
        if os.path.exists(self.path_servers):
            if os.path.exists(self.path_servers):    
                found_servers= os.listdir(self.path_servers)
                servers=sorted(found_servers)

        distros=['arch', 'debian', 'ubuntu']

        self.comboBoxDistros.addItems(distros)
        self.comboBoxDistros.setCurrentIndex(1)

        self.comboBoxCostumes.addItems(costumes)
        self.comboBoxAccessories.addItems(accessories)
        self.comboBoxServers.addItems(servers)

        self.pushButtonShowCostume.clicked.connect(self.costume_show)
        self.pushButtonShowAccessory.clicked.connect(self.accessory_show)
        self.pushButtonShowServer.clicked.connect(self.server_show)

        self.show()

    ##
    @QtCore.Slot()
    def costume_show(self):
        file_path=filename=self.path_costumes + '/' + self.comboBoxCostumes.currentText() + '/'
        file_name=self.comboBoxDistros.currentText()+ '.yml'
        filename=file_path+file_name
        print(filename)
        if os.path.isfile(filename):
            dialog=TextEditor()
            dialog.setWindowTitle("PenGUI")
            dialog.setFilename(filename)
            dialog.openFilename()
            dialog.exec(self)

        else:
            QMessageBox.information(self, 'PenGUI', "There is no version for " + self.comboBoxCostumes.currentText())

    ##
    @QtCore.Slot()
    def accessory_show(self):
        file_path=filename=self.path_accessories + '/' + self.comboBoxAccessories.currentText() + '/'
        file_name=self.comboBoxDistros.currentText()+ '.yml'
        filename=file_path+file_name
        print(filename)
        if os.path.isfile(filename):
            dialog=TextEditor()
            dialog.setWindowTitle("PenGUI")
            dialog.setFilename(filename)
            dialog.openFilename()
            dialog.exec(self)
        else:
            QMessageBox.information(self, 'PenGUI', "There is no version for " + self.comboBoxAccessories.currentText())


    ##
    @QtCore.Slot()
    def server_show(self):
        file_path=filename=self.path_servers + '/' + self.comboBoxServers.currentText() + '/'
        file_name=self.comboBoxDistros.currentText()+ '.yml'
        filename=file_path+file_name
        print(filename)
        if os.path.isfile(filename):
            dialog=TextEditor()
            dialog.setWindowTitle("PenGUI")
            dialog.setFilename(filename)
            dialog.openFilename()
            dialog.exec(self)
        else:
            QMessageBox.information(self, 'PenGUI', "There is no version for " + self.comboBoxAccessories.currentText())
