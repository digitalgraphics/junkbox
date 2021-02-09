from raphScripts.junkbox.component.thumbnailWidget import ThumbnailWidget
from raphScripts.junkbox.ui.assetViewWidget import Ui_assetViewWidget
from raphScripts.junkbox.manager.fileManager import FileManager

from PySide2.QtWidgets import QMainWindow, QWidget, QListWidget, QListWidgetItem, QTreeWidgetItem
from PySide2.QtCore import QSize, Qt, Signal
from PySide2.QtGui import QIcon, QPixmap

class AssetViewWidget(QWidget):
    selectionChanged = Signal(list)

    def __init__(self, parent=None):
        super(AssetViewWidget, self).__init__(parent)
        self.ui = Ui_assetViewWidget()
        self.ui.setupUi(self)

        self.ui.thumbnailViewWidget.setIconSize(QSize(100,100))

        self.ui.thumbnailViewWidget.itemSelectionChanged.connect(self.listSelectionChanged)
        self.ui.listViewWidget.itemSelectionChanged.connect(self.treeSelectionChanged)
        self.ui.searchEdit.textChanged.connect(self.textSearchChanged)

        self.ui.thumbnailSizeSlider.valueChanged.connect(self.setThumbnailSize)
        self.setThumbnailSize( self.ui.thumbnailSizeSlider.value())

        self.ui.styleViewButton.buttonPressed.connect(self.styleViewPressed)
        self.showThumbnailView()
        self.ui.collectionLabel.hide()
        self.ui.itemCountLabel.hide()

        self.assetList = []

    def textSearchChanged(self, text):
        self.ui.thumbnailViewWidget.blockSignals(True)
        self.ui.listViewWidget.blockSignals(True)

        self.loadFiles(self.fileList)

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
        self.ui.thumbnailViewWidget.setIconSize(QSize(size,size))  

    def treeSelectionChanged(self):
        selectedItems = self.ui.listViewWidget.selectedItems()
        selectedIndicesSet = set()

        for selectedItem in selectedItems:
            selectedIndicesSet.add(selectedItem.data(0, Qt.UserRole))

        self.updateSelectedItems(selectedIndicesSet)


    def listSelectionChanged(self ):
        selectedItems = self.ui.thumbnailViewWidget.selectedItems()
        selectedIndicesSet = set()

        for selectedItem in selectedItems:
            selectedIndicesSet.add(selectedItem.data( Qt.UserRole))

        self.updateSelectedItems(selectedIndicesSet)
        

    def updateSelectedItems(self, selectedIndicesSet ):

        # prevent from triggering the "select" event

        self.ui.thumbnailViewWidget.blockSignals(True)
        self.ui.listViewWidget.blockSignals(True)

        selectedFilePath = []

        for i in range(len(self.assetList)):

            listWidget = self.assetList[i][0]
            treeWidget = self.assetList[i][1]

            if i in selectedIndicesSet:
                listWidget.setSelected(True)
                treeWidget.setSelected(True)
                selectedFilePath.append( self.assetList[i][2])
            else:
                listWidget.setSelected(False)
                treeWidget.setSelected(False)

        self.selectionChanged.emit(selectedFilePath)

        # re activate the "select" event

        self.ui.thumbnailViewWidget.blockSignals(False)
        self.ui.listViewWidget.blockSignals(False)

    def setTitle( self, title):
        self.ui.collectionLabel.show()
        self.ui.collectionLabel.setText(title)

    def clear(self):
        self.ui.thumbnailViewWidget.clear()
        self.ui.listViewWidget.clear()
        self.assetList = []
    
    def loadFiles( self, fileList):  
        self.clear()

        filterText = self.ui.searchEdit.text()

        self.fileList = fileList

        nbShownFiles = 0

        for curDict in self.fileList:
            basename = FileManager.getFileBaseName(curDict["filePath"])

            if not filterText or filterText in basename:
                self.addItem( curDict["filePath"], curDict["thumbnailPath"])
                nbShownFiles += 1

        self.ui.itemCountLabel.show()

        if nbShownFiles < 2:
            self.ui.itemCountLabel.setText("( " + str(nbShownFiles) + " asset )")
        else:
            self.ui.itemCountLabel.setText("( " + str(nbShownFiles) + " assets )")

    def addItem(self, filePath, thumbnailPath):

        icon = QIcon(thumbnailPath)

        basename = FileManager.getFileBaseName(filePath)
        modifyDate = FileManager.getFileModifyDate(filePath)
        extensionType = FileManager.getFileExtensionType(filePath)
        fileSize = FileManager.getFileSize(filePath)


        # add into the list 

        listWidget = QListWidgetItem(icon, basename)
        listWidget.setData(Qt.UserRole, len(self.assetList) )

        self.ui.thumbnailViewWidget.addItem(listWidget)

        # add into the tree

        data = [basename, fileSize, extensionType, modifyDate]
        treeWidget = QTreeWidgetItem(self.ui.listViewWidget, data)
        treeWidget.setData(0, Qt.UserRole, len(self.assetList) )
        treeWidget.setIcon(0, icon)

        self.assetList.append( [ listWidget, treeWidget, filePath] )