from junkbox.ui.settingsdialog import Ui_settingsDialog
import junkbox.utils.file as fileUtils

from PySide2.QtWidgets import QDialog, QWidget, QTreeWidgetItem, QFileDialog, QInputDialog, QMessageBox
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap


class SettingsDialog(QDialog):
    def __init__(self, dataPaths, historyPath, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.ui = Ui_settingsDialog()
        self.ui.setupUi(self)

        self.setDataPaths(dataPaths)

        self.ui.addButton.clicked.connect(self.addPathClicked)
        self.ui.removeButton.clicked.connect(self.removePathClicked)
        self.ui.treeWidget.itemChanged.connect(self.fieldEdited)
        self.ui.treeWidget.itemSelectionChanged.connect(self.selectionChanged)
        self.ui.treeWidget.itemDeselected.connect(self.selectionChanged)

        self.ui.removeButton.setEnabled(False)
        self.ui.filePathEdit.setText(historyPath)

    def selectionChanged(self):
        if len(self.ui.treeWidget.selectedItems()) > 0:
            self.ui.removeButton.setEnabled(True)
        else:
            self.ui.removeButton.setEnabled(False)

    def fieldEdited(self, item, column):
        if column == 1 and not fileUtils.existingPath(item.text(1)):
            QMessageBox.warning(self, 'Wrong working path',
                                'The modified working path does not exist', QMessageBox.StandardButton.Ok)

    def addPathClicked(self):
        path = str(QFileDialog.getExistingDirectory(
            self, "Select a directory"))

        if not path:
            return

        name, ok = QInputDialog.getText(
            self, 'Path name', 'Enter a name for the new path')

        if not ok:
            return
        else:
            self.addDataPath(name, path, True)

    def removePathClicked(self):
        reply = QMessageBox.question(
            self, 'Delete assets path', "Are you sure to delete the path", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            selectedItem = self.ui.treeWidget.selectedItems()[0]
            parent = self.ui.treeWidget.invisibleRootItem()
            parent.removeChild(selectedItem)
            del selectedItem

    def setDataPaths(self, dataPaths):
        for name, path, isEditable in dataPaths:
            self.addDataPath(name, path, isEditable)

    def addDataPath(self, name, path, isEditable):
        item = QTreeWidgetItem(self.ui.treeWidget, [name, path])
        if isEditable:
            item.setFlags(item.flags() | Qt.ItemIsEditable)
        else:
            item.setDisabled(True)

    def getDataPaths(self):
        parent = self.ui.treeWidget.invisibleRootItem()
        nbChildren = parent.childCount()
        dataPaths = []
        for i in range(nbChildren):
            item = parent.child(i)
            name = item.text(0)
            path = item.text(1)
            isEditable = not item.isDisabled()

            if fileUtils.existingPath(path):
                dataPaths.append([name, path, isEditable])

        return dataPaths

    def getHistoryPath(self):
        return self.ui.filePathEdit.text()
