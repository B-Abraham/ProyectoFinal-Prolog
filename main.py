from pyswip import Prolog
import tkinter as tk
from tkinter import Frame, ttk
from PIL import Image, ImageTk

from GUI import *
from python_prolog_interface import *

prolog = Prolog()
prolog.consult("proyecto_final_grupo1.pl")
preguntas = []

def respuesta(r):
    global preguntas
    if(preguntas.__len__() > 1):
        display_pregunta(preguntas[0],label_pregunta)
        preguntas.pop(0)
    else:
        print("fin")




def begin():
    begin_gui(animal_entry,begin_game,label1,ressi,resno)
    adivinado = animal_entry.get()
    
    clausulas = get_clauses(prolog,adivinado)
    temp = []
    for i in clausulas:
        [temp.append(j) for j in i if j not in temp]
    clausulas = temp

    global preguntas
    preguntas = clausulas
    
    ronda(clausulas)

def ronda(clausulas):
    global preguntas
    preguntas.pop(0)
    for pregunta in clausulas:
        if(bool(list(prolog.query("busca("+pregunta+")."))) is False):
            display_pregunta(pregunta,label_pregunta)


# Root o raiz de la interfaz grafica (tkinter)
root = tk.Tk()
root.title("Proyecto Final")
root.geometry('1280x720')
root.config(bg="lightgray")

#Widgets estaticos
left_frame = Frame(root, width=1260, height=700)
left_frame.place(x=10,y=10)
title = ttk.Label(root, text='Adivina Quien',font=("TkDefaultFont", 14))
title.place(x=540, y=50)
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
ressi = ttk.Button(root,text="Si",command=lambda: respuesta('cierto('))
resno = ttk.Button(root,text="No",command=lambda: respuesta('falso('))
label_pregunta = ttk.Label(root, text="")

initialize_gui(label1,animal_entry,begin_game)

root.mainloop()