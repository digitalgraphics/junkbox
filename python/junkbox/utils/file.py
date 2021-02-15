import os
import datetime
import json
import time
import math
import shutil
import glob
from enum import Enum

from junkbox.resource import resource_rc

"""
name : FilterMode
description : enumeration from filter mode
"""
class FilterMode(Enum):
    FolderOnly = 1
    FileOnly = 2
    FolderAndFile = 3

"""
name : getFileThumbnail
description : get the tumbnail path of the given maya file
param : 
    - filePath : the file path to get the thumbnail
return : the path of the thumbnail
"""
def getFileThumbnail(filePath):
    thumbnailPath = filePath.replace(".ma", ".jpg")

    if os.path.exists(thumbnailPath):
        return thumbnailPath
    else:
        return ":/icon/mayaLogo.png"


"""
name : getFileBaseName
description : get the base name of the given file path
param : 
    - filePath : the file path to get the base name
    - withExtension : True if the extension is kept
return : the base name ( with extension )
"""
def getFileBaseName(filePath, withExtension=True):
    basename = os.path.basename(filePath)

    if withExtension:
        return basename
    else:
        return basename.split(".")[0]

"""
name : getFolderBaseName
description : get the base name of the given folder path
param : 
    - dirPath : the folder path to get the base name
return : the base name of the given folder
"""
def getFolderBaseName(dirPath):
    basename = os.path.basename(dirPath)
    return basename

"""
name : getFileCreationDate
description : get the creation date of the given file path
param : 
    - filePath : the file path
return : the creation date
"""
def getFileCreationDate(filePath):
    fileTime = os.path.getctime(filePath)
    return time.strftime('%d-%m-%Y %H:%M', time.gmtime(fileTime))

"""
name : getFileModifyDate
description : get the formatted modified date of the given file path
param : 
    - filePath : the file path
return : the formatted modified date
"""
def getFileModifyDate(filePath):
    fileTime = os.path.getmtime(filePath)
    return time.strftime('%d-%m-%Y %H:%M', time.gmtime(fileTime))

"""
name : getfileExtensionType
description : get the file extension info of the given file path
param : 
    - filePath : the file path
return : the extension info
"""
def getFileExtensionType(filePath):
    filename, extension = os.path.splitext(filePath)
    return extension.replace('.', '') + " File"

"""
name : getFileSize
description : get the formatted file size if the given file path
param : 
    - filePath : the file path
return : the formatted file size
"""
def getFileSize(filePath):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    nbytes = os.path.getsize(filePath)
    rank = int((math.log10(nbytes)) / 3)
    rank = min(rank, len(suffixes) - 1)
    human = nbytes / (1024.0 ** rank)
    f = ('%.2f' % human).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[rank])

"""
name : getFolderPathOfFile
description : get the folder path of a given file path
param : 
    - filePath : the file path
return : the parent folder path
"""
def getFolderPathOfFile(filePath):
    return os.path.dirname(os.path.abspath(filePath))

"""
name : createFolder
description : create a folder according to the given folder path
param : 
    - folderPath : the folder path to create
"""
def createFolder(folderPath):
    os.mkdir(folderPath)


"""
name : getFolders
description : get an objets corresponging to the inner folder
    hierarchy of the given folder path
param : 
    - filterKeyword : a keyword to filter the inner folder
    - filterMode : the way to apply the filter keyword
return : an objet that represents the hierarchy of the inner folders
"""
def getFolders(path, filterKeyword=None, filterMode=None):

    # check if the directory contains the filter keyword in
    # its children
    def dirContainsKeyword(curPath):
        if filterKeyword == None:
            return True

        for root, dirs, files in os.walk(curPath, topdown=False):
            if (filterMode == FilterMode.FileOnly or filterMode == FilterMode.FolderAndFile) and any(filterKeyword.lower() in s.lower() for s in files):
                return True
            if (filterMode == FilterMode.FolderOnly or filterMode == FilterMode.FolderAndFile) and filterKeyword in getFolderBaseName(root):
                return True

        return False

    # convert a directory to the object with the hierarchy
    def dirToDict(curPath):
        curDir = dict()
        for filename in os.listdir(curPath):
            path = os.path.join(curPath, filename)
            if os.path.isdir(path) and dirContainsKeyword(path):
                curDir[filename] = dirToDict(
                    path)

        return curDir

    return dirToDict(path)


"""
name : normPath
description : norm the given file path
param : 
    - path : the file path
return : the normed file path
"""
def normPath(path):
    return os.path.normpath(path)


"""
name : existingPath
description : check if the given path exists
param : 
    - path : the path to check
return : True if the path exists
"""
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
