from os import system, name
from time import sleep
import random

print()


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
                            /.'              '.||  |
                           |=-                -=| (
                            \'.               .'||  |
                             '-.,_____ _____.-'  '-'
                                   [_____]=8  \033[0m\n
    ''')


class Board:
    """Class that creates boards and airships.

    Attributes:
        size (int): The size of the board.
        title (str): The title of the board (added dynamically in __init__).
        board (List[List[str]]): The game board represented as a list of lists.
    """
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
        for _ in range(self.size - 1):
            x_row = random.randint(0, self.size - 1)
            y_column = random.randint(0, self.size - 1)

            # Check if the chosen coordinates are taken
            while self.board[x_row][y_column] == "X":
                # If occupied, generate new random coordinates
                x_row = random.randint(0, self.size - 1)
                y_column = random.randint(0, self.size - 1)

            # Place airship at the random spot
            self.board[x_row][y_column] = "X"


class Game:
    """ Main class to manage the game logic."""
    def __init__(self):
        self.player_name = ""
        self.size = 0
        self.player_board = None
        self.computer_hid_board = None
        self.computer_g_board = None
        self.turns_left = 10

    def restart_game(self):
        """Reset the main game."""
        clear()
        Images.airship()
        print(TextCentering().center_text(
            "Thanks for playing! Restarting the game..."
            )
            )
        sleep(5)
        clear()
        self.__init__()
        self.input_name()
        self.table_size()
        self.player_board = Board(self.size, self.player_name)
        self.computer_hid_board = Board(self.size, "Enemy Hidden")
        self.computer_g_board = Board(self.size, "Enemy")
        Board.create_airships(self.computer_hid_board)
        Board.create_airships(self.player_board)
        self.run_game()

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
                "That is an invalid grid size! Insert 4, 6!"
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

            # Ask for user input
            size = input(
                TextCentering().center_text(
                    "Please insert your grid size!\n"
                    )
                    )
            clear()

            # Validate table options
            if size not in ["4", "6"]:
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
                sleep(3)
                clear()
                self.size = int(size)
                break

    def get_user_atk_input(self):
        """Validate user input."""
        while True:  # Create an infinite loop
            try:
                clear()
                self.computer_g_board.print_to_console()
                self.player_board.print_to_console()
                print(TextCentering().center_text(
                    f"You have {self.turns_left} turns remaining!"
                    )
                    )
                # Ask for row user input
                x_row = input(TextCentering().center_text(
                    "Enter the Enemy row number to attack:\n"
                ))

                # Validate the row input
                if int(x_row) not in range(0, self.size):
                    raise ValueError("Invalid input")

                # Ask for column user input
                y_column = input(TextCentering().center_text(
                    "Enter the Enemy column number to attack:\n"
                ))

                # Validate the column input
                if int(y_column) not in range(0, self.size):
                    raise ValueError("Invalid input")

                # If the input is valid, break out of the loop
                break

            except ValueError:
                # Display a helper message if invalid input
                clear()
                self.computer_g_board.print_to_console()
                self.player_board.print_to_console()
                print(TextCentering().center_text(
                    f"Invalid input, insert numbers 0 to {self.size - 1}"
                ))
                sleep(3)
                clear()

        # Return the row and column
        return int(x_row), int(y_column)

    def run_game(self):
        """Run the main game loop."""
        while self.turns_left > 0:
            # Display enemy and player boards
            self.computer_g_board.print_to_console()
            self.player_board.print_to_console()

            # Display turns left
            print(TextCentering().center_text(
                f"Turns left = {self.turns_left}"
                )
                )

            # Get player input return
            player_guess_row, player_guess_column = self.get_user_atk_input()

            # Check player input is valid
            while self.computer_g_board.board[
                player_guess_row][
                    player_guess_column] in ["-", "X"]:

                print(TextCentering().center_text(
                    "Captain please choose another coordinates!"
                    )
                    )
                sleep(3)
                clear()
                self.run_game()

            # Check if player hit or miss
            if self.computer_hid_board.board[
                player_guess_row][
                    player_guess_column] == "X":
                clear()
                Images.airship()
                print(TextCentering().center_text(
                    "One of the Enemy Airships is falling from the sky!"
                    )
                    )
                sleep(3)
                self.computer_g_board.board[
                    player_guess_row][
                        player_guess_column] = "X"
                clear()
            else:
                clear()
                Images.airship()
                print(TextCentering().center_text(
                    "You shot went into the void!"
                    )
                    )
                sleep(3)
                self.computer_g_board.board[
                    player_guess_row][
                        player_guess_column] = "-"
                clear()
                self.turns_left -= 1

            # Check if player wins
            if self.enemy_sunk_ships(self.computer_g_board) == (self.size - 1):
                clear()
                clear()
                Images.airship()
                print(TextCentering().center_text(
                    "-----------------------------------"
                    )
                    )
                print(TextCentering().center_text(
                    "You win!"
                    )
                    )
                print(TextCentering().center_text(
                    f"You hit all {self.size - 1} Airships!"
                    )
                    )
                print(TextCentering().center_text(
                    "-----------------------------------"
                    )
                    )
                sleep(10)
                game.restart_game()

            # Get computers random attack
            computer_guess_row = random.randint(0, (self.size - 1))
            computer_guess_column = random.randint(0, (self.size - 1))
            while self.player_board.board[
                computer_guess_row][
                    computer_guess_column
                    ] in ["-", "O"]:
                computer_guess_row = random.randint(0, (self.size - 1))
                computer_guess_column = random.randint(0, (self.size - 1))

            # Check if computer hit or miss
            if self.player_board.board[
                computer_guess_row][
                    computer_guess_column
                    ] == "X":
                Images.airship()
                print(TextCentering().center_text(
                    "One of YOUR Airships is falling from the sky!"
                    )
                    )
                sleep(3)
                self.player_board.board[
                    computer_guess_row][
                        computer_guess_column
                        ] = "O"
                clear()
            else:
                Images.airship()
                print(TextCentering().center_text(
                    "The Enemy shot went into the void!"
                    )
                    )
                sleep(3)
                self.player_board.board[
                    computer_guess_row][
                        computer_guess_column
                        ] = "-"
                clear()

            # Check if computer wins
            if self.player_sunk_ships(self.player_board) == (self.size - 1):
                clear()
                clear()
                Images.airship()
                print(TextCentering().center_text(
                    "-----------------------------------"
                    )
                    )
                print(TextCentering().center_text(
                    "You lose!"
                    )
                    )
                print(TextCentering().center_text(
                    f"The Enemy hit all your {self.size - 1} Airships!"
                    )
                    )
                print(TextCentering().center_text(
                    "-----------------------------------"
                    )
                    )
                sleep(10)
                game.restart_game()

            # Check if player run out of turns
            else:
                clear()
                Images.airship()
                print(TextCentering().center_text(
                    f"You have {self.turns_left} turns remaining!"
                    )
                    )
                sleep(3)
                clear()
                if self.turns_left == 0:
                    clear()
                    Images.airship()
                    print(TextCentering().center_text(
                        "You lose!!"
                        )
                        )
                    print(TextCentering().center_text(
                        "You run out of turns!"
                        )
                        )
                    sleep(10)
                    game.restart_game()

    @staticmethod
    def enemy_sunk_ships(board):
        """Count the number if enemy sunken ships"""
        sunk_ships = sum(row.count("X") for row in board.board)
        return sunk_ships

    @staticmethod
    def player_sunk_ships(board):
        """Count the number if player sunken ships"""
        sunk_ships = sum(row.count("0") for row in board.board)
        return sunk_ships


# Code taken from stack overflow
def clear():
    """Clear the console screen"""

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == "__main__":
    # Create a game instance
    game = Game()

    # Ask player name
    game.input_name()

    # Show welcome screen
    game.welcome_screen()

    # Ask player table size
    game.table_size()

    # Create boards
    game.player_board = Board(game.size, game.player_name)
    game.computer_hid_board = Board(game.size, "Enemy Hidden")
    game.computer_g_board = Board(game.size, "Enemy")

    # Create airships
    Board.create_airships(game.computer_hid_board)
    Board.create_airships(game.player_board)

    # Run Game
    game.run_game()
