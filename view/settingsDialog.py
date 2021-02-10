from raphScripts.junkbox.ui.settingsDialog import Ui_SettingsDialog
from raphScripts.junkbox.manager.fileManager import FileManager

from PySide2.QtWidgets import QDialog, QWidget, QTreeWidgetItem, QFileDialog, QInputDialog, QMessageBox
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap


class SettingsDialog(QDialog):
    def __init__(self, dataPaths, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

        self.setDataPaths(dataPaths)

        self.ui.addButton.clicked.connect(self.addPathClicked)
        self.ui.treeWidget.itemChanged.connect(self.fieldEdited)

    def fieldEdited(self, item, column):
        if column == 1 and not FileManager.existingPath(item.text(1)):
            QMessageBox.warning(self, 'Wrong working path',
                                'The modified working path does not exist', QMessageBox.StandardButton.Ok)

    def addPathClicked(self):
        path = str(QFileDialog.getExistingDirectory(
            self, "Select a directory"))
        name, ok = QInputDialog.getText(
            self, 'Path name', 'Enter a name for the new path')

        if not ok:
            return
        else:
            self.addDataPath(name, path, True)

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

            if FileManager.existingPath(path):
                dataPaths.append([name, path, isEditable])

        return dataPaths
