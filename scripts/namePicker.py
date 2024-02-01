import random
import yaml

nameList = []
resourcesPath = "scripts/resources/"

def randomName(ymalName):
    with open(resourcesPath + ymalName, 'r') as stream:
        nameList = yaml.safe_load(stream)['human']

    print(nameList[random.randrange(len(nameList))-1])

if __name__ == '__main__':
    randomName("firstNames.yml")
