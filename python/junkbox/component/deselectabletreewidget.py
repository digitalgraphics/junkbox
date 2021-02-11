from PySide2.QtWidgets import QTreeWidget
from PySide2.QtCore import QItemSelectionModel, Signal


class DeselectableTreeWidget(QTreeWidget):

    itemDeselected = Signal()

    def __init__(self, parent=None):
        super(DeselectableTreeWidget, self).__init__(parent)


    def mousePressEvent(self, event):
        item = self.indexAt(event.pos())

        selected = self.selectionModel().isSelected(item)

        if (item.row() == -1 and item.column() == -1):
            self.clearSelection()
            self.setFocus()
            self.itemDeselected.emit()
        
        super(DeselectableTreeWidget, self).mousePressEvent(event)
