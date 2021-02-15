from PySide2.QtWidgets import QTreeWidget
from PySide2.QtCore import Signal

"""
name : DeselectableTreeWidget
description : QTreeWidget that deselects all selected items
    when clicking outide all items
"""
class DeselectableTreeWidget(QTreeWidget):

    itemDeselected = Signal()

    def __init__(self, parent=None):
        super(DeselectableTreeWidget, self).__init__(parent)

    """
    name : mousePressEvent
    description : override mousePressEvent to deselect items
        when clicking outside the items
    """
    def mousePressEvent(self, event):
        item = self.indexAt(event.pos())

        selected = self.selectionModel().isSelected(item)

        if (item.row() == -1 and item.column() == -1):
            self.clearSelection()
            self.setFocus()
            self.itemDeselected.emit()
        
        super(DeselectableTreeWidget, self).mousePressEvent(event)
