# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'produceeONuyQ.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_DialogProduce(object):
    def setupUi(self, DialogProduce):
        if not DialogProduce.objectName():
            DialogProduce.setObjectName(u"DialogProduce")
        DialogProduce.resize(640, 480)
        self.buttonBox = QDialogButtonBox(DialogProduce)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(DialogProduce)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 360, 81, 16))
        self.lineEditCommand = QLineEdit(DialogProduce)
        self.lineEditCommand.setObjectName(u"lineEditCommand")
        self.lineEditCommand.setGeometry(QRect(110, 360, 411, 23))
        self.pushButtonRun = QPushButton(DialogProduce)
        self.pushButtonRun.setObjectName(u"pushButtonRun")
        self.pushButtonRun.setGeometry(QRect(550, 350, 83, 71))
        self.layoutWidget = QWidget(DialogProduce)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 621, 314))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelAddons = QLabel(self.layoutWidget)
        self.labelAddons.setObjectName(u"labelAddons")

        self.gridLayout.addWidget(self.labelAddons, 0, 0, 1, 1)

        self.labelPrefix = QLabel(self.layoutWidget)
        self.labelPrefix.setObjectName(u"labelPrefix")

        self.gridLayout.addWidget(self.labelPrefix, 1, 0, 1, 1)

        self.lineEditPrefix = QLineEdit(self.layoutWidget)
        self.lineEditPrefix.setObjectName(u"lineEditPrefix")

        self.gridLayout.addWidget(self.lineEditPrefix, 1, 1, 1, 2)

        self.labelBasename = QLabel(self.layoutWidget)
        self.labelBasename.setObjectName(u"labelBasename")

        self.gridLayout.addWidget(self.labelBasename, 2, 0, 1, 1)

        self.lineEditBasename = QLineEdit(self.layoutWidget)
        self.lineEditBasename.setObjectName(u"lineEditBasename")

        self.gridLayout.addWidget(self.lineEditBasename, 2, 1, 1, 2)

        self.labelFilters = QLabel(self.layoutWidget)
        self.labelFilters.setObjectName(u"labelFilters")

        self.gridLayout.addWidget(self.labelFilters, 3, 0, 1, 1)

        self.labelCompression = QLabel(self.layoutWidget)
        self.labelCompression.setObjectName(u"labelCompression")

        self.gridLayout.addWidget(self.labelCompression, 4, 0, 1, 1)

        self.labelTheme = QLabel(self.layoutWidget)
        self.labelTheme.setObjectName(u"labelTheme")

        self.gridLayout.addWidget(self.labelTheme, 5, 0, 1, 1)

        self.comboBoxTheme = QComboBox(self.layoutWidget)
        self.comboBoxTheme.setObjectName(u"comboBoxTheme")

        self.gridLayout.addWidget(self.comboBoxTheme, 5, 1, 1, 2)

        self.checkBoxClone = QCheckBox(self.layoutWidget)
        self.checkBoxClone.setObjectName(u"checkBoxClone")

        self.gridLayout.addWidget(self.checkBoxClone, 6, 0, 1, 1)

        self.checkBoxCryptedClone = QCheckBox(self.layoutWidget)
        self.checkBoxCryptedClone.setObjectName(u"checkBoxCryptedClone")

        self.gridLayout.addWidget(self.checkBoxCryptedClone, 7, 0, 1, 2)

        self.checkBoxScript = QCheckBox(self.layoutWidget)
        self.checkBoxScript.setObjectName(u"checkBoxScript")

        self.gridLayout.addWidget(self.checkBoxScript, 8, 0, 1, 1)

        self.checkBoxUnsecure = QCheckBox(self.layoutWidget)
        self.checkBoxUnsecure.setObjectName(u"checkBoxUnsecure")

        self.gridLayout.addWidget(self.checkBoxUnsecure, 9, 0, 1, 1)

        self.checkBoxUnsecure_2 = QCheckBox(self.layoutWidget)
        self.checkBoxUnsecure_2.setObjectName(u"checkBoxUnsecure_2")

        self.gridLayout.addWidget(self.checkBoxUnsecure_2, 10, 0, 1, 1)

        self.comboBoxAddons = QComboBox(self.layoutWidget)
        self.comboBoxAddons.setObjectName(u"comboBoxAddons")

        self.gridLayout.addWidget(self.comboBoxAddons, 0, 1, 1, 2)

        self.comboBoxFilters = QComboBox(self.layoutWidget)
        self.comboBoxFilters.setObjectName(u"comboBoxFilters")

        self.gridLayout.addWidget(self.comboBoxFilters, 3, 1, 1, 2)

        self.comboBoxCompression = QComboBox(self.layoutWidget)
        self.comboBoxCompression.setObjectName(u"comboBoxCompression")

        self.gridLayout.addWidget(self.comboBoxCompression, 4, 1, 1, 2)


        self.retranslateUi(DialogProduce)
        self.buttonBox.accepted.connect(DialogProduce.accept)
        self.buttonBox.rejected.connect(DialogProduce.reject)

        QMetaObject.connectSlotsByName(DialogProduce)
    # setupUi

    def retranslateUi(self, DialogProduce):
        DialogProduce.setWindowTitle(QCoreApplication.translate("DialogProduce", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogProduce", u"Command", None))
        self.pushButtonRun.setText(QCoreApplication.translate("DialogProduce", u"run/copy", None))
        self.labelAddons.setText(QCoreApplication.translate("DialogProduce", u"Addons", None))
        self.labelPrefix.setText(QCoreApplication.translate("DialogProduce", u"Prefix", None))
        self.labelBasename.setText(QCoreApplication.translate("DialogProduce", u"Basename", None))
        self.labelFilters.setText(QCoreApplication.translate("DialogProduce", u"Filters", None))
        self.labelCompression.setText(QCoreApplication.translate("DialogProduce", u"Compression", None))
        self.labelTheme.setText(QCoreApplication.translate("DialogProduce", u"Theme", None))
        self.checkBoxClone.setText(QCoreApplication.translate("DialogProduce", u"Clone", None))
        self.checkBoxCryptedClone.setText(QCoreApplication.translate("DialogProduce", u"Crypted Clone", None))
        self.checkBoxScript.setText(QCoreApplication.translate("DialogProduce", u"Script", None))
        self.checkBoxUnsecure.setText(QCoreApplication.translate("DialogProduce", u"Unsecure", None))
        self.checkBoxUnsecure_2.setText(QCoreApplication.translate("DialogProduce", u"Yolk", None))
    # retranslateUi

