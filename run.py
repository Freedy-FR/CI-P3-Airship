from os import system, name
from time import sleep
import random


class TextCentering:
    def __init__(self, width=80, fillchar=' '):
        self.width = width
        self.fillchar = fillchar
    
    def center_text(self, text):
        centered_text = text.center(self.width, self.fillchar)
        return centered_text


class Images:
    @staticmethod
    def airship():
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
        print("---{:^10}--- ".format(self.title))
        heading = [" "] + [str(i) for i in range(self.size)]
        separator = ["+"] * self.size
        print(" " + " ".join(heading))
        print("   " + " ".join(separator))
        
        for i, row in enumerate(self.board):
            print("-{}|{}|".format(i, "|".join(row)))
        print()
        
    def create_airships(self):
        for i in range((self.size - 1)):
            x_row, y_column = random.randint(0, (self.size - 1)), random.randint(0, (self.size - 1))
            while self.board[x_row][y_column] == "X":
                x_row, y_column = random.randint(0, (self.size - 1)), random.randint(0, (self.size - 1))
            self.board[x_row][y_column] = "X"


class Game:
    def __init__(self):
        self.player_name = ""
        self.size = 0
        self.player_board = None
        self.computer_hid_board = None
        self.computer_guess_board = None
        self.turns_left = 10

    def input_name(self):
        while True:
            clear()
            Images.airship()
            name = ""
            alert = TextCentering().center_text("Please insert a name between 1 and 6 letters\n")
            print(TextCentering().center_text("We are going to need your name on this adventure Captain!"))
            name = input(TextCentering().center_text("Please tell me your name?\n")).strip()
            if not 0 < len(name) <= 6:
                clear()
                Images.airship()
                print(alert)
                sleep(2)
            else:
                clear()
                Images.airship()
                print(TextCentering().center_text("That is a fair name captain!"))
                sleep(2)
                clear()
                self.player_name = name.capitalize()
                break

    def welcome_screen(self):
        clear()
        Images.airship()
        print(TextCentering().center_text(f" {self.player_name} Welcome to Airship battles!\n"))
        sleep(2)
        clear()

    def table_size(self):
        
        while True:
            alert_table = TextCentering().center_text(
                "That is an invalid grid size! Insert 4, 6, 8 !"
                    )
            Images.airship()
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
            size = input(
                TextCentering().center_text(
                    "Please insert your grid size!\n"
                    )
                    )
            clear()
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
        while self.turns_left > 0:
            self.computer_guess_board.print_to_console()
            self.computer_hid_board.print_to_console()
            self.player_board.print_to_console()
            print(TextCentering().center_text(f"Turns left = {self.turns_left}"))

            # Get player input
            player_guess_row, player_guess_column = self.get_user_atk_input()

            # Check player guess on open board
            while self.computer_guess_board.board[player_guess_row][player_guess_column] in ["-", "X"]:
                print(TextCentering().center_text("Captain please choose another coordinates!"))
                sleep(2)
                player_guess_row, player_guess_column = self.get_user_atk_input()

            if self.computer_hid_board.board[player_guess_row][player_guess_column] == "X":
                print(TextCentering().center_text("One of the Enemy Airships is falling from the sky!"))
                sleep(2)
                self.computer_guess_board.board[player_guess_row][player_guess_column] = "X"
                clear()
            else:
                print(TextCentering().center_text("You shot went into the void!"))
                sleep(2)
                self.computer_guess_board.board[player_guess_row][player_guess_column] = "-"
                clear()
                self.turns_left -= 1

            if self.enemy_sunk_ships(self.computer_guess_board) == (self.size - 1):
                clear()
                print(TextCentering().center_text("-----------------------------------"))
                print(TextCentering().center_text("You win!"))
                print(TextCentering().center_text(f"You hit all {self.size - 1} Airships!"))
                print(TextCentering().center_text("-----------------------------------"))
                sleep(10)
                break

            computer_guess_row = random.randint(0, (self.size - 1))
            computer_guess_column = random.randint(0, (self.size - 1))
            while self.player_board.board[computer_guess_row][computer_guess_column] in ["-", "O"]:
                computer_guess_row = random.randint(0, (self.size - 1))
                computer_guess_column = random.randint(0, (self.size - 1))
            
            if self.player_board.board[computer_guess_row][computer_guess_column] == "X":
                print(TextCentering().center_text("One of YOUR Airships is falling from the sky!"))
                sleep(2)
                self.player_board.board[computer_guess_row][computer_guess_column] = "O"
                clear()
            else:
                print(TextCentering().center_text("The Enemy shot went into the void!"))
                sleep(2)
                self.player_board.board[computer_guess_row][computer_guess_column] = "-"
                clear()

            if self.player_sunk_ships(self.player_board) == (self.size - 1):
                clear()
                print(TextCentering().center_text("-----------------------------------"))
                print(TextCentering().center_text("You lose!"))
                print(TextCentering().center_text(f"The Enemy hit all your {self.size - 1} Airships!"))
                print(TextCentering().center_text("-----------------------------------"))
                sleep(10)
                break
            else:
                clear()
                print(TextCentering().center_text(f"You have {self.turns_left} turns remaining!"))
                sleep(2)
                if self.turns_left == 0:
                    clear()
                    self.computer_guess_board.print_to_console()
                    self.player_board.print_to_console()
                    print(TextCentering().center_text("You lose!!"))
                    print(TextCentering().center_text("You run out of turns!"))
                    sleep(10)
                    break

    @staticmethod
    def enemy_sunk_ships(board):
        sunk_ships = sum(row.count("X") for row in board.board)
        return sunk_ships

    @staticmethod
    def player_sunk_ships(board):
        sunk_ships = sum(row.count("0") for row in board.board)
        return sunk_ships

    def get_user_atk_input(self):
        try:   
            x_row = input(TextCentering().center_text("Enter the Enemy row number to attack: "))
            while int(x_row) not in range(0, self.size):
                print(TextCentering().center_text('Not a valid row Captain!'))
                sleep(2)
                x_row = input(TextCentering().center_text("Enter the Enemy row number to attack: "))

            y_column = input(TextCentering().center_text("Enter the Enemy column number to attack: "))
            while int(y_column) not in range(0, self.size):
                print(TextCentering().center_text('Not a valid column Captain!'))
                sleep(2)
                y_column = input(TextCentering().center_text("Enter the Enemy column number to attack: "))
            return int(x_row), int(y_column)
        except ValueError or KeyError or AttributeError:
            print(TextCentering().center_text(f"Invalid input, please insert a number from 0 to {self.size - 1}"))
            sleep(3)
            clear()
            self.run_game()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

if __name__ == "__main__":
    game = Game()
    game.input_name()
    game.welcome_screen()
    game.table_size()

    game.player_board = Board(game.size, game.player_name)
    game.computer_hid_board = Board(game.size, "Enemy Hidden")
    game.computer_guess_board = Board(game.size, "Enemy")

    Board.create_airships(game.computer_hid_board)
    Board.create_airships(game.player_board)

    game.run_game()
