import tkinter as tk
from tkinter import ttk
import sqlite3

class SeriesTab(ttk.Frame):
    def __init__(self, notebook):
        super().__init__(notebook)
        notebook.add(self, text="Series")

        series_label = tk.Label(self, text="My Series List", font=("Helvetica", 12))
        series_label.place(x=10, y=10)

        order_label = tk.Label(self, text="Sort By:", width=8)
        order_label.place(x=140, y=15)

        order_combobox = ttk.Combobox(self, width=15)
        order_combobox['values'] = ("alphabetical", "date", "rating")
        order_combobox.place(x=200, y=15)

        all_series_listbox = tk.Listbox(self, width=50, height=30)
        all_series_listbox.place(x=10, y=40)

        scrollbar_all_series = tk.Scrollbar(self, command=all_series_listbox.yview)
        scrollbar_all_series.place(x=315, y=40, height=480)
        all_series_listbox.config(yscrollcommand=scrollbar_all_series.set)

        selected_series_text_area = tk.Text(self, width=40, height=30)
        selected_series_text_area.place(x=350, y=40)

        scrollbar_selected_series = tk.Scrollbar(self, command=selected_series_text_area.yview)
        scrollbar_selected_series.place(x=675, y=40, height=480)
        selected_series_text_area.config(yscrollcommand=scrollbar_selected_series.set)

        def load_series():
            conn = sqlite3.connect("register_table.db")
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM register_table WHERE category='Series'")
            series = cursor.fetchall()

            all_series_listbox.delete(0, tk.END)

            for s in series:
                all_series_listbox.insert(tk.END, s[0])

            conn.close()

        def sort_series():
            selected_option = order_combobox.get()
            conn = sqlite3.connect("register_table.db")
            cursor = conn.cursor()

            if selected_option == "alphabetical":
                cursor.execute("SELECT name FROM register_table WHERE category='Series' ORDER BY name ASC")
            elif selected_option == "date":
                cursor.execute("SELECT name FROM register_table WHERE category='Series' ORDER BY date ASC")
            elif selected_option == "rating":
                cursor.execute("SELECT name FROM register_table WHERE category='Series' ORDER BY score DESC")

            series = cursor.fetchall()
            all_series_listbox.delete(0, tk.END)

            for s in series:
                all_series_listbox.insert(tk.END, s[0])

            conn.close()

        def show_selected_series(event):
            selected_index = all_series_listbox.curselection()
            if selected_index:
                selected_series_name = all_series_listbox.get(selected_index)
                selected_series_text_area.delete("1.0", tk.END)
                selected_series_data = load_series_data(selected_series_name)
                selected_series_text_area.insert(tk.END, selected_series_data)

        def load_series_data(series_name):
            conn = sqlite3.connect("register_table.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM register_table WHERE name=?", (series_name,))
            series_data = cursor.fetchone()
            conn.close()

            if series_data:
                date = f"Date: {series_data[7]}\n"
                name = f"Name: {series_data[0]}\n"
                genre = f"Genre: {series_data[2]}\n"
                description = f"Description: {series_data[6]}"
                return date + name + genre + description
            else:
                return "Series not found!"

        all_series_listbox.bind("<Visibility>", lambda event: load_series())
        all_series_listbox.bind("<<ListboxSelect>>", show_selected_series)
        order_combobox.bind("<<ComboboxSelected>>", lambda event: sort_series())
