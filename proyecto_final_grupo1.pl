:-dynamic cierto/1.
:-dynamic falso/1.

% elegir cantidad de intentos, si se acaban, se termina la ronda

adivina(P,buho):-
    tamano(P,pequeno),
    tamano_pico(P,pequeno),
    color_plumaje(P,marron),
    color_pico(P,negro),
    nocturno(P),
    alimentacion(P,rapina),
    puede_volar(P),
    migran(P).
adivina(P,ganso):-
    tamano(P,mediano),
    tamano_pico(P,mediano),
    color_plumaje(P,blanco),
    color_pico(P,naranja),
    alimentacion(P,omnivoros),
    puede_nadar(P),
    puede_volar(P),
    puede_caminar(P),
    migran(P).
adivina(P,gallo):-
    tamano(P,pequeno),
    tamano_pico(P,pequeno),
    color_plumaje(P,blanco),
    color_pico(P,amarillo),
    alimentacion(P,omnivoros),
    puede_caminar(P).
adivina(P,aguila):-
    tamano(P,mediano),
    tamano_pico(P,grande),
    color_plumaje(P,marron),
    color_pico(P,amarillo),
    alimentacion(P,carnivoro),
    puede_volar(P),
    migran(P).
adivina(P,flamenco):-
    tamano(P,grande),
    tamano_pico(P,grande),
    color_plumaje(P,rosado),
    color_pico(P,blanco_negro),
    alimentacion(P,omnivoro),
    puede_volar(P),
    puede_caminar(P),
    migran(P).
adivina(P,loro):-
    tamano(P,pequeno),
    tamano_pico(P,mediano),
    color_plumaje(P,rojo),
    color_pico(P,blanco),
    alimentacion(P,omnivoro),
    puede_volar(P),
    puede_caminar(P),
    migran(P).
adivina(P,tucan):-
    tamano(P,pequeno),
    tamano_pico(P,grande),
    color_plumaje(P,negro),
    color_pico(P,naranja),
    alimentacion(P,herbivoros),
    puede_volar(P),
    migran(P).
adivina(P,cisne_negro):-
    tamano(P,mediano),
    tamano_pico(P,mediano),
    color_plumaje(P,negro),
    color_pico(P,rojo),
    alimentacion(P,herbivoro),
    puede_nadar(P),
    puede_volar(P),
    puede_caminar(P),
    migran(P).
adivina(P,pinguino):-
    tamano(P,mediano),
    tamano_pico(P,mediano),
    color_plumaje(P,blanco_negro),
    color_pico(P,amarillo),
    alimentacion(P,carnivoro),
    puede_nadar(P),
    puede_caminar(P),
    migran(P).
adivina(P,avestruz):-
    tamano(P,grande),
    tamano_pico(P,mediano),
    color_plumaje(P,negro),
    color_pico(P,amarillo),
    alimentacion(P,herbivoro),
    puede_caminar(P).

visualiza_pregunta(A):-write(A), write('(si/no)? ').
pregunta(A,Resp):-visualiza_pregunta(A), read(Resp).

responde(si, A):-!,assertz(cierto(A)).
responde(no, A):-!,assertz(falso(A)), fail.

preguntable(nocturno(_)).
preguntable(puede_nadar(_)).
preguntable(puede_volar(_)).
preguntable(puede_caminar(_)).
preguntable(migran(_)).
preguntable(tamano(_,_)).
preguntable(tamano_pico(_,_)).
preguntable(color_plumaje(_,_)).
preguntable(color_pico(_,_)).
preguntable(alimentacion(_,_)).

resuelve(true):-!.
resuelve((A,B)):-!,resuelve(A), resuelve(B).
resuelve(A):-falso(A), !, fail.
resuelve(A):-cierto(A),!.
resuelve(A):-clause(A,B),resuelve(B).
resuelve(A):-preguntable(A),pregunta(A,Resp),responde(Resp,A).