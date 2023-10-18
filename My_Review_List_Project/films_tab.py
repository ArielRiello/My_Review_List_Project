import tkinter as tk
from tkinter import ttk
import sqlite3

class FilmsTab(ttk.Frame):
    def __init__(self, notebook):
        super().__init__(notebook)
        notebook.add(self, text="Movies")

        movies_label = tk.Label(self, text="My Movie List", font=("Helvetica", 12))
        movies_label.place(x=10, y=10)

        order_label = tk.Label(self, text="Sort By:", width=8)
        order_label.place(x=140, y=15)

        order_combobox = ttk.Combobox(self, width=15)
        order_combobox['values'] = ("alphabetical", "date", "rating")
        order_combobox.place(x=200, y=15)

        all_movies_listbox = tk.Listbox(self, width=50, height=30)
        all_movies_listbox.place(x=10, y=40)

        scrollbar_all_movies = tk.Scrollbar(self, command=all_movies_listbox.yview)
        scrollbar_all_movies.place(x=315, y=40, height=480)
        all_movies_listbox.config(yscrollcommand=scrollbar_all_movies.set)

        selected_movie_text_area = tk.Text(self, width=40, height=30)
        selected_movie_text_area.place(x=350, y=40)

        scrollbar_selected_movie = tk.Scrollbar(self, command=selected_movie_text_area.yview)
        scrollbar_selected_movie.place(x=675, y=40, height=480)
        selected_movie_text_area.config(yscrollcommand=scrollbar_selected_movie.set)

        def load_movies():
            conn = sqlite3.connect("register_table.db")
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM register_table WHERE category='Films'")
            movies = cursor.fetchall()

            all_movies_listbox.delete(0, tk.END)

            for movie in movies:
                all_movies_listbox.insert(tk.END, movie[0])

            conn.close()

        def sort_movies():
            selected_option = order_combobox.get()
            conn = sqlite3.connect("register_table.db")
            cursor = conn.cursor()

            if selected_option == "alphabetical":
                cursor.execute("SELECT name FROM register_table WHERE category='Films' ORDER BY name ASC")
            elif selected_option == "date":
                cursor.execute("SELECT name FROM register_table WHERE category='Films' ORDER BY date ASC")
            elif selected_option == "rating":
                cursor.execute("SELECT name FROM register_table WHERE category='Films' ORDER BY score DESC")

            movies = cursor.fetchall()
            all_movies_listbox.delete(0, tk.END)

            for movie in movies:
                all_movies_listbox.insert(tk.END, movie[0])

            conn.close()

        def show_selected_movie(event):
            selected_index = all_movies_listbox.curselection()
            if selected_index:
                selected_movie_name = all_movies_listbox.get(selected_index)
                selected_movie_text_area.delete("1.0", tk.END)
                selected_movie_data = load_movie_data(selected_movie_name)
                selected_movie_text_area.insert(tk.END, selected_movie_data)

        def load_movie_data(movie_name):
            conn = sqlite3.connect("register_table.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM register_table WHERE name=?", (movie_name,))
            movie_data = cursor.fetchone()
            conn.close()

            if movie_data:
                date = f"Date: {movie_data[7]}\n"
                name = f"Name: {movie_data[0]}\n"
                genre = f"Genre: {movie_data[2]}\n"
                description = f"Description: {movie_data[6]}"
                return date + name + genre + description
            else:
                return "Movie not found!"

        all_movies_listbox.bind("<Visibility>", lambda event: load_movies())
        all_movies_listbox.bind("<<ListboxSelect>>", show_selected_movie)
        order_combobox.bind("<<ComboboxSelected>>", lambda event: sort_movies())
