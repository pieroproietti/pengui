# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wardrobe_showoJbNTS.ui'
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
        self.pushButtonShowCostume = QPushButton(DialogWardrobeShow)
        self.pushButtonShowCostume.setObjectName(u"pushButtonShowCostume")
        self.pushButtonShowCostume.setGeometry(QRect(563, 80, 71, 21))
        self.pushButtonShowAccessory = QPushButton(DialogWardrobeShow)
        self.pushButtonShowAccessory.setObjectName(u"pushButtonShowAccessory")
        self.pushButtonShowAccessory.setGeometry(QRect(563, 120, 61, 31))
        self.labelServers = QLabel(DialogWardrobeShow)
        self.labelServers.setObjectName(u"labelServers")
        self.labelServers.setGeometry(QRect(3, 170, 131, 25))
        self.pushButtonShowServer = QPushButton(DialogWardrobeShow)
        self.pushButtonShowServer.setObjectName(u"pushButtonShowServer")
        self.pushButtonShowServer.setGeometry(QRect(562, 170, 61, 31))
        self.comboBoxServers = QComboBox(DialogWardrobeShow)
        self.comboBoxServers.setObjectName(u"comboBoxServers")
        self.comboBoxServers.setGeometry(QRect(140, 170, 401, 33))
        self.comboBoxAccessories = QComboBox(DialogWardrobeShow)
        self.comboBoxAccessories.setObjectName(u"comboBoxAccessories")
        self.comboBoxAccessories.setGeometry(QRect(141, 120, 401, 33))
        self.labelCostumes = QLabel(DialogWardrobeShow)
        self.labelCostumes.setObjectName(u"labelCostumes")
        self.labelCostumes.setGeometry(QRect(4, 71, 112, 25))
        self.comboBoxDistros = QComboBox(DialogWardrobeShow)
        self.comboBoxDistros.setObjectName(u"comboBoxDistros")
        self.comboBoxDistros.setGeometry(QRect(137, 20, 114, 33))
        self.comboBoxCostumes = QComboBox(DialogWardrobeShow)
        self.comboBoxCostumes.setObjectName(u"comboBoxCostumes")
        self.comboBoxCostumes.setGeometry(QRect(141, 71, 401, 33))
        self.labelAccessories = QLabel(DialogWardrobeShow)
        self.labelAccessories.setObjectName(u"labelAccessories")
        self.labelAccessories.setGeometry(QRect(4, 120, 131, 25))
        self.labelDistro = QLabel(DialogWardrobeShow)
        self.labelDistro.setObjectName(u"labelDistro")
        self.labelDistro.setGeometry(QRect(0, 20, 81, 25))

        self.retranslateUi(DialogWardrobeShow)
        self.buttonBox.accepted.connect(DialogWardrobeShow.accept)
        self.buttonBox.rejected.connect(DialogWardrobeShow.reject)

        QMetaObject.connectSlotsByName(DialogWardrobeShow)
    # setupUi

    def retranslateUi(self, DialogWardrobeShow):
        DialogWardrobeShow.setWindowTitle(QCoreApplication.translate("DialogWardrobeShow", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.pushButtonShowCostume.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"show selected costume", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonShowCostume.setText(QCoreApplication.translate("DialogWardrobeShow", u"Show", None))
#if QT_CONFIG(tooltip)
        self.pushButtonShowAccessory.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"show selected accessory", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonShowAccessory.setText(QCoreApplication.translate("DialogWardrobeShow", u"Show", None))
#if QT_CONFIG(tooltip)
        self.labelServers.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Servers", None))
#endif // QT_CONFIG(tooltip)
        self.labelServers.setText(QCoreApplication.translate("DialogWardrobeShow", u"Servers", None))
#if QT_CONFIG(tooltip)
        self.pushButtonShowServer.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"show selected server", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonShowServer.setText(QCoreApplication.translate("DialogWardrobeShow", u"Show", None))
#if QT_CONFIG(tooltip)
        self.comboBoxServers.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Select server to show", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.comboBoxAccessories.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Select accessory to show", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelCostumes.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Costumes", None))
#endif // QT_CONFIG(tooltip)
        self.labelCostumes.setText(QCoreApplication.translate("DialogWardrobeShow", u"Costumes:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxDistros.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"select distribution ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.comboBoxCostumes.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Select the costume to wear", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelAccessories.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Accessories: applied to costumes ", None))
#endif // QT_CONFIG(tooltip)
        self.labelAccessories.setText(QCoreApplication.translate("DialogWardrobeShow", u"Accessories:", None))
#if QT_CONFIG(tooltip)
        self.labelDistro.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"distros", None))
#endif // QT_CONFIG(tooltip)
        self.labelDistro.setText(QCoreApplication.translate("DialogWardrobeShow", u"Distros:", None))
    # retranslateUi

