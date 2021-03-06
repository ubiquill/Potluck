# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mw.ui'
#
# Created: Thu Jul 21 21:29:00 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(611, 509)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QtCore.Qt.ArrowCursor)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/potlucklogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777204, 16777215))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.queryEdit = QtGui.QLineEdit(self.centralwidget)
        self.queryEdit.setInputMask(_fromUtf8(""))
        self.queryEdit.setObjectName(_fromUtf8("queryEdit"))
        self.horizontalLayout.addWidget(self.queryEdit)
        self.queryButton = QtGui.QPushButton(self.centralwidget)
        self.queryButton.setEnabled(True)
        self.queryButton.setObjectName(_fromUtf8("queryButton"))
        self.horizontalLayout.addWidget(self.queryButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.queryList = QtGui.QTreeWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.queryList.sizePolicy().hasHeightForWidth())
        self.queryList.setSizePolicy(sizePolicy)
        self.queryList.setUniformRowHeights(True)
        self.queryList.setItemsExpandable(True)
        self.queryList.setAllColumnsShowFocus(False)
        self.queryList.setColumnCount(4)
        self.queryList.setObjectName(_fromUtf8("queryList"))
        self.queryList.header().setCascadingSectionResizes(False)
        self.queryList.header().setDefaultSectionSize(75)
        self.queryList.header().setHighlightSections(False)
        self.queryList.header().setMinimumSectionSize(5)
        self.queryList.header().setSortIndicatorShown(True)
        self.queryList.header().setStretchLastSection(True)
        self.horizontalLayout_2.addWidget(self.queryList)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.applyButton = QtGui.QPushButton(self.centralwidget)
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.horizontalLayout_5.addWidget(self.applyButton)
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.horizontalLayout_5.addWidget(self.quitButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMinimumSize(QtCore.QSize(100, 0))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSync = QtGui.QAction(MainWindow)
        self.actionSync.setObjectName(_fromUtf8("actionSync"))
        self.actionUpgrade = QtGui.QAction(MainWindow)
        self.actionUpgrade.setObjectName(_fromUtf8("actionUpgrade"))
        self.actionView_Changes = QtGui.QAction(MainWindow)
        self.actionView_Changes.setObjectName(_fromUtf8("actionView_Changes"))
        self.actionClear_Changes = QtGui.QAction(MainWindow)
        self.actionClear_Changes.setObjectName(_fromUtf8("actionClear_Changes"))
        self.toolBar.addAction(self.actionSync)
        self.toolBar.addAction(self.actionUpgrade)
        self.toolBar.addAction(self.actionView_Changes)
        self.toolBar.addAction(self.actionClear_Changes)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Potluck", None, QtGui.QApplication.UnicodeUTF8))
        self.queryEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Cool App....", None, QtGui.QApplication.UnicodeUTF8))
        self.queryButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.queryList.setSortingEnabled(True)
        self.queryList.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Installed", None, QtGui.QApplication.UnicodeUTF8))
        self.queryList.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Repo", None, QtGui.QApplication.UnicodeUTF8))
        self.queryList.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.queryList.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.applyButton.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSync.setText(QtGui.QApplication.translate("MainWindow", "Sync", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSync.setToolTip(QtGui.QApplication.translate("MainWindow", "Refresh Package Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpgrade.setText(QtGui.QApplication.translate("MainWindow", "Mark Upgrades", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpgrade.setToolTip(QtGui.QApplication.translate("MainWindow", "Upgrade All Currently Installed Applications", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView_Changes.setText(QtGui.QApplication.translate("MainWindow", "View Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView_Changes.setToolTip(QtGui.QApplication.translate("MainWindow", "List All Packages That Will Be Altered", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear_Changes.setText(QtGui.QApplication.translate("MainWindow", "Clear Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear_Changes.setToolTip(QtGui.QApplication.translate("MainWindow", "Undo All Changes", None, QtGui.QApplication.UnicodeUTF8))

from . import icons_rc
