:-dynamic cierto/1.
:-dynamic falso/1.


% En este apartado es donde se guardan las caracteristicas que posee
% cada ave.

adivina(P,buho):-
    puede_volar(P),
    migra(P),
    tipo_de_alimentacion(P,carnivoro),
    color_del_pico(P,negro),
    color_del_plumaje(P,marron),
    tamano(P,mediano),
    tamano_del_pico(P,pequeno),
    nocturno(P).

adivina(P,flamenco):-
    puede_nadar(P),
    puede_volar(P),
    migra(P),
    puede_caminar(P),
    tipo_de_alimentacion(P,omnivoro),
    color_del_pico(P,amarillo),
    color_del_plumaje(P,rosado),
    tamano(P,grande),
    tamano_del_pico(P,grande).

adivina(P,ganso):-
    puede_nadar(P),
    puede_volar(P),
    migra(P),
    puede_caminar(P),
    tipo_de_alimentacion(P,omnivoro),
    color_del_pico(P,naranja),
    color_del_plumaje(P,blanco),
    tamano(P,mediano),
    tamano_del_pico(P,mediano).



adivina(P,gallo):-
    puede_caminar(gallo),
    tipo_de_alimentacion(P,omnivoro),
    color_del_pico(P,amarillo),
    color_del_plumaje(P,blanco),
    tamano(P,mediano),
    tamano_del_pico(P,pequeno).

adivina(P,aguila):-
    puede_volar(P),
    migra(P),
    puede_caminar(P),
    tipo_de_alimentacion(P,carnivoro),
    color_del_pico(P,amarillo),
    color_del_plumaje(P,marron),
    tamano(P,mediano),
    tamano_del_pico(P,mediano).

adivina(P,loro):-
    puede_volar(P),
    migra(P),
    puede_caminar(P),
    tipo_de_alimentacion(P,omnivoro),
    color_del_pico(P,blanco),
    color_del_plumaje(P,rojo),
    tamano(P,pequeno),
    tamano_del_pico(P,mediano).


adivina(P,tucan):-
    puede_volar(P),
    migra(P),
    tipo_de_alimentacion(P,herbivoro),
    color_del_pico(P,naranja),
    color_del_plumaje(P,negro),
    tamano(P,pequeno),
    tamano_del_pico(P,grande).

adivina(P,cisne_negro):-
    puede_nadar(P),
    puede_volar(P),
    migra(P),
    puede_caminar(P),
    tipo_de_alimentacion(P,herbivoro),
    color_del_pico(P,rojo),
    color_del_plumaje(P,negro),
    tamano(P,mediano),
    tamano_del_pico(P,mediano).

adivina(P,pinguino):-
    puede_nadar(P),
    migra(P),
    puede_caminar(P),
    tipo_de_alimentacion(P,carnivoro),
    color_del_pico(P,amarillo),
    color_del_plumaje(P,blanco_negro),
    tamano(P,mediano),
    tamano_del_pico(P,mediano),
    tiene_aletas(P).

adivina(P,avestruz):-
    puede_caminar(P),
    tipo_de_alimentacion(P,herbivoro),
    color_del_pico(P,amarillo),
    color_del_plumaje(P,negro),
    tamano(P,grande),
    tamano_del_pico(P,mediano).


visualiza_pregunta(A):-write(A), write('(si/no)? ').
pregunta(A,Resp):-visualiza_pregunta(A), read(Resp).

% En este apartado es donde se guarda tanto lo cierto como lo falso.
responde(si, A):-!,assertz(cierto(A)).
responde(no, A):-!,assertz(falso(A)).

%En este apartado se encuentran las preguntas por realizar.
preguntable(puede_nadar(_)).
preguntable(puede_volar(_)).
preguntable(migra(_)).
preguntable(puede_caminar(_)).
preguntable(tipo_de_alimentacion(_,_)).
preguntable(color_del_pico(_,_)).
preguntable(color_del_plumaje(_,_)).
preguntable(tamano(_,_)).
preguntable(tamano_del_pico(_,_)).
preguntable(nocturno(_)).
preguntable(tiene_aletas(_)).

% En este apartado es donde se ejecuta el programa.
resuelve(true):-!.
resuelve((A,B)):-!,resuelve(A), resuelve(B).
resuelve(A):-falso(A), !, fail.
resuelve(A):-cierto(A),!.
resuelve(A):-clause(A,B),resuelve(B).
%resuelve(A):-preguntable(A),pregunta(A,Resp),responde(Resp,A).

busca(A):- cierto(A),!.
busca(A):- falso(A).

preguntado(A):- cierto(A).
preguntado(A):- falso(A).
