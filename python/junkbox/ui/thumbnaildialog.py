# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Documents/maya/2020/prefs/scripts/junkbox/python/junkbox/ui/thumbnaildialog.ui'
#
# Created: Thu Feb 18 14:10:34 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_thumbnailDialog(object):
    def setupUi(self, thumbnailDialog):
        thumbnailDialog.setObjectName("thumbnailDialog")
        thumbnailDialog.resize(281, 394)
        self.verticalLayout = QtWidgets.QVBoxLayout(thumbnailDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.thumbnailWidget = ThumbnailWidget(thumbnailDialog)
        self.thumbnailWidget.setObjectName("thumbnailWidget")
        self.verticalLayout.addWidget(self.thumbnailWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(thumbnailDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(thumbnailDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), thumbnailDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), thumbnailDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(thumbnailDialog)

    def retranslateUi(self, thumbnailDialog):
        thumbnailDialog.setWindowTitle(QtWidgets.QApplication.translate("thumbnailDialog", "Thumbnail Creation", None, -1))

from junkbox.component.thumbnailwidget import ThumbnailWidget
