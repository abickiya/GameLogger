""" This file defines a game object """


class Game:

    def __init__(self, name: "String", status: bool):
        self.name = name
        self.status = status

    def get_name(self) -> "String":
        return self.name

    def get_status(self) -> bool:
        return self.status

    def status_to_str(self) -> "String":
        return str(self.status)

    def set_name(self, new_name):
        self.name = new_name

    def set_status(self, new_status):
        self.status = new_status
