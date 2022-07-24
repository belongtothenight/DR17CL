# DaVinci Resolve 17 Clip Loader
## ATTENTION: This project is not finished, not under developing.
The original way to automate this project is by using its API, but it can only be triggered with the internal console, which is no way reachable using script without directly interact with GUI. Also, despite the detailed description on API, the available functions are not really helpful in automation workflow and quite time consuminig to try out their full functionalities. With these two reasons, making it inevidable to automate this process using 'pyautogui' or 'keyboard' + 'mouse' library. This approach is way too unreliable, it can work on partial tesing, but fail when conbined together.</br>
Overall, currently availble method to fully automate my daily video editing workflow is not yet achievable.
### DR17CL Work Flow
0. Startup
1. Open youtube studio and audio library in google.
   1. Choosing Video
   2. Choosing Audio
2. Open DaVinci Resolve 17 browser, request filename, create new project, and change resolution settings.
   1. Launch DaVinci Resolve
   2. Request filename
   3. Create new project
   4. Change project settings
3. Import selected video and audio.
   1. Import Video
   2. Import Audio
4. Automatically put video and audio into timeline.
   1. Create first timeline for YT.
   2. Move video in timeline
   3. Move audio in timeline
5. Duplicate timeline after color is adjusted.
   1. Adjust video color.
   2. Duplicate timeline for IG.
6. In YT videos, add title automatically(audio name and creator), adjust video length, add fade in and out on video and audio.
   1. Adjust video length
   2. Add title for audio
   3. Add fade in and out for video and audio
   4. Limit export timeline length
7. In IG videos, adjust video and audio length, add fade in and out on audio.
   1. Adjust video and audio length
   2. Add fade in and out for audio
8. Configure both timeline render settings.
   1. Configure YT timeline.
   2. Configure IG timeline.
9.  Ask for final confirmation.
   3.  Ask for confirmation
10. Render both timeline.
   4.  Trigger rendering.
   5.  Read progress and show in progress bar?

### Additional Functionality
1. Progress of entire script visualize on GUI.

### DR17CL Requirement

https://gist.github.com/X-Raym/2f2bf453fc481b9cca624d7ca0e19de8

DaVinci Resolve Scripting Doc
C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\README.txt