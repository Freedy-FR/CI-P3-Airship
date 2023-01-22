from os import system, name
from time import sleep

# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Code taken from stack overflow
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
                sleep(0.5)
                print("We are going to need your name for this adventure captain!")
                name = input("Please tell me your name captain?\n")
                clear()
            elif len(name) > 6:
                sleep(0.5)
                print("Name is too big captain!")
                name = input("Please insert a name between 1 and 6 letters\n")
                clear()
            else:
                clear()
                print("That is a fair name captain!")
                sleep(2)
                clear()
                return name.capitalize()


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

        print(f" {player_name} Welcome to Airship battles!\n")
        sleep(5)
        clear()

class SetBoard:
    """
    Create a board instance and print to the console if called
    """

    def __init__(self, board, size, username):
        self.board = board
        self.username = username
        self.size = size
    
    def print_to_console(self):
        #Create an username title to the board
        #Center the username
        print("---{:^10}--- ".format(self.username))
        # print(f"  -- {self.username} --")

        #Create the heading based on the size given
        heading = []
        separator = []
        for i in range(self.size):
            heading.append(f"{i}")
            separator.append(f"|")
        print("  " + " ".join(heading))
        print("  " + " ".join(separator))


        #Create an instance of the board
        row_number = 0
        for row in self.board:
            # print("%d|%s|" % (row_number, "|".join(row)))
            print("{}|{}|".format(row_number, "|".join(row)))
            row_number += 1
        print()


def RunGame():

    username = UsernameInput.input_name()
    Welcome.welcome_screen(username)

    size = 8

    player_guess_board = SetBoard([[" "] * size for i in range(size)], size, username)

    SetBoard.print_to_console(player_guess_board)

    computer_hid_board = SetBoard([[" "] * size for i in range(size)], size, "Enemy Hidden")
    computer_guess_board = SetBoard([[" "] * size for i in range(size)], size, "Enemy")

    SetBoard.print_to_console(computer_guess_board)

    #Print to visualize in test
    SetBoard.print_to_console(computer_hid_board)

RunGame()
