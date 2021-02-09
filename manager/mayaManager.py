import maya.cmds as cmds
import maya.mel as mel
from raphScripts.junkbox.manager.fileManager import FileManager
import os

class MayaManager(object):

    @classmethod
    def isEmptySelection(cls):
        selection = cmds.ls(selection = True)

        if len(selection) < 1:
            return True
        else:
            return False

    @classmethod
    def saveMayaSelection(cls, path, filename, pixmap, centered=False):
        if filename[0] == "/" or filename[1] == "\\":
            filename = filename[1:]

        mayaFilename = os.path.join( path, filename + ".mb")
        thumbnailFilename = os.path.join( path, filename + ".jpg")

        selection = cmds.ls(selection = True)

        if len(selection) < 1:
            cmds.confirmDialog( title='Empty selection', message='Nothing is currently selected')
            return False

        if centered:
            cls.groupSelected(filename)

        cmds.file( mayaFilename, force=True, options="v=0;", type="mayaBinary", preserveReferences=True, exportSelected=True)
        pixmap.save(thumbnailFilename, 'jpg')

        if centered:
            cmds.delete()

        return True

    @classmethod
    def importScene(cls, filename, asReference=True):
        basename = FileManager.getFileBaseName(filename, withExtension=False)

        if asReference:
            mel.eval('file -r -type "mayaBinary"  -ignoreVersion -gl -mergeNamespacesOnClash false -namespace "' + basename + '" -options "v=0;" "' + filename + '";')
        else:   
            mel.eval('file -import -type "mayaBinary"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "' + basename + '" -options "v=0;"  -pr  -importTimeRange "combine" "' + filename + '";')

    @classmethod
    def groupSelected( cls, groupName ):
        oldSelection = cmds.ls(selection = True)
        cmds.duplicate(returnRootsOnly=True)
        newSelection = cmds.ls(selection = True)

        cls.convertSelectionToParents()

        grp = cmds.group( newSelection, name=groupName )
        cmds.select(grp, replace=True)

        pivot = cmds.xform(grp,q=1,ws=1,rp=1)
        pivot = map(lambda x: -x, pivot) 

        cmds.move(pivot[0], pivot[1], pivot[2],grp, relative=True)
        cmds.makeIdentity( apply=True, translate=True, scale=True, rotate=True, normal=False, preserveNormals=True)
    
    @classmethod
    def getCenterSelected(cls):
        selection = cmds.ls(selection=True)
        centroid = [0,0,0]

        for obj in selection:
            objCenter = cmds.xform(obj, q=True, ws=True, rp=True)
            centroid[0] += objCenter[0]
            centroid[1] += objCenter[1]
            centroid[2] += objCenter[2]

        centroid[0] /= len(selection)
        centroid[1] /= len(selection)
        centroid[2] /= len(selection)

        return centroid

    @classmethod
    def convertSelectionToParents(cls):
        curSelection = cmds.ls(selection=True)

        if len(curSelection) > 0:
            oldSelection = []
            curSelection = cmds.ls(selection=True)

            while len(oldSelection) != len(curSelection):
                oldSelection = curSelection
                mel.eval("pickWalk -d up;")
                curSelection = cmds.ls(selection=True)
        
        return