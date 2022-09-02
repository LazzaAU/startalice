This script is used for 
- updating Alice and/or
- starting alice with or without logging and/or
- starting in manual mode or permanently (via the alice service)

It's just a personal script i created cause i was bored :) but feel free to use it if you feel the urge

Setup -
a. Install colorama using ``` pip3 install colorama ``` to the PI Alice is installed on

1. Add this script to the PI that ProjectAlice is running on. add it to ``` /home/pi ``` directory
2. Open the .bashrc file ``` nano ~/.bashrc ```
3. Add this to the bottom of the file ``` alias startalice="python3 startalice.py" ```
4. Close and reopen the terminal or type ``` source .bashrc ```
5. Now type ``` startalice ``` in the command line to activate the script and follow on screen prompts

Script modifications -
1. Change alicePath variable to your ProjectAlice path. default is /home/pi/ProjectAlice see line 28
2. If you want to run Alice on rc3 branch, comment out  ``` branch = 'master' ``` and un comment ``` # branch = '1.0.0-rc3' ```
    (see lines 30 and 31 / 32 below)
    
I'm well aware i could of done this in a few lines of bash code. However, like i said... i was bored and wanted something to code. Feel free to use it :)
