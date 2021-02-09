import raphScripts.junkbox.ui.thumbnailWidget as thumbnailWidgetUi
reload(thumbnailWidgetUi)

from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPixmap

class ThumbnailWidget(QWidget):
    def __init__(self, parent=None):
        super(ThumbnailWidget, self).__init__(parent)
        self.ui = thumbnailWidgetUi.Ui_thumbnailWidget()
        self.ui.setupUi(self)

        self.setMaximumWidth(200)

        self.ui.icon.setPixmap(QPixmap("C:/Users/rjouretz/Desktop/237-536x354.jpg"))

        self.ui.label.setText("jdflmkj mlkjsdfm lqkjsqmdl kfjmlqskdfj omiezrtjh oieuht kljerhtlkejrthelskrjth lksejrghldkjfshl")
    
    def setIcon(self, pixmap):
        self.pixmap = pixmap
    
    def setLabel( self, label):
        self.label = label
        self.ui.label.setText(self.label)