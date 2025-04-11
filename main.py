from classes import *

all_characters = []

def main():
    user_prompt()


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

def print_to_file():
    file_name = input("What would you like your file to be called? No spaces and without the .txt, please: ")
    f = open(f"{file_name}.txt", "w")
    for char in all_characters:
        f.write(str(char))
        f.write("\n")
        f.write(f"Ability Scores: {str(char.attributes)}")
        f.write("\n")
        f.write(f"Feats: {str(char.feats)}")
        f.write("\n")
        f.write(f"Spells: {str(char.spells)}")
        f.write("\n")
    f.close()


def user_prompt():
    while(True):
        response = input("Hello user! Would you like to 'Create', 'Check', 'Print', or 'Exit'? ").lower()
        if response == "create":
            all_characters.append(create_character())
        elif response == "check":
            print("Available characters: ")
            for i in range(0, len(all_characters)):
                print(f"{i}: {all_characters[i]}")
            choice = int(input("Which character would you like to check? (Please select using index): "))
            try:
                character = all_characters[choice] 
                choice = input(f"Would you like to check 'spells', check 'feats', or 'level up' for {character.name}? ").lower()
                if choice == "spells":
                    character.get_spells()
                elif choice == "feats":
                    character.get_feats()
                elif choice == "level up":
                    character.level_up()
            except:
                print("I'm sorry, something went wrong")
        elif response == "print":
            print_to_file()
        elif response == "exit":
            break
        else:
            print("I'm sorry, I didn't recognize that response.")

main()