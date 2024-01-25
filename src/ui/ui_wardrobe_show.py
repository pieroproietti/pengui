# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wardrobe_showXipRET.ui'
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
    QVBoxLayout, QWidget)

class Ui_DialogWardrobeShow(object):
    def setupUi(self, DialogWardrobeShow):
        if not DialogWardrobeShow.objectName():
            DialogWardrobeShow.setObjectName(u"DialogWardrobeShow")
        DialogWardrobeShow.resize(1024, 300)
        self.buttonBox = QDialogButtonBox(DialogWardrobeShow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 230, 991, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.labelServers = QLabel(DialogWardrobeShow)
        self.labelServers.setObjectName(u"labelServers")
        self.labelServers.setGeometry(QRect(3, 170, 131, 25))
        self.labelCostumes = QLabel(DialogWardrobeShow)
        self.labelCostumes.setObjectName(u"labelCostumes")
        self.labelCostumes.setGeometry(QRect(4, 71, 112, 25))
        self.comboBoxDistros = QComboBox(DialogWardrobeShow)
        self.comboBoxDistros.setObjectName(u"comboBoxDistros")
        self.comboBoxDistros.setGeometry(QRect(137, 20, 771, 33))
        self.labelAccessories = QLabel(DialogWardrobeShow)
        self.labelAccessories.setObjectName(u"labelAccessories")
        self.labelAccessories.setGeometry(QRect(4, 120, 131, 25))
        self.labelDistro = QLabel(DialogWardrobeShow)
        self.labelDistro.setObjectName(u"labelDistro")
        self.labelDistro.setGeometry(QRect(0, 20, 81, 25))
        self.widget = QWidget(DialogWardrobeShow)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(140, 71, 771, 113))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBoxCostumes = QComboBox(self.widget)
        self.comboBoxCostumes.setObjectName(u"comboBoxCostumes")

        self.verticalLayout_2.addWidget(self.comboBoxCostumes)

        self.comboBoxAccessories = QComboBox(self.widget)
        self.comboBoxAccessories.setObjectName(u"comboBoxAccessories")

        self.verticalLayout_2.addWidget(self.comboBoxAccessories)

        self.comboBoxServers = QComboBox(self.widget)
        self.comboBoxServers.setObjectName(u"comboBoxServers")

        self.verticalLayout_2.addWidget(self.comboBoxServers)

        self.widget1 = QWidget(DialogWardrobeShow)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(930, 70, 84, 115))
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButtonShowCostume = QPushButton(self.widget1)
        self.pushButtonShowCostume.setObjectName(u"pushButtonShowCostume")

        self.verticalLayout_3.addWidget(self.pushButtonShowCostume)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButtonShowAccessory = QPushButton(self.widget1)
        self.pushButtonShowAccessory.setObjectName(u"pushButtonShowAccessory")

        self.verticalLayout.addWidget(self.pushButtonShowAccessory)

        self.pushButtonShowServer = QPushButton(self.widget1)
        self.pushButtonShowServer.setObjectName(u"pushButtonShowServer")

        self.verticalLayout.addWidget(self.pushButtonShowServer)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(DialogWardrobeShow)
        self.buttonBox.accepted.connect(DialogWardrobeShow.accept)
        self.buttonBox.rejected.connect(DialogWardrobeShow.reject)

        QMetaObject.connectSlotsByName(DialogWardrobeShow)
    # setupUi

    def retranslateUi(self, DialogWardrobeShow):
        DialogWardrobeShow.setWindowTitle(QCoreApplication.translate("DialogWardrobeShow", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.labelServers.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Servers", None))
#endif // QT_CONFIG(tooltip)
        self.labelServers.setText(QCoreApplication.translate("DialogWardrobeShow", u"Servers", None))
#if QT_CONFIG(tooltip)
        self.labelCostumes.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Costumes", None))
#endif // QT_CONFIG(tooltip)
        self.labelCostumes.setText(QCoreApplication.translate("DialogWardrobeShow", u"Costumes:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxDistros.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"select distribution ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelAccessories.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Accessories: applied to costumes ", None))
#endif // QT_CONFIG(tooltip)
        self.labelAccessories.setText(QCoreApplication.translate("DialogWardrobeShow", u"Accessories:", None))
#if QT_CONFIG(tooltip)
        self.labelDistro.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"distros", None))
#endif // QT_CONFIG(tooltip)
        self.labelDistro.setText(QCoreApplication.translate("DialogWardrobeShow", u"Distros:", None))
#if QT_CONFIG(tooltip)
        self.comboBoxCostumes.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Select the costume to wear", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.comboBoxAccessories.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Select accessory to show", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.comboBoxServers.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"Select server to show", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButtonShowCostume.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"show selected costume", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonShowCostume.setText(QCoreApplication.translate("DialogWardrobeShow", u"Show", None))
#if QT_CONFIG(tooltip)
        self.pushButtonShowAccessory.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"show selected accessory", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonShowAccessory.setText(QCoreApplication.translate("DialogWardrobeShow", u"Show", None))
#if QT_CONFIG(tooltip)
        self.pushButtonShowServer.setToolTip(QCoreApplication.translate("DialogWardrobeShow", u"show selected server", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonShowServer.setText(QCoreApplication.translate("DialogWardrobeShow", u"Show", None))
    # retranslateUi

