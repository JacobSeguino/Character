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

if __name__ == '__main__':
    requestMessage()