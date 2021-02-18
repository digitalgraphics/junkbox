from junkbox.ui.creationdialog import Ui_creationDialog
import junkbox.utils.thumbnail as thumbnailUtils
import junkbox.utils.mayautil as mayaUtils
import junkbox.utils.file as fileUtils
from junkbox.view.browsecollectiondialog import BrowseCollectionDialog

from PySide2.QtWidgets import QDialog, QWidget, QListWidget, QListWidgetItem, QGraphicsScene, QMessageBox
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QIcon, QPixmap

import os


class CreationDialog(QDialog):
    def __init__(self, workingDirPath, parent=None):
        super(CreationDialog, self).__init__(parent)
        self.ui = Ui_creationDialog()
        self.ui.setupUi(self)

        self.workingDirPath = workingDirPath

        self.ui.browseCollectionButton.buttonPressed.connect(
            self.openBrowseWidget)

    def setCollectionPath(self, path):
        self.ui.collectionPathEdit.setText(path)

    def openBrowseWidget(self):
        browseCollectionDialog = BrowseCollectionDialog(
            self.workingDirPath, self.parent())

        if browseCollectionDialog.exec_():
            self.setCollectionPath(browseCollectionDialog.getLocalPath())

    def checkFilename(self, filename):
        if not filename:
            QMessageBox.warning(self, 'No filename entered',
                                'Please enter a filename for the new asset',
                                QMessageBox.StandardButton.Ok)
            return False

        if " " in filename:
            QMessageBox.warning(self, 'Wrong filename format',
                                'The filename cannot contain spaces',
                                QMessageBox.StandardButton.Ok)
            return False

        if filename[0].isdigit():
            QMessageBox.warning(self, 'Wrong filename format',
                                'The filename cannot start with a number',
                                QMessageBox.StandardButton.Ok)

        return True

    def checkCollection(self, collectionName):
        if not collectionName:
            QMessageBox.warning(
                self, 'No collection name entered',
                'Please enter a collection name for the new asset',
                QMessageBox.StandardButton.Ok)
            return False

        if " " in collectionName:
            QMessageBox.warning(self, 'Wrong collection name format',
                                'The collection name cannot contain spaces',
                                QMessageBox.StandardButton.Ok)
            return False

        if collectionName[0].isdigit():
            QMessageBox.warning(
                self, 'Wrong collection name format',
                'The collection name cannot start with a number',
                QMessageBox.StandardButton.Ok)

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

        filePath = path + '/' + filename
        newPath, newName = fileUtils.getVersionFilePath(filePath)

        if filename != newName:
            reply = QMessageBox.question(
                self, 'Incremented name',
                'The asset name already exists. The current name will be incremented to '
                + newName, QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.No:
                return

            filename = newName

        if mayaUtils.isEmptySelection():
            QMessageBox.warning(self, 'Empty selection',
                                'Nothing is currently selected',
                                QMessageBox.StandardButton.Ok)
            return

        pixmap = self.ui.thumbnailWidget.getThumbnail()

        self.ui.thumbnailWidget.removeEventCallback()

        mayaUtils.saveMayaSelection(path, filename, pixmap, centered=True)

        super(CreationDialog, self).accept()

    def reject(self):
        self.ui.thumbnailWidget.removeEventCallback()
        super(CreationDialog, self).reject()
