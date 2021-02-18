from PySide2.QtWidgets import QWidget, QGraphicsScene, QMessageBox, QDialog
from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QPixmap

from junkbox.ui.assetpreviewwidget import Ui_assetPreviewWidget
from junkbox.view.thumbnaildialog import ThumbnailDialog

import junkbox.utils.file as fileUtils
import junkbox.utils.mayautil as mayaUtils

import os
"""
name : AssetPreviewWidget
description : QWidget that reprensents an Assets preview panel 
"""


class AssetPreviewWidget(QWidget):
    thumbnailChanged = Signal(QPixmap)

    def __init__(self, parent=None):
        super(AssetPreviewWidget, self).__init__(parent)
        self.ui = Ui_assetPreviewWidget()
        self.ui.setupUi(self)

        # connections
        self.ui.importCopyButton.clicked.connect(self.importCopyClicked)
        self.ui.importReferenceButton.clicked.connect(
            self.importReferenceClicked)
        self.ui.openInMayaButton.clicked.connect(self.openInMayaClicked)
        self.ui.refreshButton.buttonPressed.connect(self.refreshPressed)

        # setup
        self.filePaths = None

    def refreshPressed(self):
        reply = QMessageBox.information(
            self, 'Thumbnail information',
            "In order to modify the thumbnail, the asset will be opened in Maya",
            QMessageBox.Yes, QMessageBox.Cancel)

        if reply == QMessageBox.Yes:
            self.openInMayaClicked()

            self.thumbnailDialog = ThumbnailDialog(self.parent())

            self.thumbnailDialog.show()
            self.thumbnailDialog.finished.connect(self.finishedThumbnailDialog)

    def finishedThumbnailDialog(self, state):
        if state == QDialog.Accepted:
            pixmap = self.thumbnailDialog.getThumbnail()

            if pixmap:
                self.setThumbnail(pixmap)
                self.thumbnailChanged.emit(pixmap)

    """
    name : openInMayaClicked
    description : slot that opens in maya the previewed asset
    """

    def openInMayaClicked(self):
        mayaUtils.openInMaya(self.filePaths[0])

    """
    name : importCopyClicked
    description : slot that imports in maya the previewed asset
    """

    def importCopyClicked(self):
        for path in self.filePaths:
            mayaUtils.importScene(path, asReference=False)

    """
    name : importReferenceClicked
    description : slot that imports as reference in maya the previewed asset
    """

    def importReferenceClicked(self):
        for path in self.filePaths:
            mayaUtils.importScene(path, asReference=True)

    """
    name : previewFiles
    description : preview the file paths given in argument
    param : 
        - filePaths : the file paths to preview
    """

    def previewFiles(self, filePaths):
        self.filePaths = filePaths

        nbFiles = len(self.filePaths)

        if nbFiles > 1:
            self.ui.assetSelectedLabel.setText(
                str(nbFiles) + " assets selected")
            self.ui.singleAssetWidget.hide()
            self.ui.multiAssetsWidget.show()
        else:
            self.ui.multiAssetsWidget.hide()
            self.ui.singleAssetWidget.show()

            self.updateInfo(self.filePaths[0])

    """
    name : updateInfo
    description : set the preview info from the panel according to the given file path
    param : 
        - filePath : the file path to get the info
    """

    def updateInfo(self, filePath):
        self.setThumbnail(fileUtils.getFileThumbnail(filePath))
        self.ui.fileNameLabel.setText(fileUtils.getFileBaseName(filePath))
        self.ui.fileTypeLabel.setText(fileUtils.getFileExtensionType(filePath))
        self.ui.fileSizeLabel.setText(fileUtils.getFileSize(filePath))
        self.ui.fileCreatedDateLabel.setText(
            fileUtils.getFileCreationDate(filePath))
        self.ui.fileLastModifiedDateLabel.setText(
            fileUtils.getFileModifyDate(filePath))

    """
    name : setThumbnail
    description : set the given thumbnail to the preview panel
    param : 
        - pixmap : the pixmap thumbnail to set
    """

    def setThumbnail(self, pixmap):
        self.ui.blankWidget.hide()

        scene = QGraphicsScene()
        self.ui.previewView.setScene(scene)
        scene.addPixmap(pixmap)
        self.ui.previewView.fitInView(scene.itemsBoundingRect(),
                                      Qt.KeepAspectRatio)

        self.ui.blankWidget.show()
