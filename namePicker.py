import random
import yaml

nameList = []

with open("firstNames.yml", 'r') as stream:
    nameList = yaml.safe_load(stream)['human']
    
print(nameList[random.randrange(len(nameList))-1])
