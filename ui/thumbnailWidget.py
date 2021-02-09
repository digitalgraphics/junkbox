# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/rjouretz/Documents/maya/2018/prefs/scripts/raphScripts/junkbox/ui/thumbnailWidget.ui'
#
# Created: Tue Feb  2 20:15:15 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_thumbnailWidget(object):
    def setupUi(self, thumbnailWidget):
        thumbnailWidget.setObjectName("thumbnailWidget")
        thumbnailWidget.resize(377, 330)
        self.verticalLayout = QtWidgets.QVBoxLayout(thumbnailWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.icon = QtWidgets.QLabel(thumbnailWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setObjectName("icon")
        self.verticalLayout.addWidget(self.icon)
        self.label = QtWidgets.QLabel(thumbnailWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(thumbnailWidget)
        QtCore.QMetaObject.connectSlotsByName(thumbnailWidget)

    def retranslateUi(self, thumbnailWidget):
        thumbnailWidget.setWindowTitle(QtWidgets.QApplication.translate("thumbnailWidget", "Form", None, -1))
        self.icon.setText(QtWidgets.QApplication.translate("thumbnailWidget", "TextLabel", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("thumbnailWidget", "TextLabel lkjglmkdjg mdslkgjsdgml kdfgjmldskgjfd msglkfdjgmlsd fkgjdmslgkdsjgmldsk", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    thumbnailWidget = QtWidgets.QWidget()
    ui = Ui_thumbnailWidget()
    ui.setupUi(thumbnailWidget)
    thumbnailWidget.show()
    sys.exit(app.exec_())

