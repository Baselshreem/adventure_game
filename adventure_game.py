import time
import random
import string
import enum


class Color(enum.Enum):
    red = "\033[91m"
    purple = "\033[95m"
    blue = "\033[94m"
    cyan = "\033[96m"
    green = "\033[92m"
    orange = "\033[33m"
    yellow = "\033[93m"
    bold = "\033[1m"
    underline = "\033[4m"
    black = "\033[0m"

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def typewriter_simulator(message):
    for char in message:
        print(char, end="")
        if char in string.punctuation:
            time.sleep(0.5)
        time.sleep(0.03)
    print("")


def input_choise():
    while True:
        option = input()
        if option == "1" or option == "2":
            return option
        print(f"Option {option} is invalid. Try again!")


def print_pause(statment_printer, delye=2):
    # this is a function to puse a masge
    print(Color.get_color() + statment_printer)
    time.sleep(delye)


def description():
    # this is a func use a puse a masge to description player
    print_pause("Welcome to the adventure game. Thank you for choosing.\n", 2)

    print_pause(
        "Now you have reached the adventure game. "
        "There are two basic options in the game. "
        "A menu will be displayed to choose to start.\n",
        1,
    )
    print_pause("In front of you is a house.\n", 2)
    print_pause("To your right is a dark cave.\n", 2)
    print_pause(
        "There are slight differences in terms"
        "of the easy and difficult level of the game.\n"
    )


def Start_Play(items, option):
    # Things that happen when the player fights
    print_pause("Enter 1 to house or 2 cave.")
    print_pause("What would you like to do?")

    # choice1 = input("(Please enter 1 or 2.)\n")

    dd = input_choise()

    if dd == "1":
        print_pause("\n\n\nThank you Home has been selected to play.\n\n\n")
        house(items, option)

    elif dd == "2":
        print_pause("\nThank you cave has been selected to play.")
        cave(items, option)


def cave(item, option):
    if "mona" not in item:

        print_pause("\nUnsuccessful selection, please play again.\n")
    while True:
        choi = input(
            "Would you like to " "(1) start agin  or (2) Repeat_Play run away?"
        )

        if choi == "1":

            if "mona" in item:
                print_pause("\nThank you successful .")

            else:
                print_pause("\nGood luck, please try again..\n")
                item.append("mona")
                Start_Play(item, option)

        elif choi == "2":
            Repeat_Play()
            break
        else:
            print_pause("please enter a corect choise number between 1-2")


def house(items, option):
    # Things that happen to the player in the house

    choise = input("1. Enter through the door\n" "2. Entry from the window\n")

    if choise == "1":
        print_pause("\n\n\nThank you for making the right choice ...\n\n\n")
        while True:
            againe = input("Would you like to play again? (y/n)").lower()

            if againe == "y":
                print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
                house(items, option)
            elif againe == "n":
                print_pause("\n\n\nThank you  see you later ...\n\n\n")
                break
            else:
                print_pause("\n\n\nplease enter a corect choise ...\n\n\n")

    elif choise == "2":
        print_pause("game over ")
        print_pause("restart selected another choices,   method game ")
        Start_Play(items, option)
    else:
        print_pause("backe playe ")
        Repeat_Play()


def Repeat_Play():
    # Things that happen when the player runs back to the field
    print_pause("\n.The game is restarting\n")
    repeat = input(
                   "Would you like to repeat again,"
                   "please select 1-OK 2-I do not agreen")
    while True:
        if repeat == "1":
            print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
            play_game()
            break
        elif repeat == "2":
            print_pause("\n\n\n Thanks see you later.\n\n\n")
            exit(0)
        else:
            Repeat_Play()
            break


def play_game():
    items = []
    option = random.choice(["Basil", "Mohamad",
                            "asad", "shraime", "sile", "dina"])
    description()
    # function used a print and push
    # a masge on screen to descrip game
    Start_Play(items, option)
    # this is a call start game and tow
    # parmeter the first items and socond is option random


play_game()
