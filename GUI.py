import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pyswip import Prolog
from python_prolog_interface import *

def show_entry(label,entry,button):
    label.place(x=230, y=80)
    entry.place(x=490, y=120)
    entry.focus()
    button.place(x=510, y=160)

def begin_gui(animal_entry,begin_game,label1,ressi,resno):
    animal_entry.place_forget()
    begin_game.place_forget()
    label1.place_forget()
    ressi.place(x=470, y=160)
    resno.place(x=570, y=160)

def display_photo(foto):
    image_label = ttk.Label(root, image=foto, text='El animal en el que estabas pensando era este?', compound='top')
    image_label.place(x=400, y=250)

