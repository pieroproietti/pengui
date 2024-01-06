# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wardrobe_showMfhoqk.ui'
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
        self.labelCostumes = QLabel(DialogWardrobeShow)
        self.labelCostumes.setObjectName(u"labelCostumes")
        self.labelCostumes.setGeometry(QRect(20, 30, 101, 16))
        self.comboBoxCostumes = QComboBox(DialogWardrobeShow)
        self.comboBoxCostumes.setObjectName(u"comboBoxCostumes")
        self.comboBoxCostumes.setGeometry(QRect(150, 30, 461, 24))
        self.pushButtonShow = QPushButton(DialogWardrobeShow)
        self.pushButtonShow.setObjectName(u"pushButtonShow")
        self.pushButtonShow.setGeometry(QRect(480, 120, 131, 71))
        self.labelDistro = QLabel(DialogWardrobeShow)
        self.labelDistro.setObjectName(u"labelDistro")
        self.labelDistro.setGeometry(QRect(20, 70, 101, 16))
        self.comboBoxDistros = QComboBox(DialogWardrobeShow)
        self.comboBoxDistros.setObjectName(u"comboBoxDistros")
        self.comboBoxDistros.setGeometry(QRect(150, 70, 461, 24))

        self.retranslateUi(DialogWardrobeShow)
        self.buttonBox.accepted.connect(DialogWardrobeShow.accept)
        self.buttonBox.rejected.connect(DialogWardrobeShow.reject)

        QMetaObject.connectSlotsByName(DialogWardrobeShow)
    # setupUi

    def retranslateUi(self, DialogWardrobeShow):
        DialogWardrobeShow.setWindowTitle(QCoreApplication.translate("DialogWardrobeShow", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.labelCostumes.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Costumes", None))
#endif // QT_CONFIG(tooltip)
        self.labelCostumes.setText(QCoreApplication.translate("DialogWardrobeShow", u"Costumes:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxCostumes.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Select the costume to wear", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButtonShow.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"show costume yaml", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonShow.setText(QCoreApplication.translate("DialogWardrobeShow", u"Show", None))
#if QT_CONFIG(tooltip)
        self.labelDistro.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"distros", None))
#endif // QT_CONFIG(tooltip)
        self.labelDistro.setText(QCoreApplication.translate("DialogWardrobeShow", u"Distros:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxDistros.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"select distribution ", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

