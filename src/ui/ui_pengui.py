# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'penguiCDRyud.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 1200)
        icon = QIcon()
        icon.addFile(u":/pengui/icons/pengui.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_Produce = QAction(MainWindow)
        self.action_Produce.setObjectName(u"action_Produce")
        self.action_Kill = QAction(MainWindow)
        self.action_Kill.setObjectName(u"action_Kill")
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.action_Configure = QAction(MainWindow)
        self.action_Configure.setObjectName(u"action_Configure")
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        self.action_Skel = QAction(MainWindow)
        self.action_Skel.setObjectName(u"action_Skel")
        self.action_Clean = QAction(MainWindow)
        self.action_Clean.setObjectName(u"action_Clean")
        self.action_Yolk = QAction(MainWindow)
        self.action_Yolk.setObjectName(u"action_Yolk")
        self.actionGet = QAction(MainWindow)
        self.actionGet.setObjectName(u"actionGet")
        self.actionList = QAction(MainWindow)
        self.actionList.setObjectName(u"actionList")
        self.actionShow = QAction(MainWindow)
        self.actionShow.setObjectName(u"actionShow")
        self.actionWear = QAction(MainWindow)
        self.actionWear.setObjectName(u"actionWear")
        self.actionRepository = QAction(MainWindow)
        self.actionRepository.setObjectName(u"actionRepository")
        self.actionBlog = QAction(MainWindow)
        self.actionBlog.setObjectName(u"actionBlog")
        self.actionUsersGuide = QAction(MainWindow)
        self.actionUsersGuide.setObjectName(u"actionUsersGuide")
        self.actionTelegram = QAction(MainWindow)
        self.actionTelegram.setObjectName(u"actionTelegram")
        self.actionConfigureTools = QAction(MainWindow)
        self.actionConfigureTools.setObjectName(u"actionConfigureTools")
        self.actionCUckoo = QAction(MainWindow)
        self.actionCUckoo.setObjectName(u"actionCUckoo")
        self.actionStatus = QAction(MainWindow)
        self.actionStatus.setObjectName(u"actionStatus")
        self.actionCalamaresInstall = QAction(MainWindow)
        self.actionCalamaresInstall.setObjectName(u"actionCalamaresInstall")
        self.actionCalamaresRemove = QAction(MainWindow)
        self.actionCalamaresRemove.setObjectName(u"actionCalamaresRemove")
        self.actionIPpaAdd = QAction(MainWindow)
        self.actionIPpaAdd.setObjectName(u"actionIPpaAdd")
        self.actionPpaRemove = QAction(MainWindow)
        self.actionPpaRemove.setObjectName(u"actionPpaRemove")
        self.actionFormatUSB = QAction(MainWindow)
        self.actionFormatUSB.setObjectName(u"actionFormatUSB")
        self.actionGetEggs = QAction(MainWindow)
        self.actionGetEggs.setObjectName(u"actionGetEggs")
        self.action_Tools = QAction(MainWindow)
        self.action_Tools.setObjectName(u"action_Tools")
        self.action_Eggs = QAction(MainWindow)
        self.action_Eggs.setObjectName(u"action_Eggs")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1600, 21))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menuCalamares = QMenu(self.menu_File)
        self.menuCalamares.setObjectName(u"menuCalamares")
        self.menu_Edit = QMenu(self.menubar)
        self.menu_Edit.setObjectName(u"menu_Edit")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        self.menu_Tools = QMenu(self.menubar)
        self.menu_Tools.setObjectName(u"menu_Tools")
        self.menuPPA = QMenu(self.menu_Tools)
        self.menuPPA.setObjectName(u"menuPPA")
        self.menuWardrobe = QMenu(self.menubar)
        self.menuWardrobe.setObjectName(u"menuWardrobe")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Tools.menuAction())
        self.menubar.addAction(self.menuWardrobe.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_File.addAction(self.menuCalamares.menuAction())
        self.menu_File.addAction(self.action_Produce)
        self.menu_File.addAction(self.action_Kill)
        self.menu_File.addAction(self.actionStatus)
        self.menu_File.addAction(self.actionCUckoo)
        self.menu_File.addAction(self.action_Exit)
        self.menuCalamares.addAction(self.actionCalamaresInstall)
        self.menuCalamares.addAction(self.actionCalamaresRemove)
        self.menu_Edit.addAction(self.action_Tools)
        self.menu_Edit.addAction(self.action_Eggs)
        self.menu_Help.addAction(self.actionUsersGuide)
        self.menu_Help.addAction(self.actionBlog)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.actionRepository)
        self.menu_Help.addAction(self.actionTelegram)
        self.menu_Help.addAction(self.action_About)
        self.menu_Tools.addAction(self.action_Clean)
        self.menu_Tools.addAction(self.menuPPA.menuAction())
        self.menu_Tools.addAction(self.action_Skel)
        self.menu_Tools.addAction(self.action_Yolk)
        self.menuPPA.addAction(self.actionIPpaAdd)
        self.menuPPA.addAction(self.actionPpaRemove)
        self.menuWardrobe.addAction(self.actionGet)
        self.menuWardrobe.addAction(self.actionList)
        self.menuWardrobe.addAction(self.actionShow)
        self.menuWardrobe.addAction(self.actionWear)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_Produce.setText(QCoreApplication.translate("MainWindow", u"&Produce", None))
        self.action_Kill.setText(QCoreApplication.translate("MainWindow", u"&Kill", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
        self.action_Configure.setText(QCoreApplication.translate("MainWindow", u"&Dad", None))
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"&About", None))
        self.action_Skel.setText(QCoreApplication.translate("MainWindow", u"&Skel", None))
        self.action_Clean.setText(QCoreApplication.translate("MainWindow", u"&Clean", None))
        self.action_Yolk.setText(QCoreApplication.translate("MainWindow", u"&Yolk", None))
        self.actionGet.setText(QCoreApplication.translate("MainWindow", u"&Get", None))
        self.actionList.setText(QCoreApplication.translate("MainWindow", u"&List", None))
        self.actionShow.setText(QCoreApplication.translate("MainWindow", u"&Show", None))
        self.actionWear.setText(QCoreApplication.translate("MainWindow", u"&Wear", None))
        self.actionRepository.setText(QCoreApplication.translate("MainWindow", u"&Repository", None))
        self.actionBlog.setText(QCoreApplication.translate("MainWindow", u"&Blog", None))
        self.actionUsersGuide.setText(QCoreApplication.translate("MainWindow", u"&Users' guide", None))
        self.actionTelegram.setText(QCoreApplication.translate("MainWindow", u"&Telegram", None))
        self.actionConfigureTools.setText(QCoreApplication.translate("MainWindow", u"&Tools", None))
        self.actionCUckoo.setText(QCoreApplication.translate("MainWindow", u"C&uckoo", None))
        self.actionStatus.setText(QCoreApplication.translate("MainWindow", u"&Status", None))
        self.actionCalamaresInstall.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.actionCalamaresRemove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.actionIPpaAdd.setText(QCoreApplication.translate("MainWindow", u"&Add", None))
        self.actionPpaRemove.setText(QCoreApplication.translate("MainWindow", u"&Remove", None))
        self.actionFormatUSB.setText(QCoreApplication.translate("MainWindow", u"Format USB", None))
        self.actionGetEggs.setText(QCoreApplication.translate("MainWindow", u"&Eggs", None))
        self.action_Tools.setText(QCoreApplication.translate("MainWindow", u"&Tools", None))
        self.action_Eggs.setText(QCoreApplication.translate("MainWindow", u"&Eggs", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuCalamares.setTitle(QCoreApplication.translate("MainWindow", u"&Calamares", None))
        self.menu_Edit.setTitle(QCoreApplication.translate("MainWindow", u"&Edit", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.menu_Tools.setTitle(QCoreApplication.translate("MainWindow", u"&Tools", None))
        self.menuPPA.setTitle(QCoreApplication.translate("MainWindow", u"&PPA", None))
        self.menuWardrobe.setTitle(QCoreApplication.translate("MainWindow", u"&Wardrobe", None))
    # retranslateUi

