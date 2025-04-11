from random import randrange

class Character:
    def __init__(self, name, level, hit_dice, title, spellcaster, subclass_level):
        self.name = name
        self.level = level
        self.feats = []
        self.spells = []
        self.hit_dice = hit_dice
        self.title = title
        self.subclass = None
        self.spellcaster =  spellcaster
        self.attributes = {}
        manual = input("Would you like to assign ability scores manually? Y/N: ").lower()
        if manual == "n":
            stats_to_assign = []
            for i in range(6):
                stat_dice = []
                for j in range(4):
                    stat_dice.append(randrange(1, 7))
                stat_dice.remove(min(stat_dice))
                stats_to_assign.append(sum(stat_dice))
            print(f"Attribute scores to assign: {stats_to_assign}")
            assign_automatically = input("Would you like these to be assigned automatically? Y/N: ").lower()
            if assign_automatically == "y":
                self.attributes["STR"] = stats_to_assign[0]
                self.attributes["DEX"] = stats_to_assign[1]
                self.attributes["CON"] = stats_to_assign[2]
                self.attributes["WIS"] = stats_to_assign[3]
                self.attributes["INT"] = stats_to_assign[4]
                self.attributes["CHA"] = stats_to_assign[5]
            else:
                self.attributes["STR"] = int(input("Set strength: "))
                self.attributes["DEX"] = int(input("Set dexterity: "))
                self.attributes["CON"] = int(input("Set constitution: "))
                self.attributes["WIS"] = int(input("Set wisdom: "))
                self.attributes["INT"] = int(input("Set intelligence: "))
                self.attributes["CHA"] = int(input("Set charisma: "))
        else:
            self.attributes["STR"] = int(input("Set strength: "))
            self.attributes["DEX"] = int(input("Set dexterity: "))
            self.attributes["CON"] = int(input("Set constitution: "))
            self.attributes["WIS"] = int(input("Set wisdom: "))
            self.attributes["INT"] = int(input("Set intelligence: "))
            self.attributes["CHA"] = int(input("Set charisma: "))
        self.generate_ability_mods()
        self.max_health = hit_dice + self.ability_mods["CON"]
        for i in range(1, self.level):
            self.max_health += randrange(1, self.hit_dice + 1) + self.ability_mods["CON"]
        if self.level >= subclass_level:
            self.new_subclass()
        if self.level >= 4:
            self.new_feat()
        if self.spellcaster:
            for i in range(self.level):
                self.new_spell()


    def generate_ability_mods(self):
        self.ability_mods = {}
        self.ability_mods["STR"] = (self.attributes["STR"] - 10) // 2
        self.ability_mods["DEX"] = (self.attributes["DEX"] - 10) // 2
        self.ability_mods["CON"] = (self.attributes["CON"] - 10) // 2
        self.ability_mods["WIS"] = (self.attributes["WIS"] - 10) // 2
        self.ability_mods["INT"] = (self.attributes["INT"] - 10) // 2
        self.ability_mods["CHA"] = (self.attributes["CHA"] - 10) // 2

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to level {self.level}!")
        self.max_health += randrange(1, self.hit_dice + 1) + self.ability_mods["CON"]
        print(f"{self.name} now has {self.max_health} HP!")
        if self.level == 3:
            self.new_subclass()
        if self.spellcaster:
            self.new_spell()
        if self.level == 4 or self.level == 8 or self.level == 12 or self.level == 16 or self.level == 19:
            self.new_feat()
        
    def new_spell(self):
        spell = input("You get a new spell! Which would you like? ")
        self.spells.append(spell)
        print(f"{spell} has been added to {self.name}'s spell list!")

    def new_feat(self):
        feat = input("You get a new feat! Which would you like? ")
        self.feats.append(feat)
        print(f"{feat} has been added to {self.name}'s feat list!")

    def new_subclass(self):
        self.subclass = input(f"Please choose a {self.title} subclass: ")
        print(f"{self.name} is now a {self.title} of the {self.subclass} subclass!")

    def get_feats(self):
        print(f"Feats for {self.name}:")
        for feat in self.feats:
            print(feat)

    def get_spells(self):
        if self.spellcaster:
            print(f"Spells for {self.name}:")
            for spell in self.spells:
                print(spell)

    def __str__(self):
        if self.subclass != None:
            return f"{self.name} is a level {self.level} {self.subclass} {self.title} with {self.max_health} total hit points."
        return f"{self.name} is a level {self.level} {self.title} with {self.max_health} total hit points."