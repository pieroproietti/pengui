# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wardrobe_showmDLAjH.ui'
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
    QDialogButtonBox, QFormLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

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
        self.pushButtonShowCostume.setGeometry(QRect(100, 250, 261, 71))
        self.pushButtonShowAccessory = QPushButton(DialogWardrobeShow)
        self.pushButtonShowAccessory.setObjectName(u"pushButtonShowAccessory")
        self.pushButtonShowAccessory.setGeometry(QRect(370, 250, 261, 71))
        self.layoutWidget = QWidget(DialogWardrobeShow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 30, 621, 181))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelCostumes = QLabel(self.layoutWidget)
        self.labelCostumes.setObjectName(u"labelCostumes")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelCostumes)

        self.comboBoxCostumes = QComboBox(self.layoutWidget)
        self.comboBoxCostumes.setObjectName(u"comboBoxCostumes")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBoxCostumes)

        self.labelAccessories = QLabel(self.layoutWidget)
        self.labelAccessories.setObjectName(u"labelAccessories")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelAccessories)

        self.comboBoxAccessories = QComboBox(self.layoutWidget)
        self.comboBoxAccessories.setObjectName(u"comboBoxAccessories")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBoxAccessories)

        self.labelDistro = QLabel(self.layoutWidget)
        self.labelDistro.setObjectName(u"labelDistro")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelDistro)

        self.comboBoxDistros = QComboBox(self.layoutWidget)
        self.comboBoxDistros.setObjectName(u"comboBoxDistros")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxDistros)


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
        self.pushButtonShowCostume.setText(QCoreApplication.translate("DialogWardrobeShow", u"&Costume", None))
#if QT_CONFIG(tooltip)
        self.pushButtonShowAccessory.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"show selected accessory", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonShowAccessory.setText(QCoreApplication.translate("DialogWardrobeShow", u"&Accessory", None))
#if QT_CONFIG(tooltip)
        self.labelCostumes.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Costumes", None))
#endif // QT_CONFIG(tooltip)
        self.labelCostumes.setText(QCoreApplication.translate("DialogWardrobeShow", u"Costumes:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxCostumes.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Select the costume to wear", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelAccessories.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Accessories: applied to costumes ", None))
#endif // QT_CONFIG(tooltip)
        self.labelAccessories.setText(QCoreApplication.translate("DialogWardrobeShow", u"Accessories:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxAccessories.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Select the accessories to wear", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelDistro.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"distros", None))
#endif // QT_CONFIG(tooltip)
        self.labelDistro.setText(QCoreApplication.translate("DialogWardrobeShow", u"Distros:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxDistros.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"select distribution ", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

