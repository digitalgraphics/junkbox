from PySide2.QtWidgets import QWidget, QPushButton
from PySide2.QtGui import QPixmap, QPainter, QIcon
from PySide2.QtCore import QSize, Qt, QObject, Signal, Slot

class FlatButton(QPushButton):

    buttonPressed = Signal(int)

    def __init__(self, *args, **kwargs):
        super(FlatButton, self).__init__(*args, **kwargs)

        self.setStyleSheet(
        """
        QPushButton {
            margin: 0;
            padding: 0; 
            background-color: transparent;
            border: transparent;
        }
        QPushButton:hover {
            background-color: rgba(255, 255, 255, 50);
        }
        QPushButton:pressed {
            background-color: rgba(255, 255, 255, 100);
        }
        """
        )

        self.setIconSize(QSize(22,23))
        self.setText("")

        self.actionId = 0
        self.actionIcons = None
    
        self.released.connect(self.buttonClicked)

    def detectNumberActions(self):
        if self.actionIcons:
            return

        self.actionIcons = [ self.icon() ]
        self.actionSignals = [ Signal() ]

        stillIcons = True
        curId = 1
        while stillIcons:
            curIcon = self.property("icon" + str(curId))

            if curIcon:
                self.actionIcons.append(curIcon)
                curId = curId + 1
            
            else:
                stillIcons = False
        

    def buttonClicked(self): 
        self.detectNumberActions()

        self.actionId = (self.actionId + 1) % len(self.actionIcons)
        self.setIcon(self.actionIcons[self.actionId])
        self.buttonPressed.emit(self.actionId)

