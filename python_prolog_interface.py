from pyswip import Prolog
import re

def get_clauses(p,nombre):
    clausulas = []
    
    for i in p.query("clause(adivina("+nombre+",X),Y)."):
        cl = i['Y'][2:]
        cl = re.sub(", ", ", ,(", cl)
        cl = re.sub(", ", ",", cl)
        cl = re.sub(",,\(", ",", cl)
        cl = re.sub(",,\(", ",", cl)
        cl = re.sub("\),", "), ", cl)
        cl = re.sub("\)+", ")", cl)
        clausulas.append(cl.split(", "))
    print(clausulas)
    return clausulas