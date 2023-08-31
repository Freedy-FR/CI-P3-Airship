from os import system, name
from time import sleep
import random

print()

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


class TextCentering:
    """Class for centering text within a specified width."""
    def __init__(self, width=80, fillchar=' '):
        self.width = width
        self.fillchar = fillchar
    
    def center_text(self, text):
        """Center the given text within the specified width."""
        centered_text = text.center(self.width, self.fillchar)
        return centered_text


class Images:
    """Class for printing ASCII art images."""
    @staticmethod
    def airship():
        """Print the airship image."""
        print('''\x1b[91m
                               Airship Battles 
                                _..--=--..._
                             .-'            '-.  .-.
                            /.'              '.\/  |
                           |=-                -=| (
                            \'.               .'/\  |
                             '-.,_____ _____.-'  '-'
                                   [_____]=8  \033[0m\n
    ''')


class Board:
    def __init__(self, size, title):
        self.size = size
        self.title = title
        self.board = [[" "] * size for _ in range(size)]

    def print_to_console(self):
        # Create an username title to the board and center username
        print("---{:^10}--- ".format(self.title))

        # Create the heading and separator based on the size given
        heading = [" "] + [str(i) for i in range(self.size)]
        separator = ["+"] * self.size

        # Print the heading and separator
        print(" " + " ".join(heading))
        print("   " + " ".join(separator))
        
        # Create an instance of the board
        for i, row in enumerate(self.board):
            print("-{}|{}|".format(i, "|".join(row)))
        print()
        
    def create_airships(self):
        # Generate random coordinates for placing an airship
        for i in range((self.size - 1)):
            x_row, y_column = random.randint(0, (self.size - 1)), random.randint(0, (self.size - 1))

            # Check if the chosen coordinates are taken
            while self.board[x_row][y_column] == "X":
                # If occupied, generate new random coordinates
                x_row, y_column = random.randint(0, (self.size - 1)), random.randint(0, (self.size - 1))
            
            # Place airship at the random spot
            self.board[x_row][y_column] = "X"


class UsernameInput:
    """
    Ask for username input and validate name
    """
    def input_name():
        name = input("Please tell me your name captain?\n")
        while True:
            if len(name) == 0:
                sleep(2)
                print("We are going to need your name for this Captain!")
                name = input("Please tell me your name captain?\n")
                clear()
            elif len(name) > 6:
                sleep(2)
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

class TableSizeInput:
    """
    """
    def table_size():        
        print("Please choose your battlefield grid size!")
        print("Insert 4: (4x4 Grid)-3 random ships")
        print("Insert 6: (6x6 Grid)-5 random ships")
        print("Insert 8: (8x8 Grid)-7 random ships\n")
        size = input("Please insert your grid size!\n")
        clear()
        while True:
            if len(size) == 0:
                sleep(2)
                print("We are going to need your prefered battlefield grid!")
                print("Insert 4: (4x4 Grid)-3 random ships")
                print("Insert 6: (6x6 Grid)-5 random ships")
                print("Insert 8: (8x8 Grid)-7 random ships\n")
                size = input("Please insert your grid size!\n")
                clear()
            elif (size != "4" and size != "6" and size != "8"):
                sleep(2)
                print("That is a invalid grid size!")
                print("Insert 4: (4x4 Grid)-3 random ships")
                print("Insert 6: (6x6 Grid)-5 random ships")
                print("Insert 8: (8x8 Grid)-7 random ships\n")
                size = input("Please insert your grid size!\n")
                clear()
            elif (size == "4" or size == "6" or size == "8"):
                clear()
                print("That is a fair grid size captain!")
                sleep(2)
                clear()
                return int(size)
        


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
                sleep(2)
                x_row = input("Enter the Enemy row number to attack: ")

            y_column = input("Enter the Enemy column number to attack: ")
            while int(y_column) not in range(0, (size)):
                print('Not a valid column Captain!')
                sleep(2)
                y_column = input("Enter the Enemy column number to attack: ")
            return int(x_row), int(y_column)
        except ValueError or KeyError or AttributeError:
            print("Invalid data, restarting the game...")
            sleep(3)
            clear()
            RunGame()
    
    def enemy_sunk_ships(self):
        sunk_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    sunk_ships += 1
        return sunk_ships

    def player_sunk_ships(self):
        sunk_ships = 0
        for row in self.board:
            for column in row:
                if column == "0":
                    sunk_ships += 1
        return sunk_ships


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

        # print computer guess_board
        SetBoard.print_to_console(computer_guess_board)

        # print player guess board
        SetBoard.print_to_console(player_guess_board)
        print(f"Turns left = {turns_left}")

        # Get player input
        player_guess_row, player_guess_column = SetAirship.user_atk_input(object, size)

        # Check player guess on open board
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

        # Check for win or loose for player and computer
        if SetAirship.enemy_sunk_ships(computer_guess_board) == (size - 1):
            clear()
            print("-----------------------------------")
            print("You win!")
            print(f"You hit all {size - 1} Airships!")
            print("-----------------------------------")
            sleep(10)
            break
        
        # Hit or miss on player board and append 
        computer_guess_row = random.randint(0, (size - 1))
        computer_guess_column = random.randint(0, (size - 1))
        while player_guess_board.board[computer_guess_row][computer_guess_column] == "-" or player_guess_board.board[computer_guess_row][computer_guess_column] == "O":
            computer_guess_row, computer_guess_column = random.randint(0, (size - 1)), random.randint(0, (size - 1))
        if player_guess_board.board[computer_guess_row][computer_guess_column] == "X":
            print("One of YOUR Airships is falling from the sky!")
            sleep(2)
            player_guess_board.board[computer_guess_row][computer_guess_column] = "O"
            clear()
        else:
            print("The Enemy shot went into the void!")
            sleep(2)
            player_guess_board.board[computer_guess_row][computer_guess_column] = "-"
            clear()        

        if SetAirship.player_sunk_ships(player_guess_board) == (size - 1):
            clear()
            print("-----------------------------------")
            print("You lose!")
            print(f"The Enemy hit all your {size - 1} Airships!")
            print("-----------------------------------")
            sleep(10)
            break
        else:
            turns_left -= 1
            clear()
            print(f"You have {turns_left} turns remaining!")
            sleep(2)
            if turns_left == 0:
                clear()
                SetBoard.print_to_console(computer_guess_board)
                SetBoard.print_to_console(player_guess_board)
                print("You run out of turns!")
                sleep(10)
                break        

RunGame()
