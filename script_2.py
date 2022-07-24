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

########################################################################################################################

lfdp = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Davinci Resolve Clip Loader/log/Project_Number.txt' # Log File Directory Path
drpmp = 'C:/Users/dachu/AppData/Roaming/Blackmagic Design/DaVinci Resolve/Support/Resolve Disk Database/Resolve Projects/Users/guest/Projects' # DaVinci Resolve Project Media Path

# Load default project requirement
#os.system('cls')
print("[LOG] Start executing script_2.py")
f = open(lfdp, 'r', encoding='utf-8')
pn = f.read()
f.close()
print("[LOG] " + pn)
projectName = "DDMS" + pn
resolve = GetResolve()
projectManager = resolve.GetProjectManager()
mediastorage = resolve.GetMediaStorage()
project = projectManager.LoadProject(projectName)
if not project:
    print("[LOG] Unable to load a project '" + projectName + "'")
    sys.exit()
mediapool = project.GetMediaPool()
rootFolder = mediapool.GetRootFolder()

# 4.1 Create first timeline for YT (finished)
# timelineName = "Timeline 1"
# timeline = mediapool.CreateEmptyTimeline(timelineName)
# if not timeline:
    # print("Unable to create timeline '" + timelineName + "'")

# 4.2 Move video in timeline


# 4.3 Move audio in timeline

print("End executing script_2.py")

'''DaVinci Resolve Scripting Command
exec(open("D:\\Note_Database\\Subject\\CPDWG Custom Program Developed With Gidhub\\Davinci Resolve Clip Loader\\script_2.py", encoding='utf-8').read())
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