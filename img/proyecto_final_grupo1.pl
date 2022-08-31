:-dynamic cierto/1.
:-dynamic falso/1.


% En este apartado es donde se guardan las caracteristicas que posee
% cada ave.

zancuda(P):- tamano(P,grande),tamano_pico(P,grande),puede_caminar(P), puede_volar(P).

rapaz(P):- tipo_de_alimentacion(P,carnivoro),tamano(P,mediano),puede_volar(P).

anseriforme(P):- puede_caminar(P),puede_nadar(P),tamano(P,mediano).


adivina(P,buho):-
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,marron),
    color_del_pico(P,negro),
    nocturno(P),
    migra(P),
    rapaz(P).

adivina(P,ganso):-
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,blanco),
    color_del_pico(P,naranja),
    tipo_de_alimentacion(P,omnivoro),
    puede_volar(P),
    migra(P),
    anseriforme(P).

adivina(P,flamenco):-
    color_del_plumaje(P,rosado),
    color_del_pico(P,amarillo),
    tipo_de_alimentacion(P,omnivoro),
    migra(P),
    puede_nadar(P),
    zancuda(P).

adivina(P,gallo):-
    tamano(P,mediano),
    tamano_del_pico(P,pequeno),
    color_del_plumaje(P,blanco),
    color_del_pico(P,amarillo),
    tipo_de_alimentacion(P,omnivoro),
    puede_caminar(gallo).

adivina(P,aguila):-
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,marron),
    color_del_pico(P,amarillo),
    puede_caminar(P),
    migra(P),
    rapaz(P).

adivina(P,loro):-
    tamano(P,pequeno),
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,rojo),
    color_del_pico(P,blanco),
    tipo_de_alimentacion(P,omnivoro),
    puede_volar(P),
    puede_caminar(P),
    migra(P).


adivina(P,tucan):-
    tamano(P,pequeno),
    tamano_del_pico(P,grande),
    color_del_plumaje(P,negro),
    color_del_pico(P,naranja),
    tipo_de_alimentacion(P,herbivoro),
    puede_volar(P),
    migra(P).

adivina(P,cisne_negro):-
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,negro),
    color_del_pico(P,rojo),
    tipo_de_alimentacion(P,herbivoro),
    puede_volar(P),
    migra(P),
    anseriforme(P).

adivina(P,pinguino):-
    tamano(P,mediano),
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,blanco_negro),
    color_del_pico(P,amarillo),
    tipo_de_alimentacion(P,carnivoro),
    puede_nadar(P),
    migra(P),
    puede_caminar(P).

adivina(P,avestruz):-
    tamano(P,grande),
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,negro),
    color_del_pico(P,amarillo),
    tipo_de_alimentacion(P,herbivoro),
    puede_caminar(P).


visualiza_pregunta(A):-write(A), write('(si/no)? ').
pregunta(A,Resp):-visualiza_pregunta(A), read(Resp).

% En este apartado es donde se guarda tanto lo cierto como lo falso.
responde(si, A):-!,assertz(cierto(A)).
responde(no, A):-!,assertz(falso(A)), fail.

%En este apartado se encuentran las preguntas por realizar.
preguntable(nocturno(_)).
preguntable(puede_nadar(_)).
preguntable(puede_volar(_)).
preguntable(puede_caminar(_)).
preguntable(migra(_)).
preguntable(color_del_plumaje(_,_)).
preguntable(color_del_pico(_,_)).
preguntable(tipo_de_alimentacion(_,_)).
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
