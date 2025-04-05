class Character:
    def __init__(self, name, level, archetype):
        self.name = name
        self.level = level
        self.archetype = archetype

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to level {self.level}!")

    def __str__(self):
        return f"{self.name} is a level {self.level} {self.archetype}"