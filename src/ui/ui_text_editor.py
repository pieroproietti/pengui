# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_editorSdDGAc.ui'
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
    QPlainTextEdit, QSizePolicy, QWidget)

class Ui_DialogTextEditor(object):
    def setupUi(self, DialogTextEditor):
        if not DialogTextEditor.objectName():
            DialogTextEditor.setObjectName(u"DialogTextEditor")
        DialogTextEditor.resize(1600, 1200)
        DialogTextEditor.setMinimumSize(QSize(800, 600))
        DialogTextEditor.setMaximumSize(QSize(1600, 1200))
        self.buttonBox = QDialogButtonBox(DialogTextEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(0, 1100, 1600, 100))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.plainTextEdit = QPlainTextEdit(DialogTextEditor)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(100, 0, 1600, 1000))

        self.retranslateUi(DialogTextEditor)
        self.buttonBox.accepted.connect(DialogTextEditor.accept)
        self.buttonBox.rejected.connect(DialogTextEditor.reject)

        QMetaObject.connectSlotsByName(DialogTextEditor)
    # setupUi

    def retranslateUi(self, DialogTextEditor):
        DialogTextEditor.setWindowTitle(QCoreApplication.translate("DialogTextEditor", u"Dialog", None))
    # retranslateUi

