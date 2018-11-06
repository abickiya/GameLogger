""" This file operates the Logger GUI """

from Game import Game
from Logger import *
from GUI_Windows import *
import tkinter


class Logger_GUI:
    """ Class governing the main Game Logger Interface """

    def __init__(self) -> None:
        self.game_list = []
        self.root = tkinter.Tk()
        self.root.columnconfigure(0, weight=1, minsize=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
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
        self.save_option = tkinter.Button(master=self.root, text='SAVE', height=2, width=10,
                                          command=self.save_pressed)
        self.view_option = tkinter.Button(master=self.root, text='VIEW', height=2, width=10,
                                          command=self.view_pressed)
        self.draw_list()
        self.view_option.place(relx=.92, rely=.15, anchor='e')
        self.add_option.place(relx=.92, rely=.30, anchor='e')
        self.edit_option.place(relx=.92, rely=.45, anchor='e')
        self.delete_option.place(relx=.92, rely=.60, anchor='e')
        self.save_option.place(relx=.92, rely=.75, anchor='e')

    def draw_list(self) -> None:
        self.list_display = tkinter.Listbox(master=self.root, width=50, height=25)
        for x in self.game_list:
            self.list_display.insert(tkinter.END, x.get_name())
        self.scrollbar = tkinter.Scrollbar(self.root, orient=tkinter.VERTICAL)
        self.scrollbar.config(command=self.list_display.yview)
        self.list_display.config(yscrollcommand=self.scrollbar.set)
        self.list_display.place(relx=.1, rely=.1)
        self.scrollbar.grid(row=0, column=2, sticky="ns")

    def view_pressed(self) -> None:
        try:
            selected = self.list_display.get(self.list_display.curselection())
        except tkinter.TclError:
            return
        g_index = find_game(self.game_list, selected)
        viewer = View_Window(self.game_list[g_index])
        viewer.show()

    def add_pressed(self) -> None:
        adder = Add_Window()
        adder.show()
        if adder.accept_flag:
            self.game_list = finish_add(self.game_list, adder.name, adder.status, adder.system)
            self.list_display.destroy()
            self.draw_list()

    def save_pressed(self) -> None:
        write_file(self.game_list)

    def dummy(self):
        print("celtics suck")


game = Logger_GUI()
game.run()

