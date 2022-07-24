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

vdp = 'D:/Note_Database/YouTube/YT Database/YTD File Video/YTDFV Recording-Minecraft/Minecraft 2022.07.14 - 18.30.51.08.mp4' # Video Directory Path
adp = 'D:/Note_Database/YouTube/YT Database/YTD File Audio/YTDFA YT Audio Library/Go Down Swinging (Instrumental) - NEFFEX.mp3' # Audio Directory Path
p2p = './picture/DaVinci_Resolve_Menu.png' # Picture 2 Path
p4p = './picture/Import_Media.png'
p5p = './picture/Open.png'
p6p = './picture/Edit.png'
p7p = './picture/Timeline_1.png'

lsp = 0.1 # Loop Sleep Parameter

os.system('cls')
time.sleep(5)

# Buffer
time.sleep(lsp * 3)
ag.moveTo(960, 540)

# Switch to Edit Tab
buf = None
while buf == None:
    print('[LOG] finding...')
    buf = ag.locateOnScreen(p7p, grayscale=True)
time.sleep(lsp)
ag.click(ag.center(buf))
time.sleep(lsp)
ag.hotkey('ctrl', 'c')
time.sleep(lsp)
ag.hotkey('ctrl', 'v')

# Buffer
time.sleep(lsp * 3)
ag.moveTo(960, 540)

