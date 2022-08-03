import monster
#Function to create the monsters


def createMonsters():
   monsterAmount = int(input("Cuantos monstruos? "))
   monsterArray = []
   id = 0

   for i in range(monsterAmount):
      typeAmount = 10
      monsterName = "Sahugai"
      ac = 12
      hp = 22
      initiative = 13
      for j in range(typeAmount):
         monsterArray.append(monster.Monster(
             id, monsterName, ac, hp, initiative))
         id += 1
   return monsterArray


def main():
   monsterArray = createMonsters()

   for i in range(len(monsterArray)):
         monsterArray[i].printMonster()

if __name__ == "__main__":
    main()
