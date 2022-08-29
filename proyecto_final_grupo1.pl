:-dynamic cierto/1.
:-dynamic falso/1.


% En este apartado es donde se guardan las caracteristicas que posee
% cada ave.


zancuda(P):- tamano(P,grande), tamano_pico(P,grande).

pajaro(P):- tamano(P,pequeño).

corredora(P):- puede_caminar(P).

rapaz(P):- tipo_alimentacion(P,carnivoro),tamano_pico(P,mediano),tamano(P,mediano).
rapaz(P):- tipo_alimentacion(P,carnivoro),tamano_pico(P,grande),tamano(P,mediano).

anseriforme(P):- puede_caminar(P),puede_nadar(P),tamano(P,mediano).

adivina(P,buho):-
    color_del_plumaje(P,marron),
    color_del_pico(P,negro),
    nocturno(P),
    puede_volar(P),
    migra(P),
    rapaz(P).
adivina(P,ganso):-
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,blanco),
    color_del_pico(P,naranja),
    alimentacion(P,omnivoro),
    puede_volar(P),
    migra(P),
    anseriforme(P).
adivina(P,gallo):-
    tamano(P,mediano),
    tamano_del_pico(P,pequeno),
    color_del_plumaje(P,blanco),
    color_del_pico(P,amarillo),
    alimentacion(P,omnivoro),
    corredora(P).
adivina(P,aguila):-
    color_del_plumaje(P,marron),
    color_del_pico(P,amarillo),
    puede_volar(P),
    puede_caminar(P),
    migra(P),
    rapaz(P).
adivina(P,flamenco):-
    color_del_plumaje(P,rosado),
    color_del_pico(P,blanco_negro),
    alimentacion(P,omnivoro),
    puede_volar(P),
    puede_caminar(P),
    migra(P),
    zancuda(P).
adivina(P,loro):-
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,rojo),
    color_del_pico(P,blanco),
    alimentacion(P,omnivoro),
    puede_volar(P),
    puede_caminar(P),
    migra(P),
    pajaro(P).
adivina(P,tucan):-
    tamano_del_pico(P,grande),
    color_del_plumaje(P,negro),
    color_del_pico(P,naranja),
    alimentacion(P,herbivoro),
    puede_volar(P),
    migra(P),
    pajaro(P).
adivina(P,cisne_negro):-
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,negro),
    color_del_pico(P,rojo),
    alimentacion(P,herbivoro),
    puede_volar(P),
    migra(P),
    anseriforme(P).
adivina(P,pinguino):-
    tamano(P,mediano),
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,blanco_negro),
    color_del_pico(P,amarillo),
    alimentacion(P,carnivoro),
    puede_nadar(P),
    migra(P),
    corredora(P).
adivina(P,avestruz):-
    tamano(P,grande),
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,negro),
    color_del_pico(P,amarillo),
    alimentacion(P,herbivoro),
    corredora(P).

visualiza_pregunta(A):-write(A), write('(si/no)? ').
pregunta(A,Resp):-visualiza_pregunta(A), read(Resp).

% En este apartado es donde se guarda tanto lo cierto como lo falso.
responde(si, A):-!,assertz(cierto(A)).
responde(no, A):-!,assertz(falso(A)), fail.

% En este apartado es donde se inicializan las preguntas y estan
% ordenadas en relacion a la regla que menos se llama a la que mas se
% llama y entre las que mas se llaman se ordenan por la diversidad que
% posee el que tiene mayor diversidad primero y la que menos diversidad
% posee de ultima para asi poder adivinar con mayor rapidez la ave.
preguntable(nocturno(_)).
preguntable(puede_nadar(_)).
preguntable(puede_volar(_)).
preguntable(puede_caminar(_)).
preguntable(migra(_)).
preguntable(color_del_plumaje(_,_)).
preguntable(color_del_pico(_,_)).
preguntable(alimentacion(_,_)).
preguntable(tamano(_,_)).
preguntable(tamano_del_pico(_,_)).

% En este apartado es donde se ejecuta el programa.
resuelve(true):-!.
resuelve((A,B)):-!,resuelve(A), resuelve(B).
resuelve(A):-falso(A), !, fail.
resuelve(A):-cierto(A),!.
resuelve(A):-clause(A,B),resuelve(B).
resuelve(A):-preguntable(A),pregunta(A,Resp),responde(Resp,A).

busca(A):- cierto(A),!.
busca(A):- falso(A).
