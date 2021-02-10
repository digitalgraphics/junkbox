import os
import datetime
import time
import math
import shutil
from enum import Enum

from raphScripts.junkbox.resource import resource_rc


class FilterMode(Enum):
    FolderOnly = 1
    FileOnly = 2
    FolderAndFile = 3


class FileManager(object):

    @classmethod
    def getFileThumbnail(cls, filePath):
        thumbnailPath = filePath.replace(".ma", ".jpg")

        if os.path.exists(thumbnailPath):
            return thumbnailPath
        else:
            return ":/icon/mayaLogo.png"

    @classmethod
    def getFileBaseName(cls, filePath, withExtension=True):
        basename = os.path.basename(filePath)

        if withExtension:
            return basename
        else:
            return basename.split(".")[0]

    @classmethod
    def getFolderBaseName(cls, dirPath):
        basename = os.path.basename(dirPath)
        return basename

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
    def getFolderPathOfFile(cls, filePath):
        return os.path.dirname(os.path.abspath(filePath))

    @classmethod
    def createFolder(cls, folderPath):
        os.mkdir(folderPath)

    @classmethod
    def getFolders(cls, path, filterKeyword=None, filterMode=None):

        def dirContainsKeyword(curPath):
            if filterKeyword == None:
                return True

            for root, dirs, files in os.walk(curPath, topdown=False):
                if (filterMode == FilterMode.FileOnly or filterMode == FilterMode.FolderAndFile) and any(filterKeyword.lower() in s.lower() for s in files):
                    return True
                if (filterMode == FilterMode.FolderOnly or filterMode == FilterMode.FolderAndFile) and filterKeyword in cls.getFolderBaseName(root):
                    return True

            return False

        def dirToDict(curPath):
            curDir = dict()
            for filename in os.listdir(curPath):
                path = os.path.join(curPath, filename)
                if os.path.isdir(path) and dirContainsKeyword(path):
                    curDir[filename] = dirToDict(
                        path)

            return curDir

        return dirToDict(path)

    @classmethod
    def normPath(cls, path):
        return os.path.normpath(path)

    @classmethod
    def existingPath(cls, path):
        return os.path.exists(path)

    @classmethod
    def removeFolder(cls, folderPath):
        if not os.listdir(folderPath):
            os.rmdir(folderPath)
        else:
            shutil.rmtree(folderPath)

    @classmethod
    def removeMayaFiles(cls, filePaths):
        for path in filePaths:
            if os.path.exists(path):
                os.remove(path)

                thumbnailPath = cls.getFileThumbnail(path)
                if os.path.exists(thumbnailPath):
                    os.remove(thumbnailPath)

    @classmethod
    def moveMayaFilesToDir(cls, srcPaths, destDir):
        for path in srcPaths:
            if cls.normPath(destDir) != cls.normPath(cls.getFolderPathOfFile(path)):
                shutil.move(path, destDir)

                thumbnailPath = cls.getFileThumbnail(path)
                if os.path.exists(thumbnailPath):
                    shutil.move(thumbnailPath, destDir)

    @classmethod
    def getMayaFilesFromFolder(cls, folderPath, filterKeyword=False, recursive=False):
        tmpList = []

        if recursive:
            for root, dirs, files in os.walk(folderPath, topdown=False):
                for name in files:
                    if name.endswith(".ma"):
                        if not filterKeyword or filterKeyword.lower() in name.lower():
                            tmpList.append(os.path.join(
                                root, name).replace("\\", "/"))
        else:
            for filename in os.listdir(folderPath):
                if filename.endswith(".ma"):
                    if not filterKeyword or filterKeyword.lower() in name.lower():
                        tmpList.append(os.path.join(
                            folderPath, filename).replace("\\", "/"))
        fileList = []

        for filePath in tmpList:
            curDict = dict()
            curDict["filePath"] = filePath
            curDict["thumbnailPath"] = cls.getFileThumbnail(filePath)

            fileList.append(curDict)

        return fileList
