import time
from pyswip import Prolog
import tkinter as tk
from tkinter import Frame, ttk
from PIL import Image, ImageTk

from GUI import *
from prolog_parser import *


prolog = Prolog()
prolog.consult("proyecto_final_grupo1.pl")
preguntas = []
adivinado = None
puntaje = 0

# Se encarga de la inicializacion del juego, una vez digitado el nombre en el prompt
def begin():
    global adivinado
    global preguntas
    global puntaje
    puntaje = 0

    begin_gui(animal_entry,begin_game,label1,ressi,resno)
    adivinado = animal_entry.get()
    preguntas = format_clauses(prolog,adivinado)
    display_pregunta(preguntas[0],label_pregunta)

# Se encarga de procesar cada pregunta una vez que se responde, y de mostrar la siguiente pregunta
def respuesta(r):
    global preguntas
    global adivinado
    global puntaje
    puntaje = puntaje + 1

    if(r == True):
        prolog.assertz("cierto("+preguntas[0]+")")
    else:
        prolog.assertz("falso("+preguntas[0]+")")
    
    resultado = list(prolog.query("resuelve(adivina("+adivinado+",X))"))
    if(bool(resultado)):
        visualizar_fin(ressi,resno,denuevosi,denuevono,label_pregunta,image_label,resultado,fotos,puntaje.__str__())
    else:
        preguntas = filter_clauses(prolog,adivinado,preguntas[0],r)
        display_pregunta(preguntas[0],label_pregunta)

# Root o raiz de la interfaz grafica (tkinter)
root = tk.Tk()
root.title("Proyecto Final")
root.geometry('1280x720')
root.config(bg="lightgray")

#Widgets estaticos
left_frame = Frame(root, width=1260, height=700)
left_frame.place(x=10,y=10)
title = ttk.Label(root, text='Adivina Quien',font=("TkDefaultFont", 18))
title.place(x=530, y=50)
exit_button = ttk.Button(root, text='Salir', command=lambda: root.quit())
exit_button.place(x=1150, y=650)

#Fotos
fotos = []
fotos.append(Image.open('./img/aguila.png'))
fotos[0] = ImageTk.PhotoImage(fotos[0].resize((200,200)))
fotos.append(Image.open('./img/avestruz.png'))
fotos[1] = ImageTk.PhotoImage(fotos[1].resize((200,200)))
fotos.append(Image.open('./img/buho.png'))
fotos[2] = ImageTk.PhotoImage(fotos[2].resize((200,200)))
fotos.append(Image.open('./img/cisne_negro.png'))
fotos[3] = ImageTk.PhotoImage(fotos[3].resize((200,200)))
fotos.append(Image.open('./img/flamenco.png'))
fotos[4] = ImageTk.PhotoImage(fotos[4].resize((200,200)))
fotos.append(Image.open('./img/gallo.png'))
fotos[5] = ImageTk.PhotoImage(fotos[5].resize((200,200)))
fotos.append(Image.open('./img/ganso.png'))
fotos[6] = ImageTk.PhotoImage(fotos[6].resize((200,200)))
fotos.append(Image.open('./img/loro.png'))
fotos[7] = ImageTk.PhotoImage(fotos[7].resize((200,200)))
fotos.append(Image.open('./img/pinguino.png'))
fotos[8] = ImageTk.PhotoImage(fotos[8].resize((200,200)))
fotos.append(Image.open('./img/tucan.png'))
fotos[9] = ImageTk.PhotoImage(fotos[9].resize((200,200)))

#Widgets utilizados durante la ejecucion del juego
label1 = ttk.Label(root, text='Escriba el nombre del animal que la computadora intentará adivinar (no se preocupe, esta no sabrá lo que escribirá):',font=("TkDefaultFont", 14))
animal = tk.StringVar()
animal_entry = ttk.Entry(root, textvariable=animal)
begin_game = ttk.Button(root,text="Comenzar juego",command=begin)
ressi = ttk.Button(root,text="Si",command=lambda: respuesta(True))
resno = ttk.Button(root,text="No",command=lambda: respuesta(False))
label_pregunta = ttk.Label(root, text="",font=("TkDefaultFont", 14))
image_label = ttk.Label(root, text='', compound='top',font=("TkDefaultFont", 14))
denuevosi = ttk.Button(root,text="Si",command=lambda: restart(label1,animal_entry,begin_game,denuevosi,denuevono,image_label,label_pregunta))
denuevono = ttk.Button(root,text="No",command=lambda: root.quit())

initialize_gui(label1,animal_entry,begin_game)

root.mainloop()