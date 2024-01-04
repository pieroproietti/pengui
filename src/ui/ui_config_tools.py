# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_toolsQzBiqC.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.pushButtonHelp = QPushButton(Dialog)
        self.pushButtonHelp.setObjectName(u"pushButtonHelp")
        self.pushButtonHelp.setGeometry(QRect(380, 270, 80, 61))
        self.pushButtonDiscard = QPushButton(Dialog)
        self.pushButtonDiscard.setObjectName(u"pushButtonDiscard")
        self.pushButtonDiscard.setGeometry(QRect(466, 270, 80, 61))
        self.pushButtonSave = QPushButton(Dialog)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        self.pushButtonSave.setGeometry(QRect(552, 270, 80, 61))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 31, 621, 199))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelLocalPathIso = QLabel(self.layoutWidget)
        self.labelLocalPathIso.setObjectName(u"labelLocalPathIso")

        self.gridLayout.addWidget(self.labelLocalPathIso, 0, 0, 1, 1)

        self.lineEditLocalPathIso = QLineEdit(self.layoutWidget)
        self.lineEditLocalPathIso.setObjectName(u"lineEditLocalPathIso")

        self.gridLayout.addWidget(self.lineEditLocalPathIso, 0, 2, 1, 1)

        self.labelLocalPathDeb = QLabel(self.layoutWidget)
        self.labelLocalPathDeb.setObjectName(u"labelLocalPathDeb")

        self.gridLayout.addWidget(self.labelLocalPathDeb, 1, 0, 1, 1)

        self.lineEditLocalPathDeb = QLineEdit(self.layoutWidget)
        self.lineEditLocalPathDeb.setObjectName(u"lineEditLocalPathDeb")

        self.gridLayout.addWidget(self.lineEditLocalPathDeb, 1, 2, 1, 1)

        self.labelRemoteHost = QLabel(self.layoutWidget)
        self.labelRemoteHost.setObjectName(u"labelRemoteHost")

        self.gridLayout.addWidget(self.labelRemoteHost, 2, 0, 1, 1)

        self.lineEditRemoteHost = QLineEdit(self.layoutWidget)
        self.lineEditRemoteHost.setObjectName(u"lineEditRemoteHost")

        self.gridLayout.addWidget(self.lineEditRemoteHost, 2, 2, 1, 1)

        self.labelRemoteUser = QLabel(self.layoutWidget)
        self.labelRemoteUser.setObjectName(u"labelRemoteUser")

        self.gridLayout.addWidget(self.labelRemoteUser, 3, 0, 1, 1)

        self.lineEditRemoteUser = QLineEdit(self.layoutWidget)
        self.lineEditRemoteUser.setObjectName(u"lineEditRemoteUser")

        self.gridLayout.addWidget(self.lineEditRemoteUser, 3, 2, 1, 1)

        self.labelRemotePathIso = QLabel(self.layoutWidget)
        self.labelRemotePathIso.setObjectName(u"labelRemotePathIso")

        self.gridLayout.addWidget(self.labelRemotePathIso, 4, 0, 1, 1)

        self.lineEditRemotePathIso = QLineEdit(self.layoutWidget)
        self.lineEditRemotePathIso.setObjectName(u"lineEditRemotePathIso")

        self.gridLayout.addWidget(self.lineEditRemotePathIso, 4, 2, 1, 1)

        self.labelRemotePathDeb = QLabel(self.layoutWidget)
        self.labelRemotePathDeb.setObjectName(u"labelRemotePathDeb")

        self.gridLayout.addWidget(self.labelRemotePathDeb, 5, 0, 1, 2)

        self.lineEditRemotePathDeb = QLineEdit(self.layoutWidget)
        self.lineEditRemotePathDeb.setObjectName(u"lineEditRemotePathDeb")

        self.gridLayout.addWidget(self.lineEditRemotePathDeb, 5, 2, 1, 1)

        self.labelFilterDeb = QLabel(self.layoutWidget)
        self.labelFilterDeb.setObjectName(u"labelFilterDeb")

        self.gridLayout.addWidget(self.labelFilterDeb, 6, 0, 1, 1)

        self.lineEditFilterDeb = QLineEdit(self.layoutWidget)
        self.lineEditFilterDeb.setObjectName(u"lineEditFilterDeb")

        self.gridLayout.addWidget(self.lineEditFilterDeb, 6, 1, 1, 2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("Dialog", u"&Help", None))
        self.pushButtonDiscard.setText(QCoreApplication.translate("Dialog", u"&Discard", None))
        self.pushButtonSave.setText(QCoreApplication.translate("Dialog", u"&Save", None))
#if QT_CONFIG(tooltip)
        self.labelLocalPathIso.setToolTip(QCoreApplication.translate("Dialog", u"local path of our ISOs images", None))
#endif // QT_CONFIG(tooltip)
        self.labelLocalPathIso.setText(QCoreApplication.translate("Dialog", u"Local path ISOs:", None))
#if QT_CONFIG(tooltip)
        self.lineEditLocalPathIso.setToolTip(QCoreApplication.translate("Dialog", u"local path of our ISOs images", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelLocalPathDeb.setToolTip(QCoreApplication.translate("Dialog", u"local path of our DEBS packages", None))
#endif // QT_CONFIG(tooltip)
        self.labelLocalPathDeb.setText(QCoreApplication.translate("Dialog", u"Local path packages .deb:", None))
#if QT_CONFIG(tooltip)
        self.lineEditLocalPathDeb.setToolTip(QCoreApplication.translate("Dialog", u"local path of our DEBS packages", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelRemoteHost.setToolTip(QCoreApplication.translate("Dialog", u"ip address of remote host where we want to export our ISOs and packages", None))
#endif // QT_CONFIG(tooltip)
        self.labelRemoteHost.setText(QCoreApplication.translate("Dialog", u"Remote host:", None))
#if QT_CONFIG(tooltip)
        self.lineEditRemoteHost.setToolTip(QCoreApplication.translate("Dialog", u"ip address of remote host where we want to export our ISOs and packages", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelRemoteUser.setToolTip(QCoreApplication.translate("Dialog", u"user name to the uset to connect remote host", None))
#endif // QT_CONFIG(tooltip)
        self.labelRemoteUser.setText(QCoreApplication.translate("Dialog", u"Remote user:", None))
#if QT_CONFIG(tooltip)
        self.lineEditRemoteUser.setToolTip(QCoreApplication.translate("Dialog", u"user name to the uset to connect remote host", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelRemotePathIso.setToolTip(QCoreApplication.translate("Dialog", u"path on remote host where we store our ISOs files", None))
#endif // QT_CONFIG(tooltip)
        self.labelRemotePathIso.setText(QCoreApplication.translate("Dialog", u"Remote path ISOs:", None))
#if QT_CONFIG(tooltip)
        self.lineEditRemotePathIso.setToolTip(QCoreApplication.translate("Dialog", u"path on remote host where we store our ISOs files", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelRemotePathDeb.setToolTip(QCoreApplication.translate("Dialog", u"path on remote host where we store our DEBS packages", None))
#endif // QT_CONFIG(tooltip)
        self.labelRemotePathDeb.setText(QCoreApplication.translate("Dialog", u"Remote path packages deb:", None))
#if QT_CONFIG(tooltip)
        self.lineEditRemotePathDeb.setToolTip(QCoreApplication.translate("Dialog", u"path on remote host where we store our DEBS packages", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelFilterDeb.setToolTip(QCoreApplication.translate("Dialog", u"path on remote host where we store our DEBS packages", None))
#endif // QT_CONFIG(tooltip)
        self.labelFilterDeb.setText(QCoreApplication.translate("Dialog", u"Filter packages deb:", None))
#if QT_CONFIG(tooltip)
        self.lineEditFilterDeb.setToolTip(QCoreApplication.translate("Dialog", u"path on remote host where we store our DEBS packages", None))
#endif // QT_CONFIG(tooltip)
        self.lineEditFilterDeb.setPlaceholderText(QCoreApplication.translate("Dialog", u"eggs_9.*.*_ ", None))
    # retranslateUi

