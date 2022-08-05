import monster
import os
import time
import json
# Function to create the monsters

"""
@TODO

x make menu (create, start)

extract monsters from json file
save state of encounter (write to file)
import encounter (read from file)

"""
# Function to search if the monster exists in the json file.
def findMonster(name):
    i = 0
    with open("monsters.json", "r") as file:
        monsterData = json.load(file)
    try:
        while(monsterData[i]["name"] != name):
            i += 1
        return i
    except IndexError:
       print("Monster not found")
       return -1

def getMonsterInfo(name, stat, index):
    i = 0
    with open("monsters.json", "r") as file:
        monsterData = json.load(file)

    #while(monsterData[i]["name"] != name):
    #    i += 1
    return monsterData[index][stat]

def createEncounter():
    monsterAmount = int(input("How many monsters? "))
    monsterArray = []
    id = 0

    for _ in range(monsterAmount):
        monsterName = input("Monster name: ")
        index = findMonster(monsterName)

        while (index  == -1):
            monsterName = input("Monster name: ")
            index = findMonster(monsterName)

        typeAmount = int(input("How many " + monsterName + "'s? "))
        ac = getMonsterInfo(monsterName, "Armor Class", index)
        hp = getMonsterInfo(monsterName, "Hit Points", index)
        initiative = input("Initiative? ")

        for _ in range(typeAmount):
            monsterArray.append(monster.Monster(
                id + 1, monsterName, ac, hp, initiative))
            id += 1
    return monsterArray

def startEncounter(monsters):
    quickPrint(monsters)


def quickPrint(monsters):
    for i in range(len(monsters)):
        monsters[i].printMonster()

def main():
    answer = " "
    while(answer != "exit"):
        print("----------------------------")
        print("------- Menu Options -------")
        print("----------------------------")
        print("-   1.  Create Encounter   -")
        print("-   2.  Start  Encounter   -")
        print("----------------------------")
        print("----------------------------")
        print("----  Type exit to stop ----")
        print("----------------------------")

        answer = input("Menu option: ")
        if (answer == "1"):
            monsterArray = createEncounter()
            print("Encounter created!")
            time.sleep(1)
            os.system("clear")
        elif(answer == "2"):
            quickPrint(monsterArray)
        elif(answer == "exit"):
            print("BYE!")
            os.system("clear")


if __name__ == "__main__":
    main()
