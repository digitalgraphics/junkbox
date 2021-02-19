# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Documents/maya/2020/prefs/scripts/junkbox/python/junkbox/ui/thumbnailwidget.ui'
#
# Created: Thu Feb 18 14:10:34 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_thumbnailWidget(object):
    def setupUi(self, thumbnailWidget):
        thumbnailWidget.setObjectName("thumbnailWidget")
        thumbnailWidget.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(thumbnailWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.manualScreenshotBox = QtWidgets.QGroupBox(thumbnailWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manualScreenshotBox.sizePolicy().hasHeightForWidth())
        self.manualScreenshotBox.setSizePolicy(sizePolicy)
        self.manualScreenshotBox.setCheckable(True)
        self.manualScreenshotBox.setChecked(False)
        self.manualScreenshotBox.setObjectName("manualScreenshotBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.manualScreenshotBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.captureButton = QtWidgets.QPushButton(self.manualScreenshotBox)
        self.captureButton.setObjectName("captureButton")
        self.horizontalLayout_3.addWidget(self.captureButton)
        self.verticalLayout.addWidget(self.manualScreenshotBox)
        self.groupBox = QtWidgets.QGroupBox(thumbnailWidget)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previewView = QtWidgets.QGraphicsView(self.groupBox)
        self.previewView.setStyleSheet("background: transparent")
        self.previewView.setObjectName("previewView")
        self.horizontalLayout_2.addWidget(self.previewView)
        self.emptySelectionLabel = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emptySelectionLabel.sizePolicy().hasHeightForWidth())
        self.emptySelectionLabel.setSizePolicy(sizePolicy)
        self.emptySelectionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.emptySelectionLabel.setObjectName("emptySelectionLabel")
        self.horizontalLayout_2.addWidget(self.emptySelectionLabel)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(thumbnailWidget)
        QtCore.QMetaObject.connectSlotsByName(thumbnailWidget)

    def retranslateUi(self, thumbnailWidget):
        thumbnailWidget.setWindowTitle(QtWidgets.QApplication.translate("thumbnailWidget", "Form", None, -1))
        self.manualScreenshotBox.setTitle(QtWidgets.QApplication.translate("thumbnailWidget", "Manual Screenshot", None, -1))
        self.captureButton.setText(QtWidgets.QApplication.translate("thumbnailWidget", "Capture", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("thumbnailWidget", "Preview", None, -1))
        self.emptySelectionLabel.setText(QtWidgets.QApplication.translate("thumbnailWidget", "Empty Selection", None, -1))

