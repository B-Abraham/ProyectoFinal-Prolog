from pyswip import Prolog
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import re

from GUI import *
from python_prolog_interface import *

prolog = Prolog()
prolog.consult("proyecto_final_grupo1.pl")

def get_clauses(p,nombre):
    animales = []
    clausulas = []
    
    for i in p.query("clause(adivina("+nombre+",X),Y)."):
        animales.append(i['X'])
        clausulas.append(i['Y'])
    return animales,clausulas

def respuesta(r):
    pass

def begin():
    begin_gui(animal_entry,begin_game,label1,ressi,resno)
    adivinado = animal_entry.get()
    animales, clausulas = get_clauses(prolog,adivinado)
    for i in clausulas:
        print(i)
    print()
    for i in animales:
        print(i)
    

def ronda(preguntas):
    for pregunta in preguntas:
        print(pregunta)

# Root o raiz de la interfaz grafica (tkinter)
root = tk.Tk()
root.title("Proyecto Final")
root.geometry('1280x720')

#Widgets estaticos
title = ttk.Label(root, text='Adivina Quien',font=("TkDefaultFont", 14))
title.place(x=510, y=20)
exit_button = ttk.Button(root, text='Salir', command=lambda: root.quit())
exit_button.place(x=1150, y=650)

#Widgets previos al inicio del juego
label1 = ttk.Label(root, text='Escriba el nombre del animal que la computadora intentará adivinar (no se preocupe, esta no sabrá lo que escribirá):')
animal = tk.StringVar()
animal_entry = ttk.Entry(root, textvariable=animal)
begin_game = ttk.Button(root,text="Comenzar juego",command=begin)

#Fotos
foto_aguila = Image.open('./img/aguila.png')
foto_aguila = ImageTk.PhotoImage(foto_aguila.resize((200,200)))
foto_avestruz = Image.open('./img/avestruz.png')
foto_avestruz = ImageTk.PhotoImage(foto_avestruz.resize((200,200)))
foto_buho = Image.open('./img/buho.png')
foto_buho = ImageTk.PhotoImage(foto_buho.resize((200,200)))
foto_cisne_negro = Image.open('./img/cisne_negro.png')
foto_cisne_negro = ImageTk.PhotoImage(foto_cisne_negro.resize((200,200)))
foto_flamenco = Image.open('./img/flamenco.png')
foto_flamenco = ImageTk.PhotoImage(foto_flamenco.resize((200,200)))
foto_gallo = Image.open('./img/gallo.png')
foto_gallo = ImageTk.PhotoImage(foto_gallo.resize((200,200)))
foto_ganso = Image.open('./img/ganso.png')
foto_ganso = ImageTk.PhotoImage(foto_ganso.resize((200,200)))
foto_loro = Image.open('./img/loro.png')
foto_loro = ImageTk.PhotoImage(foto_loro.resize((200,200)))
foto_pinguino = Image.open('./img/pinguino.png')
foto_pinguino = ImageTk.PhotoImage(foto_pinguino.resize((200,200)))
foto_tucan = Image.open('./img/tucan.png')
foto_tucan = ImageTk.PhotoImage(foto_tucan.resize((200,200)))

#Widgets durante la ejecucion del juego
ressi = ttk.Button(root,text="Si",command=respuesta('si.'))
resno = ttk.Button(root,text="No",command=respuesta('no.'))

show_entry(label1,animal_entry,begin_game)

root.mainloop()