import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime

from category_options import (
    animes_gender_options,
    films_series_gender_options
)

class RegisterTab(ttk.Frame):
    def __init__(self, notebook):
        super().__init__(notebook)
        notebook.add(self, text="Register")

        def update_gender_options(event):
            selected = list_category_cobobox.get()
            if selected == "Animes":
                gender_category_cobobox['values'] = animes_gender_options
            elif selected in ("Films", "Series"):
                gender_category_cobobox['values'] = films_series_gender_options
            else:
                gender_category_cobobox['values'] = () 


        def save_data():
            name = name_text.get("1.0", "end-1c") 
            category = list_category_cobobox.get()
            gender = gender_category_cobobox.get()
            seasons = seasons_text.get("1.0", "end-1c")
            episodes = episodes_text.get("1.0", "end-1c")
            score = selected_var.get()
            description = description_text.get("1.0", "end-1c")
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

            conn = sqlite3.connect("list_register.db")
            cursor = conn.cursor()

            cursor.execute("INSERT INTO register_table VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                           (name, category, gender, seasons, episodes, score, description, current_date))

            conn.commit()
            conn.close()

            print("Dados salvos no banco de dados")

        def select_register():
            self.selected_option.set("Register")

        def select_update():
            self.selected_option.set("Update")

        def select_delete():
            self.selected_option.set("Delete")

        

        form_label = tk.Label(self, text="Form", font=("Helvetica", 12))
        form_label.place(x=10, y=10)

        self.selected_option = tk.StringVar()

        register_radiobutton = ttk.Radiobutton(self, text="Register", 
                                               variable=self.selected_option, 
                                               value="Register", 
                                               command=select_register)
        register_radiobutton.place(x=60, y=10)

        update_radiobutton = ttk.Radiobutton(self, text="Update", 
                                             variable=self.selected_option,
                                               value="Update", 
                                               command=select_update)
        update_radiobutton.place(x=130, y=10)

        delete_radiobutton = ttk.Radiobutton(self, text="Delete", 
                                             variable=self.selected_option, 
                                             value="Delete", 
                                             command=select_delete)
        delete_radiobutton.place(x=200, y=10)

        list_category_label = tk.Label(self, text="List Category")
        list_category_label.place(x=10, y=40)
        list_category_cobobox = ttk.Combobox(self, width=41, height=3)
        list_category_cobobox.place(x=10, y=60)
        list_category_cobobox['values'] = ("Animes", "Films", "Series")

        name_label = tk.Label(self, text="Name")
        name_label.place(x=10, y=90)
        name_text = tk.Text(self, width=33, height=1)
        name_text.place(x=10, y=110)

        gender_category_label = tk.Label(self, text="Gender")
        gender_category_label.place(x=10, y=140)

        gender_category_cobobox = ttk.Combobox(self, width=41, height=10)
        gender_category_cobobox.place(x=10, y=160)
        
        list_category_cobobox.bind("<<ComboboxSelected>>", update_gender_options)

        seasons_label = tk.Label(self, text="Seasons")
        seasons_label.place(x=10, y=190)
        seasons_text = tk.Text(self, width=15, height=1)
        seasons_text.place(x=10, y=210)

        episodes_label = tk.Label(self, text="Episodes")
        episodes_label.place(x=150, y=190)
        episodes_text = tk.Text(self, width=16, height=1)
        episodes_text.place(x=150, y=210)

        score_label = tk.Label(self, text="Score")
        score_label.place(x=10, y=240)

        selected_var = tk.IntVar()

        x_position = 10
        y_position = 280

        for value in range(0, 6):
            radiobutton = ttk.Radiobutton(self, variable=selected_var, value=value)
            radiobutton.place(x=x_position, y=y_position)
            text_label = tk.Label(self, text=str(value))
            text_label.place(x=x_position, y=y_position - 20)

            x_position += 50

        description_label = tk.Label(self, text="Description")
        description_label.place(x=10, y=300)
        description_text = tk.Text(self, width=33, height=10)
        description_text.place(x=10, y=330)

        save_button = tk.Button(self, text="Save", width=37, command=save_data)
        save_button.place(x=10, y=505)
