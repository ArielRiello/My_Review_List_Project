import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime

from category_options import (
    animes_genre_options,
    films_series_genre_options
)

class RegisterTab(ttk.Frame):

    def fill_data_from_name(self):

        selected_name = self.update_dialog_name_combobox.get()

        conn = sqlite3.connect("register_table.db")

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM register_table WHERE name = ?", (selected_name,))
        data = cursor.fetchone()

        if data:
            self.name_entry.delete("1.0", "end")
            self.name_entry.insert("1.0", data[0])
            self.category_combobox.set(data[1])
            self.genre_combobox.set(data[2])
            self.seasons_entry.delete("1.0", "end")
            self.seasons_entry.insert("1.0", data[3])
            self.episodes_entry.delete("1.0", "end")
            self.episodes_entry.insert("1.0", data[4])
            self.score_var.set(data[5])
            self.description_entry.delete("1.0", "end")
            self.description_entry.insert("1.0", data[6])

        conn.close()
        self.update_dialog.destroy()


    def open_update_dialog(self):
        if self.selected_option.get() == "Update":
            self.update_dialog = tk.Toplevel(self)
            self.update_dialog.title("Select Name to Update")

            category_label = tk.Label(self.update_dialog, text="Select Category")
            category_label.pack(pady=10)

            category_combobox = ttk.Combobox(self.update_dialog, values=("Animes", "Films", "Series"))
            category_combobox.pack(pady=10)

            name_label = tk.Label(self.update_dialog, text="Select Name")
            name_label.pack(pady=10)

            self.update_dialog_name_combobox = ttk.Combobox(self.update_dialog)
            self.update_dialog_name_combobox.pack(pady=10)


            def on_category_selected(event):
                selected_category = category_combobox.get()
                conn = sqlite3.connect("register_table.db")
                cursor = conn.cursor()

                cursor.execute("SELECT name FROM register_table WHERE category=?", (selected_category,))
                names = [row[0] for row in cursor.fetchall()]
                self.update_dialog_name_combobox['values'] = names

                conn.close()

            category_combobox.bind("<<ComboboxSelected>>", on_category_selected)

            select_button = tk.Button(self.update_dialog, text="Select", command=self.fill_data_from_name)
            select_button.pack(pady=10)

            
    def open_delete_dialog(self):
        if self.selected_option.get() == "Delete":
            delete_dialog = tk.Toplevel(self)
            delete_dialog.title("Select Name to Delete")


            def delete_selected_name():
                selected_name = delete_dialog_name_combobox.get()

                conn = sqlite3.connect("register_table.db")
                cursor = conn.cursor()

                cursor.execute("DELETE FROM register_table WHERE name = ?", (selected_name,))
                conn.commit()

                conn.close()
                delete_dialog.destroy()

                print(f"Deleted entry with name: {selected_name}")

            name_label = tk.Label(delete_dialog, text="Select Name")
            name_label.pack()

            delete_dialog_name_combobox = ttk.Combobox(delete_dialog)
            delete_dialog_name_combobox.pack()

            conn = sqlite3.connect("register_table.db")
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM register_table")
            names = [row[0] for row in cursor.fetchall()]
            delete_dialog_name_combobox['values'] = names

            conn.close()

            delete_button = tk.Button(delete_dialog, text="Delete", command=delete_selected_name)
            delete_button.pack()


    def __init__(self, notebook):
        super().__init__(notebook)
        notebook.add(self, text="Register")


        def update_genre_options(event):
            selected = self.category_combobox.get()
            if selected == "Animes":
                self.genre_combobox['values'] = animes_genre_options
            elif selected in ("Films", "Series"):
                self.genre_combobox['values'] = films_series_genre_options
            else:
                self.genre_combobox['values'] = ()


        def save_data():
            name = self.name_entry.get("1.0", "end-1c")
            category = self.category_combobox.get()
            genre = self.genre_combobox.get()
            seasons = self.seasons_entry.get("1.0", "end-1c")
            episodes = self.episodes_entry.get("1.0", "end-1c")
            score = self.score_var.get()
            description = self.description_entry.get("1.0", "end-1c")
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            conn = sqlite3.connect("register_table.db")
            cursor = conn.cursor()

            cursor.execute("SELECT 1 FROM register_table WHERE name=?", (name,))
            exists = cursor.fetchone()

            if exists:
                cursor.execute("""
                    UPDATE register_table
                    SET category = ?, genre = ?, seasons = ?, episodes = ?, score = ?, description = ?, date = ?
                    WHERE name = ?
                """, (category, genre, seasons, episodes, score, description, current_date, name))
                print("Data updated in the database")
            else:
                cursor.execute("INSERT INTO register_table VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                            (name, category, genre, seasons, episodes, score, description, current_date))
                print("Data saved to the database")

            conn.commit()
            conn.close()


        form_label = tk.Label(self, text="Form", font=("Helvetica", 12))
        form_label.place(x=10, y=10)

        self.selected_option = tk.StringVar()

        register_radiobutton = ttk.Radiobutton(self, text="Register", 
                                               variable=self.selected_option, 
                                               value="Register")
        register_radiobutton.place(x=60, y=10)

        update_radiobutton = ttk.Radiobutton(self, text="Update",
                                             variable=self.selected_option,
                                             value="Update",
                                             command=self.open_update_dialog)
        update_radiobutton.place(x=130, y=10)

        delete_radiobutton = ttk.Radiobutton(self, text="Delete",
                                             variable=self.selected_option,
                                             value="Delete",
                                             command=self.open_delete_dialog) 
        delete_radiobutton.place(x=200, y=10)


        category_label = tk.Label(self, text="Category")
        category_label.place(x=10, y=40)
        self.category_combobox = ttk.Combobox(self, width=41, height=3)
        self.category_combobox.place(x=10, y=60)
        self.category_combobox['values'] = ("Animes", "Films", "Series")

        name_label = tk.Label(self, text="Name")
        name_label.place(x=10, y=90)
        self.name_entry = tk.Text(self, width=33, height=1)
        self.name_entry.place(x=10, y=110)

        genre_label = tk.Label(self, text="Genre")
        genre_label.place(x=10, y=140)

        self.genre_combobox = ttk.Combobox(self, width=41, height=10)
        self.genre_combobox.place(x=10, y=160)
        
        self.category_combobox.bind("<<ComboboxSelected>>", update_genre_options)

        seasons_label = tk.Label(self, text="Seasons")
        seasons_label.place(x=10, y=190)
        self.seasons_entry = tk.Text(self, width=15, height=1)
        self.seasons_entry.place(x=10, y=210)

        episodes_label = tk.Label(self, text="Episodes")
        episodes_label.place(x=150, y=190)
        self.episodes_entry = tk.Text(self, width=16, height=1)
        self.episodes_entry.place(x=150, y=210)

        score_label = tk.Label(self, text="Score")
        score_label.place(x=10, y=240)

        self.score_var = tk.IntVar()

        x_position = 10
        y_position = 280

        for value in range(0, 6):
            radiobutton = ttk.Radiobutton(self, variable=self.score_var, value=value)
            radiobutton.place(x=x_position, y=y_position)
            score_text_label = tk.Label(self, text=str(value))
            score_text_label.place(x=x_position, y=y_position - 20)

            x_position += 50

        description_label = tk.Label(self, text="Description")
        description_label.place(x=10, y=300)
        self.description_entry = tk.Text(self, width=33, height=10)
        self.description_entry.place(x=10, y=330)

        save_button = tk.Button(self, text="Save", width=37, command=save_data)
        save_button.place(x=10, y=505)