# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:/sandbox/raphaelJ/junkbox/python/junkbox/ui/assetpreviewwidget.ui'
#
# Created: Mon Feb 22 15:59:01 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_assetPreviewWidget(object):
    def setupUi(self, assetPreviewWidget):
        assetPreviewWidget.setObjectName("assetPreviewWidget")
        assetPreviewWidget.resize(260, 527)
        self.verticalLayout = QtWidgets.QVBoxLayout(assetPreviewWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.singleAssetWidget = QtWidgets.QWidget(assetPreviewWidget)
        self.singleAssetWidget.setObjectName("singleAssetWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.singleAssetWidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.previewView = QtWidgets.QGraphicsView(self.singleAssetWidget)
        self.previewView.setMinimumSize(QtCore.QSize(0, 200))
        self.previewView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.previewView.setStyleSheet("background:transparent")
        self.previewView.setObjectName("previewView")
        self.verticalLayout_6.addWidget(self.previewView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.singleAssetWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.refreshButton = FlatButton(self.singleAssetWidget)
        self.refreshButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshButton.setIcon(icon)
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_2.addWidget(self.refreshButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.singleAssetWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.fileNameWidget = QtWidgets.QWidget(self.singleAssetWidget)
        self.fileNameWidget.setObjectName("fileNameWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fileNameWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileNameLabel = QtWidgets.QLabel(self.fileNameWidget)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.horizontalLayout.addWidget(self.fileNameLabel)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fileNameWidget)
        self.label_3 = QtWidgets.QLabel(self.singleAssetWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.fileTypeWidget = QtWidgets.QWidget(self.singleAssetWidget)
        self.fileTypeWidget.setObjectName("fileTypeWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fileTypeWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.fileTypeLabel = QtWidgets.QLabel(self.fileTypeWidget)
        self.fileTypeLabel.setObjectName("fileTypeLabel")
        self.verticalLayout_5.addWidget(self.fileTypeLabel)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fileTypeWidget)
        self.label_4 = QtWidgets.QLabel(self.singleAssetWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.fileSizeWidget = QtWidgets.QWidget(self.singleAssetWidget)
        self.fileSizeWidget.setObjectName("fileSizeWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.fileSizeWidget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.fileSizeLabel = QtWidgets.QLabel(self.fileSizeWidget)
        self.fileSizeLabel.setObjectName("fileSizeLabel")
        self.verticalLayout_7.addWidget(self.fileSizeLabel)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fileSizeWidget)
        self.label_7 = QtWidgets.QLabel(self.singleAssetWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.createdDateWidget = QtWidgets.QWidget(self.singleAssetWidget)
        self.createdDateWidget.setObjectName("createdDateWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.createdDateWidget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.fileCreatedDateLabel = QtWidgets.QLabel(self.createdDateWidget)
        self.fileCreatedDateLabel.setObjectName("fileCreatedDateLabel")
        self.verticalLayout_8.addWidget(self.fileCreatedDateLabel)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.createdDateWidget)
        self.lastModifiedDateLabel = QtWidgets.QLabel(self.singleAssetWidget)
        self.lastModifiedDateLabel.setObjectName("lastModifiedDateLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lastModifiedDateLabel)
        self.lastModifiedDateWidget = QtWidgets.QWidget(self.singleAssetWidget)
        self.lastModifiedDateWidget.setObjectName("lastModifiedDateWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.lastModifiedDateWidget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.fileLastModifiedDateLabel = QtWidgets.QLabel(self.lastModifiedDateWidget)
        self.fileLastModifiedDateLabel.setObjectName("fileLastModifiedDateLabel")
        self.verticalLayout_9.addWidget(self.fileLastModifiedDateLabel)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lastModifiedDateWidget)
        self.verticalLayout_6.addLayout(self.formLayout)
        self.blankWidget = QtWidgets.QWidget(self.singleAssetWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blankWidget.sizePolicy().hasHeightForWidth())
        self.blankWidget.setSizePolicy(sizePolicy)
        self.blankWidget.setObjectName("blankWidget")
        self.verticalLayout_6.addWidget(self.blankWidget)
        self.openInMayaButton = QtWidgets.QPushButton(self.singleAssetWidget)
        self.openInMayaButton.setObjectName("openInMayaButton")
        self.verticalLayout_6.addWidget(self.openInMayaButton)
        self.verticalLayout_2.addWidget(self.singleAssetWidget)
        self.multiAssetsWidget = QtWidgets.QWidget(assetPreviewWidget)
        self.multiAssetsWidget.setObjectName("multiAssetsWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.multiAssetsWidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.assetSelectedLabel = QtWidgets.QLabel(self.multiAssetsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetSelectedLabel.sizePolicy().hasHeightForWidth())
        self.assetSelectedLabel.setSizePolicy(sizePolicy)
        self.assetSelectedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.assetSelectedLabel.setObjectName("assetSelectedLabel")
        self.verticalLayout_4.addWidget(self.assetSelectedLabel)
        self.verticalLayout_2.addWidget(self.multiAssetsWidget)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.importReferenceButton = QtWidgets.QPushButton(assetPreviewWidget)
        self.importReferenceButton.setObjectName("importReferenceButton")
        self.verticalLayout_3.addWidget(self.importReferenceButton)
        self.importCopyButton = QtWidgets.QPushButton(assetPreviewWidget)
        self.importCopyButton.setObjectName("importCopyButton")
        self.verticalLayout_3.addWidget(self.importCopyButton)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(assetPreviewWidget)
        QtCore.QMetaObject.connectSlotsByName(assetPreviewWidget)

    def retranslateUi(self, assetPreviewWidget):
        assetPreviewWidget.setWindowTitle(QtWidgets.QApplication.translate("assetPreviewWidget", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "File summary", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "File name", None, -1))
        self.fileNameLabel.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "TextLabel", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "File type", None, -1))
        self.fileTypeLabel.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "TextLabel", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "File size", None, -1))
        self.fileSizeLabel.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "TextLabel", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "Created date", None, -1))
        self.fileCreatedDateLabel.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "TextLabel", None, -1))
        self.lastModifiedDateLabel.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "Last modified", None, -1))
        self.fileLastModifiedDateLabel.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "TextLabel", None, -1))
        self.openInMayaButton.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "open in Maya", None, -1))
        self.assetSelectedLabel.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "x assets selected", None, -1))
        self.importReferenceButton.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "import as reference", None, -1))
        self.importCopyButton.setText(QtWidgets.QApplication.translate("assetPreviewWidget", "import as copy", None, -1))

from junkbox.component.flatbutton import FlatButton
from junkbox.resource import resource_rc
