import junkbox.utils.thumbnail as thumbnailUtils
import junkbox.utils.mayautil as mayaUtils
import junkbox.utils.file as fileUtils

from junkbox.ui.thumbnailwidget import Ui_thumbnailWidget
from PySide2.QtWidgets import QWidget, QGraphicsScene
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap

import maya.OpenMaya as OpenMaya


class ThumbnailWidget(QWidget):
    def __init__(self, parent=None):
        super(ThumbnailWidget, self).__init__(parent)
        self.ui = Ui_thumbnailWidget()
        self.ui.setupUi(self)

        self.thumbnailPixmap = QPixmap()

        self.addEventCallback()
        self.ui.previewView.setScene(QGraphicsScene())
        self.ui.previewView.setWindowFlags(Qt.FramelessWindowHint)

        self.captureDefaultThumbnail()
        self.updatePreview()

        self.ui.manualScreenshotBox.toggled.connect(
            self.manualScreenshotToggled)
        self.ui.captureButton.clicked.connect(self.captureManualThumbnail)

    def addEventCallback(self):
        self.eventCallbackId = OpenMaya.MEventMessage.addEventCallback(
            "SelectionChanged", self.mayaSelectionChanged)

    def removeEventCallback(self):
        OpenMaya.MMessage.removeCallback(self.eventCallbackId)

    def mayaSelectionChanged(self, *args, **kwargs):

        self.updatePreview()

        if mayaUtils.isEmptySelection() == False:
            if self.ui.manualScreenshotBox.isChecked():
                self.captureManualThumbnail()
            else:
                self.captureDefaultThumbnail()

    def updatePreview(self):
        if mayaUtils.isEmptySelection():
            self.ui.previewView.hide()
            self.ui.emptySelectionLabel.show()
        else:
            self.ui.emptySelectionLabel.hide()
            self.ui.previewView.show()

    def manualScreenshotToggled(self, state):
        if state == False and mayaUtils.isEmptySelection() == False:
            self.captureDefaultThumbnail()

    def captureDefaultThumbnail(self):
        if mayaUtils.isEmptySelection():
            return

        self.removeEventCallback()
        self.thumbnailPixmap = thumbnailUtils.getDefaultThumbnail(
            onSelected=True)
        scene = self.ui.previewView.scene()
        scene.addPixmap(self.thumbnailPixmap)
        self.ui.previewView.fitInView(scene.itemsBoundingRect(),
                                      Qt.KeepAspectRatio)
        self.addEventCallback()

    def captureManualThumbnail(self):
        if mayaUtils.isEmptySelection():
            return

        self.removeEventCallback()
        self.thumbnailPixmap = thumbnailUtils.getManualThumbnail()
        scene = self.ui.previewView.scene()
        scene.addPixmap(self.thumbnailPixmap)
        self.ui.previewView.fitInView(scene.itemsBoundingRect(),
                                      Qt.KeepAspectRatio)
        self.addEventCallback()

    def showEvent(self, event):
        scene = self.ui.previewView.scene()
        self.ui.previewView.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)

    def resizeEvent(self, event):
        scene = self.ui.previewView.scene()
        self.ui.previewView.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)

    def getThumbnail(self):
        if mayaUtils.isEmptySelection():
            return None
        else:
            return self.thumbnailPixmap.scaled(300, 300, Qt.KeepAspectRatio,
                                               Qt.SmoothTransformation)
