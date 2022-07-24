from logging import root
import os
import sys
import tkinter
from tkinter import filedialog
import webbrowser as wb
import importlib as ipl

def GetResolve():
	try:
	# The PYTHONPATH needs to be set correctly for this import statement to work.
	# An alternative is to import the DaVinciResolveScript by specifying absolute path (see ExceptionHandler logic)
		import DaVinciResolveScript as bmd
	except ImportError:
		expectedPath=os.getenv('PROGRAMDATA') + "\\Blackmagic Design\\DaVinci Resolve\\Support\\Developer\\Scripting\\Modules\\"		
		# check if the default path has it...
		print("Unable to find module DaVinciResolveScript from $PYTHONPATH - trying default locations")
		try:
			import imp
			bmd = imp.load_source('DaVinciResolveScript', expectedPath+"DaVinciResolveScript.py")
		except ImportError:
			# No fallbacks ... report error:
			print("Unable to find module DaVinciResolveScript - please ensure that the module DaVinciResolveScript is discoverable by python")
			print("For a default DaVinci Resolve installation, the module is expected to be located in: "+expectedPath)
			sys.exit()
	print("DaVinci Resolve module found")
	return bmd.scriptapp("Resolve")

def CreateNewProject():
    # Set the project settings
    print("Project name: " + projectName)
    print("Framerate: " + str(framerate))
    print("Width: " + str(width))
    print("Height: " + str(height))

    # Create project and set parameters:
    resolve = GetResolve()
    projectManager = resolve.GetProjectManager()
    mediastorage = resolve.GetMediaStorage()
    # project = projectManager.CreateProject('./DDMS/' + projectName)
    project = projectManager.CreateProject(projectName)

    if not project:
        print("Unable to create a project '" + projectName + "'")
        sys.exit()
    return resolve, projectManager, mediastorage, project

def LoadProject():
    # used for script testing
    resolve = GetResolve()
    projectManager = resolve.GetProjectManager()
    mediastorage = resolve.GetMediaStorage()
    project = projectManager.LoadProject(projectName)
    if not project:
        print("Unable to load a project '" + projectName + "'")
        resolve, projectManager, mediastorage, project = CreateNewProject()
    return resolve, projectManager, mediastorage, project

def ResolveProjectInitialize():
    # Set the project settings
    resolve, projectManager, mediastorage, project = LoadProject()
    # resolve, projectManager, mediastorage, project = CreateNewProject ()

    project.SetSetting("timelineFrameRate", str(framerate))
    project.SetSetting("timelineResolutionWidth", str(width))
    project.SetSetting("timelineResolutionHeight", str(height))

    # Add folder contents to Media Pool:
    mediapool = project.GetMediaPool()
    rootFolder = mediapool.GetRootFolder()

    # Create timeline:
    # timelineName = "Timeline 1"
    # timeline = mediapool.CreateEmptyTimeline(timelineName)
    # if not timeline:
    #     print("Unable to create timeline '" + timelineName + "'")
    return resolve, projectManager, project, mediapool, mediastorage, rootFolder, clips

if __name__ == '__main__':
    os.system('cls')
    print("Start executing drcl.py")

    # Default parameters for the project
    global project_num, projectName, framerate, width, height, mediaPath, resolve, projectManager, project
    project_num = 36
    projectName = "DDMS" + str(project_num)
    framerate = 60
    width = 1920
    height = 1080
    mediaPath = "C:/Users/dachu/AppData/Roaming/Blackmagic Design/DaVinci Resolve/Support/Resolve Disk Database/Resolve Projects/Users/guest/Projects" + projectName + "/"

    # # Workflow
    # # 4.1 Open YouTube Audio Library (Doen't work)
    # url = 'https://studio.youtube.com/channel/UCwHILYLxBpkE5NbuoPO8Rcw/music'
    # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    # wb.get(chrome_path).open(url)
    
    # 4.2 Open DaVinci Resolve, create new project, done initialize settings
    resolve, projectManager, project, mediapool, mediastorage, rootFolder, clips = ResolveProjectInitialize()

    # 4.3 Import media from folder
    resolve.OpenPage("media")
    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    video_path = filedialog.askopenfile()
    print("Video path: " + str(video_path))
    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    audio_path = filedialog.askopenfile()
    print("Audio path: " + str(audio_path))

    # # Add new folder in Media Pool:
    # root = mediapool.GetRootFolder()
    # print(str(root))
    # mediapool.AddSubFolder(root, "Media")

    clip1 = mediastorage.AddItemListToMediaPool(video_path)
    print(str(clip1))
    clip2 = mediastorage.AddItemListToMediaPool(audio_path)
    print(str(clip2))

    timeline = mediapool.CreateEmptyTimeline("Timeline 1")
    print(str(timeline))
    mediapool.AppendToTimeline(clip1)
    print(str(timeline))
    mediapool.AppendToTimeline(clip2)
    print(str(timeline))
    
    projectManager.SaveProject()

    print("End executing drcl.py")

'''DaVinci Resolve Scripting Command
exec(open("D:\\Note_Database\\Subject\\CPDWG Custom Program Developed With Gidhub\\Davinci Resolve Clip Loader\\drcl.py", encoding='utf-8').read())
'''

'''Links
https://www.youtube.com/watch?v=4gtz4J9cxbE
https://note.com/hitsugi_yukana/n/n1601e81df8d7
https://github.com/search?l=Python&q=davinci+resolve&type=Repositories
https://github.com/pressreset/resutil/blob/master/resutil.py
https://github.com/deric/DaVinciResolve-API-Docs/tree/main/examples/python
https://diop.github.io/davinci-resolve-api/#/
https://www.youtube.com/results?search_query=davinci+resolve+api+add+media+to+media+pool
'''