import time
import ctypes
import math
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as OpenMaya
import maya.OpenMayaUI as OpenMayaUI

from raphScripts.junkbox.manager.mayaManager import MayaManager
from PySide2.QtGui import QPixmap, QPainter, QImage, QColor
from PySide2.QtCore import Qt

class ThumbnailManager(object):

    @classmethod
    def screenshotView( cls, view):
        # screenshot the viewport

        #read the color buffer from the view, and save the MImage to disk
        image = OpenMaya.MImage()
        
        if view.getRendererName() == view.kViewport2Renderer:   
            # viewport 2   
            image.create(view.portWidth(), view.portHeight(), 4, OpenMaya.MImage.kFloat)
            view.readColorBuffer(image)
            image.convertPixelFormat(OpenMaya.MImage.kByte)
        else:
            # viewport 1
            view.readColorBuffer(image)

        width = view.portWidth()
        height = view.portHeight()
        ptr = ctypes.cast(image.pixels().__long__(), ctypes.POINTER(ctypes.c_char))
        ptrAsStr = ctypes.string_at(ptr, width * height * 4)
        qimg = QImage(ptrAsStr, width, height, QImage.Format_ARGB32)
        #qimg = qimg.rgbSwapped().mirrored(horizontal=False, vertical=True)
        qimg = qimg.mirrored(horizontal=False, vertical=True)

        # # Prep MImage
        # image.verticalFlip()

        # # Get the width and height
        # wUtil = OpenMaya.MScriptUtil()
        # wUtil.createFromInt(0)
        # wPtr = wUtil.asUintPtr()

        # hUtil = OpenMaya.MScriptUtil()
        # hUtil.createFromInt(0)
        # hPtr = hUtil.asUintPtr()

        # image.getSize(wPtr, hPtr)

        # width = wUtil.getUint(wPtr)
        # height = hUtil.getUint(hPtr)

        # # byte size
        # imSize = width * height * 4

        # # pass pointer to QImage
        # buf = ctypes.c_ubyte * imSize
        # buf = buf.from_address(long(image.pixels()))
        # qimage = QImage(buf, width, height, QImage.Format_RGB32).rgbSwapped()



        # resize image
        pixmap = QPixmap.fromImage(qimg)
        width = pixmap.size().width()
        height = pixmap.size().height()
        minVal = min( width, height)
        widthThreshold = (width - minVal) / 2
        heightThresh = (height - minVal) / 2

        pixmap = pixmap.copy( widthThreshold, heightThresh, minVal, minVal)

        final = QPixmap(minVal, minVal)
        final.fill(Qt.black)

        painter = QPainter(final)
        painter.drawPixmap(0, 0, minVal, minVal, pixmap)
        painter.end()

        return final

    @classmethod
    def getCurrentViewData( cls ):
        # get the name of the current camera

        mel.eval('setNamedPanelLayout( "Single Perspective View" )')

        def intersection(lst1, lst2): 
            lst3 = [value for value in lst1 if value in lst2] 
            return lst3

        actView = cmds.getPanel(wf=True) 

        if actView not in cmds.getPanel(type='modelPanel'):
            visiblePanel = cmds.getPanel( visiblePanels=True)
            allModelPanel = cmds.getPanel(type="modelPanel")
            visibleModelPanel = intersection( allModelPanel, visiblePanel)
            actView = visibleModelPanel[0]

        view = OpenMayaUI.M3dView()
        cmds.setFocus(actView)
        OpenMayaUI.M3dView.getM3dViewFromModelEditor(actView, view)

        cam = OpenMaya.MDagPath()
        view.getCamera(cam)
        camPath = cam.partialPathName()
        
        return (actView, view, camPath)

    @classmethod
    def simplifyView( cls, actView ):
        # hide UI elements   

        attrKeys = ['sel', 'manipulators', 'grid', 'hud', 'hos', 'cameras']
        attrValues = [0, 0, 0, 0, 0, 0]
        attrOldValues = []

        # get old values

        for attr in attrKeys:
            attrOldValues.append(cmds.modelEditor(actView, q=1, **{ attr : True } ) )
            

        # set wanted values

        for i in range(len(attrKeys)):
            attrOldValues.append(cmds.modelEditor(actView, e=1, **{ attrKeys[i] : attrValues[i] } ) )

        restoreParam = {
            "keys" : attrKeys,
            "values" : attrOldValues
        }

        # show inly selected

        cmds.isolateSelect( actView, state=1 )
        cmds.isolateSelect( actView, addSelected=True )

        cmds.refresh()

        return restoreParam

    @classmethod
    def restoreView( cls, actView, params ):
        # restore UI elements
        for i in range(len(params["keys"])):
            attr = params["keys"][i]
            params["values"].append(cmds.modelEditor(actView, e=1, **{ attr : params["values"][i] } ) )

        # show unselected

        cmds.isolateSelect( actView, state=False )


    @classmethod
    def getManualThumbnail( cls ):
        (actView, view, camPath) = cls.getCurrentViewData()
        restoreParam = cls.simplifyView( actView )
        pixmap = cls.screenshotView(view)
        cls.restoreView( actView, restoreParam)
        return pixmap

    @classmethod
    def distanceBtwPos(cls, pos1, pos2):
        dx = pos1[0] - pos2[0]
        dy = pos1[1] - pos2[1]
        dz = pos1[2] - pos2[2]
        return math.sqrt( dx*dx + dy*dy + dz*dz )

    @classmethod
    def getDefaultThumbnail( cls, onSelected = False ):

        (actView, view, camPath) = cls.getCurrentViewData()

        selection = cmds.ls(selection = True)

        selectionCenter = MayaManager.getCenterSelected()

        # create a new camera and look though

        

        cameraName = cmds.camera()

        cmds.select(selection, add=True)

        cmds.viewFit(cameraName[0])

        cameraPos = cmds.xform( cameraName[0], q=True, ws=True, t=True)
        defaultCamPos = [20, 10, 15]

        defaultDistance = cls.distanceBtwPos([0,0,0], defaultCamPos)
        distance = cls.distanceBtwPos(selectionCenter, cameraPos)

        ratio = 1.3 / defaultDistance * distance
        defaultCamPos = map(lambda x: x * ratio, defaultCamPos) 

        if onSelected:
            cmds.move( defaultCamPos[0] + selectionCenter[0], defaultCamPos[1] + selectionCenter[1], defaultCamPos[2] + selectionCenter[2], cameraName[0] )
            cmds.viewLookAt( cameraName[0], pos=(selectionCenter[0], selectionCenter[1], selectionCenter[2]) )
        else:
            cmds.move( defaultCamPos[0], defaultCamPos[1], defaultCamPos[2], cameraName[0] )
            cmds.viewLookAt( cameraName[0], pos=(0.0, 0.0, 0.0) )

        cmds.lookThru( actView, cameraName[1], nc=0.001, fc=5000.0 )

        

        restoreParam = cls.simplifyView( actView )

        pixmap = cls.screenshotView(view)

    
        # reset the previous camera

        cmds.lookThru( actView, camPath, nc=0.001, fc=5000.0 )
        cmds.delete(cameraName[0])

        cls.restoreView( actView, restoreParam)

        return pixmap

        
