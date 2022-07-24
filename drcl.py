# Import Pypl Library
from multiprocessing import Value
from tkinter import DISABLED
import pyautogui as ag
import keyboard as kb
import PySimpleGUI as sg
import webbrowser as wb
import sys
import time
import os
import subprocess
# Import Custom Library
import gui_layout as gl
import gui_event_handler as geh

global mf, vdp, adp, awp, cp, drpdp, lsp, lef, pn
mf = "drcl.py" # Main Filename
vdp = 'D:/Note_Database/YouTube/YT Database/YTD File Video/YTDFV Recording-Minecraft' # Video Directory Path
adp = 'D:/Note_Database/YouTube/YT Database/YTD File Audio/YTDFA YT Audio Library' # Audio Directory Path
awp = 'https://studio.youtube.com/channel/UCwHILYLxBpkE5NbuoPO8Rcw/music' # Audio Website Path
cp = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s &' # Chrome Path 
drpdp = 'C:/Users/dachu/AppData/Roaming/Blackmagic Design/DaVinci Resolve/Support/Resolve Disk Database/Resolve Projects/Users/guest/Projects' # DaVinci Resolve Directory Path
drps1ec = 'exec(open("D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Davinci Resolve Clip Loader/script_1.py", encoding="utf-8").read())' # DaVinci Resolve Python Script 1 Execute Command
p1p = './picture/Untitled_Project.png' # Picture 1 Path
p2p = './picture/DaVinci_Resolve_Menu.png' # Picture 2 Path
p4p = './picture/Import_Media.png'
p5p = './picture/Open.png'
p6p = './picture/Edit.png'
p7p = './picture/Timeline_1.png'
lfdp = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Davinci Resolve Clip Loader/log/Project_Number.txt' # Log File Directory Path
lsp = 0.1 # Loop Sleep Parameter
lef = False # Loop Execution Flag
pn = 1000 # Project Number

def make_window_1():
    layout = [
        [sg.Text("Start executing " + mf + "!")],
        [sg.HSeparator()],
        [sg.Text("Type 'n': Next")],
        [sg.Text("Type 'q': Quit")]
    ]
    window = sg.Window('DrCL Startup', layout, grab_anywhere=True, resizable=True, margins=(0,0), keep_on_top=True, use_default_focus=False)
    return window

def make_window_2():
    layout = [
        [sg.Text("Choose a video file in local folder.")],
        [sg.Text("Video Directory: "), sg.Input(enable_events=True, key='FOLDER01', default_text=vdp), sg.FileBrowse(initial_folder=vdp)],
        [sg.Text(key='TEXT01')],
        [sg.HSeparator()],
        [sg.Text("Type 'n': Next")],
        [sg.Text("Type 'q': Quit")]
    ]
    window = sg.Window('DrCL Startup', layout, grab_anywhere=True, resizable=True, margins=(0,0), keep_on_top=True)
    return window

def make_window_3():
    layout = [
        [sg.Text("Choose a audio file from Google Audio Library and download it.")],
        #[sg.Text("Opening " + awp + "...")],
        [sg.Text("Download Directory: " + adp)],
        [sg.Text("Audio Directory: "), sg.Input(enable_events=True, key='FOLDER02', default_text=adp), sg.FileBrowse(initial_folder=adp)],
        [sg.Text(key='TEXT02')],
        [sg.HSeparator()],
        [sg.Text("Type 'n': Next")],
        [sg.Text("Type 'q': Quit")]
    ]
    window = sg.Window('DrCL Startup', layout, grab_anywhere=True, resizable=True, margins=(0,0), keep_on_top=True, relative_location=(-400, -350))
    return window

def make_window_4():
    layout = [
        [sg.Text("Type the DDMS Project Number like \'01\'")],
        [sg.Text("Check privous project at: "), sg.Input(drpdp, disabled=True, text_color='gray')],
        [sg.Text("Project Number: "), sg.Input(key='INPUT01'), sg.Button('Confirm', key='BUTTON01')],
        [sg.Text(key='TEXT03')],
        [sg.HSeparator()],
        [sg.Text("Type 'n': Next")],
        [sg.Text("Type 'q': Quit")]
    ]
    window = sg.Window('DrCL Startup', layout, grab_anywhere=True, resizable=True, margins=(0,0), keep_on_top=True)
    return window

def make_window_5():
    layout = [
        [sg.Text("Drag video and audio into timeline. Type 'n' when finished")],
        [sg.HSeparator()],
        [sg.Text("Type 'n': Next")],
        [sg.Text("Type 'q': Quit")]
    ]
    window = sg.Window('DrCL Startup', layout, grab_anywhere=True, resizable=True, margins=(0,0), keep_on_top=True, relative_location=(400, -350))
    return window

def make_window_6():
    layout = [
        [sg.Text("Adjust video color. Type 'n' when finished")],
        [sg.HSeparator()],
        [sg.Text("Type 'n': Next")],
        [sg.Text("Type 'q': Quit")]
    ]
    window = sg.Window('DrCL Startup', layout, grab_anywhere=True, resizable=True, margins=(0,0), keep_on_top=True, relative_location=(-600, -350))
    return window

if __name__ == '__main__':
    os.system('cls')
    print("\n[LOG] Start executing " + mf + "......")

    # Testing
    

    # 0 Startup Window
    print("[LOG] Startup Window")
    # Open GUI
    window = make_window_1()
    while True:
        event, values = window.read(timeout=100)
        # GUI Event Handling
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            # print('============ Event = ', event, ' ==============')
            # print('-------- Values Dictionary (key=value) --------')
            # for key in values:
            #     print(key, ' = ',
            #     values[key])
            pass
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        # Focus on GUI
        if lef == False:
            ag.click(x=975, y=567)
        lef = True
        # Keyboard Event Handling
        if kb.is_pressed('q'):
            print("[LOG] End executing " + mf + "......")
            sys.exit()
        if kb.is_pressed('n'):
            print("[LOG] next......")
            break
    window.close()
    lef = False
    
    # 1.1 Choosing Video
    print("[LOG] Choosing Video")
    # Open GUI
    window = make_window_2()
    while True:
        event, values = window.read(timeout=100)
        # GUI Event Handling
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            # print('============ Event = ', event, ' ==============')
            # print('-------- Values Dictionary (key=value) --------')
            # for key in values:
            #     print(key, ' = ',
            #     values[key])
            pass
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        # Focus on GUI
        if lef == False:
            ag.click(x=975, y=567)
        lef = True
        # Custom GUI Event Handling
        if event == 'FOLDER01':
            window['FOLDER01'].update(disabled=True)
            vdp = values['FOLDER01']
            print("[LOG] Selected Path: " + vdp)
            window['TEXT01'].update(value='Selected Path: ' + vdp)
        # Keyboard Event Handling
        if kb.is_pressed('q'):
            print("[LOG] End executing " + mf + "......")
            sys.exit()
        if kb.is_pressed('n'):
            print("[LOG] next......")
            break
    window.close()
    lef = False

    # 1.2 Choosing Audio
    print("[LOG] Choosing Audio")
    wb.get(cp).open(awp)
    time.sleep(lsp * 10)
    # Open GUI
    window = make_window_3()
    while True:
        event, values = window.read(timeout=100)
        # General Event Handling
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            # print('============ Event = ', event, ' ==============')
            # print('-------- Values Dictionary (key=value) --------')
            # for key in values:
            #     print(key, ' = ',
            #     values[key])
            pass
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        # Focus on GUI
        if lef == False:
            ag.click(x=542, y=236)#----------
        lef = True
        # Custom GUI Event Handling
        if event == 'FOLDER02':
            window['FOLDER02'].update(disabled=True)
            adp = values['FOLDER02']
            print("[LOG] Selected Path: " + adp)
            window['TEXT02'].update(value='Selected Path: ' + adp)
        # Keyboard Event Handling
        if kb.is_pressed('q'):
            print("[LOG] End ennxecuting " + mf + "......")
            sys.exit()
        if kb.is_pressed('n'):
            print("[LOG] next......")
            break
    window.close()
    lef = False
    for i in range(0, 2):
        os.system("TASKKILL /F /IM chrome.exe")

    # 2.1 Launch Davinci Resolve
    print("[LOG] Launch Davinci Resolve")
    kb.send('win+s')
    time.sleep(lsp * 5)
    kb.write("DaVinci")
    time.sleep(lsp * 5)
    kb.send('enter')
    time.sleep(lsp * 5)
    '''
    ATTENTION: Can't use these commands to launch DaVinci Resolve, since they all holds the program unstill its closed, then proceed to next commend in script.
    cmd = ['C:/Program Files/Blackmagic Design/DaVinci Resolve/Resolve.exe']
    os.chdir('C:/Program Files/Blackmagic Design/DaVinci Resolve')
    os.system('Resolve.exe')
    # os.startfile(cmd[0])
    # subprocess.call(cmd)
    # process = subprocess.Popen(cmd, stdout=subprocess.PIPE)'''

    # 2.2 Request filename
    # Open Windows Explorer For Checking Project Name
    subprocess.Popen('explorer')
    # Open GUI
    window = make_window_4()
    while True:
        event, values = window.read(timeout=100)
        # General Event Handling
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            # print('============ Event = ', event, ' ==============')
            # print('-------- Values Dictionary (key=value) --------')
            # for key in values:
            #     print(key, ' = ',
            #     values[key])
            pass
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        # Focus on GUI
        if lef == False:
            time.sleep(lsp * 5)
            ag.click(x=939, y=552)
        lef = True
        # Custom GUI Event Handling
        if event == 'BUTTON01':
            pn = values['INPUT01']
            print("[LOG] Clicked Confirm! New project name: DDMS" + pn)
            window['TEXT03'].update(value='New project name: DDMS' + pn)
            # Store the values local log file
            f = open(lfdp, 'w', encoding='utf-8')
            f.write(pn)
            f.close()            
        # Keyboard Event Handling
        if kb.is_pressed('q'):
            print("[LOG] End ennxecuting " + mf + "......")
            sys.exit()
        if kb.is_pressed('n'):
            print("[LOG] next......")
            break
    window.close()
    lef = False

    # 2.3 Create new project with default settings
    # Operate DaVinci Resolve Project Manager
    for i in range(0, 2):
        # os.system("TASKKILL /F /IM explorer.exe && start explorer.exe")
        pass
    while True:
        if ag.locateOnScreen(p1p, grayscale=True) != None:
            ag.click(x=897, y=323, clicks=2)
            break
    # Operate DaVinci Resolve Concole
    while True:
        if ag.locateOnScreen(p2p, grayscale=True) != None:
            break
    time.sleep(lsp*5)
    ag.click(x=679, y=30)
    time.sleep(lsp)
    ag.click(x=687, y=527)
    time.sleep(lsp)
    ag.click(x=911, y=326)
    time.sleep(lsp)
    # Run script 'script_1.py', execute 2.3 + 2.4
    ag.typewrite(drps1ec)
    kb.send('enter')
    # Close Console
    ag.click(x=1255, y=295)
    # Buffer
    time.sleep(lsp * 3)
    ag.moveTo(960, 540)

    # 3.1 Import Video
    dp_1 = ''
    dp_2 = ''
    buf = False
    vdp_split = vdp.split('/')
    vdplen = len(vdp_split)
    for i in range(0, vdplen-1):
        dp_1 = dp_1 + vdp_split[i] + '/'
    dp_2 = vdp_split[-1]
    # Import Video
    kb.send('ctrl+i')
    time.sleep(lsp * 20)
    kb.write(dp_2)
    time.sleep(lsp * 5)
    while True:
        if ag.locateOnScreen(p4p, grayscale=True) != None:
            kb.send('f4')
            kb.send('ctrl+a')
            kb.send('delete')
            kb.write(dp_1)
            kb.send('enter')
            break
    while buf == False:
        print("[LOG] finding...")
        buf = ag.locateOnScreen(p5p, grayscale=True)
    time.sleep(lsp)
    ag.click(ag.center(buf))

    # Buffer
    time.sleep(lsp * 3)
    ag.moveTo(960, 540)

    # 3.2 Import Audio
    dp_1 = ''
    dp_2 = ''
    buf = None
    adp_split = adp.split('/')
    adplen = len(adp_split)
    for i in range(0, adplen-1):
        dp_1 = dp_1 + adp_split[i] + '/'
    dp_2 = adp_split[-1]

    print(dp_1)
    print(dp_2)

    # Import Audio
    kb.send('ctrl+i')
    time.sleep(lsp * 20)
    kb.write(dp_2)
    time.sleep(lsp * 5)
    while True:
        if ag.locateOnScreen(p4p, grayscale=True) != None:
            kb.send('f4')
            kb.send('ctrl+a')
            kb.send('delete')
            kb.write(dp_1)
            kb.send('enter')
            break
    while buf == None:
        print("[LOG] finding...")
        buf = ag.locateOnScreen(p5p, grayscale=True)
    time.sleep(lsp)
    ag.click(ag.center(buf))

    # 4 Load video and audio into timeline
    # Buffer
    time.sleep(lsp * 3)
    ag.moveTo(960, 540)
    # Switch to Edit Tab
    buf = None
    while buf == None:
        print('[LOG] finding...')
        buf = ag.locateOnScreen(p6p, grayscale=True)
    ag.click(ag.center(buf))
    # Buffer
    time.sleep(lsp * 3)
    ag.moveTo(960, 540)
    # Open GUI
    window = make_window_5()
    while True:
        event, values = window.read(timeout=100)
        # GUI Event Handling
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            # print('============ Event = ', event, ' ==============')
            # print('-------- Values Dictionary (key=value) --------')
            # for key in values:
            #     print(key, ' = ',
            #     values[key])
            pass
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        # Focus on GUI
        if lef == False:
            ag.click(x=1367, y=227)
        lef = True
        # Keyboard Event Handling
        if kb.is_pressed('q'):
            print("[LOG] End executing " + mf + "......")
            sys.exit()
        if kb.is_pressed('n'):
            print("[LOG] next......")
            break
    window.close()
    lef = False

    # 5.1 Adjust video color
    # Open GUI
    window = make_window_6()
    while True:
        event, values = window.read(timeout=100)
        # GUI Event Handling
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            # print('============ Event = ', event, ' ==============')
            # print('-------- Values Dictionary (key=value) --------')
            # for key in values:
            #     print(key, ' = ',
            #     values[key])
            pass
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        # Focus on GUI
        if lef == False:
            ag.click(x=374, y=217)
        lef = True
        # Keyboard Event Handling
        if kb.is_pressed('q'):
            print("[LOG] End executing " + mf + "......")
            sys.exit()
        if kb.is_pressed('n'):
            print("[LOG] next......")
            break
    window.close()
    lef = False

    # 5.2 Duplicate timeline for IG
    # Buffer
    time.sleep(lsp * 3)
    ag.moveTo(960, 540)
    # Switch to Edit Tab
    buf = None
    while buf == None:
        print('[LOG] finding...')
        buf = ag.locateOnScreen(p6p, grayscale=True)
    ag.click(ag.center(buf))
    # Buffer
    time.sleep(lsp * 3)
    ag.moveTo(960, 540)
    # Click on Timeline
    buf = None
    while buf == None:
        print('[LOG] finding...')
        buf = ag.locateOnScreen(p7p, grayscale=True)
    time.sleep(lsp * 3)
    ag.click(ag.center(buf))
    time.sleep(lsp * 3)
    ag.hotkey('ctrl', 'c')
    time.sleep(lsp * 3)
    ag.hotkey('ctrl', 'v')

    # 6

    # Buffer
    time.sleep(lsp * 3)
    ag.moveTo(960, 540)

    # End executing
    print("[LOG] End executing " + mf + "......\n")
    sys.exit(0)
