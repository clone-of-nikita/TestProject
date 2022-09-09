import sqlite3
from tkinter import *


class App:
    def __init__(self):
        self.login = None
        self.password = None
        self.entry_1 = None
        self.root = root
        self.mainWindow()
        self.variables()
        self.sqlConnect()

    def sqlConnect(self):
        self.connect = sqlite3.connect('Names.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute("create table dhcp (mac text not NULL primary key, hostname text, model text, location zalupa text)")
        self.connect.commit()
        self.cursor.close()

    def variables(self):
        self.root = root
        self.login = StringVar()
        self.password = StringVar()

    def mainWindow(self):
        self.root.title("Random shit")
        self.root.geometry("650x500")
        self.root.resizable(False, False)
        self.btn_1 = Button(root, text="Hello", bg='Gray', padx=20, pady=10, command=self.buttonToDo)
        self.btn_1.place(x=330, y=400, anchor="n", height=40, width=150, bordermode=OUTSIDE)

        self.entry_1 = Entry(root, textvariable=self.login)
        self.entry_1.place(x=330, y=250, anchor="n", height=30, width=150, bordermode=OUTSIDE)

        self.entry_2 = Entry(root, textvariable=self.password)
        self.entry_2.place(x=330, y=150, anchor="n", height=30, width=150, bordermode=OUTSIDE)

    def buttonToDo(self):
        self.x = []
        self.entry_1_1 = self.entry_2.get()
        self.entry_2_1 = self.entry_1.get()
        self.x.append(self.entry_1_1)
        self.x.append(self.entry_2_1)
        print(self.x)


root = Tk()
myapp = App()
root.mainloop()
