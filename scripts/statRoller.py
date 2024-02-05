"""
Stat roller still still needs tweaking for tweaking out put
but in good state for basic use.

for use call statGetter()
"""

import random

def statRoller():
    temp = []
    stat = 0
    for i in range(4):
        temp.append(random.randrange(6)+1)
    temp.sort(reverse=True)
    temp.pop()
    for i in temp:
        stat += i
    return int(stat)

def statGetter():
    strength = statRoller()
    dexterity = statRoller()
    constitution = statRoller()
    intelligence = statRoller()
    wisdom = statRoller()
    charisma = statRoller()
    print("Str: " + str(strength))
    print("Dex: " + str(dexterity))
    print("Con: " + str(constitution))
    print("Int: " + str(intelligence))
    print("Wis: " + str(wisdom))
    print("Cha : " + str(charisma))
    attributes = {'Strength' : {'stat': strength, 'mod' : modFinder(strength)},
                  'Dexterity' : {'stat': dexterity, 'mod' : modFinder(dexterity)},
                  'Constitution' : {'stat': constitution, 'mod' : modFinder(constitution)},
                  'Intelligence' : {'stat': intelligence, 'mod' : modFinder(intelligence)},
                  'Wisdom' : {'stat': wisdom, 'mod' : modFinder(wisdom)},
                  'Charisma' : {'stat': charisma, 'mod' : modFinder(charisma)} }
    print(attributes)

def modFinder(stat):
    return (stat - 10)//2
