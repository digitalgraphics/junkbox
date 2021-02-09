import os
import datetime
import time
import math
import shutil

class FileManager(object):
    dataPath = "C:/Users/rjouretz/Documents/maya/2018/prefs/scripts/raphScripts/junkbox/DATA"

    @classmethod
    def getFileThumbnail(cls, filePath):
        thumbnailPath = filePath.replace(".mb",".jpg")

        if os.path.exists(thumbnailPath):
            return thumbnailPath
        else:
            return None

    @classmethod
    def getFileBaseName(cls, filePath, withExtension=True):
        basename = os.path.basename(filePath)

        if withExtension:
            return basename
        else:
            return basename.split(".")[0]

    @classmethod
    def getFileCreationDate(cls, filePath):
        fileTime = os.path.getctime(filePath)
        return time.strftime('%d-%m-%Y %H:%M', time.gmtime(fileTime))

    @classmethod
    def getFileModifyDate(cls, filePath):
        fileTime = os.path.getmtime(filePath)
        return time.strftime('%d-%m-%Y %H:%M', time.gmtime(fileTime))

    @classmethod
    def getFileExtensionType(cls, filePath):
        filename, extension = os.path.splitext(filePath)
        return extension.replace('.', '') + " File"

    @classmethod
    def getFileSize(cls, filePath):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        nbytes = os.path.getsize(filePath)
        rank = int((math.log10(nbytes)) / 3)
        rank = min(rank, len(suffixes) - 1)
        human = nbytes / (1024.0 ** rank)
        f = ('%.2f' % human).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[rank])

    @classmethod
    def createFolder(cls, folderPath):
        os.mkdir(folderPath)

    @classmethod
    def getRootFolderPath(cls):
        return cls.dataPath

    @classmethod
    def getFolders( cls, path ):

        def dirToDict( curPath ):
            curDir = dict()
            for filename in os.listdir(curPath):
                if os.path.isdir(os.path.join(curPath, filename)):
                    curDir[filename] =  dirToDict(os.path.join( curPath , filename))

            return curDir

        return dirToDict(path)

    @classmethod
    def removeFolder(cls, folderPath):
        os.rmdir(folderPath)

    @classmethod
    def removeFiles(cls, filePaths):
        for path in filePaths:
            if os.path.exists(path):
                os.remove(path)

    @classmethod
    def moveFilesToDir(cls, srcPaths, destDir):
        for f in srcPaths:
            shutil.move(f, destDir)

    @classmethod
    def getMayaFilesFromFolder(cls, folderPath):
        fileList = []
        for filename in os.listdir(folderPath):
            if filename.endswith(".mb"): 
                filePath = os.path.join(folderPath, filename).replace("\\","/")

                curDict = dict()
                curDict["filePath"] = filePath
                curDict["thumbnailPath"] = cls.getFileThumbnail(filePath)

                fileList.append(curDict)
        
        return fileList

            

        