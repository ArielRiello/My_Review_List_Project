import tkinter as tk
from tkinter import ttk

class SeriesTab(ttk.Frame):
    def __init__(self, notebook):
        super().__init__(notebook)
        notebook.add(self, text="Series")

