from os import system, name
from time import sleep

def clear():
    """
    Clear the console screen
    """
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class UsernameInput:
    """
    Ask for username input and validate name
    """
    def input_name():
        name = input("Please tell me your name captain?\n")        
        while True:
            if len(name) == 0:
                print("We are going to need your name for this adventure captain!")
                name = input("Please tell me your name captain?\n")                
            else:
                return name


class Welcome: 
    def welcome_screen(player_name):
        """
        Show welcome screen and message to the user
        """
        print('''                      . ___
                    __,' __`.                _..----....____
        __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
  _..-''-------'   `'   `'   `'     O ``-''._   ,;') _,'
,'________________                          \`-._`-','
 `._              ```````````------...___   '-.._'-:
    ```--.._      ,.                     ````--...__\-.
            `.--. `-`                       ____    |  |`
              `. `.                       ,'`````.  ;  ;`
                `._`.        __________   `.      \'__/`
                   `-:._____/______/___/____`.     \  `
                               |       `._    `.    /
                               `._________`-.   `.   `.___
                                                  `------ ''')

        print(f" {player_name} Welcome to Airship battles!")


def RunGame():

    username = UsernameInput.input_name()    
    Welcome.welcome_screen(username)

RunGame()


# Write your code to expect a terminal of 80 characters wide and 24 rows high