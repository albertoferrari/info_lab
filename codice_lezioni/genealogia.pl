padre(pippo,gino).
padre(luca,pippo).
padre(francesco,luca).
padre(pippo,manuela).
padre(luca,genoveffa).
padre(luca,giuseppina).

madre(giulia,gino).
madre(lina,pippo).
madre(gelda,luca).
madre(giulia,manuela).
madre(lina,genoveffa).
madre(franca,giuseppina).

genitore(X,Y) :- padre(X,Y).
genitore(X,Y) :- madre(X,Y).

antenato(X,Y) :- genitore(X,Y).
antenato(X,Y) :- genitore(X,Z), antenato(Z,Y).

fratello_sorella(X,Y) :-
padre(Z,X), padre(Z,Y), madre(W,X), madre(W,Y), X \= Y.
fratellastro_sorellastra(X,Y) :-
genitore(W,X), genitore(W,Y), X \= Y.
zio_zia(X,Y) :- genitore(Z,Y), fratello_sorella(X,Z).
