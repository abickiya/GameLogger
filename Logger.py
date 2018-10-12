""" This program will run the logger """

from Game import Game
import sys


def main_loop():
    """ The main loop that starts the program, only real job is to greet user and start menu"""
    print("\nWelcome the the Game Logger!\n\n")
    main_menu()
    print("\nGoodbye!")


def main_menu():
    """ Main Menu where user can access all of programs functions"""
    game_list = load_file()
    while True:
        print("\nMAIN MENU\nType \"p\" to see print options")
        print("Type \"a\" to add games to the list\nType \"e\" to edit\n"
              "Type \"d\" to delete\nType \"s\" to save to a file\nType \"q\" to quit\n")
        status = input()
        if status == "p":
            print_games(game_list)
        elif status == "a":
            game_list = game_manager(game_list)
        elif status == "e":
            game_list = edit_menu(game_list)
        elif status == "d":
            game_list = delete_menu(game_list)
        elif status == "s":
            write_file(game_list)
        elif status == "q":
            break


def game_manager(game_list) -> "Game List":
    """ This loop manages adding games and is responsible for handing the updated list back to the main menu """
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
    """ This function takes the Game List and add a game based on data given by the user """
    g_name = input("\nEnter game name\n")
    g_status = finish_status()
    g_console = input("Enter game console played on\n")
    new_game = Game(g_name, g_status, g_console)
    game_list.append(new_game)
    return game_list


def print_games(game_list: "Game List"):
    """ Gives the user various ways to print from the Game List """
    print("\nEnter 1 to print all games\nEnter 2 to print beaten games\n"
          "Enter 3 to print unbeaten games\nEnter 4 to print games by console played on\n"
          "Enter 5 for detailed entry on one game\n")
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
    elif command == '4':
        target_console = input("Enter console to search for\n")
        for i in game_list:
            if i.get_console() == target_console:
                print(i.get_name())
    elif command == '5':
        target = input("Please enter the game you would like to search for\n")
        position = find_game(game_list, target)
        if position == -1:
            print("\nGame not found, returning to MAIN MENU")
        else:
            print("\nName: " + game_list[position].get_name() + "\nBeaten: " + game_list[position].status_to_str()
                  + "\nConsole: " + game_list[position].get_console())
    else:
        print("\nInvalid input, returning to MAIN MENU")


def finish_status() -> bool:
    """ This function asks the user if they have beaten a game and passes the appropriate boolean """
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
    """ This function handles editing an entry on the list """
    if not game_list:
        print("\nEmtpy list, returning to MAIN MENU")
        return game_list
    status = input("Enter the name of the game you want to edit")
    position = find_game(game_list, status)
    if position == -1:
        print("Game not found, returning to MAIN MENU")
    else:
        print("Game found\n" + game_list[position].get_name())
        g_name = input("\nEnter game name\n")
        g_status = finish_status()
        g_console = input("\nEnter game console played on\n")
        game_list[position].set_name(g_name)
        game_list[position].set_status(g_status)
        game_list[position].set_console(g_console)
        print("Game data changed\n" + game_list[position].get_name())
        print("Returning to MAIN MENU")
        return game_list


def delete_menu(game_list: "Game List") -> "Game List":
    """ This function deleting editing an entry on the list """
    if not game_list:
        print("\nEmtpy list, returning to MAIN MENU")
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
    """ This function find a game in the list and returns its index """
    result = -1
    for i in range(len(game_list)):
        if game_list[i].name == g_name:
            result = i
            break
    return result


def load_file() -> "Game List":
    """ Asks the user if they want to load the list from a file, if not, does nothing"""
    print("Would you like to load a Game Log from a file?\n"
          "Type \"y\" for yes and \"n\" for no\n")
    while True:
        status = input()
        if status == 'n':
            return []
        elif status == 'y':
            game_list = file_reader()
            return game_list
        else:
            print("Invalid entry, please try again...")


def file_reader() -> "Game List":
    """ Interprets text file and creates list """
    print("\nLoading from file")
    glist = []
    try:
        infile = open("Saved_Log.txt", "r")
    except FileNotFoundError:
        print("No valid save file detected, returning to MAIN MENU\n")
        return
    for line in infile:
        entries = line.split('\t')
        glist.append(Game(entries[0], entries[1], entries[2]))
    print("Load Successful\n")
    return glist


def write_file(game_list: "Game List"):
    """ Writes list data to file """
    print("\nWriting to file")
    if not game_list:
        print("No data to save, save cancelled, returning to MAIN MENU")
        return
    outfile = open("Saved_Log.txt", "w")
    for i in game_list:
        outfile.write(i.get_name() + '\t' + i.status_to_str() + '\t' + i.get_console() + '\n')
    outfile.close()
    print("Write Successful\n")
    return



main_loop()
