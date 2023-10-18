import tkinter as tk
from tkinter import ttk
import sqlite3

from animes_tab import AnimesTab
from films_tab import FilmsTab
from series_tab import SeriesTab
from register_tab import RegisterTab

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Review List")
        self.root.geometry("740x580")

        conn = sqlite3.connect("register_table.db")
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS register_table
                          (name TEXT, category TEXT, 
                       genre TEXT, seasons TEXT, 
                       episodes TEXT, score INTEGER, 
                       description TEXT, date TEXT)''')

        conn.commit()
        conn.close()

        self.notebook = ttk.Notebook(self.root)
        self.notebook.place(x=10, y=10, width=720, height=560)

        self.animes_tab = AnimesTab(self.notebook)
        self.films_tab = FilmsTab(self.notebook)
        self.series_tab = SeriesTab(self.notebook)
        self.register_tab = RegisterTab(self.notebook)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
