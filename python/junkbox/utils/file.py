import os
import datetime
import json
import time
import math
import shutil
import glob
from enum import Enum

from junkbox.resource import resource_rc


class FilterMode(Enum):
    FolderOnly = 1
    FileOnly = 2
    FolderAndFile = 3


def getFileThumbnail(filePath):
    thumbnailPath = filePath.replace(".ma", ".jpg")

    if os.path.exists(thumbnailPath):
        return thumbnailPath
    else:
        return ":/icon/mayaLogo.png"


def getFileBaseName(filePath, withExtension=True):
    basename = os.path.basename(filePath)

    if withExtension:
        return basename
    else:
        return basename.split(".")[0]


def getFolderBaseName(dirPath):
    basename = os.path.basename(dirPath)
    return basename


def getFileCreationDate(filePath):
    fileTime = os.path.getctime(filePath)
    return time.strftime('%d-%m-%Y %H:%M', time.gmtime(fileTime))


def getFileModifyDate(filePath):
    fileTime = os.path.getmtime(filePath)
    return time.strftime('%d-%m-%Y %H:%M', time.gmtime(fileTime))


def getFileExtensionType(filePath):
    filename, extension = os.path.splitext(filePath)
    return extension.replace('.', '') + " File"


def getFileSize(filePath):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    nbytes = os.path.getsize(filePath)
    rank = int((math.log10(nbytes)) / 3)
    rank = min(rank, len(suffixes) - 1)
    human = nbytes / (1024.0 ** rank)
    f = ('%.2f' % human).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[rank])


def getFolderPathOfFile(filePath):
    return os.path.dirname(os.path.abspath(filePath))


def createFolder(folderPath):
    os.mkdir(folderPath)


def getFolders(path, filterKeyword=None, filterMode=None):

    def dirContainsKeyword(curPath):
        if filterKeyword == None:
            return True

        for root, dirs, files in os.walk(curPath, topdown=False):
            if (filterMode == FilterMode.FileOnly or filterMode == FilterMode.FolderAndFile) and any(filterKeyword.lower() in s.lower() for s in files):
                return True
            if (filterMode == FilterMode.FolderOnly or filterMode == FilterMode.FolderAndFile) and filterKeyword in getFolderBaseName(root):
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


def normPath(path):
    return os.path.normpath(path)


def existingPath(path):
    return os.path.exists(path)


def updateVersionLetter(letter):
    if not letter:
        return 'a'

    lastLetter = letter[-1]
    if lastLetter != 'z':
        return letter[:-1] + chr(ord(lastLetter) + 1)
    else:
        return letter + 'a'


def getVersionFilePath(filePath):

    folderPath = getFolderPathOfFile(filePath)
    basename = getFileBaseName(filePath, withExtension=False)
    pattern = folderPath + '/' + basename + "_*"
    fileList = [getFileBaseName(str(s), withExtension=False)
                for s in glob.glob(pattern)]

    if len(fileList) == 0:
        if len(glob.glob(folderPath + '/' + basename + "*")) > 0:
            return folderPath, basename + "_" + updateVersionLetter('')
        else:
            return folderPath, basename
    else:
        fileList = sorted(fileList, key=str.lower)
        lastLetters = fileList[-1].split("_")[-1]
        newtLetters = updateVersionLetter(lastLetters)
        return folderPath, basename + "_" + newtLetters


def removeFolder(folderPath):
    if not os.listdir(folderPath):
        os.rmdir(folderPath)
    else:
        shutil.rmtree(folderPath)


def removeMayaFiles(filePaths):
    for path in filePaths:
        if os.path.exists(path):
            os.remove(path)

            thumbnailPath = getFileThumbnail(path)
            if os.path.exists(thumbnailPath):
                os.remove(thumbnailPath)


def moveMayaFilesToDir(srcPaths, destDir):
    for path in srcPaths:
        if normPath(destDir) != normPath(getFolderPathOfFile(path)):
            shutil.move(path, destDir)

            thumbnailPath = getFileThumbnail(path)
            if os.path.exists(thumbnailPath):
                shutil.move(thumbnailPath, destDir)


def getMayaFilesFromFolder(folderPath, filterKeyword=False, recursive=False):
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
        curDict["thumbnailPath"] = getFileThumbnail(filePath)

        fileList.append(curDict)

    return fileList


def writeJsonFile(data, filePath):
    with open(filePath, 'w') as outfile:
        json.dump(data, outfile)


def readJsonFile(filePath):
    print filePath
    if existingPath(filePath):
        with open(filePath) as json_file:
            return json.load(json_file)
    else:
        return {}
