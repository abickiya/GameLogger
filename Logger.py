""" This program will run the logger """

from Game import Game
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
    game_manager()
    print("Goodbye!")


def game_manager():
    game_list = []
    while True:
        print("Would you like to add a game?\nType \"y\" for yes and \"n\" for no\n")
        status = input()
        if status == "n":
            break
        elif status == "y":
            game_list = add_game( game_list )
        else:
            print("Invalid entry, please try again...\n")


def add_game( game_list ):
    g_name = input("Enter game name\n")
    new_game = Game( g_name, False)
    game_list.append( new_game )
    return game_list


main_loop()
