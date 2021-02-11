# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:/sandbox/raphaelJ/junkbox/python/junkbox/ui/mainwindow.ui'
#
# Created: Thu Feb 11 17:32:55 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1149, 602)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
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
        self.searchEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout_2.addWidget(self.searchEdit)
        self.dataPathComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.dataPathComboBox.setObjectName("dataPathComboBox")
        self.dataPathComboBox.addItem("")
        self.dataPathComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.dataPathComboBox)
        self.settingsButton = FlatButton(self.centralwidget)
        self.settingsButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon)
        self.settingsButton.setObjectName("settingsButton")
        self.horizontalLayout_2.addWidget(self.settingsButton)
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
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1149, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtWidgets.QApplication.translate("mainWindow", "MainWindow", None, -1))
        self.newAssetButton.setText(QtWidgets.QApplication.translate("mainWindow", "New Asset", None, -1))
        self.searchEdit.setPlaceholderText(QtWidgets.QApplication.translate("mainWindow", "Search ...", None, -1))
        self.dataPathComboBox.setItemText(0, QtWidgets.QApplication.translate("mainWindow", "Shared Server", None, -1))
        self.dataPathComboBox.setItemText(1, QtWidgets.QApplication.translate("mainWindow", "test", None, -1))

from junkbox.component.flatbutton import FlatButton
from junkbox.component.assetviewwidget import AssetViewWidget
from junkbox.component.assetpreviewwidget import AssetPreviewWidget
from junkbox.component.assethierarchywidget import AssetHierarchyWidget
from junkbox.resource import resource_rc
