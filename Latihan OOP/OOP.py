class Hero:
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.health = inputHealth
        self.name = inputName
        self.power = inputPower
        self.armor = inputArmor

hero1= Hero ("Sniper",100,50,30)

print (hero1.__sizeof__)
