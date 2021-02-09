# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/rjouretz/Documents/maya/2018/prefs/scripts/raphScripts/junkbox/ui/browseCollectionDialog.ui'
#
# Created: Tue Feb  9 10:39:54 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_BrowseCollectionDialog(object):
    def setupUi(self, BrowseCollectionDialog):
        BrowseCollectionDialog.setObjectName("BrowseCollectionDialog")
        BrowseCollectionDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(BrowseCollectionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.assetHierarchyWidget = AssetHierarchyWidget(BrowseCollectionDialog)
        self.assetHierarchyWidget.setObjectName("assetHierarchyWidget")
        self.verticalLayout.addWidget(self.assetHierarchyWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(BrowseCollectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(BrowseCollectionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), BrowseCollectionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), BrowseCollectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BrowseCollectionDialog)

    def retranslateUi(self, BrowseCollectionDialog):
        BrowseCollectionDialog.setWindowTitle(QtWidgets.QApplication.translate("BrowseCollectionDialog", "Dialog", None, -1))

from raphScripts.junkbox.component.assetHierarchyWidget import AssetHierarchyWidget
