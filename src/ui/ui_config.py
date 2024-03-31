# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configlboXVN.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QWidget)
import resources_rc

class Ui_DialogConfig(object):
    def setupUi(self, DialogConfig):
        if not DialogConfig.objectName():
            DialogConfig.setObjectName(u"DialogConfig")
        DialogConfig.resize(800, 600)
        DialogConfig.setMinimumSize(QSize(640, 480))
        DialogConfig.setMaximumSize(QSize(1600, 1200))
        icon = QIcon()
        icon.addFile(u":/pengui/icons/pengui.svg", QSize(), QIcon.Normal, QIcon.Off)
        DialogConfig.setWindowIcon(icon)
#if QT_CONFIG(accessibility)
        DialogConfig.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        DialogConfig.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox = QDialogButtonBox(DialogConfig)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(420, 560, 371, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Help|QDialogButtonBox.Ok)
        self.checkBoxMakeIsohybrid = QCheckBox(DialogConfig)
        self.checkBoxMakeIsohybrid.setObjectName(u"checkBoxMakeIsohybrid")
        self.checkBoxMakeIsohybrid.setGeometry(QRect(-20, 260, 122, 31))
        self.checkBoxMakeMd5sum = QCheckBox(DialogConfig)
        self.checkBoxMakeMd5sum.setObjectName(u"checkBoxMakeMd5sum")
        self.checkBoxMakeMd5sum.setGeometry(QRect(-10, 300, 245, 31))
        self.layoutWidget = QWidget(DialogConfig)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(150, 230, 247, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget1 = QWidget(DialogConfig)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(1, 16, 771, 230))
        self.formLayout = QFormLayout(self.layoutWidget1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_snapshot_dir = QLabel(self.layoutWidget1)
        self.label_snapshot_dir.setObjectName(u"label_snapshot_dir")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_snapshot_dir)

        self.lineEditSnapshotDir = QLineEdit(self.layoutWidget1)
        self.lineEditSnapshotDir.setObjectName(u"lineEditSnapshotDir")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditSnapshotDir)

        self.label_snashot_prefix = QLabel(self.layoutWidget1)
        self.label_snashot_prefix.setObjectName(u"label_snashot_prefix")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_snashot_prefix)

        self.lineEditSnapshotPrefix = QLineEdit(self.layoutWidget1)
        self.lineEditSnapshotPrefix.setObjectName(u"lineEditSnapshotPrefix")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditSnapshotPrefix)

        self.label_snapshot_basename = QLabel(self.layoutWidget1)
        self.label_snapshot_basename.setObjectName(u"label_snapshot_basename")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_snapshot_basename)

        self.lineEditSnapshotBasename = QLineEdit(self.layoutWidget1)
        self.lineEditSnapshotBasename.setObjectName(u"lineEditSnapshotBasename")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEditSnapshotBasename)

        self.label_user_opt = QLabel(self.layoutWidget1)
        self.label_user_opt.setObjectName(u"label_user_opt")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_user_opt)

        self.lineEditUserOpt = QLineEdit(self.layoutWidget1)
        self.lineEditUserOpt.setObjectName(u"lineEditUserOpt")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEditUserOpt)

        self.label_user_opt_passwd = QLabel(self.layoutWidget1)
        self.label_user_opt_passwd.setObjectName(u"label_user_opt_passwd")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_user_opt_passwd)

        self.lineEditUserOptPasswd = QLineEdit(self.layoutWidget1)
        self.lineEditUserOptPasswd.setObjectName(u"lineEditUserOptPasswd")
        self.lineEditUserOptPasswd.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEditUserOptPasswd)

        self.label_root_passwd = QLabel(self.layoutWidget1)
        self.label_root_passwd.setObjectName(u"label_root_passwd")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_root_passwd)

        self.lineEditRootPasswd = QLineEdit(self.layoutWidget1)
        self.lineEditRootPasswd.setObjectName(u"lineEditRootPasswd")
        self.lineEditRootPasswd.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEditRootPasswd)


        self.retranslateUi(DialogConfig)

        QMetaObject.connectSlotsByName(DialogConfig)
    # setupUi

    def retranslateUi(self, DialogConfig):
        DialogConfig.setWindowTitle(QCoreApplication.translate("DialogConfig", u"Form", None))
#if QT_CONFIG(tooltip)
        DialogConfig.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBoxMakeIsohybrid.setToolTip(QCoreApplication.translate("DialogConfig", u"Create isohybrid ISO image", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxMakeIsohybrid.setText(QCoreApplication.translate("DialogConfig", u"isohybrid", None))
#if QT_CONFIG(tooltip)
        self.checkBoxMakeMd5sum.setToolTip(QCoreApplication.translate("DialogConfig", u"Create MD5/SHA256 Checksum of the live ISO", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxMakeMd5sum.setText(QCoreApplication.translate("DialogConfig", u"md5sum", None))
#if QT_CONFIG(tooltip)
        self.label_snapshot_dir.setToolTip(QCoreApplication.translate("DialogConfig", u"The place were we make eggs, usually /home/eggs", None))
#endif // QT_CONFIG(tooltip)
        self.label_snapshot_dir.setText(QCoreApplication.translate("DialogConfig", u"Nest", None))
#if QT_CONFIG(tooltip)
        self.lineEditSnapshotDir.setToolTip(QCoreApplication.translate("DialogConfig", u"The place were we make eggs, usually /home/eggs", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_snashot_prefix.setToolTip(QCoreApplication.translate("DialogConfig", u"Prefix to be used with basenage to get ISO image filename", None))
#endif // QT_CONFIG(tooltip)
        self.label_snashot_prefix.setText(QCoreApplication.translate("DialogConfig", u"Prefix", None))
#if QT_CONFIG(tooltip)
        self.lineEditSnapshotPrefix.setToolTip(QCoreApplication.translate("DialogConfig", u"Prefix to be used with basenage to get ISO image filename", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_snapshot_basename.setToolTip(QCoreApplication.translate("DialogConfig", u"volid of the ISO image", None))
#endif // QT_CONFIG(tooltip)
        self.label_snapshot_basename.setText(QCoreApplication.translate("DialogConfig", u"Basename", None))
#if QT_CONFIG(tooltip)
        self.lineEditSnapshotBasename.setToolTip(QCoreApplication.translate("DialogConfig", u"volid of the ISO image", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_user_opt.setToolTip(QCoreApplication.translate("DialogConfig", u"Live user name for live system/ISO image", None))
#endif // QT_CONFIG(tooltip)
        self.label_user_opt.setText(QCoreApplication.translate("DialogConfig", u"Live user name", None))
#if QT_CONFIG(tooltip)
        self.lineEditUserOpt.setToolTip(QCoreApplication.translate("DialogConfig", u"Live user name for live system/ISO image", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_user_opt_passwd.setToolTip(QCoreApplication.translate("DialogConfig", u"Live user password for live system/ISO image", None))
#endif // QT_CONFIG(tooltip)
        self.label_user_opt_passwd.setText(QCoreApplication.translate("DialogConfig", u"Live user password", None))
#if QT_CONFIG(tooltip)
        self.lineEditUserOptPasswd.setToolTip(QCoreApplication.translate("DialogConfig", u"Live user password for live system/ISO image", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_root_passwd.setToolTip(QCoreApplication.translate("DialogConfig", u"root password for live system/ISO image", None))
#endif // QT_CONFIG(tooltip)
        self.label_root_passwd.setText(QCoreApplication.translate("DialogConfig", u"Live root password", None))
#if QT_CONFIG(tooltip)
        self.lineEditRootPasswd.setToolTip(QCoreApplication.translate("DialogConfig", u"root password for live system/ISO image", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

