
class item:
    def __init__(self, name, type, weight, value, dur, range, ammo, location, qty):
        self.name = name
        self.type = type
        self.weight = weight
        self.value = value
        self.dur = dur
        self.range = range
        self.ammo = ammo
        self.location = location
        self.qty = qty

    def stats(self):
        return "Name: {:<20}\
                Type: {:<10}\
                Weight: {:<3}\
                Value: {:<5}\
                Dur: {:<8}\
                Range: {:<3}\
                Ammo: {:<4}\
                Location : {:<4}\
                Qty : {:<4}".format(self.name, self.type, self.weight, self.value, self.dur, self.range, self.ammo, self.location, self.qty)


class weapon:
    def __init__(self, type, damage, weight, value, dur, range, ammo):
        self.type = type    # name of weapon
        self.damage = damage    # max damage of weapon
        self.weight = weight    # weight of weapon
        self.value = value  # how much to buy
        self.dur = dur  # durabilty of weapon - brakes at 0 dur
        self.range = range  # weapon range
        self.ammo = ammo

    def stats(self):
        return 'Type: {: <20} \
                Damage:  {: <3} \
                Weight: {: <3} \
                Value: {: <5} \
                Dur: {: <4} \
                Range: {: <3} \
                Ammo: {: <3}'.format(self.type, self.damage, self.weight, self.value, self.dur, self.range, self.ammo)


class armor:
    def __init__(self, type, protection, weight, value, dur, location):
        self.type = type    # name of armor
        self.protection = protection    # damage armor blocks
        self.weight = weight    # weight of armor
        self.value = value  # how much to buy
        self.dur = dur  # durabilty of armor - brakes at 0 dur
        self.location = location  # location on body

    def stats(self):
        return 'Type: {: <20} \
                Protect: {: <3} \
                Weight: {: <3} \
                Value: {: <9} \
                Dur: {: <4} \
                Location: {: <10}'.format(self.type, self.protection, self.weight, self.value, self.dur, self.location)


weapons = [weapon('None', 0, 0, 0, 0, 0, 'none'),
           weapon('Dagger', 1, 1, 1, 20, 0, 'none'),
           weapon('Short Sword', 2, 2, 2, 40, 0, 'none'),
           weapon('Sword', 3, 3, 3, 50, 0, 'none'),
           weapon('Long Sword', 4, 4, 4, 70, 1, 'none'),
           weapon('Great Sword', 5, 5, 5, 80, 1, 'none'),
           weapon('Enchanted Sword', 6, 2, 10, 140, 1, 'none'),
           weapon('Magic Spear', 2, 4, 4, 80, 10, 'infinty'),
           weapon('Battle Axe', 3, 3, 4, 50, 1, 'none'),
           weapon('Club', 2, 2, 3, 100, 1, 'none'),
           weapon('Bow', 2, 1, 2, 100, 10, 10),
           weapon('Long Bow', 3, 2, 4, 85, 15, 10),
           weapon('Short Bow', 2, 2, 2, 75, 5, 10),
           weapon('Cross Bow', 4, 3, 6, 100, 20, 10),
           weapon('Magic Trident', 5, 3, 5, 100, 10, 'infinity'),
           weapon('Enchanted Bow', 4, 2, 7, 150, 25, 20)]

# type, damage, weight, value, dur, range, ammo

armors = [armor('None', 0, 0, 0, 0, 'anything'),  # no armor
          armor('Leather Helmet', 1, 1, 1, 20, 'head'),
          armor('Leather Chestplate', 2, 2, 2, 30, 'chest'),
          armor('Leather Leggings', 1, 1, 1, 20, 'legs'),
          armor('Leather Boots', 1, 1, 1, 20, 'feet'),
          armor('Iron Helmet', 3, 3, 4, 40, 'head'),
          armor('Iron Chestplate', 6, 5, 6, 50, 'chest'),
          armor('Iron Leggings', 3, 3, 4, 40, 'legs'),
          armor('Iron Boots', 3, 3, 3, 40, 'feet'),
          armor('Chain Male Helmet', 2, 1, 3, 40, 'head'),
          armor('Chain Male Chestplate', 3, 2, 5, 50, 'chest'),
          armor('Chain Male Leggings', 2, 2, 3, 40, 'legs'),
          armor('Chain Male Boots', 2, 2, 2, 40, 'feet')]

#                               Weight  Value           Range           Location
#        Name           Type       Wgt  $    Dur         Rng      Ammmo   Loc   Qty
items = [
    item('None',        'none',     0,  0,  'none    ',   0,     'none', 'any',  1),
    item('Flash Light', 'Light',    1,  3,  'infinity',   1,     'none', 'arm',  1),
    item('TNT',         'Bomb',     1,  5,  'one-time',   '5x5', 'bomb', 'none', 1),
    item('Bread',       'Food',    .5,  1,  'one-time',   1,     'none', 'arm',  1),
    item('Carrot',      'Food',    .5,  1,  'one-time',   1,     'none', 'arm',  1),
    item('Arrows',      'Ammo',     2,  2,   20,          1,     'none', 'arm',  20),
    item('HP Potion',   'Potion',  .5,  6,  'one-time',   1,     'none', 'arm',  1)]
# self.type, self.protection, self.weight, self.value, self.dur, self.location


class chracter:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.inventory = []
        self.head = armors[1]  # armor on head
        self.chest = armors[0]  # armor on chest
        self.legs = armors[0]  # armor on legs
        self.feet = armors[0]  # armor on feet
        self.weapon = weapons[0]

    def protection(self):
        protection = 0.0
        if self.head != armors[0]:
            protection += self.head.protection

    def invetory_weight(self):
        inventory_weight = 0.0
        for item in self.inventory:
            inventory_weight += item.weight

        return inventory_weight

    def carried_weight(self):
        return 0.0


print('')
print("                                                                                       *** Weapon Types ***")


for w in weapons:
    print(w.stats())
print('')
print("                                                                                       *** Armor Types ***")
for a in armors:
    print(a.stats())
print('')
print("                                                                                       *** Item Types ***")
for i in items:
    print(i.stats())

player = chracter('simon')
player.inventory = [weapons[1], items[1], items[3]]
print(player.invetory_weight())
