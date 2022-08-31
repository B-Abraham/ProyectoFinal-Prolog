from pyswip import Prolog
import re

def format_clauses(p,nombre):
    clausulas = []
    
    for i in p.query("clause(adivina("+nombre+",X),Y)."):
        cl = i['Y'][2:]
        cl = re.sub(", ", ", ,(", cl)
        cl = re.sub(", ", ",", cl)
        cl = re.sub(",,\(", ",", cl)
        cl = re.sub(",,\(", ",", cl)
        cl = re.sub("\),", "), ", cl)
        cl = re.sub("\)+", ")", cl)
        for j in cl.split(", "):
            if j not in clausulas:
                clausulas.append(j)
    return clausulas

def filter_clauses(p,nombre,clause,bool):
    clausulas = []
    
    for i in p.query("clause(adivina("+nombre+",X),Y)."):
        cl = i['Y'][2:]
        cl = re.sub(", ", ", ,(", cl)
        cl = re.sub(", ", ",", cl)
        cl = re.sub(",,\(", ",", cl)
        cl = re.sub(",,\(", ",", cl)
        cl = re.sub("\),", "), ", cl)
        cl = re.sub("\)+", ")", cl)
        cl = cl.split(", ")
        print("cl")
        print(cl)
        print(" ")
        if(clause not in cl):
            for j in cl:
                if j not in clausulas:
                    print(j)
                    clausulas.append(j)
    return clausulas