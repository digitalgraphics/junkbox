from junkbox.ui.thumbnaildialog import Ui_thumbnailDialog

from PySide2.QtWidgets import QDialog

import os


class ThumbnailDialog(QDialog):
    def __init__(self, parent=None):
        super(ThumbnailDialog, self).__init__(parent)
        self.ui = Ui_thumbnailDialog()
        self.ui.setupUi(self)

    def getThumbnail(self):
        return self.ui.thumbnailWidget.getThumbnail()

    def accept(self):
        self.ui.thumbnailWidget.removeEventCallback()
        super(ThumbnailDialog, self).accept()

    def reject(self):
        self.ui.thumbnailWidget.removeEventCallback()
        super(ThumbnailDialog, self).reject()