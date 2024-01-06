import sys
import os

from PySide6 import QtCore
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QApplication, QMessageBox, QDialog
from PySide6.QtGui import QClipboard

from utilies import U
from text_editor import TextEditor

from ui.ui_wardrobe_show import Ui_DialogWardrobeShow

##
#
class WardrobeShow(Ui_DialogWardrobeShow, QDialog):
    path_costumes=os.path.expanduser('~')+"/.wardrobe/costumes"

    def __init__(self, parent=None):
        super().__init__(parent) # parent
        self.setupUi(self) # mandatory

        if not U.wardrobe_exists():
            msgBox = QMessageBox(self)
            msgBox.setText("Import wardrobe before.\nUse:\n\neggs wardrobe get\n")
            msgBox.exec()
            sys.exit()
        
        # recupero i costumes da .wardrobe/costumes/
        self.path_costumes=os.path.expanduser('~')+"/.wardrobe/costumes"

        sorted_costumes=[]
        if os.path.exists(self.path_costumes):
            if os.path.exists(self.path_costumes):    
                found_costumes= os.listdir(self.path_costumes)
                sorted_costumes=sorted(found_costumes)
        
        costumes=[]
        costumes.extend(sorted_costumes)

        self.comboBoxCostumes.addItems(costumes)
        distros=['arch', 'debian', 'ubuntu']
        self.comboBoxDistros.addItems(distros)
        self.pushButtonShow.clicked.connect(self.costume_show)


    ##
    @QtCore.Slot()
    def costume_show(self):
        file_path=filename=self.path_costumes + '/' + self.comboBoxCostumes.currentText() + '/'
        file_name=self.comboBoxDistros.currentText()+ '.yml'
        filename=file_path+file_name
        print(filename)
        if os.path.isfile(filename):
            dialog=TextEditor()
            dialog.setWindowTitle(filename)
            dialog.setFilename(filename)
            dialog.openFilename()
            dialog.exec()
        else:
            msgBox = QMessageBox(self)
            msgBox.setText("There is no version for " + self.comboBoxCostumes.currentText())
            msgBox.exec()