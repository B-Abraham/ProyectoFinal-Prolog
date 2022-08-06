from json import load
from pyswip import Prolog
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk



prolog = Prolog()
prolog.consult("proyecto_final_grupo1.pl")

def query():  
    res = []  
    for soln in prolog.query("resuelve(adivina(ave8,X))."):
        res.append(soln["X"])
    return res

def respuesta(r):
    pass

def show_entry():
    label1.place(x=230, y=80)
    animal_entry.place(x=490, y=120)
    animal_entry.focus()
    begin_game.place(x=510, y=160)

def begin():
    adivinar = animal_entry.get()
    animal_entry.place_forget()
    begin_game.place_forget()
    label1.place_forget()

    query1.place(x=470, y=160)
    query2.place(x=570, y=160)
    res = query()
    test = ttk.Label(root,text=adivinar)
    test.place(x=490, y=120)
    test = ttk.Label(root,text=res)
    test.place(x=490, y=100)


def display_photo(foto):
    image_label = ttk.Label(root, image=foto, text='El animal en el que estabas pensando era este?', compound='top')
    image_label.place(x=400, y=250)

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
query1 = ttk.Button(root,text="Si",command=respuesta('si.'))
query2 = ttk.Button(root,text="No",command=respuesta('no.'))

show_entry()




root.mainloop()


