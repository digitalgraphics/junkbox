from PySide2.QtWidgets import QWidget, QGraphicsScene
from PySide2.QtCore import Qt

from junkbox.ui.assetpreviewwidget import Ui_assetPreviewWidget

import junkbox.utils.file as fileUtils
import junkbox.utils.mayautil as mayaUtils

import os

"""
name : 
description : 
param : 
return : 
"""
class AssetPreviewWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(AssetPreviewWidget, self).__init__(*args, **kwargs)
        self.ui = Ui_assetPreviewWidget()
        self.ui.setupUi(self)

        self.ui.importCopyButton.clicked.connect(self.importCopyClicked)
        self.ui.importReferenceButton.clicked.connect(
            self.importReferenceClicked)
        self.ui.openInMayaButton.clicked.connect(self.openInMayaClicked)

        self.filePaths = None

    def openInMayaClicked(self):
        mayaUtils.openInMaya(self.filePaths[0])

    def importCopyClicked(self):
        for path in self.filePaths:
            mayaUtils.importScene(path, asReference=False)

    def importReferenceClicked(self):
        for path in self.filePaths:
            mayaUtils.importScene(path, asReference=True)

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

    def updateInfo(self, filePath):
        self.setThumbnail(fileUtils.getFileThumbnail(filePath))
        self.ui.fileNameLabel.setText(fileUtils.getFileBaseName(filePath))
        self.ui.fileTypeLabel.setText(
            fileUtils.getFileExtensionType(filePath))
        self.ui.fileSizeLabel.setText(fileUtils.getFileSize(filePath))
        self.ui.fileCreatedDateLabel.setText(
            fileUtils.getFileCreationDate(filePath))
        self.ui.fileLastModifiedDateLabel.setText(
            fileUtils.getFileModifyDate(filePath))

    def setThumbnail(self, pixmap):
        self.ui.blankWidget.hide()

        scene = QGraphicsScene()
        self.ui.previewView.setScene(scene)
        scene.addPixmap(pixmap)
        self.ui.previewView.fitInView(
            scene.itemsBoundingRect(), Qt.KeepAspectRatio)

        self.ui.blankWidget.show()
