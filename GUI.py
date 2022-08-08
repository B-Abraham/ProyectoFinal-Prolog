import tkinter as tk
from tkinter import ttk
from python_prolog_interface import *

def initialize_gui(label,entry,button):
    label.place(x=270, y=100)
    entry.place(x=530, y=140)
    entry.focus()
    button.place(x=550, y=180)
    

def begin_gui(animal_entry,begin_game,label1,ressi,resno):
    animal_entry.place_forget()
    begin_game.place_forget()
    label1.place_forget()
    ressi.place(x=510, y=180)
    resno.place(x=610, y=180)

def display_photo(root,foto):
    image_label = ttk.Label(root, image=foto, text='El animal en el que estabas pensando era este?', compound='top')
    image_label.place(x=410, y=275)

def display_pregunta(pregunta,label_pregunta):
    texto = parsear_pregunta(pregunta)
    label_pregunta.config(text = texto)
    label_pregunta.place(x=480, y=120)

def parsear_pregunta(pregunta):
    if(pregunta.find("nocturno") != 0):
        return "¿El animal en que estas pensando es nocturno?"
    elif(pregunta.find("puede_nadar") != 0):
        return "¿El animal en que estas pensando puede nadar?"
    elif(pregunta.find("puede_volar") != 0):
        return "¿El animal en que estas pensando puede volar?"
    elif(pregunta.find("tamano(") != 0):
        return "¿El animal en que estas pensando es de tamaño X?"
    elif(pregunta.find("tamano_del_pico") != 0):
        return "¿El animal en que estas pensando tiene pico X?"

"""
preguntable(nocturno(_)).
preguntable(puede_nadar(_)).
preguntable(puede_volar(_)).
preguntable(puede_caminar(_)).
preguntable(migra(_)).
preguntable(color_del_plumaje(_,_)).
preguntable(color_del_pico(_,_)).
preguntable(alimentacion(_,_)).
preguntable(tamano(_,_)).
preguntable(tamano_del_pico(_,_)).
"""
