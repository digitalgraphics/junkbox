from PySide2.QtWidgets import QWidget, QTreeWidgetItem, QInputDialog, QMessageBox
from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QIcon

from junkbox.resource import resource_rc
from junkbox.ui.assethierarchywidget import Ui_assetHierarchyWidget

import os
import junkbox.utils.file as fileUtils

"""
name : assetHierarchyWidget
description : QWidget that represents the rowsing collection hierarchy panel.
"""
class AssetHierarchyWidget(QWidget):
    collectionDoubleClicked = Signal(str)
    collectionClicked = Signal(str)
    collectionRemoved = Signal(str)
    collectionDeselected = Signal()

    def __init__(self, *args, **kwargs):
        super(AssetHierarchyWidget, self).__init__(*args, **kwargs)
        self.ui = Ui_assetHierarchyWidget()
        self.ui.setupUi(self)

        # connections
        self.ui.treeWidget.itemDoubleClicked.connect(self.elemDoubleClicked)
        self.ui.treeWidget.itemClicked.connect(self.elemClicked)
        self.ui.treeWidget.itemDeselected.connect(self.elemDeselected)
        self.ui.addCollectionButton.buttonPressed.connect(
            self.addCollectionClicked)
        self.ui.removeCollectionButton.buttonPressed.connect(
            self.removeCollectionClicked)

        # setup
        self.ui.treeWidget.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.dirPath = None

    """
    name : elemDeselected
    description : signals that collections are deselected
    """
    def elemDeselected(self):
        self.collectionDeselected.emit()

    """
    name : clear
    description : clear the current collection selection
    """
    def clear(self):
        self.ui.treeWidget.clear()

    """
    name : refresh
    description : refresh the folder displayed in the view
    """
    def refresh(self):
        self.setFolders(self.dirPath)

    """
    name : setFolders
    description : open a folder to display in the view
    param : 
        - dirpath : the directory path to open
        - filterKeyword : pattern to filter the files and folders
    """
    def setFolders(self, dirpath, filterKeyword=None):
        self.clear()
        self.dirPath = dirpath
        dirDict = fileUtils.getFolders(
            self.dirPath, filterKeyword, fileUtils.FilterMode.FolderAndFile)

        def createDir(item, curDict):
            for k, v in curDict.items():
                child = QTreeWidgetItem(item, [k])
                child.setIcon(0, QIcon(":/icon/collection.png"))

                createDir(child, v)

        createDir(self.ui.treeWidget, dirDict)

    """
    name : openCollectionPath
    description : open the hierarchy path to according to the given path
    param : 
        - collectionPath : the local path of an existing opened folder
    """
    def openCollectionPath(self, collectionPath):
        collections = collectionPath.split("/")
        parent = self.ui.treeWidget.invisibleRootItem()

        for collection in collections:
            if collection:
                nbChildren = parent.childCount()
                for i in range(nbChildren):
                    item = parent.child(i)
                    name = item.text(0)

                    if collection in name:
                        item.setExpanded(True)
                        parent = item
                        break

        if parent:
            self.ui.treeWidget.setCurrentItem(parent)
            self.ui.treeWidget.itemClicked.emit(parent, 0)

    """
    name : removeCollectionClicked
    description : remove the selected item from the collection
    """
    def removeCollectionClicked(self):
        selection = self.ui.treeWidget.selectedItems()

        if len(selection) < 1:
            self.removeCollection(None)
        else:
            self.removeCollection(selection[0])

    """
    name : removeCollection
    description : remove the given qtreewidgetitem from the collection
    param : 
        - item : the qtreewidgetitem to remove
    """
    def removeCollection(self, item):
        if not item:
            QMessageBox.warning(self, 'No collection selected',
                                'Please select a collection to remove', QMessageBox.StandardButton.Ok)
            return

        reply = QMessageBox.question(self, 'Delete a collection', 'Are you sure to delete the collection "' +
                                     item.text(0) + '" ?', QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.No:
            return

        parent = item.parent()

        if not parent:
            parent = self.ui.treeWidget.invisibleRootItem()

        fullpath = self.getCollectionPath(item, True)
        parent.takeChild(parent.indexOfChild(item))

        if fullpath[0] == "/" or fullpath[1] == "\\":
            fullpath = fullpath[1:]

        fileUtils.removeFolder(fullpath)
        self.collectionRemoved.emit(fullpath)

    """
    name : addCollectionClicked
    description : add a collection as child of the selected collection
    """
    def addCollectionClicked(self):
        selection = self.ui.treeWidget.selectedItems()
        parent = self.ui.treeWidget.invisibleRootItem()

        description = "New collection at root"

        if len(selection) > 0:
            parent = selection[0]
            description = "New collection inside " + parent.text(0)

        nameAlreadyExists = True

        while nameAlreadyExists:
            nameWrongFormat = True

            while nameWrongFormat:
                text, ok = QInputDialog.getText(
                    self, 'New collection', description)

                if not ok:
                    return

                if not text:
                    QMessageBox.warning(
                        self, 'Wrong name format', 'The name cannot be empty', QMessageBox.StandardButton.Ok)

                elif " " in text:
                    QMessageBox.warning(
                        self, 'Wrong name format', 'The name cannot contain spaces', QMessageBox.StandardButton.Ok)

                elif text[0].isdigit():
                    QMessageBox.warning(
                        self, 'Wrong name format', 'The name cannot start with a number', QMessageBox.StandardButton.Ok)

                else:
                    nameWrongFormat = False

            nameAlreadyExists = False

            child_count = parent.childCount()
            for i in range(child_count):
                item = parent.child(i)
                name = item.text(0)  # text at first (0) column

                if name == text:
                    nameAlreadyExists = True
                    QMessageBox.warning(self, 'Existing collection', 'The collection "' +
                                        name + '" already exists', QMessageBox.StandardButton.Ok)

        if ok and text:
            if len(selection) > 0:
                parent.setExpanded(True)
            self.addCollection(text, parent)

    """
    name : addCollection
    description : add a collection named 'name' as child of the given parent
    param : 
        - name : the name of the new collection
        - parent : the parent of the new collection 
    """
    def addCollection(self, name, parent):
        item = QTreeWidgetItem(parent, [name])
        item.setIcon(0, QIcon(":/icon/collection.png"))
        self.ui.treeWidget.setCurrentItem(item)
        fullpath = self.getCollectionPath(item, True)

        if fullpath[0] == "/" or fullpath[1] == "\\":
            fullpath = fullpath[1:]

        fileUtils.createFolder(fullpath)
        self.ui.treeWidget.itemClicked.emit(item, 0)

    """
    name : elemDoubleClicked
    description : emit the collectionDoubleClicked signal 
        with the local path of the selected collection
    param : 
        - collection : the selected collection
        - column : the selected column
    """
    def elemDoubleClicked(self, collection, column):
        localPath = self.getSelectedCollectionPath()
        self.collectionDoubleClicked.emit(localPath)

    """
    name : elemClicked
    description : emit the collectionClicked signal with the
        local path of the selected collection
    param : 
        - collection : the selected collection
        - column : the selected column
    """
    def elemClicked(self, collection, column):
        localPath = self.getSelectedCollectionPath()
        self.collectionClicked.emit(localPath)

    """
    name : getSelectedCOllectionName
    description : get the name of the selected collection
    return : the name of the selected collection
    """
    def getSelectedCollectionName(self):
        selection = self.ui.treeWidget.selectedItems()

        if len(selection) < 1:
            return ""

        return selection[0].text(0)

    """
    name : getSelectedCollectionPath
    description : get the path of the selected collection
    param : 
        - fullPath : True to get the fullpath (local otherwise)
    return : the path of the selected collection
    """
    def getSelectedCollectionPath(self, fullPath=False):
        selection = self.ui.treeWidget.selectedItems()

        if len(selection) < 1:
            return ""

        curItem = selection[0]

        return self.getCollectionPath(curItem, fullPath)

    """
    name : getCollectionPath
    description : get the path of the given collection
    param : 
        - fullPath : True to get the full path (local otherwise)
    return : the path of the selected collection
    """
    def getCollectionPath(self, item, fullPath=False):
        path = ""
        while type(item) != type(None):
            path = "/" + item.text(0) + path
            item = item.parent()

        if fullPath:
            if path[0] == "/" or path[1] == "\\":
                path = path[1:]

            return os.path.join(self.dirPath, path).replace("\\", "/")
        else:
            return path
