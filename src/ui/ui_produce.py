# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'producejJALbS.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
    QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QWidget)
import resources_rc

class Ui_DialogProduce(object):
    def setupUi(self, DialogProduce):
        if not DialogProduce.objectName():
            DialogProduce.setObjectName(u"DialogProduce")
        DialogProduce.resize(800, 600)
        DialogProduce.setMinimumSize(QSize(640, 480))
        icon = QIcon()
        icon.addFile(u":/pengui/icons/pengui.svg", QSize(), QIcon.Normal, QIcon.Off)
        DialogProduce.setWindowIcon(icon)
        DialogProduce.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox = QDialogButtonBox(DialogProduce)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(401, 550, 371, 31))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Help|QDialogButtonBox.Ok)
        self.lineEditCommand = QLineEdit(DialogProduce)
        self.lineEditCommand.setObjectName(u"lineEditCommand")
        self.lineEditCommand.setGeometry(QRect(30, 440, 761, 61))
        self.labelTheme = QLabel(DialogProduce)
        self.labelTheme.setObjectName(u"labelTheme")
        self.labelTheme.setGeometry(QRect(30, 310, 73, 25))
        self.labelExclude = QLabel(DialogProduce)
        self.labelExclude.setObjectName(u"labelExclude")
        self.labelExclude.setGeometry(QRect(20, 150, 141, 25))
        self.labelCompression = QLabel(DialogProduce)
        self.labelCompression.setObjectName(u"labelCompression")
        self.labelCompression.setGeometry(QRect(30, 240, 137, 25))
        self.comboBoxCompression = QComboBox(DialogProduce)
        self.comboBoxCompression.setObjectName(u"comboBoxCompression")
        self.comboBoxCompression.setGeometry(QRect(170, 240, 621, 33))
        self.layoutWidget = QWidget(DialogProduce)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 151, 33))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBoxTheme = QComboBox(DialogProduce)
        self.comboBoxTheme.setObjectName(u"comboBoxTheme")
        self.comboBoxTheme.setGeometry(QRect(170, 310, 621, 33))
        self.layoutWidget1 = QWidget(DialogProduce)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 370, 563, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBoxScript = QCheckBox(self.layoutWidget1)
        self.checkBoxScript.setObjectName(u"checkBoxScript")

        self.horizontalLayout.addWidget(self.checkBoxScript)

        self.checkBoxClone = QCheckBox(self.layoutWidget1)
        self.checkBoxClone.setObjectName(u"checkBoxClone")

        self.horizontalLayout.addWidget(self.checkBoxClone)

        self.checkBoxCryptedClone = QCheckBox(self.layoutWidget1)
        self.checkBoxCryptedClone.setObjectName(u"checkBoxCryptedClone")

        self.horizontalLayout.addWidget(self.checkBoxCryptedClone)

        self.checkBoxYolk = QCheckBox(self.layoutWidget1)
        self.checkBoxYolk.setObjectName(u"checkBoxYolk")

        self.horizontalLayout.addWidget(self.checkBoxYolk)

        self.checkBoxUnsecure = QCheckBox(self.layoutWidget1)
        self.checkBoxUnsecure.setObjectName(u"checkBoxUnsecure")
        self.checkBoxUnsecure.setTristate(False)

        self.horizontalLayout.addWidget(self.checkBoxUnsecure)

        self.labelAddons = QLabel(DialogProduce)
        self.labelAddons.setObjectName(u"labelAddons")
        self.labelAddons.setGeometry(QRect(22, 12, 78, 25))
        self.comboBoxAddons = QComboBox(DialogProduce)
        self.comboBoxAddons.setObjectName(u"comboBoxAddons")
        self.comboBoxAddons.setGeometry(QRect(150, 10, 641, 33))
        self.lineEditPrefix = QLineEdit(DialogProduce)
        self.lineEditPrefix.setObjectName(u"lineEditPrefix")
        self.lineEditPrefix.setGeometry(QRect(170, 50, 641, 33))
        self.checkBoxPrefix = QCheckBox(DialogProduce)
        self.checkBoxPrefix.setObjectName(u"checkBoxPrefix")
        self.checkBoxPrefix.setGeometry(QRect(22, 52, 84, 31))
        self.checkBoxBasename = QCheckBox(DialogProduce)
        self.checkBoxBasename.setObjectName(u"checkBoxBasename")
        self.checkBoxBasename.setGeometry(QRect(22, 91, 136, 31))
        self.lineEditBasename = QLineEdit(DialogProduce)
        self.lineEditBasename.setObjectName(u"lineEditBasename")
        self.lineEditBasename.setGeometry(QRect(170, 90, 621, 33))
        self.layoutWidget2 = QWidget(DialogProduce)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(187, 141, 571, 33))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBoxCryptedclone = QCheckBox(self.layoutWidget2)
        self.checkBoxCryptedclone.setObjectName(u"checkBoxCryptedclone")

        self.horizontalLayout_2.addWidget(self.checkBoxCryptedclone)

        self.checkBoxCustom = QCheckBox(self.layoutWidget2)
        self.checkBoxCustom.setObjectName(u"checkBoxCustom")

        self.horizontalLayout_2.addWidget(self.checkBoxCustom)

        self.checkBoxUsr = QCheckBox(self.layoutWidget2)
        self.checkBoxUsr.setObjectName(u"checkBoxUsr")

        self.horizontalLayout_2.addWidget(self.checkBoxUsr)


        self.retranslateUi(DialogProduce)
        self.buttonBox.accepted.connect(DialogProduce.accept)
        self.buttonBox.rejected.connect(DialogProduce.reject)

        QMetaObject.connectSlotsByName(DialogProduce)
    # setupUi

    def retranslateUi(self, DialogProduce):
        DialogProduce.setWindowTitle(QCoreApplication.translate("DialogProduce", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.lineEditCommand.setToolTip(QCoreApplication.translate("DialogProduce", u"command to produce ISO", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelTheme.setToolTip(QCoreApplication.translate("DialogProduce", u"Select the desired theme. To download themes: eggs wardrobe get", None))
#endif // QT_CONFIG(tooltip)
        self.labelTheme.setText(QCoreApplication.translate("DialogProduce", u"Theme", None))
#if QT_CONFIG(tooltip)
        self.labelExclude.setToolTip(QCoreApplication.translate("DialogProduce", u"Filters are used to remove private or unnecessaries informations from the image, note exclude.list.template is always applied", None))
#endif // QT_CONFIG(tooltip)
        self.labelExclude.setText(QCoreApplication.translate("DialogProduce", u"Exclude list:", None))
#if QT_CONFIG(tooltip)
        self.labelCompression.setToolTip(QCoreApplication.translate("DialogProduce", u"You can choose from three types of compression: fast (default), standart and max", None))
#endif // QT_CONFIG(tooltip)
        self.labelCompression.setText(QCoreApplication.translate("DialogProduce", u"Compression", None))
#if QT_CONFIG(tooltip)
        self.comboBoxCompression.setToolTip(QCoreApplication.translate("DialogProduce", u"Select compression", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.comboBoxTheme.setToolTip(QCoreApplication.translate("DialogProduce", u"Select theme", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBoxScript.setToolTip(QCoreApplication.translate("DialogProduce", u"It only creates the scripts necessary to create the ISO, but does not create it.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxScript.setText(QCoreApplication.translate("DialogProduce", u"Script", None))
#if QT_CONFIG(tooltip)
        self.checkBoxClone.setToolTip(QCoreApplication.translate("DialogProduce", u"Performs a complete clone of the system, will include users and users' data", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxClone.setText(QCoreApplication.translate("DialogProduce", u"Clone", None))
#if QT_CONFIG(tooltip)
        self.checkBoxCryptedClone.setToolTip(QCoreApplication.translate("DialogProduce", u"Performs a complete clone of the system, users and users' data will be encrypted in a LUKS Volume inside the ISO ", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxCryptedClone.setText(QCoreApplication.translate("DialogProduce", u"Cryptedclone", None))
#if QT_CONFIG(tooltip)
        self.checkBoxYolk.setToolTip(QCoreApplication.translate("DialogProduce", u"Generates or regenerates a local repository /var/local/yolk to allow installation even in the absence of the Internet.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxYolk.setText(QCoreApplication.translate("DialogProduce", u"Yolk", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUnsecure.setToolTip(QCoreApplication.translate("DialogProduce", u"Selecting unsecure will also copy the data in /root to the ISO", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUnsecure.setText(QCoreApplication.translate("DialogProduce", u"Unsecure", None))
#if QT_CONFIG(tooltip)
        self.labelAddons.setToolTip(QCoreApplication.translate("DialogProduce", u"configures the addons and creates a link to the selected one on the desktop", None))
#endif // QT_CONFIG(tooltip)
        self.labelAddons.setText(QCoreApplication.translate("DialogProduce", u"Addons", None))
#if QT_CONFIG(tooltip)
        self.comboBoxAddons.setToolTip(QCoreApplication.translate("DialogProduce", u"Select addons to insert", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEditPrefix.setToolTip(QCoreApplication.translate("DialogProduce", u"prefix", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBoxPrefix.setToolTip(QCoreApplication.translate("DialogProduce", u"Prefix eg: egg-of_DISTRONAME-CODENAME-", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxPrefix.setText(QCoreApplication.translate("DialogProduce", u"Prefix", None))
#if QT_CONFIG(tooltip)
        self.checkBoxBasename.setToolTip(QCoreApplication.translate("DialogProduce", u"Basename (usually hostname)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxBasename.setText(QCoreApplication.translate("DialogProduce", u"Basename", None))
#if QT_CONFIG(tooltip)
        self.lineEditBasename.setToolTip(QCoreApplication.translate("DialogProduce", u"basename", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBoxCryptedclone.setToolTip(QCoreApplication.translate("DialogProduce", u"Add exclude.list.d/clone.list", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxCryptedclone.setText(QCoreApplication.translate("DialogProduce", u"clone", None))
#if QT_CONFIG(tooltip)
        self.checkBoxCustom.setToolTip(QCoreApplication.translate("DialogProduce", u"Add exclude.list.d/custom", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxCustom.setText(QCoreApplication.translate("DialogProduce", u"custom", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUsr.setToolTip(QCoreApplication.translate("DialogProduce", u"Add exclude.list.d/usr to the /etc/penguins-eggs.d/exclude.list", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUsr.setText(QCoreApplication.translate("DialogProduce", u"usr", None))
    # retranslateUi

