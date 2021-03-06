'''
quadrati casuali
- chiede all'utente un numero n
- disegna n quadrati
	- tutti con lato di 100 pixel
	- ciascuno in posizione casuale
	- ciascuno con un colore casuale
'''

import g2d
from random import randint

dim = 600        # dimensione canvas
lato = 100       # lato del quadrato
n = int(input("numero quadrati: "))

g2d.init_canvas((dim, dim))

i = 0
while i < n:
    # coordinate
    x = randint(0,dim-lato)   
    y = randint(0,dim-lato) 
    # colore
    colore = randint(0,255), randint(0,255), randint(0,255)
    # disegno
    g2d.draw_rect(colore, (x, y, lato, lato))
    i += 1

g2d.main_loop()
