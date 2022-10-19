import uuid
import App.Utilities.dice as Dices
import App.utilities.distances as Distances


# A super class for items
class Item:
    def __init__(self, name:str) -> None:
        self.name = name

# A class for stackable items (ie. torches)
class Stackable(Item):
    def __init__(self, name: str, quantity: int = 1) -> None:
        self.name = name
        self.quantity = quantity
        super().__init__(self.name)
        #TODO Add something to merge similar items on item creation

#TODO Add class for measurable items (ie. ropes)
#TODO Add class for ammunition (ie. arrows)

# Add class for unique items (ie.weapons)
class Unique(Item):
    def __init__(self, name: str) -> None:
        self.name = name
        self.uuid = uuid.uuid4()
        super().__init__(self.name)

# Adds a class for weapons (ranged and melee)
class Weapon(Unique):
    def __init__(self, name: str, damage: Dices.Dice) -> None:
        self.name = name
        self.damage = damage
        super().__init__(name)
        self.uuid = self.uuid
        #TODO Add a system to incorporate damage type (ie. piercing)
        
# Adds a class for melee weapons()
class Melee(Weapon):
    def __init__(self, name: str, damage: Dices.Dice) -> None:
        self.name = name
        self.damage = damage
        super().__init__(self.name, self.damage)
        self.uuid = self.uuid

#Add a class for ranged weapons
class Range(Weapon):
    def __init__(self, name: str, damage: Dices.Dice, n_distance: Distances.Distance, l_distance: Distances.Distance) -> None:
        self.name = name
        self.damage = damage
        super().__init__(name, damage)
        self.uuid = self.uuid
        assert n_distance <= l_distance, "The normal range distance must shoreter then the long distance"
        self.n_distance = n_distance
        self.l_distance = l_distance
        #TODO Add a system to use ammunition