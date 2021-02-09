# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/rjouretz/Documents/maya/2018/prefs/scripts/raphScripts/junkbox/ui/mainWindow.ui'
#
# Created: Tue Feb  9 22:23:08 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1149, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.newAssetButton = QtWidgets.QPushButton(self.centralwidget)
        self.newAssetButton.setObjectName("newAssetButton")
        self.horizontalLayout_2.addWidget(self.newAssetButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.searchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout_2.addWidget(self.searchLineEdit)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.pushButton = FlatButton(self.centralwidget)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.assetHierarchyWidget = AssetHierarchyWidget(self.centralwidget)
        self.assetHierarchyWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.assetHierarchyWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.assetHierarchyWidget.setObjectName("assetHierarchyWidget")
        self.horizontalLayout.addWidget(self.assetHierarchyWidget)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.assetViewWidget = AssetViewWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetViewWidget.sizePolicy().hasHeightForWidth())
        self.assetViewWidget.setSizePolicy(sizePolicy)
        self.assetViewWidget.setObjectName("assetViewWidget")
        self.horizontalLayout.addWidget(self.assetViewWidget)
        self.assetPreviewSeparator = QtWidgets.QFrame(self.centralwidget)
        self.assetPreviewSeparator.setFrameShape(QtWidgets.QFrame.VLine)
        self.assetPreviewSeparator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.assetPreviewSeparator.setObjectName("assetPreviewSeparator")
        self.horizontalLayout.addWidget(self.assetPreviewSeparator)
        self.assetPreviewContainerWidget = QtWidgets.QWidget(self.centralwidget)
        self.assetPreviewContainerWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.assetPreviewContainerWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.assetPreviewContainerWidget.setObjectName("assetPreviewContainerWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.assetPreviewContainerWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.assetPreviewWidget = AssetPreviewWidget(self.assetPreviewContainerWidget)
        self.assetPreviewWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.assetPreviewWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.assetPreviewWidget.setObjectName("assetPreviewWidget")
        self.verticalLayout_2.addWidget(self.assetPreviewWidget)
        self.horizontalLayout.addWidget(self.assetPreviewContainerWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1149, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.newAssetButton.setText(QtWidgets.QApplication.translate("MainWindow", "New Asset", None, -1))
        self.searchLineEdit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Search ...", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Shared Server", None, -1))
        self.comboBox.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "test", None, -1))

from raphScripts.junkbox.component.flatButton import FlatButton
from raphScripts.junkbox.component.assetViewWidget import AssetViewWidget
from raphScripts.junkbox.component.assetPreviewWidget import AssetPreviewWidget
from raphScripts.junkbox.component.assetHierarchyWidget import AssetHierarchyWidget
from raphScripts.junkbox.resource import resource_rc
