# Import Pypl Library
from logging import root
import os
import sys

'''
ATTENTION: This is not the main module, please run drcl.py instead.
This script is used to execute work flow section 2.
Open DaVinci Resolve project manager, requestion filename, create new porject, change resolution settings.
2-3. Create new project
2-4. Change project settings
'''

def GetResolve():
	try:
	# The PYTHONPATH needs to be set correctly for this import statement to work.
	# An alternative is to import the DaVinciResolveScript by specifying absolute path (see ExceptionHandler logic)
		import DaVinciResolveScript as bmd
	except ImportError:
		expectedPath=os.getenv('PROGRAMDATA') + "\\Blackmagic Design\\DaVinci Resolve\\Support\\Developer\\Scripting\\Modules\\"		
		# check if the default path has it...
		print("[LOG] Unable to find module DaVinciResolveScript from $PYTHONPATH - trying default locations")
		try:
			import imp
			bmd = imp.load_source('DaVinciResolveScript', expectedPath+"DaVinciResolveScript.py")
		except ImportError:
			# No fallbacks ... report error:
			print("[LOG] Unable to find module DaVinciResolveScript - please ensure that the module DaVinciResolveScript is discoverable by python")
			print("[LOG] For a default DaVinci Resolve installation, the module is expected to be located in: "+expectedPath)
			sys.exit()
	print("[LOG] DaVinci Resolve module found")
	return bmd.scriptapp("Resolve")

########################################################################################################################

lfdp = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Davinci Resolve Clip Loader/log/Project_Number.txt' # Log File Directory Path

#os.system('cls')
print("[LOG] [LOG] Start executing drcl.py")
f = open(lfdp, 'r', encoding='utf-8')
pn = f.read()
f.close()
print("[LOG] " + pn)

# Default parameters for the project
global project_num, projectName, framerate, width, height, mediaPath, resolve, projectManager, project
project_num = pn
projectName = "DDMS" + project_num
framerate = 60
width = 1920
height = 1080
mediaPath = "C:/Users/dachu/AppData/Roaming/Blackmagic Design/DaVinci Resolve/Support/Resolve Disk Database/Resolve Projects/Users/guest/Projects" + projectName + "/"

# 2-3. Create new project
resolve = GetResolve()
projectManager = resolve.GetProjectManager()
mediastorage = resolve.GetMediaStorage()
project = projectManager.CreateProject(projectName)

if not project:
    print("[LOG] Unable to create a project '" + projectName + "'")
    sys.exit()

# 2-4. Change project settings
project.SetSetting("timelineFrameRate", str(framerate))
project.SetSetting("timelineResolutionWidth", str(width))
project.SetSetting("timelineResolutionHeight", str(height))
print("[LOG] Project name: " + projectName)
print("[LOG] Framerate: " + str(framerate))
print("[LOG] Width: " + str(width))
print("[LOG] Height: " + str(height))

print("[LOG] Project {0} created".format(projectName))

print("[LOG] End executing script_1.py")

'''DaVinci Resolve Scripting Command
exec(open("D:\\Note_Database\\Subject\\CPDWG Custom Program Developed With Gidhub\\Davinci Resolve Clip Loader\\script_1.py", encoding='utf-8').read())
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