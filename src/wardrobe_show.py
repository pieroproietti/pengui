import sys
import os
import yaml

import webbrowser

from PySide6 import QtCore
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QApplication, QMessageBox, QDialog
from PySide6.QtGui import QClipboard

from ui.ui_wardrobe_show import Ui_DialogWardrobeShow
from terminal import Terminal
from utilies import U


##
#
class WardrobeShow(Ui_DialogWardrobeShow, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent) # parent
        self.setupUi(self) # mandatory

        if not U.wardrobe_exists():
            msgBox = QMessageBox(self)
            msgBox.setText(".wardrobe does not exist in your home, use: eggs wardrobe get")
            msgBox.exec()
            return
        
        # recupero i costumes da .wardrobe/costumes/
        path_costumes=os.path.expanduser('~')+"/.wardrobe/costumes"

        sorted_costumes=[]
        if os.path.exists(path_costumes):
            if os.path.exists(path_costumes):    
                found_costumes= os.listdir(path_costumes)
                sorted_costumes=sorted(found_costumes)
        
        costumes=[]
        costumes.extend(sorted_costumes)

        self.comboBoxCostumes.addItems(costumes)
        self.pushButtonShow.clicked.connect(self.show)


    ##
    #    
    def show(self):
        Terminal.execute(self, 'eggs wardrobe show ' + self.comboBoxCostumes.currentText())




