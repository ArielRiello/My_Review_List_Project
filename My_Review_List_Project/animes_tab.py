import tkinter as tk
from tkinter import ttk
import sqlite3

class AnimesTab(ttk.Frame):
    def __init__(self, notebook):
        super().__init__(notebook)
        notebook.add(self, text="Animes")

        anime_list_label = tk.Label(self, text="My List of Animes", font=("Helvetica", 12))
        anime_list_label.place(x=10, y=10)

        order_label = tk.Label(self, text="Order By:", width=8)
        order_label.place(x=140, y=15)

        order_combobox = ttk.Combobox(self, width=15)
        order_combobox['values'] = ("alphabetical", "date", "score") 
        order_combobox.place(x=200, y=15)

        all_animes_listbox = tk.Listbox(self, width=50, height=30)
        all_animes_listbox.place(x=10, y=40)

        scrollbar_all_animes = tk.Scrollbar(self, command=all_animes_listbox.yview)
        scrollbar_all_animes.place(x=315, y=40, height=480)
        all_animes_listbox.config(yscrollcommand=scrollbar_all_animes.set)

        selected_anime_text_area = tk.Text(self, width=40, height=30)
        selected_anime_text_area.place(x=350, y=40)

        scrollbar_selected_anime = tk.Scrollbar(self, command=selected_anime_text_area.yview)
        scrollbar_selected_anime.place(x=675, y=40, height=480)
        selected_anime_text_area.config(yscrollcommand=scrollbar_selected_anime.set)

        def load_animes():
            conn = sqlite3.connect("list_register.db")
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM register_table WHERE category='Animes'")
            animes = cursor.fetchall()

            all_animes_listbox.delete(0, tk.END)

            for anime in animes:
                all_animes_listbox.insert(tk.END, anime[0])

            conn.close()

        def sort_animes():
            selected_option = order_combobox.get()
            conn = sqlite3.connect("list_register.db")
            cursor = conn.cursor()
            
            if selected_option == "alphabetical":
                cursor.execute("SELECT name FROM register_table WHERE category='Animes' ORDER BY name ASC")
            elif selected_option == "date":
                cursor.execute("SELECT name FROM register_table WHERE category='Animes' ORDER BY date ASC")
            elif selected_option == "score":
                cursor.execute("SELECT name FROM register_table WHERE category='Animes' ORDER BY score DESC")

            animes = cursor.fetchall()
            all_animes_listbox.delete(0, tk.END)

            for anime in animes:
                all_animes_listbox.insert(tk.END, anime[0])

            conn.close()

        def show_selected_anime(event):
            selected_index = all_animes_listbox.curselection()
            if selected_index:
                selected_anime_name = all_animes_listbox.get(selected_index)
                selected_anime_text_area.delete("1.0", tk.END)
                selected_anime_data = load_anime_data(selected_anime_name)
                selected_anime_text_area.insert(tk.END, selected_anime_data)

        def load_anime_data(anime_name):
            conn = sqlite3.connect("list_register.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM register_table WHERE name=?", (anime_name,))
            anime_data = cursor.fetchone()
            conn.close()

            if anime_data:
                date = f"Date: {anime_data[7]}\n"
                name = f"Name: {anime_data[0]}\n"
                gender = f"Gender: {anime_data[2]}\n"
                seasons = f"Seasons: {anime_data[3]}\n"
                episodes = f"Episodes: {anime_data[4]}\n"
                description = f"Description: {anime_data[6]}"
                return date + name + gender + seasons + episodes + description
            else:
                return "Anime not found !"

        all_animes_listbox.bind("<Visibility>", lambda event: load_animes())
        all_animes_listbox.bind("<<ListboxSelect>>", show_selected_anime)
        order_combobox.bind("<<ComboboxSelected>>", lambda event: sort_animes())
