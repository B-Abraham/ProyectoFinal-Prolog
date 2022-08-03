from pyswip import Prolog

prolog = Prolog()
prolog.consult("proyecto_final_grupo1.pl")

for soln in prolog.query("resuelve(adivina(ave8,X))."):
    print(soln["X"])