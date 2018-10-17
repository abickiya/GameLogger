""" This file operates the Logger GUI """

from Game import Game
from Logger import *
import tkinter

class Logger_GUI:
    """ Class running an Othello game """

    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(master=self.root, width=500, height=500)
        self.canvas.grid()
        self.draw_entry()

    def draw_entry(self) -> None:
        welcome_label = tkinter.Label(master=self.root, text="Welcome to the Game Logger!", font=('Helvetica', 25))
        load_option = tkinter.Button(master=self.root, text='Load from a file', height=5, width=15)
        new_option = tkinter.Button(master=self.root, text='Start a new list', height=5, width=15)
        welcome_label.grid(column=0, row=0, sticky=tkinter.N)
        load_option.place(relx=.35, rely=.5, anchor='center')
        new_option.place(relx=.65, rely=.5, anchor='center')

    def run(self) -> None:
        self.root.mainloop()


game = Logger_GUI()
game.run()


'''
        self.mode_button = tkinter.Button(master = self.root, text = 'Click to set rules and start game',
            font = ('Helvetica', 15), command = self._mode_button_pressed)
            
'''
