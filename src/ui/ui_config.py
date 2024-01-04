# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configTcPJhS.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import resources_rc

class Ui_DialogConfig(object):
    def setupUi(self, DialogConfig):
        if not DialogConfig.objectName():
            DialogConfig.setObjectName(u"DialogConfig")
        DialogConfig.resize(640, 480)
        DialogConfig.setMinimumSize(QSize(640, 480))
        DialogConfig.setMaximumSize(QSize(640, 480))
        icon = QIcon()
        icon.addFile(u":/pengui/icons/pengui.svg", QSize(), QIcon.Normal, QIcon.Off)
        DialogConfig.setWindowIcon(icon)
#if QT_CONFIG(accessibility)
        DialogConfig.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        DialogConfig.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox = QDialogButtonBox(DialogConfig)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(440, 440, 171, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.pushButtonSave = QPushButton(DialogConfig)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        self.pushButtonSave.setGeometry(QRect(440, 230, 171, 61))
        self.pushButtonDiscard = QPushButton(DialogConfig)
        self.pushButtonDiscard.setObjectName(u"pushButtonDiscard")
        self.pushButtonDiscard.setGeometry(QRect(350, 230, 83, 61))
        self.checkBoxMakeIsohybrid = QCheckBox(DialogConfig)
        self.checkBoxMakeIsohybrid.setObjectName(u"checkBoxMakeIsohybrid")
        self.checkBoxMakeIsohybrid.setGeometry(QRect(1, 220, 85, 22))
        self.label_user_opt = QLabel(DialogConfig)
        self.label_user_opt.setObjectName(u"label_user_opt")
        self.label_user_opt.setGeometry(QRect(1, 118, 100, 16))
        self.label_snapshot_basename = QLabel(DialogConfig)
        self.label_snapshot_basename.setObjectName(u"label_snapshot_basename")
        self.label_snapshot_basename.setGeometry(QRect(1, 84, 69, 16))
        self.label_user_opt_passwd = QLabel(DialogConfig)
        self.label_user_opt_passwd.setObjectName(u"label_user_opt_passwd")
        self.label_user_opt_passwd.setGeometry(QRect(1, 152, 125, 16))
        self.label_snapshot_dir = QLabel(DialogConfig)
        self.label_snapshot_dir.setObjectName(u"label_snapshot_dir")
        self.label_snapshot_dir.setGeometry(QRect(1, 16, 30, 16))
        self.lineEditRootPasswd = QLineEdit(DialogConfig)
        self.lineEditRootPasswd.setObjectName(u"lineEditRootPasswd")
        self.lineEditRootPasswd.setGeometry(QRect(132, 186, 491, 23))
        self.lineEditRootPasswd.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.lineEditUserOpt = QLineEdit(DialogConfig)
        self.lineEditUserOpt.setObjectName(u"lineEditUserOpt")
        self.lineEditUserOpt.setGeometry(QRect(132, 118, 491, 23))
        self.checkBoxMakeMd5sum = QCheckBox(DialogConfig)
        self.checkBoxMakeMd5sum.setObjectName(u"checkBoxMakeMd5sum")
        self.checkBoxMakeMd5sum.setGeometry(QRect(132, 220, 82, 22))
        self.lineEditSnapshotPrefix = QLineEdit(DialogConfig)
        self.lineEditSnapshotPrefix.setObjectName(u"lineEditSnapshotPrefix")
        self.lineEditSnapshotPrefix.setGeometry(QRect(132, 50, 491, 23))
        self.lineEditUserOptPasswd = QLineEdit(DialogConfig)
        self.lineEditUserOptPasswd.setObjectName(u"lineEditUserOptPasswd")
        self.lineEditUserOptPasswd.setGeometry(QRect(132, 152, 491, 23))
        self.lineEditUserOptPasswd.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.lineEditSnapshotBasename = QLineEdit(DialogConfig)
        self.lineEditSnapshotBasename.setObjectName(u"lineEditSnapshotBasename")
        self.lineEditSnapshotBasename.setGeometry(QRect(132, 84, 491, 23))
        self.lineEditSnapshotDir = QLineEdit(DialogConfig)
        self.lineEditSnapshotDir.setObjectName(u"lineEditSnapshotDir")
        self.lineEditSnapshotDir.setGeometry(QRect(132, 16, 491, 23))
        self.label_root_passwd = QLabel(DialogConfig)
        self.label_root_passwd.setObjectName(u"label_root_passwd")
        self.label_root_passwd.setGeometry(QRect(1, 186, 123, 16))
        self.label_snashot_prefix = QLabel(DialogConfig)
        self.label_snashot_prefix.setObjectName(u"label_snashot_prefix")
        self.label_snashot_prefix.setGeometry(QRect(1, 50, 37, 16))
        self.pushButtonHelp = QPushButton(DialogConfig)
        self.pushButtonHelp.setObjectName(u"pushButtonHelp")
        self.pushButtonHelp.setGeometry(QRect(260, 230, 83, 61))

        self.retranslateUi(DialogConfig)

        QMetaObject.connectSlotsByName(DialogConfig)
    # setupUi

    def retranslateUi(self, DialogConfig):
        DialogConfig.setWindowTitle(QCoreApplication.translate("DialogConfig", u"Form", None))
#if QT_CONFIG(tooltip)
        DialogConfig.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonSave.setText(QCoreApplication.translate("DialogConfig", u"&Save", None))
        self.pushButtonDiscard.setText(QCoreApplication.translate("DialogConfig", u"&Discard", None))
#if QT_CONFIG(tooltip)
        self.checkBoxMakeIsohybrid.setToolTip(QCoreApplication.translate("DialogConfig", u"Create isohybrid ISO image", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxMakeIsohybrid.setText(QCoreApplication.translate("DialogConfig", u"isohybrid", None))
#if QT_CONFIG(tooltip)
        self.label_user_opt.setToolTip(QCoreApplication.translate("DialogConfig", u"Live user name for live system/ISO image", None))
#endif // QT_CONFIG(tooltip)
        self.label_user_opt.setText(QCoreApplication.translate("DialogConfig", u"Live user name", None))
#if QT_CONFIG(tooltip)
        self.label_snapshot_basename.setToolTip(QCoreApplication.translate("DialogConfig", u"volid of the ISO image", None))
#endif // QT_CONFIG(tooltip)
        self.label_snapshot_basename.setText(QCoreApplication.translate("DialogConfig", u"Basename", None))
#if QT_CONFIG(tooltip)
        self.label_user_opt_passwd.setToolTip(QCoreApplication.translate("DialogConfig", u"Live user password for live system/ISO image", None))
#endif // QT_CONFIG(tooltip)
        self.label_user_opt_passwd.setText(QCoreApplication.translate("DialogConfig", u"Live user password", None))
#if QT_CONFIG(tooltip)
        self.label_snapshot_dir.setToolTip(QCoreApplication.translate("DialogConfig", u"The place were we make eggs, usually /home/eggs", None))
#endif // QT_CONFIG(tooltip)
        self.label_snapshot_dir.setText(QCoreApplication.translate("DialogConfig", u"Nest", None))
#if QT_CONFIG(tooltip)
        self.lineEditRootPasswd.setToolTip(QCoreApplication.translate("DialogConfig", u"root password for live system/ISO image", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEditUserOpt.setToolTip(QCoreApplication.translate("DialogConfig", u"Live user name for live system/ISO image", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBoxMakeMd5sum.setToolTip(QCoreApplication.translate("DialogConfig", u"Create MD5/SHA256 Checksum of the live ISO", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxMakeMd5sum.setText(QCoreApplication.translate("DialogConfig", u"md5sum", None))
#if QT_CONFIG(tooltip)
        self.lineEditSnapshotPrefix.setToolTip(QCoreApplication.translate("DialogConfig", u"Prefix to be used with basenage to get ISO image filename", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEditUserOptPasswd.setToolTip(QCoreApplication.translate("DialogConfig", u"Live user password for live system/ISO image", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEditSnapshotBasename.setToolTip(QCoreApplication.translate("DialogConfig", u"volid of the ISO image", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEditSnapshotDir.setToolTip(QCoreApplication.translate("DialogConfig", u"The place were we make eggs, usually /home/eggs", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_root_passwd.setToolTip(QCoreApplication.translate("DialogConfig", u"root password for live system/ISO image", None))
#endif // QT_CONFIG(tooltip)
        self.label_root_passwd.setText(QCoreApplication.translate("DialogConfig", u"Live root password", None))
#if QT_CONFIG(tooltip)
        self.label_snashot_prefix.setToolTip(QCoreApplication.translate("DialogConfig", u"Prefix to be used with basenage to get ISO image filename", None))
#endif // QT_CONFIG(tooltip)
        self.label_snashot_prefix.setText(QCoreApplication.translate("DialogConfig", u"Prefix", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("DialogConfig", u"&Help", None))
    # retranslateUi

