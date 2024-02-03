import random
import yaml

resourcesPath = "scripts/resources/"
classListYml = "classList.yml"

def classPicker():
    with open(resourcesPath + classListYml, 'r') as stream:
        nameList = yaml.safe_load(stream)["class"].keys()
    
    print(list(nameList)[random.randrange(len(nameList))-1]+" ")
   

if __name__ == '__main__':
    classPicker()