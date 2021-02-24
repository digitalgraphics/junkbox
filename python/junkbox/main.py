scriptFolder = 'H:/sandbox/raphaelJ/junkbox/python/'
"""
name : reloadAll
description : reload all the junkbox modules
"""


def reloadAll():
    for i in range(2):
        import junkbox.component.flatbutton
        reload(junkbox.component.flatbutton)
        import junkbox.resource
        reload(junkbox.resource)

        import junkbox.utils.file
        reload(junkbox.utils.file)
        import junkbox.utils.mayautil
        reload(junkbox.utils.mayautil)
        import junkbox.utils.thumbnail
        reload(junkbox.utils.thumbnail)

        import junkbox.view.settingsdialog
        reload(junkbox.view.settingsdialog)
        import junkbox.view.thumbnaildialog
        reload(junkbox.view.thumbnaildialog)
        import junkbox.view.browsecollectiondialog
        reload(junkbox.view.browsecollectiondialog)
        import junkbox.view.creationdialog
        reload(junkbox.view.creationdialog)
        import junkbox.view.mainwindow
        reload(junkbox.view.mainwindow)

        import junkbox.component.deselectabletreewidget
        reload(junkbox.component.deselectabletreewidget)
        import junkbox.component.thumbnailwidget
        reload(junkbox.component.thumbnailwidget)
        import junkbox.component.assetpreviewwidget
        reload(junkbox.component.assetpreviewwidget)
        import junkbox.component.assetviewwidget
        reload(junkbox.component.assetviewwidget)
        import junkbox.component.assethierarchywidget
        reload(junkbox.component.assethierarchywidget)

        import junkbox.ui.settingsdialog
        reload(junkbox.ui.settingsdialog)
        import junkbox.ui.thumbnailwidget
        reload(junkbox.ui.thumbnailwidget)
        import junkbox.ui.thumbnaildialog
        reload(junkbox.ui.thumbnaildialog)
        import junkbox.ui.assetpreviewwidget
        reload(junkbox.ui.assetpreviewwidget)
        import junkbox.ui.browsecollectiondialog
        reload(junkbox.ui.browsecollectiondialog)
        import junkbox.ui.creationdialog
        reload(junkbox.ui.creationdialog)
        import junkbox.ui.assethierarchywidget
        reload(junkbox.ui.assethierarchywidget)
        import junkbox.ui.assetviewwidget
        reload(junkbox.ui.assetviewwidget)
        import junkbox.ui.mainwindow
        reload(junkbox.ui.mainwindow)


"""
name : compileResources
description : compite the resource file using maya binary files
"""


def compileResources():
    import subprocess
    mayaFolder = "C:/Program Files/Autodesk/Maya2018/bin/"
    qrcFilename = 'junkbox/resource/resource.qrc'
    bashCommand = [
        mayaFolder + "pyside2-rcc.exe", scriptFolder + qrcFilename, "-o",
        scriptFolder + qrcFilename.replace(".qrc", "_rc.py")
    ]

    process = subprocess.Popen(bashCommand,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    output, err = process.communicate()


"""
name : compileUis
description : compile all the ui files from junkbox/ui to py files
"""


def compileUis():
    from pyside2uic import compileUi
    import os

    uiPath = scriptFolder + 'junkbox/ui'
    for file in os.listdir(uiPath):
        if file.endswith(".ui"):
            file = uiPath + "/" + file
            print "compile : " + file
            tmp = uiPath + '/tmp.py'

            uiOutput = open(tmp, "w")
            compileUi(file, uiOutput, False, 4, False)
            uiOutput.close()

            fin = open(tmp, "rt")
            fout = open(file.replace(".ui", ".py"), "wt")

            for line in fin:
                fout.write(
                    line.replace('import resource_rc',
                                 'from junkbox.resource import resource_rc'))

            fin.close()
            fout.close()


"""
name : run
param : 
    - needCompileresources : True to recompile the resource file
    - needCompileUis : True to compile all the ui from junkbox/ui
    - needReloadAll : True to reload all the junkbox modules
description : run the main junkbox window
"""


def run(needCompileResources=False, needCompileUis=False, needReloadAll=False):

    if needCompileResources:
        compileResources()

    if needCompileUis:
        compileUis()

    if needReloadAll:
        reloadAll()

    from junkbox.view.mainwindow import MainWindow
    MainWindow().show()
