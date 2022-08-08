:-dynamic cierto/1.
:-dynamic falso/1.


% En este apartado es donde se guardan las caracteristicas que posee
% cada ave.
adivina(P,buho):-
    tamano(P,pequeno),
    tamano_del_pico(P,pequeno),
    color_del_plumaje(P,marron),
    color_del_pico(P,negro),
    nocturno(P),
    alimentacion(P,carnivoro),
    puede_volar(P),
    migra(P).
adivina(P,ganso):-
    tamano(P,mediano),
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,blanco),
    color_del_pico(P,naranja),
    alimentacion(P,omnivoro),
    puede_nadar(P),
    puede_volar(P),
    puede_caminar(P),
    migra(P).
adivina(P,gallo):-
    tamano(P,pequeno),
    tamano_del_pico(P,pequeno),
    color_del_plumaje(P,blanco),
    color_del_pico(P,amarillo),
    alimentacion(P,omnivoro),
    puede_caminar(P).
adivina(P,aguila):-
    tamano(P,mediano),
    tamano_del_pico(P,grande),
    color_del_plumaje(P,marron),
    color_del_pico(P,amarillo),
    alimentacion(P,carnivoro),
    puede_volar(P),
    puede_caminar(P),
    migra(P).
adivina(P,flamenco):-
    tamano(P,grande),
    tamano_del_pico(P,grande),
    color_del_plumaje(P,rosado),
    color_del_pico(P,blanco_negro),
    alimentacion(P,omnivoro),
    puede_volar(P),
    puede_caminar(P),
    migra(P).
adivina(P,loro):-
    tamano(P,pequeno),
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,rojo),
    color_del_pico(P,blanco),
    alimentacion(P,omnivoro),
    puede_volar(P),
    puede_caminar(P),
    migra(P).
adivina(P,tucan):-
    tamano(P,pequeno),
    tamano_del_pico(P,grande),
    color_del_plumaje(P,negro),
    color_del_pico(P,naranja),
    alimentacion(P,herbivoro),
    puede_volar(P),
    migra(P).
adivina(P,cisne_negro):-
    tamano(P,mediano),
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,negro),
    color_del_pico(P,rojo),
    alimentacion(P,herbivoro),
    puede_nadar(P),
    puede_volar(P),
    puede_caminar(P),
    migra(P).
adivina(P,pinguino):-
    tamano(P,mediano),
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,blanco_negro),
    color_del_pico(P,amarillo),
    alimentacion(P,carnivoro),
    puede_nadar(P),
    puede_caminar(P),
    migra(P).
adivina(P,avestruz):-
    tamano(P,grande),
    tamano_del_pico(P,mediano),
    color_del_plumaje(P,negro),
    color_del_pico(P,amarillo),
    alimentacion(P,herbivoro),
    puede_caminar(P).

% En este apartado es donde se realiza las preguntas y se lee la
% respuesta
% visualiza_pregunta(A):-write(A), write('(si/no)? ').
% pregunta(A,Resp):-visualiza_pregunta(A), read(Resp).

% En este apartado es donde se guarda tanto lo cierto como lo falso.
responde(si, A):-!,assertz(cierto(A)).
responde(no, A):-!,assertz(falso(A)).

% En este apartado es donde se realizan las preguntas y estan ordenadas
% en relacion a la regla que menos se llama a la que mas se llama y
% entre las que mas se llaman se ordenan por la diversidad que posee el
% que tiene mayor diversidad primero y la que menos diversidad posee
% de ultima para asi poder adivinar con mayor rapidez la ave.
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
% resuelve(A):-preguntable(A),pregunta(A,Resp),responde(Resp,A).

busca(A):- cierto(A),!.
busca(A):- falso(A).