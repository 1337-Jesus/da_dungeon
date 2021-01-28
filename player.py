class Player:
    def __init__(self,hp,dmg):
        self.dmg = dmg
        self.hp = hp
        self.name = self.set_name()
        self.armour = 0
        self.inventory = Inventory()
        self.alive = True
        self.off_hand = False
        self.def_hand = False
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


class Item:
    def __init__(self, name, typus, dmg_value, armour_value): 
        self.name = name
        self.typus = typus                      #typus can be either: "off" or "def"
        self.dmg_value = dmg_value
        self.armour_value = armour_value
        self.equipped_status = False
    def equip(self,bearer):
        if self.typus == "off":
            if bearer.off_hand == False:
                bearer.off_hand = True                
                bearer.dmg += self.dmg_value
                self.equipped_status = True
           elif bearer.off_hand == True:
                print('You are carring a Weapon already, please unequip first')
        elif self.typus == 'def':
            if bearer.def_hand == False:
                bearer.def_hand = True
                self.equipped_status = True
                bearer.armour += self.armour_value
            elif bearer.def_hand == True:
                print('You are carring a Shield already, please unequip first')
    def unequip(self,bearer):
        if  self.typus == off:
            if bearer.off_hand == True:
                bearer.off_hand = False
                self.equipped_status = False
                bearer.dmg -= self.dmg_value
            elif bearer.off_hand == False:
                print('Nothing to unequip!')
        elif self.typus == 'def':
            if bearer.def_hand == True:
                bearer.def_hand == False
                self.equipped_status = False
                bearer.armour -= self.armour_value
            elif bearer.def_hand == False:
                print('Nothing defensive to unequip!')
    def give_bonus
        

class Inventory:
    def __init__(self):
        self.content = []
        self.max_items = 5
    """
    def pickup_item(self,item):
        self.content.append(item)
        self.armour += item.armour_value
        self.dmg += item.dmg_value
    def drop_item(self,item):
        self.content.remove(item)
        self.armour -= item.armour_value
        self.dmg -= item.dmg_value
"""



me = Player(100,10)
enemy = Player(50,5)

sword = Item('sword','off',3,0)
leather_armour = Item('Leather Armour', 'def',0,2)
chainmail = Item('Chainmail','def',0,15)
todo
function setz euip_status nicht korrekt
self.equipped_status = True
noch zu designen
class Map/World:
class Room: