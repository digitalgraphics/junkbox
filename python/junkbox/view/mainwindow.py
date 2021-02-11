from junkbox.ui.mainwindow import Ui_mainWindow
import junkbox.utils.file as fileUtils
from junkbox.view.creationdialog import CreationDialog
from junkbox.view.settingsdialog import SettingsDialog

from PySide2.QtWidgets import QMainWindow, QWidget, QListWidget, QListWidgetItem, QDialog, QMessageBox
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon, QPixmap

from maya import OpenMayaUI as omui
import maya.cmds as cmds
import maya.mel as mel
from shiboken2 import wrapInstance

import os
import sys


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
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.historyPath = [
            s for s in sys.path if 'prefs' in s][0] + "/junkbox_history.json"

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
        path = "H:/sandbox/raphaelJ/junkbox_assets_library"
        isEditable = False
        self.dataPaths = [[name, path, isEditable]]

        data = fileUtils.readJsonFile(self.historyPath)

        if len(data) > 0:
            for workingPath in data['workingPath']:
                self.dataPaths.append(
                    [workingPath['name'], workingPath['path'], True])

        self.updateWorkingDataPaths()

    def settingsPressed(self):
        settingsDialog = SettingsDialog(self.dataPaths)

        if settingsDialog.exec_():
            self.dataPaths = settingsDialog.getDataPaths()
            self.updateWorkingDataPaths()

    def updateWorkingDataPaths(self):
        prevText = self.ui.dataPathComboBox.currentText()

        self.ui.dataPathComboBox.clear()

        data = {}
        data['workingPath'] = []

        for name, path, isEditable in self.dataPaths:
            self.ui.dataPathComboBox.addItem(name)
            if name != self.dataPaths[0][0]:
                data['workingPath'].append({
                    'name': name,
                    'path': path
                })

        fileUtils.writeJsonFile(data, self.historyPath)

        self.ui.dataPathComboBox.setCurrentText(prevText)
        self.updateCurrentWorkingPath()

    def updateCurrentWorkingPath(self):
        name, path, isEditable = self.dataPaths[self.ui.dataPathComboBox.currentIndex(
        )]
        if fileUtils.existingPath(path):
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

            fileList = fileUtils.getMayaFilesFromFolder(
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
