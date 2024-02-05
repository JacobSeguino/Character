"""
This scrips goal is to roll levels for character to uses it
import levelPicker and call the function
levelPickerForRando() if you and want a random 1-20

or you can call 
levelPickerForEncounter(cr) and in cr add the 
Chalanage Rating (CR) of the party and it will give you
a random roll that is between two less or two more 
the the parties current CR.
"""

import random

failureMessage = 'that was not 1-20'

def requestMessage():
    print("What is the partie's CR? (Leave blank if you don't care about maching lvl for party)")
    x = input()
    crTester(x)

def levelPickerForEncounter(cr):
    if cr == 20 or cr == 19:
        max = 20
    else:
        max = cr+2
    min = cr-2
    level = random.randrange(int(min), int(max), 1)+1
    print("Level: " + str(level))

def levelPickerForRando():
    level = random.randrange(20)+1
    print("Level: " + str(level))

def crTester(cr):
    if cr == "" :
        levelPickerForRando()
        return
    
    try:
        int(cr)
    except ValueError:
        print (failureMessage)
        requestMessage()
        return

    n = int(cr)
    if n <= 1 or n >= 20:
        print(failureMessage)
        requestMessage()
        return

    levelPickerForEncounter(int(cr))
