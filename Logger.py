""" This program will run the logger """

import Game
import sys


def main_loop():
    print("Welcome the the Game Logger!\n\nWould you like to create a list?\nType \"y\" for yes and \"n\" for no\n")
    while True:
        status = input()
        if status == "n":
            sys.exit()
        if not status == "y":
            print("Invalid entry, please try again...\n")
        else:
            break;
    #Run rest of loop
    game_list = []


main_loop()
