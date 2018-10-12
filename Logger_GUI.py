""" This file operates the Logger GUI """

from Game import Game
from Logger import *
import tkinter

class Logger_GUI:
    """ Class running an Othello game """

    def __init__(self):
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(master=self.root, width=500, height=500, background='blue')

    def run(self) -> None:
        self.root.mainloop()


game = Logger_GUI()
game.run()
