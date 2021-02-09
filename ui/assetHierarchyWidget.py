# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/rjouretz/Documents/maya/2018/prefs/scripts/raphScripts/junkbox/ui/assetHierarchyWidget.ui'
#
# Created: Tue Feb  9 22:23:08 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_assetHierarchyWidget(object):
    def setupUi(self, assetHierarchyWidget):
        assetHierarchyWidget.setObjectName("assetHierarchyWidget")
        assetHierarchyWidget.resize(299, 528)
        self.verticalLayout = QtWidgets.QVBoxLayout(assetHierarchyWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(assetHierarchyWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addCollectionButton = FlatButton(assetHierarchyWidget)
        self.addCollectionButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addCollectionButton.setIcon(icon)
        self.addCollectionButton.setObjectName("addCollectionButton")
        self.horizontalLayout_2.addWidget(self.addCollectionButton)
        self.removeCollectionButton = FlatButton(assetHierarchyWidget)
        self.removeCollectionButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeCollectionButton.setIcon(icon1)
        self.removeCollectionButton.setObjectName("removeCollectionButton")
        self.horizontalLayout_2.addWidget(self.removeCollectionButton)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget = DeselectableTreeWidget(assetHierarchyWidget)
        self.treeWidget.setStyleSheet("QTreeView::item {\n"
"    padding: 2px 0;\n"
"    border: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"     background-color: #5285A6;\n"
"}\n"
"\n"
"QTreeView{\n"
"    border: none;\n"
"    outline: 0;\n"
"}")
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setVisible(False)
        self.verticalLayout.addWidget(self.treeWidget)

        self.retranslateUi(assetHierarchyWidget)
        QtCore.QMetaObject.connectSlotsByName(assetHierarchyWidget)

    def retranslateUi(self, assetHierarchyWidget):
        assetHierarchyWidget.setWindowTitle(QtWidgets.QApplication.translate("assetHierarchyWidget", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("assetHierarchyWidget", "Collections", None, -1))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("assetHierarchyWidget", "1", None, -1))

from raphScripts.junkbox.component.deselectableTreeWidget import DeselectableTreeWidget
from raphScripts.junkbox.component.flatButton import FlatButton
from raphScripts.junkbox.resource import resource_rc
