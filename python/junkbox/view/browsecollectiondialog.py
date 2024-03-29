from junkbox.ui.browsecollectiondialog import Ui_browseCollectionDialog

from PySide2.QtWidgets import QDialog, QWidget, QListWidget, QListWidgetItem
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon, QPixmap


class BrowseCollectionDialog(QDialog):
    def __init__(self, workingDirPath, parent=None):
        super(BrowseCollectionDialog, self).__init__(parent)
        self.ui = Ui_browseCollectionDialog()
        self.ui.setupUi(self)

        self.workingDirPath = workingDirPath
        self.ui.assetHierarchyWidget.setFolders(self.workingDirPath)

        self.ui.assetHierarchyWidget.collectionDoubleClicked.connect(
            self.validateCollection)

    def validateCollection(self):
        self.accept()

    def getLocalPath(self):
        return self.ui.assetHierarchyWidget.getSelectedCollectionPath()

    def getAbsolutePath(self):
        return self.ui.assetHierarchyWidget.getSelectedCollectionPath(True)
