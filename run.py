from os import system, name
from time import sleep
import random

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
                sleep(0.5)
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
        sleep(1)
        clear()

class TableSizeInput:
    """
    """
    def table_size():        
        print("Please choose your battlefield grid size!")
        print("4 x 4 Grid insert 4")
        print("6 x 6 Grid insert 6")
        print("8 x 8 Grid insert 8")
        size = input("Please insert your grid size!\n")
        clear()
        while True:
            if len(size) == 0:
                sleep(0.5)
                print("We are going to need your prefered battlefield grid!")
                print("4 x 4 Grid insert 4")
                print("6 x 6 Grid insert 6")
                print("8 x 8 Grid insert 8")
                size = input("Please insert your grid size!\n")
                clear()
            elif (size != "4" and size != "6" and size != "8"):
                sleep(0.5)
                print("That is a invalid grid size!")
                print("4 x 4 Grid insert 4")
                print("6 x 6 Grid insert 6")
                print("8 x 8 Grid insert 8")
                size = input("Please insert your grid size!\n")
                clear()
            elif (size == "4" or size == "6" or size == "8"):
                clear()
                print("That is a fair grid size captain!")
                sleep(2)
                clear()
                return int(size)
        


class SetBoard:
    """
    Create a board instance and print to the console if called
    """

    def __init__(self, board, size, username):
        self.board = board
        self.username = username
        self.size = size
    
    def print_to_console(self):

        #Create an username title to the board and center username
        print("---{:^10}--- ".format(self.username))

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

class SetAirship:
    def __init__(self, board, size):
        self.board = board
        self.size = size
        

    def create_airships(self):
        for i in range((self.size - 1)):
            self.x_row, self.y_column = random.randint(0, (self.size - 1)), random.randint(0, (self.size - 1))
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, (self.size - 1)), random.randint(0, (self.size - 1))
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def user_atk_input(self, size):

        try:   
            x_row = input("Enter the Enemy row number to attack: ")
            while int(x_row) not in range(0, (size)):
                print('Not a valid row Captain!')
                x_row = input("Enter the Enemy row number to attack: ")

            y_column = input("Enter the Enemy column number to attack: ")
            while int(y_column) not in range(0, (size)):
                print('Not a valid column Captain!')
                y_column = input("Enter the Enemy column number to attack: ")
            return int(x_row), int(y_column)
        except ValueError or KeyError or AttributeError:
            print("Invalid data, restarting the game...")
            sleep(3)
            clear()
            RunGame()

def RunGame():

    # get username input
    username = UsernameInput.input_name()
    
    # display  welcomescreen
    Welcome.welcome_screen(username)
    
    # get table grid size
    size = TableSizeInput.table_size()
    
    # set player guess board
    player_guess_board = SetBoard([[" "] * size for i in range(size)], size, username)

    # set enemy hidden board
    computer_hid_board = SetBoard([[" "] * size for i in range(size)], size, "Enemy Hidden")
    # set computer guess board
    computer_guess_board = SetBoard([[" "] * size for i in range(size)], size, "Enemy")

    # Set enemy ships at random
    SetAirship.create_airships(computer_hid_board)

    # Set player ships a random
    SetAirship.create_airships(player_guess_board)
    
    turns_left = 10
    while turns_left > 0:

        # Print enemy hidden board with ships
        SetBoard.print_to_console(computer_hid_board)

        # print computer guess_board
        SetBoard.print_to_console(computer_guess_board)

        # print player guess board
        SetBoard.print_to_console(player_guess_board)
        print(f"Turns left = {turns_left}")

        # Get player input
        player_guess_row, player_guess_column = SetAirship.user_atk_input(object, size)

        print(player_guess_row, player_guess_column)

        # check player guess on open board
        while computer_guess_board.board[player_guess_row][player_guess_column] == "-" or computer_guess_board.board[player_guess_row][player_guess_column] == "X":
            print("Captain please choose another coordinates!")
            sleep(2)
            player_guess_row, player_guess_column = SetAirship.user_atk_input(object, size)

        # Hit or miss on computer hidden board and append enemy open guess board
        if computer_hid_board.board[player_guess_row][player_guess_column] == "X":
            print("One of the Enemy Airships is falling from the sky!")
            sleep(2)
            computer_guess_board.board[player_guess_row][player_guess_column] = "X"
            clear()
        else:
            print("You shot went into the void!")
            sleep(2)
            computer_guess_board.board[player_guess_row][player_guess_column] = "-"
            clear()


    

RunGame()
