import random
import yaml
import sys

nameList = []
resourcesPath = "scripts/resources/"
firstNameYml = "firstNames.yml"
lastNameYml = "lastNames.yml"
race = 'human'

def randomName(ymalName, raceChoice):
    with open(resourcesPath + ymalName, 'r') as stream:
        nameList = yaml.safe_load(stream)[raceChoice]

    sys.stdout.write(nameList[random.randrange(len(nameList))-1]+" ")

def namePicker(choice):
    randomName(firstNameYml, race)
    if choice == "full" or choice == "full name":
        randomName(lastNameYml, race)

if __name__ == '__main__':
    print('full name or single')
    x = input()
    namePicker(x)
