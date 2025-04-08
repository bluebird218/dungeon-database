from classes import *

all_characters = []
chr1 = Bard("Vatti", 2)
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
        print("I'm sorry, that class is not currently supported.")
        return
    print(chr)
    return chr


def user_prompt():
    while(True):
        response = input("Hello user! Would you like to 'Create', 'Check', or 'Exit'? ").lower()
        if response == "create":
            all_characters.append(create_character())
        elif response == "check":
            print("Available characters: ")
            for i in range(0, len(all_characters)):
                print(f"{i}: {all_characters[i]}")
            choice = int(input("Which character would you like to check? (Please select using index): "))
            try:
                character = all_characters[choice] 
                choice = input(f"Would you like to 'check spells', 'check feats', or 'level up' for {character.name}? ").lower()
                if choice == "check spells":
                    character.check_spells()
                elif choice == "check feats":
                    character.check_feats()
                elif choice == "level up":
                    character.level_up()
            except:
                print("I'm sorry, something went wrong")
        elif response == "exit":
            break
        else:
            print("I'm sorry, I didn't recognize that response.")

user_prompt()