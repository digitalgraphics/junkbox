# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/rjouretz/Documents/maya/2018/prefs/scripts/raphScripts/junkbox/ui/settingsDialog.ui'
#
# Created: Wed Feb 10 18:08:53 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(615, 221)
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(SettingsDialog)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addButton = QtWidgets.QPushButton(SettingsDialog)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_2.addWidget(self.addButton)
        self.removeButton = QtWidgets.QPushButton(SettingsDialog)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout_2.addWidget(self.removeButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtWidgets.QApplication.translate("SettingsDialog", "Dialog", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("SettingsDialog", "name", None, -1))
        self.treeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("SettingsDialog", "path", None, -1))
        self.addButton.setText(QtWidgets.QApplication.translate("SettingsDialog", "Add", None, -1))
        self.removeButton.setText(QtWidgets.QApplication.translate("SettingsDialog", "Remove", None, -1))

