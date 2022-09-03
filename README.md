## This script is used for 
- Updating Alice and/or
- Starting alice with or without logging and/or
- Starting in manual mode or permanently (via the alice service)

It's just a personal script I created because I was bored :) but feel free to use it if you feel the urge.

NOTE: The Official Project Alice way is to run [ProjectAlices CLI tool](https://pypi.org/project/projectalice-cli/). 
As I like to play with skill making for Alice, I tend to spend more time on the actual Alice Pi, than remotely,
where the CLI tool is used. Therefore, this just suits me :)

# Setup -


a. Install colorama using ``` pip3 install colorama ``` to the PI that Alice is installed on.

1. Add this script to the PI that ProjectAlice is running on. Add it to ``` /home/pi ``` directory
2. Open the .bashrc file ``` nano ~/.bashrc ```
3. Add this to the bottom of the file ``` alias startalice="python3 startalice.py" ```
4. Close and reopen the terminal or type ``` source .bashrc ```
5. Now type ``` startalice ``` in the command line to activate the script and follow-on screen prompts

# Script modifications -
1. Change alicePath variable to your ProjectAlice path. default is ```/home/pi/ProjectAlice``` see line 28
2. If you want to run Alice on rc3 branch (for example), comment out  ``` branch = 'master' ``` and un comment ``` # branch = '1.0.0-rc3' ```
    (see lines 30 and 31 / 32 in the code)
    
I'm well aware I could have done this in a few lines of bash code. However, like I said... I was bored and wanted something to code.
Feel free to use it :)
