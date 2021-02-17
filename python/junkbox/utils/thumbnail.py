import time
import ctypes
import math
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as OpenMaya
import maya.OpenMayaUI as OpenMayaUI
import junkbox.utils.mayautil as mayaUtils

from PySide2.QtGui import QPixmap, QPainter, QImage, QColor
from PySide2.QtCore import Qt


def screenshotView(view):
    # screenshot the viewport

    # read the color buffer from the view, and save the MImage to disk
    image = OpenMaya.MImage()

    if view.getRendererName() == view.kViewport2Renderer:
        # viewport 2
        image.create(view.portWidth(), view.portHeight(),
                     4, OpenMaya.MImage.kFloat)
        view.readColorBuffer(image)
        image.convertPixelFormat(OpenMaya.MImage.kByte)
    else:
        # viewport 1
        view.readColorBuffer(image)

    width = view.portWidth()
    height = view.portHeight()
    ptr = ctypes.cast(image.pixels().__long__(),
                      ctypes.POINTER(ctypes.c_char))
    ptrAsStr = ctypes.string_at(ptr, width * height * 4)
    qimg = QImage(ptrAsStr, width, height, QImage.Format_ARGB32)
    #qimg = qimg.rgbSwapped().mirrored(horizontal=False, vertical=True)
    qimg = qimg.mirrored(horizontal=False, vertical=True)

    # resize image
    pixmap = QPixmap.fromImage(qimg)
    width = pixmap.size().width()
    height = pixmap.size().height()
    minVal = min(width, height)
    widthThreshold = (width - minVal) / 2
    heightThresh = (height - minVal) / 2

    pixmap = pixmap.copy(widthThreshold, heightThresh, minVal, minVal)

    final = QPixmap(minVal, minVal)
    final.fill(Qt.black)

    painter = QPainter(final)
    painter.drawPixmap(0, 0, minVal, minVal, pixmap)
    painter.end()

    return final


def getCurrentViewData():
    # get the name of the current camera

    mel.eval('setNamedPanelLayout( "Single Perspective View" )')

    def intersection(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

    actView = cmds.getPanel(wf=True)

    if actView not in cmds.getPanel(type='modelPanel'):
        visiblePanel = cmds.getPanel(visiblePanels=True)
        allModelPanel = cmds.getPanel(type="modelPanel")
        visibleModelPanel = intersection(allModelPanel, visiblePanel)
        actView = visibleModelPanel[0]

    view = OpenMayaUI.M3dView()
    cmds.setFocus(actView)
    OpenMayaUI.M3dView.getM3dViewFromModelEditor(actView, view)

    cam = OpenMaya.MDagPath()
    view.getCamera(cam)
    camPath = cam.partialPathName()

    return (actView, view, camPath)


def simplifyView(actView):
    # hide UI elements

    attributes = [
        {
            "key": "sel",
            "newValue": 0,
        },
        {
            "key": "manipulators",
            "newValue": 0,
        },
        {
            "key": "grid",
            "newValue": 0,
        },
        {
            "key": "hud",
            "newValue": 0,
        },
        {
            "key": "hos",
            "newValue": 0,
        },
        {
            "key": "cameras",
            "newValue": 0,
        },
        {
            "key": "displayAppearance",
            "newValue": "smoothShaded",
        },
        {
            "key": "displayLights",
            "newValue": "default",
        },
        {
            "key": "displayTextures",
            "newValue": 0,
        },
    ]

    # get old values

    for attr in attributes:
        attr["oldValue"] = cmds.modelEditor(
            actView, q=1, **{attr["key"]: True})

    # set wanted values

    for attr in attributes:
        cmds.modelEditor(
            actView, e=1, **{attr["key"]: attr["newValue"]})

    cmds.duplicate(returnRootsOnly=True)
    mel.eval('sets -e -forceElement initialShadingGroup;')

    # show inly selected
    mel.eval('enableIsolateSelect %s %d' % (actView, 1))

    cmds.refresh()

    return attributes


def restoreView(actView, attributes):
    # restore UI elements
    for attr in attributes:
        cmds.modelEditor(
            actView, e=1, **{attr["key"]: attr["oldValue"]})

    # show unselected

    cmds.delete()
    mel.eval('enableIsolateSelect %s %d' % (actView, 0))


def getManualThumbnail():
    (actView, view, camPath) = getCurrentViewData()
    selection = cmds.ls(selection=True)
    restoreParam = simplifyView(actView)
    pixmap = screenshotView(view)
    restoreView(actView, restoreParam)
    cmds.select(selection, replace=True)
    return pixmap


def distanceBtwPos(pos1, pos2):
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    dz = pos1[2] - pos2[2]
    return math.sqrt(dx*dx + dy*dy + dz*dz)


def getDefaultThumbnail(onSelected=False):

    (actView, view, camPath) = getCurrentViewData()

    selection = cmds.ls(selection=True)

    selectionCenter = mayaUtils.getCenterSelected()

    # create a new camera and look though

    cameraName = cmds.camera()

    cmds.select(selection, add=True)

    cmds.viewFit(cameraName[0])

    cameraPos = cmds.xform(cameraName[0], q=True, ws=True, t=True)
    defaultCamPos = [20, 10, 15]

    defaultDistance = distanceBtwPos([0, 0, 0], defaultCamPos)
    distance = distanceBtwPos(selectionCenter, cameraPos)

    ratio = 1.3 / defaultDistance * distance
    defaultCamPos = map(lambda x: x * ratio, defaultCamPos)

    if onSelected:
        cmds.move(defaultCamPos[0] + selectionCenter[0], defaultCamPos[1] +
                  selectionCenter[1], defaultCamPos[2] + selectionCenter[2], cameraName[0])
        cmds.viewLookAt(cameraName[0], pos=(
            selectionCenter[0], selectionCenter[1], selectionCenter[2]))
    else:
        cmds.move(defaultCamPos[0], defaultCamPos[1],
                  defaultCamPos[2], cameraName[0])
        cmds.viewLookAt(cameraName[0], pos=(0.0, 0.0, 0.0))

    cmds.lookThru(actView, cameraName[1], nc=0.001, fc=5000.0)

    restoreParam = simplifyView(actView)

    pixmap = screenshotView(view)

    # reset the previous camera

    cmds.lookThru(actView, camPath, nc=0.001, fc=5000.0)
    cmds.delete(cameraName[0])

    restoreView(actView, restoreParam)

    cmds.select(selection, replace=True)

    return pixmap
