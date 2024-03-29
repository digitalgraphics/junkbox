import maya.cmds as cmds
import maya.mel as mel
import junkbox.utils.file as fileUtils
import os


def isEmptySelection():
    selection = cmds.ls(selection=True)

    if len(selection) < 1:
        return True
    else:
        return False


def updateThumbnail(filePath, pixmap):
    thumbnailFilename = fileUtils.getPathThumbnail(filePath)
    pixmap.save(thumbnailFilename, 'jpg')


def saveMayaSelection(path, filename, pixmap, centered=False):
    if filename[0] == "/" or filename[1] == "\\":
        filename = filename[1:]

    mayaFilename = os.path.join(path, filename + ".ma")
    thumbnailFilename = os.path.join(path, filename + ".jpg")

    selection = cmds.ls(selection=True)

    if len(selection) < 1:
        cmds.confirmDialog(title='Empty selection',
                           message='Nothing is currently selected')
        return False

    if centered:
        groupSelected(filename)

    cmds.file(mayaFilename,
              force=True,
              options="v=0;",
              type="mayaAscii",
              preserveReferences=True,
              exportSelected=True)
    pixmap.save(thumbnailFilename, 'jpg')

    if centered:
        cmds.delete()

    return True


def openInMaya(filename):
    try:
        mel.eval(
            'file -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "' +
            filename + '";')
    except RuntimeError:
        reply = cmds.confirmDialog(
            title='Unsaved changes',
            message='Save the current scene before opening the new one ?',
            button=['Yes', 'No'],
            defaultButton='Yes',
            cancelButton='No',
            dismissString='Close')

        if reply == 'Yes':
            cmds.file(save=True)
            mel.eval(
                'file -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "' +
                filename + '";')
            mel.eval('addRecentFile("' + filename + '", "mayaAscii");')
        elif reply == 'No':
            mel.eval(
                'file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "'
                + filename + '";')
            mel.eval('addRecentFile("' + filename + '", "mayaAscii");')


def importScene(filename, asReference=True):
    basename = fileUtils.getFileBaseName(filename, withExtension=False)

    if asReference:
        mel.eval(
            'file -r -type "mayaAscii"  -ignoreVersion -gl -mergeNamespacesOnClash false -namespace "'
            + basename + '" -options "v=0;" "' + filename + '";')
    else:
        mel.eval(
            'file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace "xx" -options "v=0;"  -pr  -importTimeRange "combine" "'
            + filename + '";')
        mel.eval('namespace -mergeNamespaceWithRoot -removeNamespace "xx";')


def groupSelected(groupName):
    oldSelection = cmds.ls(selection=True)
    cmds.duplicate(returnRootsOnly=True)
    newSelection = cmds.ls(selection=True)

    mel.eval('sets -e -forceElement initialShadingGroup;')

    convertSelectionToParents()

    grp = cmds.group(newSelection, name=groupName)
    cmds.select(grp, replace=True)

    pivot = cmds.xform(grp, q=1, ws=1, rp=1)
    pivot = map(lambda x: -x, pivot)

    cmds.move(pivot[0], pivot[1], pivot[2], grp, relative=True)
    cmds.makeIdentity(apply=True,
                      translate=True,
                      scale=True,
                      rotate=True,
                      normal=False,
                      preserveNormals=True)


def getCenterSelected():
    selection = cmds.ls(selection=True)

    bbox = cmds.exactWorldBoundingBox(selection)
    centroid = [(bbox[0] + bbox[3]) / 2, (bbox[1] + bbox[4]) / 2,
                (bbox[2] + bbox[5]) / 2]

    return centroid


def convertSelectionToParents():
    curSelection = cmds.ls(selection=True)

    if len(curSelection) > 0:
        oldSelection = []
        curSelection = cmds.ls(selection=True)

        while len(oldSelection) != len(curSelection):
            oldSelection = curSelection
            mel.eval("pickWalk -d up;")
            curSelection = cmds.ls(selection=True)

    return
