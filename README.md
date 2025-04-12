This project was created by bluebird 218

Hello, and welcome to my first personal project! For this project, I wanted to do my best to recreate the act of creating a Dungeons and Dragons character (specifically for 5th Edition) to the best of my ability. 
To do so, I created one main 'Character' class and a bunch of other classes for each type of character (fighter, wizard, etc.) that would inherit whatever they needed from the main Character class.

I've made use of the input() function so that when the main.py file is run, a user prompt runs in the command line that guides the user through what is possible. Those functions are:
-Creating a character
-Checking created characters (You can look at feats, spells, and also level up)
-Printing to a text file for storage
-Reading from a text file (I wanted to implement a way to import them directly into the system to allow those characters to them be modified, but the way I made __init__ for the Character class with input() would probably make this a pain)
-Exiting from the command line

Running the file should be pretty simple, just make sure you have the character.py, classes.py, and main.py file in the same folder.
