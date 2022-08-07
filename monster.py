class Monster:
    def __init__(self,monstID,  monster, ac, hp, initiative):
        self.monstID = monstID
        self.monster = monster
        self.ac = ac
        self.hp = hp
        self.maxHP = hp
        self.initiative = initiative

    def printMonster(self):
        print("| {:<5}{:<20}{:<5}{:<3}/{:<8}{:<10}|".format(self.monstID, self.monster, self.ac[:2], self.hp, self.maxHP, self.initiative))

    def setMonsterHealth(self, damage):
        self.hp -= damage

    def getHP(self):
        return self.hp
