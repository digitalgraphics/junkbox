from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import QSize, Signal

"""
name : FlatButton
description : QPushButton that has flat design et can loop over
    mutiple icon/action when clicked
"""
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

    """
    name : detectNumberActions
    description : detect the number of actions assigned to
        the current button
    """
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
        

    """
    name : buttonClicked
    description : slot that emit the action associated to the
        current displayed icon
    """
    def buttonClicked(self): 
        self.detectNumberActions()

        self.actionId = (self.actionId + 1) % len(self.actionIcons)
        self.setIcon(self.actionIcons[self.actionId])
        self.buttonPressed.emit(self.actionId)

