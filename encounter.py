import json

class Monster:
    def __init__(self,monstID,  monster, ac, hp, initiative):
        self.monstID = monstID
        self.monster = monster
        self.ac = ac
        self.hp = hp
        self.initiative = initiative

    def getMonster(self) -> None:
        #print(self.monstID)
        #print(self.monster)
        #print(self.ac)
        #print(self.hp)
        #print(self.initiative)
        print(self.monstID, self.monster, self.ac, self.hp, self.initiative)

def main():
   monsterAmount = int(input("Cuantos monstruos? "))
   monsterArray = []
   id = 0

   for i in range(monsterAmount):
       monsterName = input("Nombre del monstruo? ")
       typeAmount = int(input("Cuantos de " + monsterName + "? "))
       ac = input("Armor class? ")
       hp = input("HP? ")
       initiative = input("Initiative? ")
       for j in range(typeAmount):
           monsterArray.append(Monster(id, monsterName, ac, hp, initiative))
           id += 1

   print(len(monsterArray))
   for i in range(len(monsterArray)):
       monsterArray[i].getMonster()
if __name__ == "__main__":
    main()
