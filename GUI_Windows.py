""" This file has to code for all popup windows for the GUI """

import tkinter


class Add_Window:
    """ This class opens up the window to add a game to the list """
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


class View_Window:
    """ This class opens up the detailed view window """
    def __init__(self, selected: "String") -> None:
        self.dialog_window = tkinter.Toplevel()
        self.canvas1 = tkinter.Canvas(master=self.dialog_window, width=300, height=75)
        self.canvas2 = tkinter.Canvas(master=self.dialog_window, width=300, height=75)
        self.canvas3 = tkinter.Canvas(master=self.dialog_window, width=300, height=75)
        self.dialog_window.rowconfigure(0, weight=1)
        self.dialog_window.rowconfigure(1, weight=1)
        self.dialog_window.rowconfigure(2, weight=1)
        self.canvas1.grid(column=0, row=0)
        self.canvas2.grid(column=0, row=1)
        self.canvas3.grid(column=0, row=2)

        g_name = selected.get_name()
        if selected.get_status:
            g_status = "Beaten"
        else:
            g_status = "Incomplete"
        g_console = "Owned for " + selected.get_console()

        name_label = tkinter.Label(master=self.dialog_window, text=g_name,
                                   font=('Helvetica', 10))
        name_label.grid(column=0, row=0)

        status_label = tkinter.Label(master=self.dialog_window, text=g_status,
                                     font=('Helvetica', 10))
        status_label.grid(column=0, row=1)

        system_label = tkinter.Label(master=self.dialog_window, text=g_console,
                                     font=('Helvetica', 10))
        system_label.grid(column=0, row=2)

    def show(self) -> None:
        self.dialog_window.grab_set()
        self.dialog_window.wait_window()

    def close_window(self) -> None:
        self.dialog_window.destroy()


class Edit_Window:
    """ This class opens up the window to add a game to the list """
    def __init__(self, selected: "String") -> None:
        self.dialog_window = tkinter.Toplevel()
        self.dialog_window.columnconfigure(1, weight=1, minsize=40)
        self.dialog_window.columnconfigure(0, weight=1)
        self.accept_flag = False

        name_label = tkinter.Label(master=self.dialog_window, text='Game Name',
                                   font=('Helvetica', 13), pady=5, padx=3)
        name_label.grid(column=0, row=0, sticky=tkinter.W)

        status_label = tkinter.Label(master=self.dialog_window, text='Completion Status',
                                     font=('Helvetica', 13), pady=5, padx=3)
        status_label.grid(column=0, row=1, sticky=tkinter.W)

        system_label = tkinter.Label(master=self.dialog_window, text='System Owned On',
                                     font=('Helvetica', 13), pady=5, padx=3)
        system_label.grid(column=0, row=2, sticky=tkinter.W)

        info_label = tkinter.Label(master=self.dialog_window, text='Editing ' + selected,
                                   font=("Helvetica", 9), padx=2, pady=2)
        info_label.grid(column=0, row=4, sticky=tkinter.SW)

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
