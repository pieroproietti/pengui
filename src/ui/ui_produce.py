# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'produceONBbwt.ui'
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
    QDialog, QDialogButtonBox, QFormLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import resources_rc

class Ui_DialogProduce(object):
    def setupUi(self, DialogProduce):
        if not DialogProduce.objectName():
            DialogProduce.setObjectName(u"DialogProduce")
        DialogProduce.resize(640, 480)
        DialogProduce.setMinimumSize(QSize(640, 480))
        DialogProduce.setMaximumSize(QSize(640, 480))
        icon = QIcon()
        icon.addFile(u":/pengui/produce", QSize(), QIcon.Normal, QIcon.Off)
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
        self.lineEditCommand.setGeometry(QRect(110, 360, 521, 23))
        self.pushButtonRun = QPushButton(DialogProduce)
        self.pushButtonRun.setObjectName(u"pushButtonRun")
        self.pushButtonRun.setGeometry(QRect(300, 390, 151, 71))
        self.pushButtonGenerate = QPushButton(DialogProduce)
        self.pushButtonGenerate.setObjectName(u"pushButtonGenerate")
        self.pushButtonGenerate.setGeometry(QRect(160, 390, 131, 71))
        self.pushButtonHelp = QPushButton(DialogProduce)
        self.pushButtonHelp.setObjectName(u"pushButtonHelp")
        self.pushButtonHelp.setGeometry(QRect(10, 390, 141, 71))
        self.layoutWidget = QWidget(DialogProduce)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 22, 611, 314))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelAddons = QLabel(self.layoutWidget)
        self.labelAddons.setObjectName(u"labelAddons")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelAddons)

        self.comboBoxAddons = QComboBox(self.layoutWidget)
        self.comboBoxAddons.setObjectName(u"comboBoxAddons")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBoxAddons)

        self.checkBoxPrefix = QCheckBox(self.layoutWidget)
        self.checkBoxPrefix.setObjectName(u"checkBoxPrefix")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.checkBoxPrefix)

        self.lineEditPrefix = QLineEdit(self.layoutWidget)
        self.lineEditPrefix.setObjectName(u"lineEditPrefix")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditPrefix)

        self.checkBoxBasename = QCheckBox(self.layoutWidget)
        self.checkBoxBasename.setObjectName(u"checkBoxBasename")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.checkBoxBasename)

        self.lineEditBasename = QLineEdit(self.layoutWidget)
        self.lineEditBasename.setObjectName(u"lineEditBasename")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEditBasename)

        self.labelFilters = QLabel(self.layoutWidget)
        self.labelFilters.setObjectName(u"labelFilters")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelFilters)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBoxCustom = QCheckBox(self.layoutWidget)
        self.checkBoxCustom.setObjectName(u"checkBoxCustom")

        self.gridLayout.addWidget(self.checkBoxCustom, 0, 0, 1, 1)

        self.checkBoxHomes = QCheckBox(self.layoutWidget)
        self.checkBoxHomes.setObjectName(u"checkBoxHomes")

        self.gridLayout.addWidget(self.checkBoxHomes, 0, 1, 1, 1)

        self.checkBoxUsr = QCheckBox(self.layoutWidget)
        self.checkBoxUsr.setObjectName(u"checkBoxUsr")

        self.gridLayout.addWidget(self.checkBoxUsr, 0, 2, 1, 1)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.gridLayout)

        self.labelCompression = QLabel(self.layoutWidget)
        self.labelCompression.setObjectName(u"labelCompression")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelCompression)

        self.comboBoxCompression = QComboBox(self.layoutWidget)
        self.comboBoxCompression.setObjectName(u"comboBoxCompression")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBoxCompression)

        self.labelTheme = QLabel(self.layoutWidget)
        self.labelTheme.setObjectName(u"labelTheme")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelTheme)

        self.comboBoxTheme = QComboBox(self.layoutWidget)
        self.comboBoxTheme.setObjectName(u"comboBoxTheme")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.comboBoxTheme)

        self.checkBoxClone = QCheckBox(self.layoutWidget)
        self.checkBoxClone.setObjectName(u"checkBoxClone")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.checkBoxClone)

        self.checkBoxCryptedClone = QCheckBox(self.layoutWidget)
        self.checkBoxCryptedClone.setObjectName(u"checkBoxCryptedClone")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.checkBoxCryptedClone)

        self.checkBoxScript = QCheckBox(self.layoutWidget)
        self.checkBoxScript.setObjectName(u"checkBoxScript")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.checkBoxScript)

        self.checkBoxUnsecure = QCheckBox(self.layoutWidget)
        self.checkBoxUnsecure.setObjectName(u"checkBoxUnsecure")
        self.checkBoxUnsecure.setTristate(False)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.checkBoxUnsecure)

        self.checkBoxYolk = QCheckBox(self.layoutWidget)
        self.checkBoxYolk.setObjectName(u"checkBoxYolk")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.checkBoxYolk)


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
        self.pushButtonRun.setText(QCoreApplication.translate("DialogProduce", u"&Run", None))
#if QT_CONFIG(tooltip)
        self.pushButtonGenerate.setToolTip(QCoreApplication.translate("DialogProduce", u"generate the command", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonGenerate.setText(QCoreApplication.translate("DialogProduce", u"&Generate", None))
#if QT_CONFIG(tooltip)
        self.pushButtonHelp.setToolTip(QCoreApplication.translate("DialogProduce", u"run or copy ib ckuobiard the generated command", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonHelp.setText(QCoreApplication.translate("DialogProduce", u"&Help", None))
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
        self.labelFilters.setToolTip(QCoreApplication.translate("DialogProduce", u"Filters are used to remove private or unnecessaries informations from the image, note exclude.list.template is always applied", None))
#endif // QT_CONFIG(tooltip)
        self.labelFilters.setText(QCoreApplication.translate("DialogProduce", u"Filters", None))
#if QT_CONFIG(tooltip)
        self.checkBoxCustom.setToolTip(QCoreApplication.translate("DialogProduce", u"Add exclude.list.custom to the /etc/penguins-eggs.d/exclude.list", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxCustom.setText(QCoreApplication.translate("DialogProduce", u"custom", None))
#if QT_CONFIG(tooltip)
        self.checkBoxHomes.setToolTip(QCoreApplication.translate("DialogProduce", u"Add exclude.list.homes to the /etc/penguins-eggs.d/exclude.list", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxHomes.setText(QCoreApplication.translate("DialogProduce", u"homes", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUsr.setToolTip(QCoreApplication.translate("DialogProduce", u"Add exclude.list.usr to the /etc/penguins-eggs.d/exclude.list", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUsr.setText(QCoreApplication.translate("DialogProduce", u"usr", None))
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

