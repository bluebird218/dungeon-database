class Character:
    def __init__(self, name, level, hit_dice, title, spellcaster):
        self.name = name
        self.level = level
        self.feats = []
        self.spells = []
        self.hit_dice = hit_dice
        self.max_health = self.level * hit_dice
        self.title = title
        self.spellcaster =  spellcaster

    def level_up(self):
        self.level += 1
        self.max_health += self.hit_dice
        if self.spellcaster:
            self.new_spells()
        print(f"{self.name} has leveled up to level {self.level}!")
        
    def new_spells(self):
        pass

    def __str__(self):
        return f"{self.name} is a level {self.level} {self.title} with {self.max_health} total hit points."