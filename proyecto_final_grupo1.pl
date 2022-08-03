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
    migran(P).
adivina(P,gallina):-
    tamano(P,mediano),
    tamano_pico(P,mediano),
    color_plumaje(P,blanco),
    color_pico(P,amarillo),
    alimentacion(P,omnivoros),
    puede_correr(P).
adivina(P,aguila):-
    tamano(P,grande),
    tamano_pico(P,mediano),
    color_plumaje(P,blanco),
    color_pico(P,amarillo),
    carnivoro(P),
    puede_volar(P),
    migran(P).
adivina(P,flamenco):-
    tamano(P,mediano),
    tamano_pico(P,mediano),
    color_plumaje(P,blanco),
    color_pico(P,amarillo),
    carnivoro(P).
adivina(P,loro):-
    tamano(P,mediano),
    tamano_pico(P,mediano),
    color_plumaje(P,blanco),
    color_pico(P,amarillo).

% adivina(P,tucan).
% adivina(P,cisne_negro).
% adivina(P,pinguino).
% adivina(P,avestruz).

visualiza_pregunta(A):-write(A), write('(si/no)? ').
pregunta(A,Resp):-visualiza_pregunta(A), read(Resp).

responde(si, A):-!,assertz(cierto(A)).
responde(no, A):-!,assertz(falso(A)), fail.

preguntable(tamano(_,_)).
preguntable(tamano_pico(_,_)).
preguntable(color_plumaje(_,_)).
preguntable(color_pico(_,_)).
preguntable(nocturno(_)).
preguntable(alimentacion(_,_)).
preguntable(puede_nadar(_)).
preguntable(puede_volar(_)).
preguntable(puede_correr(_)).
preguntable(migran(_)).

resuelve(true):-!.
resuelve((A,B)):-!,resuelve(A), resuelve(B).
resuelve(A):-falso(A), !, fail.
resuelve(A):-cierto(A),!.
resuelve(A):-clause(A,B),resuelve(B).
resuelve(A):-preguntable(A),pregunta(A,Resp),responde(Resp,A).

imagen(buho,'/img/buho.jpg').