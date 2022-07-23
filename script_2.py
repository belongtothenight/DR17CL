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
lsp = 0.1 # Loop Sleep Parameter

os.system('cls')
time.sleep(5)

# Split video source file path
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
time.sleep(lsp)
kb.write(dp_2)
time.sleep(lsp)
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

# Split audio source file path
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
time.sleep(lsp)
kb.write(dp_2)
time.sleep(lsp)
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
print(type(buf))
print(buf)
time.sleep(lsp)
ag.click(ag.center(buf))