""" This file defines a game object. """


class Game:

    def __init__(self, name: "String", status: bool, console: "String"):
        self.name = name
        self.status = status
        self.console = console

    def get_name(self) -> "String":
        return self.name

    def get_name_lower(self) -> "String":
        return self.name.lower()

    def get_status(self) -> bool:
        return self.status

    def get_console(self) -> "String":
        return self.console

    def status_to_str(self) -> "String":
        return str(self.status)

    def set_name(self, new_name) -> None:
        self.name = new_name

    def set_status(self, new_status)-> None:
        self.status = new_status

    def set_console(self, new_console)-> None:
        self.console = new_console

    def __str__(self):
            return "{:40}{:10}{:10}".format(self.name, self.status, self.console)
