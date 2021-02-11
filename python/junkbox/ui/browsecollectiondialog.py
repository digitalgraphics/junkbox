# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:/sandbox/raphaelJ/junkbox/python/junkbox/ui/browsecollectiondialog.ui'
#
# Created: Thu Feb 11 17:32:55 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_browseCollectionDialog(object):
    def setupUi(self, browseCollectionDialog):
        browseCollectionDialog.setObjectName("browseCollectionDialog")
        browseCollectionDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(browseCollectionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.assetHierarchyWidget = AssetHierarchyWidget(browseCollectionDialog)
        self.assetHierarchyWidget.setObjectName("assetHierarchyWidget")
        self.verticalLayout.addWidget(self.assetHierarchyWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(browseCollectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(browseCollectionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), browseCollectionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), browseCollectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(browseCollectionDialog)

    def retranslateUi(self, browseCollectionDialog):
        browseCollectionDialog.setWindowTitle(QtWidgets.QApplication.translate("browseCollectionDialog", "Dialog", None, -1))

from junkbox.component.assethierarchywidget import AssetHierarchyWidget
