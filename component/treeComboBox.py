# if True:
#     import raphScripts.junkbox.resource
#     reload(raphScripts.junkbox.resource)


# from raphScripts.junkbox.resource import resource_rc


# from PySide2.QtWidgets import QWidget, QComboBox, QTreeWidgetItem, QTreeWidget
# from PySide2.QtCore import QSize, Qt, QEvent, QModelIndex
# from PySide2.QtGui import QIcon, QPixmap, QStandardItemModel, QStandardItem

# class TreeComboBox(QComboBox):
#     def __init__(self, parent=None):
#         super(TreeComboBox, self).__init__(parent)

#         self.skipNextHide = False
#         v = QTreeWidget(self)
#         self.setView(v)
#         v.header().hide()
#         v.viewport().installEventFilter(self)

#         item = v
#         for i in range(5):
#             item = QTreeWidgetItem(item, ["name" + str(i)])
#             item.setIcon(0, QIcon(":/icon/collection.png"))

#         self.setModel(self.view().model())
#         self.show()

#         self.clickedItem = None

#         self.view().expanded.connect(self.itemChanged)
#         self.view().collapsed.connect(self.itemChanged)
#         self.view().itemPressed.connect(self.collectionClicked)

#     def itemChanged(self, modelIndex ):
#         self.showPopup()

#     def collectionClicked( self, item, column):
#         self.clickedItem = item

#     def eventFilter(self, object, event):

#         try:
#             if self.clickedItem == None:
#                 if event.type() == QEvent.MouseButtonRelease:
#                     return True
#         except:
#             pass

#         self.clickedItem = None

#         return super(TreeComboBox, self).eventFilter( object, event)


#     def showPopup(self):
#         self.view().update()
#         self.setRootModelIndex(QModelIndex())
#         super(TreeComboBox, self).showPopup()

#     def hidePopup(self):
#         self.setRootModelIndex(self.view().currentIndex().parent())
#         self.setCurrentIndex( self.view().currentIndex().row())

#         if self.skipNextHide:
#             self.skipNextHide = False
#         else:
#             super(TreeComboBox, self).hidePopup()