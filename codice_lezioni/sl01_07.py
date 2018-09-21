'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 orologio classico
 disegnare 12 tacche a raggiera, come in un orologio classico
 miglioramento: disegnare anche le tacche dei minuti, più piccole
 (usare math.sin e math.cos per determinare le posizioni in cui disegnare)
'''

import g2d
from random import randint
from math import sin,cos,pi

dim = 600           			# dimensione canvas
colore = 0,0,0					# colore prime tacche
centro = dim/2					# centro dell'orologio
r = 100							# raggio interno tacche
l1 = 10							# lunghezza prime tacche
l2 = 5							# lunghezza tacche minuti

g2d.init_canvas((dim, dim))

angolo = 0
while angolo < 360:
    # coordinate 
    x = centro + r*sin(angolo*pi/180)   
    y = centro + r*cos(angolo*pi/180)
    x2 = centro + (r+l1)*sin(angolo*pi/180)  
    y2 = centro + (r+l1)*cos(angolo*pi/180)
    # disegno
    g2d.draw_line(colore,(x,y),(x2,y2))
    angolo = angolo + 30

colore = 255,0,0				# colore seconde tacche
angolo = 0
while angolo < 360:
    # coordinate 
    x = centro + r*sin(angolo*pi/180)   
    y = centro + r*cos(angolo*pi/180)
    x2 = centro + (r+l2)*sin(angolo*pi/180)  
    y2 = centro + (r+l2)*cos(angolo*pi/180)
    # disegno
    if angolo%30 != 0:			# non sovrascrive tacche precedenti
        g2d.draw_line(colore,(x,y),(x2,y2))
    angolo = angolo + 6

g2d.main_loop()
