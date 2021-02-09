from raphScripts.junkbox.resource import resource_rc
from raphScripts.junkbox.manager.fileManager import FileManager
from raphScripts.junkbox.manager.mayaManager import MayaManager
from raphScripts.junkbox.ui.assetPreviewWidget import Ui_assetPreviewWidget
from raphScripts.junkbox.view.browseCollectionDialog import BrowseCollectionDialog

from PySide2.QtWidgets import QWidget, QMessageBox, QGraphicsScene
from PySide2.QtCore import QSize, Qt, Signal
from PySide2.QtGui import QIcon, QPixmap

import os

class AssetPreviewWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(AssetPreviewWidget, self).__init__(*args, **kwargs)
        self.ui = Ui_assetPreviewWidget()
        self.ui.setupUi(self)

        self.ui.importCopyButton.clicked.connect(self.importCopyClicked)
        self.ui.importReferenceButton.clicked.connect(self.importReferenceClicked)
        self.ui.openInMayaButton.clicked.connect(self.openInMayaClicked)

        self.filePaths = None

    def openInMayaClicked( self ):
        MayaManager.openInMaya(self.filePaths[0])

    def importCopyClicked( self ):
        for path in self.filePaths:
            MayaManager.importScene( path, asReference=False )

    def importReferenceClicked( self ):
        for path in self.filePaths:
            MayaManager.importScene( path, asReference=True )

    def previewFiles( self, filePaths):
        self.filePaths = filePaths

        nbFiles = len( self.filePaths )

        if nbFiles > 1:
            self.ui.assetSelectedLabel.setText(str(nbFiles) + " assets selected")
            self.ui.singleAssetWidget.hide()
            self.ui.multiAssetsWidget.show()
        else:
            self.ui.multiAssetsWidget.hide()
            self.ui.singleAssetWidget.show()
            
            self.updateInfo(self.filePaths[0])

    def updateInfo( self, filePath):
        self.setThumbnail( FileManager.getFileThumbnail(filePath))
        self.ui.fileNameLabel.setText( FileManager.getFileBaseName(filePath))
        self.ui.fileTypeLabel.setText( FileManager.getFileExtensionType(filePath))
        self.ui.fileSizeLabel.setText( FileManager.getFileSize(filePath))
        self.ui.fileCreatedDateLabel.setText( FileManager.getFileCreationDate(filePath))
        self.ui.fileLastModifiedDateLabel.setText( FileManager.getFileModifyDate(filePath))

    def setThumbnail( self, pixmap):
        self.ui.blankWidget.hide()

        scene = QGraphicsScene()
        self.ui.previewView.setScene(scene)
        scene.addPixmap(pixmap)
        self.ui.previewView.fitInView(scene.itemsBoundingRect(),Qt.KeepAspectRatio)

        self.ui.blankWidget.show()


