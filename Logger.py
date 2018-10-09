""" This program will run the logger """

from Game import Game
import sys


def main_loop():
    print("Welcome the the Game Logger!\n\nWould you like to import a saved log?\n"
          "Type \"y\" for yes and \"n\" for no\n")
    while True:
        status = input()
        if status == "n":
            sys.exit()
        if status == "y":
            break
        else:
            print("Invalid entry, please try again...")
    main_menu()
    print("\nGoodbye!")


def main_menu():
    game_list = []
    game_list = game_manager(game_list)
    while True:
        print("\nMAIN MENU\nType \"p\" to see print options")
        print("Type \"a\" to add more games to the list\nType \"e\" to edit\n"
              "Type \"d\" to delete\nType \"q\" to quit\n")
        status = input()
        if status == "p":
            print_games(game_list)
        elif status == "a":
            game_list = game_manager(game_list)
        elif status == "e":
            game_list = edit_menu(game_list)
        elif status == "d":
            game_list = delete_menu(game_list)
        elif status == "q":
            break


def game_manager(game_list) -> "Game List":
    while True:
        print("\nWould you like to add a game?\nType \"y\" for yes and \"n\" for no\n")
        status = input()
        if status == "n":
            break
        elif status == "y":
            game_list = add_game(game_list)
        else:
            print("Invalid entry, please try again...\n")
    return game_list


def add_game(game_list: "Game List") -> "Game List":
    g_name = input("\nEnter game name\n")
    g_status = finish_status()
    new_game = Game(g_name, g_status)
    game_list.append(new_game)
    return game_list


def print_games(game_list: "Game List"):
    print("Enter 1 to print all games\nEnter 2 to print beaten games\nEnter 3 to print unbeaten games")
    command = input()
    if command == '1':
        print("\nHere are all the games you added:\n")
        for i in game_list:
            print(i.get_name())
    elif command == '2':
        print("\nHere all the games you have beaten\n")
        for i in game_list:
            if i.get_status():
                print(i.get_name())
    elif command == '3':
        print("\nHere all the games you haven't beaten\n")
        for i in game_list:
            if not i.get_status():
                print(i.get_name())
    else:
        print("\nInvalid input, returning to MAIN MENU")


def finish_status() -> bool:
    print("Have you beaten this game? Enter \"y\" for yes and \"n\" for no")
    while True:
        status = input()
        if status == "y":
            return True
        elif status == 'n':
            return False
        else:
            print("Invalid input please try again")


def edit_menu(game_list: "Game List") -> "Game List":
    if not game_list:
        print("Emtpy list, returning to MAIN MENU")
        return game_list
    status = input("Enter the name of the game you want to edit")
    position = find_game(game_list, status)
    if position == -1:
        print("Game not found, returning to MAIN MENU")
    else:
        print("Game found\n" + game_list[position].get_name())
        g_name = input("\nEnter game name\n")
        g_status = finish_status()
        game_list[position].set_name(g_name)
        game_list[position].set_status(g_status)
        print("Game data changed\n" + game_list[position].get_name())
        print("Returning to MAIN MENU")
        return game_list


def delete_menu(game_list: "Game List") -> "Game List":
    if not game_list:
        print("Emtpy list, returning to MAIN MENU")
        return game_list
    status = input("Enter the name of the game you want to delete")
    position = find_game(game_list, status)
    if position == -1:
        print("Game not found, returning to MAIN MENU")
    else:
        print("Game found\n" + game_list[position].get_name())
        game_list.pop(position)
        print("Game deleted")
        print("Returning to MAIN MENU")
        return game_list


def find_game(game_list, g_name):
    result = -1
    for i in range(len(game_list)):
        if game_list[i].name == g_name:
            result = i
            break
    return result




main_loop()
