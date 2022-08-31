

def initialize_gui(label,entry,button):
    label.place(x=150, y=100)
    entry.place(x=530, y=140)
    entry.focus()
    button.place(x=550, y=180)
    

def begin_gui(animal_entry,begin_game,label1,ressi,resno):
    animal_entry.place_forget()
    begin_game.place_forget()
    label1.place_forget()
    ressi.place(x=510, y=180)
    resno.place(x=610, y=180)

def display_pregunta(pregunta,label_pregunta):
    texto = parsear_pregunta(pregunta)
    label_pregunta.config(text = texto,font=("TkDefaultFont", 14))
    label_pregunta.place(x=400, y=120)

def visualizar_fin(ressi,resno,assertsi,assertno,label_pregunta,image_label,resultado,fotos,puntaje):
    display_foto(image_label,resultado,fotos,puntaje)
    ressi.place_forget()
    resno.place_forget()
    label_pregunta.config(text = "Quieres jugar de nuevo?")
    label_pregunta.place(x=510, y=350)
    assertsi.place(x=510, y=400)
    assertno.place(x=610, y=400)

def restart(label,entry,button,denuevosi,denuevono,image_label,label_pregunta):
    denuevosi.place_forget()
    denuevono.place_forget()
    image_label.place_forget()
    label_pregunta.place_forget()
    initialize_gui(label,entry,button)

def display_foto(image_label,resultado,fotos,puntaje):
    dictfotos = {"aguila":0,
                "avestruz":1,
                "buho":2,
                "cisne_negro":3,
                "flamenco":4,
                "gallo":5,
                "ganso":6,
                "loro":7,
                "pinguino":8,
                "tucan":9,
                }
    if(resultado != []):
        if(dictfotos[resultado[0]['X']]):
            image_label.config(image=fotos[dictfotos[resultado[0]['X']]])
            image_label.config(text='El animal en el que estabas pensando era un '+resultado[0]['X']+', y tu puntaje fue de: '+puntaje)
            
            image_label.place(x=300, y=100)
    else:
        image_label.config(image=None)
        image_label.config(text='El animal en el que estabas pensando no lo tengo registrado...')
        image_label.place(x=300, y=100)

def parsear_pregunta(pregunta):
    if(pregunta.find("nocturno") != -1):
        return "¿El animal en que estas pensando es nocturno?"
    elif(pregunta.find("puede_nadar") != -1):
        return "¿El animal en que estas pensando puede nadar?"
    elif(pregunta.find("tiene_aletas") != -1):
        return "¿El animal en que estas pensando tiene aletas?"
    elif(pregunta.find("puede_volar") != -1):
        return "¿El animal en que estas pensando puede volar?"
    elif(pregunta.find("puede_caminar") != -1):
        return "¿El animal en que estas pensando puede caminar?"
    elif(pregunta.find("migra") != -1):
        return "¿El animal en que estas pensando suele migrar?"
    elif(pregunta.find("alimentacion") != -1):
        if(pregunta.find("carnivoro") != -1):
            return "¿El animal en que estas pensando es carnivoro?"
        elif(pregunta.find("herbivoro") != -1):
            return "¿El animal en que estas pensando es herbivoro?"
        else:
            return "¿El animal en que estas pensando es omnivoro?"
    elif(pregunta.find("tamano(") != -1):
        tamano = pregunta.split(",")[1][:-1]
        return "¿El animal en que estas pensando es de tamaño "+tamano+"?"
    elif(pregunta.find("tamano_del_pico") != -1):
        tamano = pregunta.split(",")[1][:-1]
        return "¿El animal en que estas pensando tiene un pico "+tamano+"?"
    elif(pregunta.find("color_del_plumaje") != -1):
        color = pregunta.split(",")[1][:-1]
        return "¿El animal en que estas pensando tiene plumaje de color "+color+"?"
    elif(pregunta.find("color_del_pico") != -1):
        color = pregunta.split(",")[1][:-1]
        return "¿El animal en que estas pensando tiene pico de color "+color+"?"