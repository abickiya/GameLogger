""" This file operates the Logger GUI """

from Game import Game
from Logger import *
import tkinter


class Add_window:

    def __init__(self) -> None:
        self.dialog_window = tkinter.Toplevel()
        name_label = tkinter.Label(master=self.dialog_window, text='Game Name',
                                   font=('Helvetica', 15), pady=5, padx=3)
        name_label.grid(column=0, row=0, sticky=tkinter.W)

        status_label = tkinter.Label(master=self.dialog_window,text='Completion Status',
                                     font=('Helvetica', 15), pady=5, padx=3)
        status_label.grid(column=0, row=1, sticky=tkinter.W)

        system_label = tkinter.Label(master=self.dialog_window, text='System owned on',
                                     font=('Helvetica', 15), pady=5, padx=3)
        system_label.grid(column=0, row=2, sticky=tkinter.W)



class Logger_gui:
    """ Class governing the main Game Logger Interface """

    def __init__(self) -> None:
        self.game_list = []
        self.root = tkinter.Tk()
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.canvas = tkinter.Canvas(master=self.root, width=500, height=500)
        self.canvas.grid()
        self.draw_entry()

    def run(self) -> None:
        self.root.mainloop()

    def draw_entry(self) -> None:
        self.welcome_label = tkinter.Label(master=self.root, text="Welcome to the Game Logger!", font=('Helvetica', 25))
        self.load_option = tkinter.Button(master=self.root, text='Load from a file', height=5, width=15,
                                          command=self.load_pressed)
        self.new_option = tkinter.Button(master=self.root, text='Start a new list', height=5, width=15,
                                         command=self.new_pressed)
        self.welcome_label.grid(column=0, row=0, sticky=tkinter.N)
        self.load_option.place(relx=.35, rely=.5, anchor='center')
        self.new_option.place(relx=.65, rely=.5, anchor='center')

    def load_pressed(self) -> None:
        self.load_option.destroy()
        self.new_option.destroy()
        self.welcome_label.destroy()
        self.game_list = file_reader()
        self.draw_controls()

    def new_pressed(self) -> None:
        self.load_option.destroy()
        self.new_option.destroy()
        self.welcome_label.destroy()
        self.draw_controls()

    def draw_controls(self) -> None:
        self.add_option = tkinter.Button(master=self.root, text='ADD', height=2, width=10,
                                         command=self.add_pressed)
        self.delete_option = tkinter.Button(master=self.root, text='DELETE', height=2, width=10,
                                            command=self.dummy)
        self.edit_option = tkinter.Button(master=self.root, text='EDIT', height=2, width=10,
                                          command=self.dummy)
        self.add_option.place(relx=.95, rely=.25, anchor='e')
        self.delete_option.place(relx=.95, rely=.40, anchor='e')
        self.edit_option.place(relx=.95, rely=.55, anchor='e')

    def add_pressed(self) -> None:
        adder = Add_window()
        print("add pressed")

    def dummy(self):
        print("Hello World")


game = Logger_gui()
game.run()
