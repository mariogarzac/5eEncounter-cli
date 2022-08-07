import monster
import os
import time
import json
import string
# Function to create the monsters

"""
@TODO

update correct enemy after others get deleted
save state of encounter (write to file)
import encounter (read from file)

"""
# Searches monster json file for the monster name. Will return index
# if found. If it does not exist, it will return -1.
def findMonster(name):
    i = 0
    with open("monsters.json", "r") as file:
        monsterData = json.load(file)
    try:
        while(monsterData[i]["name"].lower() != name.lower()):
            i += 1
        return i
    except IndexError:
       print("Monster not found")
       return -1

# returns specific stat for a monster
def getMonsterInfo(name, stat, index):
    with open("monsters.json", "r") as file:
        monsterData = json.load(file)

    return monsterData[index][stat]

def getHP(hp):
    return int(hp.split()[0])

# Creates an encounter by asking for amount of monsters
# and how many of each.
def createEncounter():
    monsterAmount = int(input("How many monsters? "))
    monsterArray = []
    id = 0

    # for loops to populate monster array.
    for _ in range(monsterAmount):
        monsterName = input("Monster name: ")
        name = ' '.join(word[0].upper() + word[1:] for word in monsterName.split())

        index = findMonster(monsterName)

        # while loop to validate monster.
        while (index  == -1):
            monsterName = input("Monster name: ")
            index = findMonster(monsterName)
            name = ' '.join(word[0].upper() + word[1:] for word in monsterName.split())

        typeAmount = int(input("How many " + name + "'s? "))
        ac = getMonsterInfo(monsterName, "Armor Class", index)
        hp = getMonsterInfo(monsterName, "Hit Points", index)
        initiative = input("Initiative? ")

        for _ in range(typeAmount):
            monsterArray.append(monster.Monster(
                id + 1, monsterName, ac, getHP(hp), initiative))
            id += 1
    return monsterArray

# Starts the encounter and finishes once the list is equal to 0.
def startEncounter(monsters):
    os.system("clear")
    quickPrint(monsters)
    dead = 0
    attackedMonster = 0

    while(dead != len(monsters) or attackedMonster != "exit"):
        try:
        attackedMonster = int(input("ID of monster getting attacked: ")) - 1

        # While loops to validate number is not greater than array size
        # and to avoid killing enemy more than once.
        while(attackedMonster >= len(monsters)):
            attackedMonster = int(input("ID of monster getting attacked: ")) - 1

        while(monsters[attackedMonster].getHP() <= 0):
            print("That enemy is dead\n")
            attackedMonster = int(input("ID of monster getting attacked: ")) - 1

        damage = int(input("Amount of damage taken: "))
        monsters[attackedMonster].setMonsterHealth(damage)

        if (monsters[attackedMonster].getHP() <= 0):
            dead += 1
        os.system("clear")
        quickPrint(monsters)

        except ValueError:
            print("Please type the appropiate value\n")

    print("Encounter Finished! ")
    time.sleep(0.5)
    os.system("clear")


def quickPrint(monsters):
    print("+-----------------------------------------------------+")
    print("| {:<5}{:<20}{:<5}{:<10}{:<10}  |".format("ID","Monster","AC","HP","Initiative"))
    print("+-----------------------------------------------------+")

    for i in range(len(monsters)):
        monsters[i].printMonster()

    print("+-----------------------------------------------------+")
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
            time.sleep(0.5)
            os.system("clear")
        elif(answer == "2"):
            startEncounter(monsterArray)
        elif(answer == "exit"):
            print("BYE!")
            os.system("clear")


if __name__ == "__main__":
    main()
