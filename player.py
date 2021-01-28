class Player:
    def __init__(self,hp,dmg):
        self.dmg = dmg
        self.hp = hp
        self.name = self.set_name()
        self.armour = 0
        self.inventory = []
        self.alive = True
    def die(self):
        if self.hp == 0:
            self.alive = False
    def set_name(self):
        name = input('Enter your Name please: ')
        return name
    def attack(self,target):
        #print('{target} is under Attack'.format(target))
        if target.armour >= self.dmg:
            print('All damage was prevented from Armour!')
        else:
            target.hp = target.hp - (self.dmg - target.armour) 
    def pickup_item(self,item):
        self.inventory.append(item)
        self.armour += item.armour_value
        self.dmg += item.dmg_value
    def drop_item(self,item):
        self.inventory.remove(item)
        self.armour -= item.armour_value
        self.dmg -= item.dmg_value

class Item:
    def __init__(self, name, dmg_value, armour_value):
        self.name = name
        self.dmg_value = dmg_value
        self.armour_value = armour_value

class Inventory:
    def __init__():
    content = []




me = Player(100,10)
enemy = Player(50,5)

sword = Item('sword',3,0)
leather_armour = Item('Leather Armour',0,2)
chainmail = Item('Chainmail',0,15)

noch zu designen
class Map/World:
class Room: