""" This file defines a game object """


class Game:

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def get_name(self):
        return self.name

    def get_status(self):
        return self.status
