import json

class Monster:
    def __init__(self,monstID,  monster, ac, hp, initiative):
        self.monstID = monstID
        self.monster = monster
        self.ac = ac
        self.hp = hp
        self.initiative = initiative

    def printMonster(self):
       print(self.monstID, self.monster, self.ac, self.hp, self.initiative)

