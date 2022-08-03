from pyswip import Prolog
import tkinter as tk
from tkinter import ttk


prolog = Prolog()

def query():
    prolog.consult("proyecto_final_grupo1.pl")
    for soln in prolog.query("resuelve(adivina(ave8,X))."):
        print(soln["X"])

root = tk.Tk()
root.title("Proyecto Final")
root.geometry('600x400+50+50')
query1 = ttk.Button(root,text="Ejecutar query",command=query)
query1.pack(ipadx=5, ipady=5, expand=True)

exit_button = ttk.Button(root, text='Salir', command=lambda: root.quit())
exit_button.pack(ipadx=5, ipady=5, expand=True)
root.mainloop()





