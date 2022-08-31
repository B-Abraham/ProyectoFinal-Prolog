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

        if(bool):
            if(clause in cl):
                for j in cl:
                    if(j not in clausulas and j != clause):
                        clausulas.append(j)
        else:
            if(clause not in cl):
                for j in cl:
                    if(j not in clausulas):
                        clausulas.append(j)

    for i in clausulas:        
        if(list(p.query("clause("+i+",X)"))):
            ind = clausulas.index(i)
            clausulas.pop(ind)
            for j in list(p.query("clause("+i+",X)")):
                cl2 = j['X'][2:]
                cl2 = re.sub(", ", ", ,(", cl2)
                cl2 = re.sub(", ", ",", cl2)
                cl2 = re.sub(",,\(", ",", cl2)
                cl2 = re.sub(",,\(", ",", cl2)
                cl2 = re.sub("\),", "), ", cl2)
                cl2 = re.sub("\)+", ")", cl2)
                cl2 = cl2.split(", ")
                for k in cl2:
                    clausulas.insert(ind,k)
    
    clausulas = filter_asserted(p,clausulas)
    return clausulas

def filter_asserted(p,preguntas):
    res = []
    for i in preguntas:
        print("busca("+i+")")
        print(p.query("busca("+i+")"))
        if(bool(list(p.query("busca("+i+")"))) == False):
            res.append(i)
    return res


