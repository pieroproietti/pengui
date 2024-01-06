# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wardrobe_showisKuwf.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_DialogWardrobeShow(object):
    def setupUi(self, DialogWardrobeShow):
        if not DialogWardrobeShow.objectName():
            DialogWardrobeShow.setObjectName(u"DialogWardrobeShow")
        DialogWardrobeShow.resize(640, 480)
        self.buttonBox = QDialogButtonBox(DialogWardrobeShow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.labelCostume = QLabel(DialogWardrobeShow)
        self.labelCostume.setObjectName(u"labelCostume")
        self.labelCostume.setGeometry(QRect(20, 30, 101, 16))
        self.comboBoxCostumes = QComboBox(DialogWardrobeShow)
        self.comboBoxCostumes.setObjectName(u"comboBoxCostumes")
        self.comboBoxCostumes.setGeometry(QRect(150, 30, 461, 24))
        self.pushButtonShow = QPushButton(DialogWardrobeShow)
        self.pushButtonShow.setObjectName(u"pushButtonShow")
        self.pushButtonShow.setGeometry(QRect(470, 100, 131, 71))

        self.retranslateUi(DialogWardrobeShow)
        self.buttonBox.accepted.connect(DialogWardrobeShow.accept)
        self.buttonBox.rejected.connect(DialogWardrobeShow.reject)

        QMetaObject.connectSlotsByName(DialogWardrobeShow)
    # setupUi

    def retranslateUi(self, DialogWardrobeShow):
        DialogWardrobeShow.setWindowTitle(QCoreApplication.translate("DialogWardrobeShow", u"Dialog", None))
        self.labelCostume.setText(QCoreApplication.translate("DialogWardrobeShow", u"costume:", None))
        self.pushButtonShow.setText(QCoreApplication.translate("DialogWardrobeShow", u"Show", None))
    # retranslateUi

