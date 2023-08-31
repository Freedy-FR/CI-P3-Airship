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
    """Class that creates boards and airships."""
    def __init__(self, size, title):
        self.size = size
        self.title = title
        self.board = [[" "] * size for _ in range(size)]

    def print_to_console(self):
        """Print the game board to the console."""
        # Create an username title to the board and center username
        print("---{:^10}--- ".format(self.title))

        # Create the heading and separator based on the size given
        heading = [" "] + [str(i) for i in range(self.size)]
        separator = ["+"] * self.size

        # Print the heading and separator
        print(" " + " ".join(heading))
        print("   " + " ".join(separator))
       
        # Create an enumerate the boards
        for i, row in enumerate(self.board):
            print("-{}|{}|".format(i, "|".join(row)))
        print()
        
    def create_airships(self):
        """Create airships on the game board."""
        # Generate random coordinates for placing an airship
        for i in range((self.size - 1)):
            x_row, y_column = random.randint(0, (self.size - 1)), random.randint(0, (self.size - 1))

            # Check if the chosen coordinates are taken
            while self.board[x_row][y_column] == "X":
                # If occupied, generate new random coordinates
                x_row, y_column = random.randint(0, (self.size - 1)), random.randint(0, (self.size - 1))

            # Place airship at the random spot
            self.board[x_row][y_column] = "X"


class Game:
    """ Main class to manage the game logic."""    
    def __init__(self):
        self.player_name = ""
        self.size = 0
        self.player_board = None
        self.computer_hid_board = None
        self.computer_guess_board = None
        self.turns_left = 10

    def input_name(self):
        """Ask for the player's name and validate it."""
        while True:
            clear()
            Images.airship()
            name = ""

            # Store alert message to the user
            alert = TextCentering().center_text(
                "Please insert a name between 1 and 6 letters\n"
                )

            # Print and ask for user input
            print(TextCentering().center_text(
                "We are going to need your name on this adventure Captain!"
                )
                )
            name = input(TextCentering().center_text(
                "Please tell me your name?\n"
                )
                ).strip()

            # Validate the user input
            if not 0 < len(name) <= 6:
                clear()
                Images.airship()
                print(alert)
                sleep(3)
            else:
                clear()
                Images.airship()
                print(TextCentering().center_text(
                    "That is a fair name captain!"
                    )
                    )
                sleep(3)
                clear()
                self.player_name = name.capitalize()
                break

    def welcome_screen(self):
        """Shows the welcome screen."""
        clear()
        Images.airship()
        # Print welcome message
        print(TextCentering().center_text(
            f" {self.player_name} Welcome to Airship battles!\n"
            )
            )
        sleep(3)
        clear()

    def table_size(self):
        """Ask for the size of the game board."""
        while True:
            # Store alert message to the user
            alert_table = TextCentering().center_text(
                "That is an invalid grid size! Insert 4, 6, 8 !"
                    )
            Images.airship()

            # Print the option to the user
            print(
                TextCentering().center_text(
                    "Please choose your battlefield grid size!\n"
                    )
                    )
            print(
                TextCentering().center_text(
                    "Insert 4: (4x4 Grid)-3 random ships"
                    )
                    )
            print(
                TextCentering().center_text(
                    "Insert 6: (6x6 Grid)-5 random ships"
                    )
                    )
            print(
                TextCentering().center_text(
                    "Insert 8: (8x8 Grid)-7 random ships\n"
                    )
                    )

            # Ask for user input
            size = input(
                TextCentering().center_text(
                    "Please insert your grid size!\n"
                    )
                    )
            clear()

            # Validate table options
            if size not in ["4", "6", "8"]:
                Images.airship()
                print(alert_table)
                sleep(2)
                clear()
            else:
                Images.airship()
                print(
                    TextCentering().center_text(
                        "That is a fair grid size captain!"
                        )
                        )
                sleep(2)
                self.size = int(size)
                break      

    def run_game(self):
        """Run the main game loop."""
        while self.turns_left > 0:
            # Display enemy and player boards
            self.computer_guess_board.print_to_console()
            self.computer_hid_board.print_to_console()
            self.player_board.print_to_console()

            # Display turns left
            print(TextCentering().center_text(
                f"Turns left = {self.turns_left}"
                )
                )



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
