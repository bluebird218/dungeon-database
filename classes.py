from character import *

class Barbarian(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 12, "barbarian", False, 3)
    
class Bard(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 8, "bard", True, 3)

class Cleric(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 8, "cleric", True, 2)

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to level {self.level}!")
        self.max_health += randrange(1, self.hit_dice + 1) + self.ability_mods["CON"]
        print(f"{self.name} now has {self.max_health} HP!")
        if self.level == 2:
            self.new_subclass()
        if self.spellcaster:
            self.new_spell()
        if self.level == 4 or self.level == 8 or self.level == 12 or self.level == 16 or self.level == 19:
            self.new_feat()

class Druid(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 8, "druid", True, 2)

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to level {self.level}!")
        self.max_health += randrange(1, self.hit_dice + 1) + self.ability_mods["CON"]
        print(f"{self.name} now has {self.max_health} HP!")
        if self.level == 2:
            self.new_subclass()
        if self.spellcaster:
            self.new_spell()
        if self.level == 4 or self.level == 8 or self.level == 12 or self.level == 16 or self.level == 19:
            self.new_feat()
    
class Fighter(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 10, "fighter", False, 3)

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to level {self.level}!")
        self.max_health += randrange(1, self.hit_dice + 1) + self.ability_mods["CON"]
        print(f"{self.name} now has {self.max_health} HP!")
        if self.spellcaster:
            self.new_spell()
        if self.level == 4 or self.level == 6 or self.level == 8 or self.level == 12 or self.level == 14 or self.level == 16 or self.level == 19:
            self.new_feat()

class Monk(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 8, "monk", False, 3)    
    
class Paladin(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 10, "paladin", True, 3)
    
class Ranger(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 10, "ranger", True, 3)
    
class Rogue(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 6, "rogue", False, 3)
    
    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to level {self.level}!")
        self.max_health += randrange(1, self.hit_dice + 1) + self.ability_mods["CON"]
        print(f"{self.name} now has {self.max_health} HP!")
        if self.spellcaster:
            self.new_spell()
        if self.level == 4 or self.level == 8 or self.level == 10 or self.level == 12 or self.level == 16 or self.level == 19:
            self.new_feat()

class Sorcerer(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 6, "sorcerer", True)
        self.new_subclass()

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to level {self.level}!")
        self.max_health += randrange(1, self.hit_dice + 1) + self.ability_mods["CON"]
        print(f"{self.name} now has {self.max_health} HP!")
        if self.spellcaster:
            self.new_spell()
        if self.level == 4 or self.level == 8 or self.level == 12 or self.level == 16 or self.level == 19:
            self.new_feat()

class Warlock(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 8, "warlock", True)
        self.new_subclass()

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to level {self.level}!")
        self.max_health += randrange(1, self.hit_dice + 1) + self.ability_mods["CON"]
        print(f"{self.name} now has {self.max_health} HP!")
        if self.spellcaster:
            self.new_spell()
        if self.level == 4 or self.level == 8 or self.level == 12 or self.level == 16 or self.level == 19:
            self.new_feat()

class Wizard(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 6, "wizard", True, 2)

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to level {self.level}!")
        self.max_health += randrange(1, self.hit_dice + 1) + self.ability_mods["CON"]
        print(f"{self.name} now has {self.max_health} HP!")
        if self.level == 2:
            self.new_subclass()
        if self.spellcaster:
            self.new_spell()
        if self.level == 4 or self.level == 8 or self.level == 12 or self.level == 16 or self.level == 19:
            self.new_feat()