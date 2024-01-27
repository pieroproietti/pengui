# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_editorWDADIr.ui'
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
        DialogTextEditor.resize(1024, 768)
        self.buttonBox = QDialogButtonBox(DialogTextEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(0, 668, 1024, 100))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.plainTextEdit = QPlainTextEdit(DialogTextEditor)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(0, 0, 1024, 668))

        self.retranslateUi(DialogTextEditor)
        self.buttonBox.accepted.connect(DialogTextEditor.accept)
        self.buttonBox.rejected.connect(DialogTextEditor.reject)

        QMetaObject.connectSlotsByName(DialogTextEditor)
    # setupUi

    def retranslateUi(self, DialogTextEditor):
        DialogTextEditor.setWindowTitle(QCoreApplication.translate("DialogTextEditor", u"Dialog", None))
    # retranslateUi

