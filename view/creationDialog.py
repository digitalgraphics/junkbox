from raphScripts.junkbox.ui.creationDialog import Ui_CreationDialog
from raphScripts.junkbox.component.asset import Asset
from raphScripts.junkbox.manager.thumbnailManager import ThumbnailManager
from raphScripts.junkbox.manager.mayaManager import MayaManager
from raphScripts.junkbox.view.browseCollectionDialog import BrowseCollectionDialog

from PySide2.QtWidgets import QDialog, QWidget, QListWidget, QListWidgetItem, QGraphicsScene , QMessageBox
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QIcon, QPixmap

import os
import maya.OpenMaya as OpenMaya

class CreationDialog(QDialog):
    def __init__(self, workingDirPath, parent=None):
        super(CreationDialog, self).__init__(parent)
        self.ui = Ui_CreationDialog()
        self.ui.setupUi(self)

        self.workingDirPath = workingDirPath
        self.thumbnailPixmap = QPixmap()

        self.addEventCallback()
        self.ui.previewView.setScene(QGraphicsScene())
        self.ui.previewView.setWindowFlags(Qt.FramelessWindowHint)

        self.captureDefaultThumbnail()
        self.updatePreview()

        self.ui.browseCollectionButton.buttonPressed.connect(self.openBrowseWidget)
        self.ui.manualScreenshotBox.toggled.connect(self.manualScreenshotToggled)
        self.ui.captureButton.clicked.connect(self.captureManualThumbnail)

    def addEventCallback(self):
        self.eventCallbackId = OpenMaya.MEventMessage.addEventCallback("SelectionChanged", self.mayaSelectionChanged)

    def removeEventCallback(self):
        OpenMaya.MMessage.removeCallback(self.eventCallbackId)

    def mayaSelectionChanged(self, *args, **kwargs):
 
        self.updatePreview()

        if MayaManager.isEmptySelection() == False:
            if self.ui.manualScreenshotBox.isChecked():
                self.captureManualThumbnail()
            else:
                self.captureDefaultThumbnail()


    def updatePreview( self ):
        if MayaManager.isEmptySelection():
            self.ui.previewView.hide()
            self.ui.emptySelectionLabel.show()
        else:
            self.ui.emptySelectionLabel.hide()
            self.ui.previewView.show()
            

    def manualScreenshotToggled( self, state):
        if state == False and MayaManager.isEmptySelection() == False:
            self.captureDefaultThumbnail()

    def captureDefaultThumbnail(self):
        if MayaManager.isEmptySelection():
            return

        self.removeEventCallback()
        self.thumbnailPixmap = ThumbnailManager.getDefaultThumbnail( onSelected=True)
        scene = self.ui.previewView.scene()
        scene.addPixmap(self.thumbnailPixmap)
        self.ui.previewView.fitInView(scene.itemsBoundingRect(),Qt.KeepAspectRatio)
        self.addEventCallback()

    def captureManualThumbnail(self):
        if MayaManager.isEmptySelection():
            return 

        self.removeEventCallback()
        self.thumbnailPixmap = ThumbnailManager.getManualThumbnail()
        scene = self.ui.previewView.scene()
        scene.addPixmap(self.thumbnailPixmap)
        self.ui.previewView.fitInView(scene.itemsBoundingRect(),Qt.KeepAspectRatio)
        self.addEventCallback()

    def showEvent(self, event):
        scene = self.ui.previewView.scene()
        self.ui.previewView.fitInView(scene.sceneRect(),Qt.KeepAspectRatio)

    def resizeEvent(self, event):
        scene = self.ui.previewView.scene()
        self.ui.previewView.fitInView(scene.sceneRect(),Qt.KeepAspectRatio)

    
    def setCollectionPath(self, path):
        self.ui.collectionPathEdit.setText(path)

    def openBrowseWidget(self):
        browseCollectionDialog = BrowseCollectionDialog( self.workingDirPath, self.parent())

        if browseCollectionDialog.exec_():
            self.setCollectionPath(browseCollectionDialog.getLocalPath())

    def checkFilename(self, filename):
        if  not filename:
            QMessageBox.warning( self, 'No filename entered', 'Please enter a filename for the new asset', QMessageBox.StandardButton.Ok )
            return False
        
        if " " in filename:
            QMessageBox.warning( self, 'Wrong filename format', 'The filename cannot contain spaces', QMessageBox.StandardButton.Ok )
            return False

        if filename[0].isdigit():
                    QMessageBox.warning( self, 'Wrong filename format', 'The filename cannot start with a number', QMessageBox.StandardButton.Ok )

        return True

    def checkCollection(self, collectionName):
        if  not collectionName:
            QMessageBox.warning( self, 'No collection name entered', 'Please enter a collection name for the new asset', QMessageBox.StandardButton.Ok )
            return False
        
        if " " in collectionName:
            QMessageBox.warning( self, 'Wrong collection name format', 'The collection name cannot contain spaces', QMessageBox.StandardButton.Ok )
            return False

        if collectionName[0].isdigit():
                    QMessageBox.warning( self, 'Wrong collection name format', 'The collection name cannot start with a number', QMessageBox.StandardButton.Ok )

        return True

    def getCollectionPath(self):
        return self.ui.collectionPathEdit.text()
   
    def accept(self):

        filename = self.ui.filenameEdit.text()
        collectionPath = self.ui.collectionPathEdit.text()

        if self.checkFilename(filename) == False:
            return
    
        if self.checkCollection(collectionPath) == False:
            return

        if collectionPath[0] == "/" or collectionPath[1] == "\\":
            collectionPath = collectionPath[1:]

        path = os.path.join(self.workingDirPath, collectionPath)

        pixmap = self.thumbnailPixmap.scaled(300, 300,Qt.KeepAspectRatio, Qt.SmoothTransformation)

        result = MayaManager.saveMayaSelection( path, filename, pixmap, centered=True)

        if result:
            self.removeEventCallback()
            super(CreationDialog, self).accept()

    def reject(self):
        self.removeEventCallback()
        super(CreationDialog, self).reject()

        
