from character import *

class Barbarian(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 12, "barbarian", False)
    
class Bard(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 8, "bard", True)

class Cleric(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 8, "cleric", True)

class Druid(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 8, "druid", True)
    
class Fighter(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 10, "fighter", False)

class Monk(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 8, "monk", False)    
    
class Paladin(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 10, "paladin", True)
    
class Ranger(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 10, "ranger", True)
    
class Rogue(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 6, "rogue", False)

class Sorcerer(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 6, "sorcerer", True)

class Warlock(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 8, "warlock", True)

class Wizard(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 6, "wizard", True)