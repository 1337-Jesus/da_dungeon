class World:
    def __init__(self,room_count):
        self.rooms = []
        for room in range(room_count):
            self.rooms.append(self.create_room(room,2))
        for room in self.rooms:
            while room.name > 0 and room.name < len(self.rooms):
                room.neighbor_a = self.rooms[room.name - 1]
                room.neighbor_b = self.rooms[room.name + 1]
    def create_room(self,name,door_count):
        room = Room(name,door_count)  
        return room 

class Room:
    def __init__(self,name,door_count):
        self.name = name
        self.neighboor_a = 0
        self.neighboor_b = 0
        self.doors = []
        for door in range(door_count):
            self.doors.append(self.create_door(self.name, self.neighboor_b))
    def create_door(self,room_1,room_2,):
        return Door(room_1,room_2)

class Door:
    def __init__(self,room_a,room_b):
        self.connects = [room_a,room_b]



print(a.rooms[3].neighbor_b.name)

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
        self.position
    def __del__(self):
        if self.hp <= 0:
            self.alive = False
            print('{} is Dead!'.format(self.name))           
    def set_name(self):
        name = input('Enter your Name please: ')
        return name
    def attack(self,target):
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
        self.is_in_inventory = False
        self.position =
    def equip(self,bearer):
       if self.is_in_inventory == True:
            if self.typus == "off":
                if bearer.off_hand == False:
                    bearer.off_hand = True                
                    bearer.dmg += self.dmg_value
                    self.equipped_status = True
                elif bearer.off_hand == True:
                    print('You are carring a Weapon already, please unequip first')
            if self.typus == 'def':
                if bearer.def_hand == False:
                    bearer.def_hand = True
                    bearer.armour += self.armour_value
                    self.equipped_status = True
                elif bearer.def_hand == True:
                    print('You are carring a Shield already, please unequip first')
    def unequip(self,bearer):
        if self.is_in_inventory == True:
            if  self.typus == 'off':
                if bearer.off_hand == True:
                    bearer.off_hand = False
                    self.equipped_status = False
                    bearer.dmg -= self.dmg_value
                elif bearer.off_hand == False:
                    print('Nothing to unequip!')
            if  self.typus == 'def':
                if bearer.def_hand == True:
                    bearer.def_hand = False
                    self.equipped_status = False
                    bearer.armour -= self.armour_value
                elif bearer.def_hand == False:
                    print('Nothing defensive to unequip!')

        

class Inventory:
    def __init__(self):
        self.content = []
        self.max_items = 5
    def pickup_item(self,item):
        self.content.append(item)
        item.is_in_inventory = True
    def drop_item(self,item):
        self.content.remove(item)
        item.is_in_inventory = True
    def list_invetory(self):
        for i in self.content:
            print(i.name)




me = Player(100,10)

enemy = Player(50,5)

sword = Item('sword','off',3,0)
leather_armour = Item('Leather Armour', 'def',0,2)
chainmail = Item('Chainmail','def',0,15)



#todo
#make neighbors work
#playerposition
#gameloop
