from classes import *

all_characters = []
chr1 = Bard("Vatti", 3)
chr2 = Druid("Mike", 5)
all_characters.append(chr1)
all_characters.append(chr2)


def create_character():
    name = input("Enter a name for your character: ")
    level = int(input("Enter a level for your character: "))
    type = input("Enter a class for your character: ").lower()
    if type == "barbarian":
        chr = Barbarian(name, level)
    elif type == "bard":
        chr = Bard(name, level)
    elif type == "cleric":
        chr = Cleric(name, level)
    elif type == "druid":
        chr = Druid(name, level)
    elif type == "fighter":
        chr = Fighter(name, level)
    elif type == "monk":
        chr = Monk(name, level)
    elif type == "paladin":
        chr = Paladin(name, level)
    elif type == "ranger":
        chr = Ranger(name, level)
    elif type == "rogue":
        chr = Rogue(name, level)
    elif type == "sorcerer":
        chr = Sorcerer(name, level)
    elif type == "warlock":
        chr = Warlock(name, level)
    elif type == "wizard":
        chr = Wizard(name, level)
    else:
        print("I'm sorry, that type is not supported.")
        return
    print(chr)
    return chr


def user_prompt():
    while(True):
        response = input("Hello user! Would you like to 'Create', 'Level Up', or 'Exit'? ").lower()
        if response == "create":
            all_characters.append(create_character())
        elif response == "level up":
            print("Available characters:")
            for character in all_characters:
                print(character)
            char = input("Which character would you like to level up? ").lower()
            for character in all_characters:
                if character.name.lower() == char:
                    character.level_up()
        elif response == "exit":
            break
        else:
            print("I'm sorry, I didn't recognize that response.")

user_prompt()