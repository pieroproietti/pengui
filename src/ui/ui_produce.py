# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'produceaLaqSJ.ui'
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
import resources_rc

class Ui_DialogProduce(object):
    def setupUi(self, DialogProduce):
        if not DialogProduce.objectName():
            DialogProduce.setObjectName(u"DialogProduce")
        DialogProduce.resize(640, 480)
        DialogProduce.setMinimumSize(QSize(640, 480))
        DialogProduce.setMaximumSize(QSize(640, 480))
        icon = QIcon()
        icon.addFile(u":/eggs/icons/eggs.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogProduce.setWindowIcon(icon)
        DialogProduce.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
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
        self.pushButtonGenerate = QPushButton(DialogProduce)
        self.pushButtonGenerate.setObjectName(u"pushButtonGenerate")
        self.pushButtonGenerate.setGeometry(QRect(110, 390, 431, 31))
        self.widget = QWidget(DialogProduce)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 21, 591, 314))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelAddons = QLabel(self.widget)
        self.labelAddons.setObjectName(u"labelAddons")

        self.gridLayout.addWidget(self.labelAddons, 0, 0, 1, 1)

        self.comboBoxAddons = QComboBox(self.widget)
        self.comboBoxAddons.setObjectName(u"comboBoxAddons")

        self.gridLayout.addWidget(self.comboBoxAddons, 0, 1, 1, 1)

        self.checkBoxPrefix = QCheckBox(self.widget)
        self.checkBoxPrefix.setObjectName(u"checkBoxPrefix")

        self.gridLayout.addWidget(self.checkBoxPrefix, 1, 0, 1, 1)

        self.lineEditPrefix = QLineEdit(self.widget)
        self.lineEditPrefix.setObjectName(u"lineEditPrefix")

        self.gridLayout.addWidget(self.lineEditPrefix, 1, 1, 1, 1)

        self.checkBoxBasename = QCheckBox(self.widget)
        self.checkBoxBasename.setObjectName(u"checkBoxBasename")

        self.gridLayout.addWidget(self.checkBoxBasename, 2, 0, 1, 1)

        self.lineEditBasename = QLineEdit(self.widget)
        self.lineEditBasename.setObjectName(u"lineEditBasename")

        self.gridLayout.addWidget(self.lineEditBasename, 2, 1, 1, 1)

        self.labelFilters = QLabel(self.widget)
        self.labelFilters.setObjectName(u"labelFilters")

        self.gridLayout.addWidget(self.labelFilters, 3, 0, 1, 1)

        self.comboBoxFilters = QComboBox(self.widget)
        self.comboBoxFilters.setObjectName(u"comboBoxFilters")

        self.gridLayout.addWidget(self.comboBoxFilters, 3, 1, 1, 1)

        self.labelCompression = QLabel(self.widget)
        self.labelCompression.setObjectName(u"labelCompression")

        self.gridLayout.addWidget(self.labelCompression, 4, 0, 1, 1)

        self.comboBoxCompression = QComboBox(self.widget)
        self.comboBoxCompression.setObjectName(u"comboBoxCompression")

        self.gridLayout.addWidget(self.comboBoxCompression, 4, 1, 1, 1)

        self.labelTheme = QLabel(self.widget)
        self.labelTheme.setObjectName(u"labelTheme")

        self.gridLayout.addWidget(self.labelTheme, 5, 0, 1, 1)

        self.comboBoxTheme = QComboBox(self.widget)
        self.comboBoxTheme.setObjectName(u"comboBoxTheme")

        self.gridLayout.addWidget(self.comboBoxTheme, 5, 1, 1, 1)

        self.checkBoxClone = QCheckBox(self.widget)
        self.checkBoxClone.setObjectName(u"checkBoxClone")

        self.gridLayout.addWidget(self.checkBoxClone, 6, 0, 1, 1)

        self.checkBoxCryptedClone = QCheckBox(self.widget)
        self.checkBoxCryptedClone.setObjectName(u"checkBoxCryptedClone")

        self.gridLayout.addWidget(self.checkBoxCryptedClone, 7, 0, 1, 1)

        self.checkBoxScript = QCheckBox(self.widget)
        self.checkBoxScript.setObjectName(u"checkBoxScript")

        self.gridLayout.addWidget(self.checkBoxScript, 8, 0, 1, 1)

        self.checkBoxUnsecure = QCheckBox(self.widget)
        self.checkBoxUnsecure.setObjectName(u"checkBoxUnsecure")
        self.checkBoxUnsecure.setTristate(False)

        self.gridLayout.addWidget(self.checkBoxUnsecure, 9, 0, 1, 1)

        self.checkBoxYolk = QCheckBox(self.widget)
        self.checkBoxYolk.setObjectName(u"checkBoxYolk")

        self.gridLayout.addWidget(self.checkBoxYolk, 10, 0, 1, 1)


        self.retranslateUi(DialogProduce)
        self.buttonBox.accepted.connect(DialogProduce.accept)
        self.buttonBox.rejected.connect(DialogProduce.reject)

        QMetaObject.connectSlotsByName(DialogProduce)
    # setupUi

    def retranslateUi(self, DialogProduce):
        DialogProduce.setWindowTitle(QCoreApplication.translate("DialogProduce", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("DialogProduce", u"Command to run", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("DialogProduce", u"Command", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRun.setToolTip(QCoreApplication.translate("DialogProduce", u"run or copy ib ckuobiard the generated command", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRun.setText(QCoreApplication.translate("DialogProduce", u"run/copy", None))
#if QT_CONFIG(tooltip)
        self.pushButtonGenerate.setToolTip(QCoreApplication.translate("DialogProduce", u"generate the command", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonGenerate.setText(QCoreApplication.translate("DialogProduce", u"generate", None))
#if QT_CONFIG(tooltip)
        self.labelAddons.setToolTip(QCoreApplication.translate("DialogProduce", u"configures the addon and creates a link to the selected one on the desktop", None))
#endif // QT_CONFIG(tooltip)
        self.labelAddons.setText(QCoreApplication.translate("DialogProduce", u"Addons", None))
#if QT_CONFIG(tooltip)
        self.comboBoxAddons.setToolTip(QCoreApplication.translate("DialogProduce", u"Select addons to insert", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBoxPrefix.setToolTip(QCoreApplication.translate("DialogProduce", u"Prefix eg: egg-of_DISTRONAME-CODENAME-", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxPrefix.setText(QCoreApplication.translate("DialogProduce", u"Prefix", None))
#if QT_CONFIG(tooltip)
        self.lineEditPrefix.setToolTip(QCoreApplication.translate("DialogProduce", u"prefix", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBoxBasename.setToolTip(QCoreApplication.translate("DialogProduce", u"Basename (usually hostname)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxBasename.setText(QCoreApplication.translate("DialogProduce", u"Basename", None))
#if QT_CONFIG(tooltip)
        self.lineEditBasename.setToolTip(QCoreApplication.translate("DialogProduce", u"basename", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelFilters.setToolTip(QCoreApplication.translate("DialogProduce", u"Filters are used to remove private or unnecessary information from the image, you can decide whether to use them or not", None))
#endif // QT_CONFIG(tooltip)
        self.labelFilters.setText(QCoreApplication.translate("DialogProduce", u"Filters", None))
#if QT_CONFIG(tooltip)
        self.comboBoxFilters.setToolTip(QCoreApplication.translate("DialogProduce", u"Select firler to use", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelCompression.setToolTip(QCoreApplication.translate("DialogProduce", u"You can choose from three types of compression: fast (default), standart and max", None))
#endif // QT_CONFIG(tooltip)
        self.labelCompression.setText(QCoreApplication.translate("DialogProduce", u"Compression", None))
#if QT_CONFIG(tooltip)
        self.comboBoxCompression.setToolTip(QCoreApplication.translate("DialogProduce", u"Select compression", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelTheme.setToolTip(QCoreApplication.translate("DialogProduce", u"Select the desired theme. To download themes: eggs wardrobe get", None))
#endif // QT_CONFIG(tooltip)
        self.labelTheme.setText(QCoreApplication.translate("DialogProduce", u"Theme", None))
#if QT_CONFIG(tooltip)
        self.comboBoxTheme.setToolTip(QCoreApplication.translate("DialogProduce", u"Select theme", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBoxClone.setToolTip(QCoreApplication.translate("DialogProduce", u"Performs a complete clone of the system by also copying users and their data", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxClone.setText(QCoreApplication.translate("DialogProduce", u"Clone", None))
#if QT_CONFIG(tooltip)
        self.checkBoxCryptedClone.setToolTip(QCoreApplication.translate("DialogProduce", u"Performs a complete clone of the system by also copying the users and their data that will be encrypted in a LUKS volume inside the ISO ", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxCryptedClone.setText(QCoreApplication.translate("DialogProduce", u"Crypted Clone", None))
#if QT_CONFIG(tooltip)
        self.checkBoxScript.setToolTip(QCoreApplication.translate("DialogProduce", u"It only creates the scripts necessary to create the ISO, but does not create it.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxScript.setText(QCoreApplication.translate("DialogProduce", u"Script", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUnsecure.setToolTip(QCoreApplication.translate("DialogProduce", u"Selecting unsecure will also copy the data in /root to the ISO", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUnsecure.setText(QCoreApplication.translate("DialogProduce", u"Unsecure", None))
#if QT_CONFIG(tooltip)
        self.checkBoxYolk.setToolTip(QCoreApplication.translate("DialogProduce", u"Generates or regenerates a local repository /var/local/yolk to allow installation even in the absence of the Internet.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxYolk.setText(QCoreApplication.translate("DialogProduce", u"Yolk", None))
    # retranslateUi

