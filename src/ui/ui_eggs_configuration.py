# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eggs_configurationfKfQlN.ui'
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
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QSize(400, 300))
        Dialog.setMaximumSize(QSize(400, 300))
#if QT_CONFIG(accessibility)
        Dialog.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        Dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 400, 241))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_snapshot_dir = QLabel(self.layoutWidget)
        self.label_snapshot_dir.setObjectName(u"label_snapshot_dir")

        self.gridLayout.addWidget(self.label_snapshot_dir, 0, 0, 1, 1)

        self.lineEditSnapshotDir = QLineEdit(self.layoutWidget)
        self.lineEditSnapshotDir.setObjectName(u"lineEditSnapshotDir")

        self.gridLayout.addWidget(self.lineEditSnapshotDir, 0, 1, 1, 1)

        self.label_snashot_prefix = QLabel(self.layoutWidget)
        self.label_snashot_prefix.setObjectName(u"label_snashot_prefix")

        self.gridLayout.addWidget(self.label_snashot_prefix, 1, 0, 1, 1)

        self.lineEditSnapshotPrefix = QLineEdit(self.layoutWidget)
        self.lineEditSnapshotPrefix.setObjectName(u"lineEditSnapshotPrefix")

        self.gridLayout.addWidget(self.lineEditSnapshotPrefix, 1, 1, 1, 1)

        self.label_snapshot_basename = QLabel(self.layoutWidget)
        self.label_snapshot_basename.setObjectName(u"label_snapshot_basename")

        self.gridLayout.addWidget(self.label_snapshot_basename, 2, 0, 1, 1)

        self.lineEditSnapshotBasename = QLineEdit(self.layoutWidget)
        self.lineEditSnapshotBasename.setObjectName(u"lineEditSnapshotBasename")

        self.gridLayout.addWidget(self.lineEditSnapshotBasename, 2, 1, 1, 1)

        self.label_user_opt = QLabel(self.layoutWidget)
        self.label_user_opt.setObjectName(u"label_user_opt")

        self.gridLayout.addWidget(self.label_user_opt, 3, 0, 1, 1)

        self.lineEditUserOpt = QLineEdit(self.layoutWidget)
        self.lineEditUserOpt.setObjectName(u"lineEditUserOpt")

        self.gridLayout.addWidget(self.lineEditUserOpt, 3, 1, 1, 1)

        self.label_user_opt_passwd = QLabel(self.layoutWidget)
        self.label_user_opt_passwd.setObjectName(u"label_user_opt_passwd")

        self.gridLayout.addWidget(self.label_user_opt_passwd, 4, 0, 1, 1)

        self.lineEditUserOptPasswd = QLineEdit(self.layoutWidget)
        self.lineEditUserOptPasswd.setObjectName(u"lineEditUserOptPasswd")
        self.lineEditUserOptPasswd.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.lineEditUserOptPasswd, 4, 1, 1, 1)

        self.label_root_passwd = QLabel(self.layoutWidget)
        self.label_root_passwd.setObjectName(u"label_root_passwd")

        self.gridLayout.addWidget(self.label_root_passwd, 5, 0, 1, 1)

        self.lineEditRootPasswd = QLineEdit(self.layoutWidget)
        self.lineEditRootPasswd.setObjectName(u"lineEditRootPasswd")
        self.lineEditRootPasswd.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.lineEditRootPasswd, 5, 1, 1, 1)

        self.checkBoxMakeMd5sum = QCheckBox(self.layoutWidget)
        self.checkBoxMakeMd5sum.setObjectName(u"checkBoxMakeMd5sum")

        self.gridLayout.addWidget(self.checkBoxMakeMd5sum, 6, 1, 1, 1)

        self.checkBoxMakeIsohybrid = QCheckBox(self.layoutWidget)
        self.checkBoxMakeIsohybrid.setObjectName(u"checkBoxMakeIsohybrid")

        self.gridLayout.addWidget(self.checkBoxMakeIsohybrid, 6, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(230, 270, 166, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Form", None))
        self.label_snapshot_dir.setText(QCoreApplication.translate("Dialog", u"Nest", None))
        self.label_snashot_prefix.setText(QCoreApplication.translate("Dialog", u"Prefix", None))
        self.label_snapshot_basename.setText(QCoreApplication.translate("Dialog", u"Basename", None))
        self.label_user_opt.setText(QCoreApplication.translate("Dialog", u"Live user name", None))
        self.label_user_opt_passwd.setText(QCoreApplication.translate("Dialog", u"Live user password", None))
        self.label_root_passwd.setText(QCoreApplication.translate("Dialog", u"Live root password", None))
        self.checkBoxMakeMd5sum.setText(QCoreApplication.translate("Dialog", u"md5sum", None))
        self.checkBoxMakeIsohybrid.setText(QCoreApplication.translate("Dialog", u"isohybrid", None))
    # retranslateUi

