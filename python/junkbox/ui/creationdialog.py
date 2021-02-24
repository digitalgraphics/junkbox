# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:/sandbox/raphaelJ/junkbox/python/junkbox/ui/creationdialog.ui'
#
# Created: Mon Feb 22 15:59:02 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_creationDialog(object):
    def setupUi(self, creationDialog):
        creationDialog.setObjectName("creationDialog")
        creationDialog.resize(335, 514)
        self.verticalLayout = QtWidgets.QVBoxLayout(creationDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(creationDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.filenameLabel = QtWidgets.QLabel(self.groupBox_3)
        self.filenameLabel.setObjectName("filenameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.filenameLabel)
        self.filenameEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.filenameEdit.setObjectName("filenameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.filenameEdit)
        self.collectionLabel = QtWidgets.QLabel(self.groupBox_3)
        self.collectionLabel.setObjectName("collectionLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.collectionLabel)
        self.collectionWidget = QtWidgets.QWidget(self.groupBox_3)
        self.collectionWidget.setObjectName("collectionWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.collectionWidget)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.collectionPathEdit = QtWidgets.QLineEdit(self.collectionWidget)
        self.collectionPathEdit.setReadOnly(True)
        self.collectionPathEdit.setObjectName("collectionPathEdit")
        self.horizontalLayout_4.addWidget(self.collectionPathEdit)
        self.browseCollectionButton = FlatButton(self.collectionWidget)
        self.browseCollectionButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/collection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browseCollectionButton.setIcon(icon)
        self.browseCollectionButton.setObjectName("browseCollectionButton")
        self.horizontalLayout_4.addWidget(self.browseCollectionButton)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.collectionWidget)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.thumbnailWidget = ThumbnailWidget(creationDialog)
        self.thumbnailWidget.setObjectName("thumbnailWidget")
        self.verticalLayout.addWidget(self.thumbnailWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(creationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(creationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), creationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), creationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(creationDialog)

    def retranslateUi(self, creationDialog):
        creationDialog.setWindowTitle(QtWidgets.QApplication.translate("creationDialog", "Asset Creation", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("creationDialog", "New asset", None, -1))
        self.filenameLabel.setText(QtWidgets.QApplication.translate("creationDialog", "Asset name", None, -1))
        self.collectionLabel.setText(QtWidgets.QApplication.translate("creationDialog", "Collection", None, -1))

from junkbox.component.thumbnailwidget import ThumbnailWidget
from junkbox.component.flatbutton import FlatButton
from junkbox.resource import resource_rc
