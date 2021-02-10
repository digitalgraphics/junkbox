if True:
    for i in range(2):
        import raphScripts.junkbox.component.flatButton
        reload(raphScripts.junkbox.component.flatButton)
        import raphScripts.junkbox.resource
        reload(raphScripts.junkbox.resource)

        import raphScripts.junkbox.manager.fileManager
        reload(raphScripts.junkbox.manager.fileManager)
        import raphScripts.junkbox.manager.mayaManager
        reload(raphScripts.junkbox.manager.mayaManager)
        import raphScripts.junkbox.manager.thumbnailManager
        reload(raphScripts.junkbox.manager.thumbnailManager)

        import raphScripts.junkbox.view.settingsDialog
        reload(raphScripts.junkbox.view.settingsDialog)
        import raphScripts.junkbox.view.browseCollectionDialog
        reload(raphScripts.junkbox.view.browseCollectionDialog)
        import raphScripts.junkbox.view.creationDialog
        reload(raphScripts.junkbox.view.creationDialog)

        import raphScripts.junkbox.component.thumbnailWidget
        reload(raphScripts.junkbox.component.thumbnailWidget)
        import raphScripts.junkbox.component.assetPreviewWidget
        reload(raphScripts.junkbox.component.assetPreviewWidget)
        import raphScripts.junkbox.component.assetViewWidget
        reload(raphScripts.junkbox.component.assetViewWidget)
        import raphScripts.junkbox.component.deselectableTreeWidget
        reload(raphScripts.junkbox.component.deselectableTreeWidget)
        import raphScripts.junkbox.component.assetHierarchyWidget
        reload(raphScripts.junkbox.component.assetHierarchyWidget)
        import raphScripts.junkbox.component.asset
        reload(raphScripts.junkbox.component.asset)

        import raphScripts.junkbox.ui.settingsDialog
        reload(raphScripts.junkbox.ui.settingsDialog)
        import raphScripts.junkbox.ui.assetPreviewWidget
        reload(raphScripts.junkbox.ui.assetPreviewWidget)
        import raphScripts.junkbox.ui.browseCollectionDialog
        reload(raphScripts.junkbox.ui.browseCollectionDialog)
        import raphScripts.junkbox.ui.creationDialog
        reload(raphScripts.junkbox.ui.creationDialog)
        import raphScripts.junkbox.ui.assetHierarchyWidget
        reload(raphScripts.junkbox.ui.assetHierarchyWidget)
        import raphScripts.junkbox.ui.assetViewWidget
        reload(raphScripts.junkbox.ui.assetViewWidget)
        import raphScripts.junkbox.ui.mainWindow
        reload(raphScripts.junkbox.ui.mainWindow)


from raphScripts.junkbox.ui.mainWindow import Ui_MainWindow
from raphScripts.junkbox.component.asset import Asset
from raphScripts.junkbox.manager.fileManager import FileManager, FilterMode
from raphScripts.junkbox.view.creationDialog import CreationDialog
from raphScripts.junkbox.view.settingsDialog import SettingsDialog

from PySide2.QtWidgets import QMainWindow, QWidget, QListWidget, QListWidgetItem, QDialog, QMessageBox
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon, QPixmap

from maya import OpenMayaUI as omui
import maya.cmds as cmds
import maya.mel as mel
from shiboken2 import wrapInstance

import os


def maya_main_window():
    '''
        Return the Maya main window widget as a Python object
        '''
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QWidget)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        parent = maya_main_window()
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.newAssetButton.clicked.connect(self.openCreationDialog)
        self.ui.assetHierarchyWidget.collectionClicked.connect(
            self.collectionClicked)
        self.ui.assetHierarchyWidget.collectionRemoved.connect(
            self.collectionRemoved)
        self.ui.assetHierarchyWidget.collectionDeselected.connect(
            self.collectionDeselected)
        self.ui.assetViewWidget.selectionChanged.connect(self.selectionChanged)
        self.ui.searchEdit.textChanged.connect(self.textSearchChanged)
        self.ui.settingsButton.buttonPressed.connect(self.settingsPressed)
        self.ui.dataPathComboBox.currentIndexChanged.connect(
            self.updateCurrentWorkingPath)

        self.hidePreview()
        self.creationDialog = None

        name = "Shared Server"
        path = "C:/Users/rjouretz/Documents/maya/2018/prefs/scripts/raphScripts/junkbox/DATA"
        isEditable = False
        self.dataPaths = [[name, path, isEditable]]
        self.updateWorkingDataPaths()

    def settingsPressed(self):
        settingsDialog = SettingsDialog(self.dataPaths, self.parent())

        if settingsDialog.exec_():
            self.dataPaths = settingsDialog.getDataPaths()
            self.updateWorkingDataPaths()

    def updateWorkingDataPaths(self):
        prevText = self.ui.dataPathComboBox.currentText()

        self.ui.dataPathComboBox.clear()

        for name, path, isEditable in self.dataPaths:
            self.ui.dataPathComboBox.addItem(name)

        self.ui.dataPathComboBox.setCurrentText(prevText)
        self.updateCurrentWorkingPath()

    def updateCurrentWorkingPath(self):
        name, path, isEditable = self.dataPaths[self.ui.dataPathComboBox.currentIndex(
        )]
        if FileManager.existingPath(path):
            self.workingDirPath = path
            self.ui.assetHierarchyWidget.setFolders(self.workingDirPath)
        else:
            self.workingDirPath = None
            QMessageBox.warning(self, 'Wrong working path',
                                'The selected working path does not exist', QMessageBox.StandardButton.Ok)

    def textSearchChanged(self, text):
        text = None if not text else text

        if text == None:
            self.ui.assetHierarchyWidget.setFolders(self.workingDirPath)
            self.ui.assetViewWidget.clear()
        else:
            self.ui.assetHierarchyWidget.setFolders(self.workingDirPath, text)

            fileList = FileManager.getMayaFilesFromFolder(
                self.workingDirPath, text, True)
            title = "search inside " + self.ui.dataPathComboBox.currentText()
            self.ui.assetViewWidget.loadFiles(
                fileList, title, self.workingDirPath)

    def hidePreview(self):
        self.ui.assetPreviewWidget.hide()

    def showPreview(self):
        self.ui.assetPreviewWidget.show()

    def collectionRemoved(self, dirPath):
        self.hidePreview()
        self.ui.assetViewWidget.clear()

    def collectionDeselected(self):
        self.hidePreview()
        self.ui.assetViewWidget.clear()

    def selectionChanged(self, filePaths):
        for i in range(2):
            if len(filePaths) < 1:
                self.hidePreview()
                return

            self.showPreview()
            self.ui.assetPreviewWidget.previewFiles(filePaths)

    def collectionClicked(self, path):
        fullPath = self.ui.assetHierarchyWidget.getSelectedCollectionPath(True)
        self.ui.assetViewWidget.loadFolder(fullPath, self.workingDirPath)

    def openCreationDialog(self):
        self.creationDialog = CreationDialog(self.workingDirPath, self)
        self.creationDialog.finished.connect(self.finishedCreationDialog)

        localPath = self.ui.assetHierarchyWidget.getSelectedCollectionPath()
        self.creationDialog.show()

        if localPath:
            self.creationDialog.setCollectionPath(localPath)

    def finishedCreationDialog(self, state):
        self.ui.assetHierarchyWidget.refresh()

        if state == QDialog.Accepted:
            collectionPath = self.creationDialog.getCollectionPath()
            self.ui.assetHierarchyWidget.openCollectionPath(collectionPath)
