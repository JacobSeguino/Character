"""
This scrip can pick the class for your npc, it is currently using info from
scripts/resources/classList.yml If you would like to add more class choices
feel free to update that yml list or have it pick from a different yaml.
"""
import random
import yaml

resourcesPath = "scripts/resources/"
classListYml = "classList.yml"


def classPicker(role):
    with open(resourcesPath + classListYml, 'r') as stream:
        nameList = yaml.safe_load(stream)["class"][role].keys()

    print(list(nameList)[random.randrange(len(nameList))-1]+" ")


def classDecider():
    role = "npc"
    if random.randrange(4) == 3:
        role = "pc"
    classPicker(role)
