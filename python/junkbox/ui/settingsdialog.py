# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Documents/maya/2020/prefs/scripts/junkbox/python/junkbox/ui/settingsdialog.ui'
#
# Created: Thu Feb 18 14:10:34 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName("settingsDialog")
        settingsDialog.resize(615, 221)
        self.verticalLayout = QtWidgets.QVBoxLayout(settingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = DeselectableTreeWidget(settingsDialog)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addButton = QtWidgets.QPushButton(settingsDialog)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_2.addWidget(self.addButton)
        self.removeButton = QtWidgets.QPushButton(settingsDialog)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout_2.addWidget(self.removeButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(settingsDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.filePathEdit = QtWidgets.QLineEdit(settingsDialog)
        self.filePathEdit.setEnabled(False)
        self.filePathEdit.setReadOnly(True)
        self.filePathEdit.setObjectName("filePathEdit")
        self.horizontalLayout_2.addWidget(self.filePathEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(settingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(settingsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), settingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), settingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(QtWidgets.QApplication.translate("settingsDialog", "Settings", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("settingsDialog", "name", None, -1))
        self.treeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("settingsDialog", "repository path", None, -1))
        self.addButton.setText(QtWidgets.QApplication.translate("settingsDialog", "Add", None, -1))
        self.removeButton.setText(QtWidgets.QApplication.translate("settingsDialog", "Remove", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("settingsDialog", "settings file path : ", None, -1))

from junkbox.component.deselectabletreewidget import DeselectableTreeWidget
from junkbox.resource import resource_rc
