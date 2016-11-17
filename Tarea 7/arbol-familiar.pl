% ag.pl
% Hechos (conocimiento)
hombre(luis).
hombre(roberto).
hombre(paco).
hombre(pedro).
hombre(juan).
mujer(andrea).
mujer(diana).
mujer(maria).
mujer(rodriga).
mujer(luz).
progenitor(pedro, maria).
progenitor(luz, maria).
progenitor(pedro, paco).
progenitor(luz, paco).
progenitor(andrea, pedro).
progenitor(luis, pedro).
progenitor(andrea, rodriga).
progenitor(luis, rodriga).
progenitor(roberto, luz).
progenitor(diana, luz).
progenitor(roberto, juan).
progenitor(diana, juan).

% madre
madre(X,Y):-mujer(X),progenitor(X,Y).

%padre
padre(X,Y):-hombre(X),progenitor(X,Y).

% hija
hija(X,Y):-mujer(X),progenitor(Y,X).

%hijo
hijo(X,Y):-hombre(X),progenitor(Y,X).

% abuelo
abuelo(X,Y):-hombre(X),progenitor(X,Z),progenitor(Z,Y).

% abuela
abuela(X,Y):-mujer(X),progenitor(X,Z),progenitor(Z,Y).

%Hermano
% si tienen la misma madre son hermanos y es hombre es su hermano
hermano(X,Y):-hombre(X),madre(Z,Y),madre(C,X),Z=C.

%Hermana
% Si tienen la misma madre y es mujer es su hermana
hermana(X,Y):-mujer(X),madre(Z,Y),madre(C,X),Z=C.

%Tia
tia(X,Y):-mujer(X),progenitor(Z,Y),hermana(X,Z),X\=Z.

%Tio
tio(X,Y):-hombre(X),progenitor(Z,Y),hermano(X,Z),X\=Z.

%Primo
primo(X,Y):-tio(A,Y);tia(A,Y),hijo(A,X).

%Prima
primo(X,Y):-tio(A,Y);tia(A,Y),hija(A,X).