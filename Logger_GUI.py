""" This file operates the Logger GUI """

from Game import Game
from Logger import *
import tkinter


class Add_Window:

    def __init__(self) -> None:
        self.dialog_window = tkinter.Toplevel()
        self.dialog_window.columnconfigure(1, weight=1, minsize=40)
        self.dialog_window.columnconfigure(0, weight=1)
        self.accept_flag = False

        name_label = tkinter.Label(master=self.dialog_window, text='Game Name',
                                   font=('Helvetica', 15), pady=5, padx=3)
        name_label.grid(column=0, row=0, sticky=tkinter.W)

        status_label = tkinter.Label(master=self.dialog_window, text='Completion Status',
                                     font=('Helvetica', 15), pady=5, padx=3)
        status_label.grid(column=0, row=1, sticky=tkinter.W)

        system_label = tkinter.Label(master=self.dialog_window, text='System Owned On',
                                     font=('Helvetica', 15), pady=5, padx=3)
        system_label.grid(column=0, row=2, sticky=tkinter.W)

        self.name_entry = tkinter.Entry(master=self.dialog_window, width=22)
        self.name_entry.grid(column=2, row=0, sticky=tkinter.E)

        self.status_entry = tkinter.Spinbox(master=self.dialog_window, values=("Beaten", "Unbeaten"))
        self.status_entry.grid(column=2, row=1, sticky=tkinter.E)

        self.system_entry = tkinter.Entry(master=self.dialog_window, width=22)
        self.system_entry.grid(column=2, row=2, sticky=tkinter.E)

        ok_button = tkinter.Button(master=self.dialog_window, text='Accept', height=2, width=7,
                                   command=self.accept_pressed)
        ok_button.grid(column=3, row=4, sticky=tkinter.S)

        cancel_button = tkinter.Button(master=self.dialog_window, text='Cancel', height=2, width=7,
                                       command=self.close_window)
        cancel_button.grid(column=4, row=4, sticky=tkinter.S)

    def show(self) -> None:
        self.dialog_window.grab_set()
        self.dialog_window.wait_window()

    def accept_pressed(self) -> None:
        self.accept_flag = True
        self.name = self.name_entry.get()
        self.status = False
        if self.status_entry.get() == "Beaten":
            self.status = True
        self.system = self.system_entry.get()
        self.close_window()

    def close_window(self) -> None:
        self.dialog_window.destroy()




class Logger_GUI:
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
        self.save_option = tkinter.Button(master=self.root, text='SAVE', height=2, width=10,
                                          command=self.save_pressed)
        self.add_option.place(relx=.95, rely=.30, anchor='e')
        self.delete_option.place(relx=.95, rely=.45, anchor='e')
        self.edit_option.place(relx=.95, rely=.60, anchor='e')
        self.save_option.place(relx=.95, rely=.15, anchor='e')

    def add_pressed(self) -> None:
        adder = Add_Window()
        adder.show()
        if adder.accept_flag:
            self.game_list = finish_add(self.game_list, adder.name, adder.status, adder.system)
        for x in self.game_list:
            print(x.get_name())

    def save_pressed(self) -> None:
        write_file(self.game_list)

    def dummy(self):
        print("hello")


game = Logger_GUI()
game.run()


""" FIX THE SAVING FIRST THING """