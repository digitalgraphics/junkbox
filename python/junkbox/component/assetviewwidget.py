from junkbox.ui.assetviewwidget import Ui_assetViewWidget
import junkbox.utils.file as fileUtils
from junkbox.view.browsecollectiondialog import BrowseCollectionDialog

from PySide2.QtWidgets import QMainWindow, QWidget, QListWidget, QListWidgetItem, QTreeWidgetItem, QMessageBox
from PySide2.QtCore import QSize, Qt, Signal
from PySide2.QtGui import QIcon, QPixmap


class AssetViewWidget(QWidget):
    selectionChanged = Signal(list)

    def __init__(self, parent=None):
        super(AssetViewWidget, self).__init__(parent)
        self.ui = Ui_assetViewWidget()
        self.ui.setupUi(self)

        self.ui.thumbnailViewWidget.setIconSize(QSize(100, 100))

        self.ui.thumbnailViewWidget.itemSelectionChanged.connect(
            self.listSelectionChanged)
        self.ui.listViewWidget.itemSelectionChanged.connect(
            self.treeSelectionChanged)
        self.ui.searchEdit.textChanged.connect(self.textSearchChanged)
        self.ui.thumbnailSizeSlider.valueChanged.connect(self.setThumbnailSize)
        self.ui.styleViewButton.buttonPressed.connect(self.styleViewPressed)
        self.ui.changeCollectionButton.buttonPressed.connect(
            self.changeCollectionPressed)
        self.ui.removeButton.buttonPressed.connect(self.removePressed)

        self.setThumbnailSize(self.ui.thumbnailSizeSlider.value())

        self.showThumbnailView()
        self.ui.collectionLabel.hide()
        self.ui.itemCountLabel.hide()

        self.ui.changeCollectionButton.setEnabled(False)
        self.ui.removeButton.setEnabled(False)

        self.assetList = []
        self.rootDirPath = None

    def changeCollectionPressed(self):
        browseCollectionDialog = BrowseCollectionDialog(
            self.rootDirPath, self.parent())

        if browseCollectionDialog.exec_():
            filePaths = self.getFilePathSelected()
            curFolder = fileUtils.getFolderPathOfFile(filePaths[0])
            destFolder = browseCollectionDialog.getAbsolutePath()

            if fileUtils.normPath(curFolder) == fileUtils.normPath(destFolder):
                QMessageBox.warning(self, 'Destination and source match',
                                    'The destination collection corresponds to the source collection', QMessageBox.StandardButton.Ok)
            else:
                fileUtils.moveMayaFilesToDir(filePaths, destFolder)
                self.removeSelectedItems()

    def removePressed(self):
        filePaths = self.getFilePathSelected()

        message = 'Are you sure to delete 1 asset ?'

        if len(filePaths) > 1:
            message = 'Are you sure to delete ' + \
                str(len(filePaths)) + ' assets ?'

        reply = QMessageBox.question(
            self, 'Delete assets', message, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            fileUtils.removeMayaFiles(filePaths)
            self.removeSelectedItems()

    def textSearchChanged(self, text):
        self.ui.thumbnailViewWidget.blockSignals(True)
        self.ui.listViewWidget.blockSignals(True)

        self.loadFiles(self.fileList, self.title, self.rootDirPath)

        self.ui.thumbnailViewWidget.blockSignals(False)
        self.ui.listViewWidget.blockSignals(False)

    def setThumbnailSize(self, size):
        self.ui.assetViewWidget.setThumbnailSize(size)

    def styleViewPressed(self, index):
        if index == 1:
            self.showListView()
            self.ui.thumbnailSizeSlider.setEnabled(False)
        else:
            self.showThumbnailView()
            self.ui.thumbnailSizeSlider.setEnabled(True)

    def showListView(self):
        self.ui.thumbnailViewWidget.hide()
        self.ui.listViewWidget.show()

    def showThumbnailView(self):
        self.ui.listViewWidget.hide()
        self.ui.thumbnailViewWidget.show()

    def setThumbnailSize(self, size):
        self.ui.thumbnailViewWidget.setIconSize(QSize(size, size))

    def treeSelectionChanged(self):
        selectedItems = self.ui.listViewWidget.selectedItems()
        selectedIndicesSet = set()

        for selectedItem in selectedItems:
            selectedIndicesSet.add(selectedItem.data(0, Qt.UserRole))

        self.updateSelectedItems(selectedIndicesSet)

    def listSelectionChanged(self):
        selectedItems = self.ui.thumbnailViewWidget.selectedItems()
        selectedIndicesSet = set()

        for selectedItem in selectedItems:
            selectedIndicesSet.add(selectedItem.data(Qt.UserRole))

        self.updateSelectedItems(selectedIndicesSet)

    def removeSelectedItems(self):
        self.ui.thumbnailViewWidget.blockSignals(True)
        self.ui.listViewWidget.blockSignals(True)

        self.removeSelectedList()
        self.removeSelectedTree()

        self.ui.thumbnailViewWidget.clearSelection()
        self.ui.listViewWidget.clearSelection()

        self.ui.thumbnailViewWidget.blockSignals(False)
        self.ui.listViewWidget.blockSignals(False)

        self.ui.changeCollectionButton.setEnabled(False)
        self.ui.removeButton.setEnabled(False)

        self.selectionChanged.emit([])

    def removeSelectedList(self):
        selectedItems = self.ui.thumbnailViewWidget.selectedItems()

        if not selectedItems:
            return

        for item in selectedItems:
            self.ui.thumbnailViewWidget.takeItem(
                self.ui.thumbnailViewWidget.row(item))

    def removeSelectedTree(self):
        selectedItems = self.ui.listViewWidget.selectedItems()

        if not selectedItems:
            return

        for item in selectedItems:
            self.ui.listViewWidget.invisibleRootItem().removeChild(item)
            del item

    def getFilePathSelected(self):
        selectedItems = self.ui.listViewWidget.selectedItems()
        selectedFilePath = []

        for item in selectedItems:
            selectedFilePath.append(
                self.assetList[item.data(0, Qt.UserRole)][2])

        return selectedFilePath

    def updateSelectedItems(self, selectedIndicesSet):

        # prevent from triggering the "select" event

        self.ui.thumbnailViewWidget.blockSignals(True)
        self.ui.listViewWidget.blockSignals(True)

        if len(selectedIndicesSet) > 0:
            self.ui.changeCollectionButton.setEnabled(True)
            self.ui.removeButton.setEnabled(True)
        else:
            self.ui.changeCollectionButton.setEnabled(False)
            self.ui.removeButton.setEnabled(False)

        selectedFilePath = []

        for i in range(len(self.assetList)):

            listWidget = self.assetList[i][0]
            treeWidget = self.assetList[i][1]

            if i in selectedIndicesSet:
                listWidget.setSelected(True)
                treeWidget.setSelected(True)
                selectedFilePath.append(self.assetList[i][2])
            else:
                listWidget.setSelected(False)
                treeWidget.setSelected(False)

        self.selectionChanged.emit(selectedFilePath)

        # re activate the "select" event

        self.ui.thumbnailViewWidget.blockSignals(False)
        self.ui.listViewWidget.blockSignals(False)

    def setTitle(self, title):
        self.ui.collectionLabel.show()
        self.ui.collectionLabel.setText(title)

    def clear(self):
        self.ui.thumbnailViewWidget.clear()
        self.ui.listViewWidget.clear()
        self.ui.itemCountLabel.hide()
        self.ui.collectionLabel.hide()
        self.ui.changeCollectionButton.setEnabled(False)
        self.ui.removeButton.setEnabled(False)
        self.assetList = []

    def loadFolder(self, workingDirPath, rootDirPath):
        fileList = fileUtils.getMayaFilesFromFolder(workingDirPath)
        title = fileUtils.getFolderBaseName(workingDirPath)
        self.loadFiles(fileList, title, rootDirPath)

    def loadFiles(self, fileList, title, rootDirPath):
        self.rootDirPath = rootDirPath
        self.title = title
        self.clear()

        self.setTitle(title)

        filterText = self.ui.searchEdit.text()

        self.fileList = fileList

        nbShownFiles = 0

        for curDict in self.fileList:
            basename = fileUtils.getFileBaseName(curDict["filePath"])

            if not filterText or filterText.lower() in basename.lower():
                self.addItem(curDict["filePath"], curDict["thumbnailPath"])
                nbShownFiles += 1

        self.ui.itemCountLabel.show()

        if nbShownFiles < 2:
            self.ui.itemCountLabel.setText(
                "( " + str(nbShownFiles) + " asset )")
        else:
            self.ui.itemCountLabel.setText(
                "( " + str(nbShownFiles) + " assets )")

    def addItem(self, filePath, thumbnailPath):

        icon = QIcon(thumbnailPath)

        basename = fileUtils.getFileBaseName(filePath)
        modifyDate = fileUtils.getFileModifyDate(filePath)
        extensionType = fileUtils.getFileExtensionType(filePath)
        fileSize = fileUtils.getFileSize(filePath)

        # add into the list

        listWidget = QListWidgetItem(icon, basename)
        listWidget.setData(Qt.UserRole, len(self.assetList))

        self.ui.thumbnailViewWidget.addItem(listWidget)

        # add into the tree

        data = [basename, fileSize, extensionType, modifyDate]
        treeWidget = QTreeWidgetItem(self.ui.listViewWidget, data)
        treeWidget.setData(0, Qt.UserRole, len(self.assetList))
        treeWidget.setIcon(0, icon)

        self.assetList.append([listWidget, treeWidget, filePath])
