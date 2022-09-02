import subprocess
import os
import random
from colorama import Fore

"""
This script is used for updating Alice and/or starting alice with or without logging and/or in manual mode or permanently

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
"""

alicePath = '/home/pi/ProjectAlice' # Add the Path to Alice.

branch = 'master'
# branch = '1.0.0-rc3'
# branch = '1.0.0-rc4'

attemptCount = 0 # Don't adjust
attemptAllowance = 3 # Number of tries before the program gives up

# You can edit the below responces to suit your needs :)
failResponce = ["Incorrect option, Try again",
                "Incorrect responce, have you thought about getting glasses ? ",
                "Really ? Have you been drinking ?.... Try again",
                "Ahhhh, you just suffered from fat finger syndrome and hit the wrong key. Try again",
                "Re read the question and choose the correct answer",
                "Time you went to specsavers, try again",
                "I see the dslyexia has kicked in again. Let's try that again"
                ]

validResponces = ["y", "n", "m", "p", "s"] # List of the only acceptable responces

# get user responce to a question
def askAQuestion(question: str, requiredResponce: list, caller = None):
    responce = input(Fore.GREEN + question).lower() # get the users input

    if responce in requiredResponce: # if input is in valid responces, return the responce
        counter(value=0)
        return responce
    else: # If user selected an incorrect responce
        failedResponce(responce=responce, requiredResponce=requiredResponce, caller=caller)

def failedResponce(responce :str, requiredResponce :list, caller: str = None):
    """
    Checks if it's an incorrect input from the user and displays notification apropriately
    :param responce: What the user selected
    :param requiredResponce: The expected responces
    :param caller: What method called the Question
    :return:
    """
    if not responce in requiredResponce: # If required value is not in the list
        counterValue = counter()
        print(Fore.BLUE + f"Your on attempt number ->> {counterValue} of {attemptAllowance}\n ")

        if counterValue <= attemptAllowance:
            item = random.randint(0,len(failResponce) - 1) # Get a random item from the list as a responce to user not choosing correctly
            print(Fore.BLUE + failResponce[item])

            if "startAlice" in caller:
                startAlice()
            elif "addlogging" in caller:
                addlogging()
            elif "askToGitpull" in caller:
                askToGitpull()

        elif counterValue == attemptAllowance + 1:
            counter(value=0)
            print(Fore.RED + "I'm not playing your stupid games any more")


def counter(value :int = None):
    """
    Count the number of failed attempts
    :param value: Specifiy what value attemptCount should be, alternatively exclude that value for actual count
    :return:
    """

    global attemptCount
    if value:
        attemptCount = value
        return attemptCount
    else:
        if attemptCount == attemptAllowance + 1:
            attemptCount = 0
        else:
            attemptCount += 1
        return attemptCount

def askToGitpull():
    gitpullAnswer = askAQuestion(question='Do you want to do a Git pull ? (y/n)', requiredResponce=["y", "n"], caller="askToGitpull")

    if gitpullAnswer == 'y':
        gitpull()
    elif gitpullAnswer == 'n':
        print(Fore.LIGHTMAGENTA_EX + 'No worries, Skipping doing a git pull')
        startAlice()


def gitpull():
    """
    Perform a git pull through submodules to update Alice tolatest files
    :return:
    """
    os.chdir(alicePath)
    subprocess.run(['sudo', 'systemctl', 'stop', 'ProjectAlice'])
    subprocess.run(['rm', '-f', 'alice.bugreport'])
    subprocess.run(['git', 'stash'])
    #git pull --recurse-submodules
    os.chdir('core/webui/public')
    subprocess.run(['git', 'submodule', 'foreach', 'git', 'checkout', f'builds_{branch}'])
    subprocess.run(['git', 'submodule', 'foreach', 'git', 'pull'])
    os.chdir(alicePath)
    subprocess.run(['git', 'checkout', branch])
    subprocess.run(['git', 'pull'])
    startAlice()

def addlogging():
    """
    Check if user wants to add logging to Alice (used for auto bug reports on GitHub)
    :return:
    """
    print('.')
    addLogging = askAQuestion(' Do you want to add logging ? (y/n)', requiredResponce=["y", "n"], caller="addlogging")

    if addLogging == 'y':
        subprocess.run(['touch','~/ProjectAlice/alice.bugreport'])
    elif addLogging == 'n':
        print(Fore.CYAN + 'Ok, logging disabled')


def startAlice():
    """
    Checks if user wants to start alice in manual or permanent state. IE: run the service or run it manually
    :return:
    """
    print('.')
    startmethod = askAQuestion('Start Alice manually or permanently or skip ? ( m / p / s )', requiredResponce=["m", "p", "s"], caller="startAlice")

    if startmethod == 'm':
        addlogging()
        os.chdir(alicePath)
        subprocess.run(['./venv/bin/python3.7', 'main.py'] )
    elif startmethod == 'p':
        addlogging()
        os.chdir(alicePath)
        subprocess.run(['sudo', 'systemctl', 'restart', 'ProjectAlice'])
    elif startmethod == "s":
        print(Fore.RED + "I'm NOT going to start Alice... skipping")

askToGitpull()
