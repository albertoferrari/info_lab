'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 pallina che si muove a serpentina
'''

import g2d

def update():
	''' 
	modifica il canvas
	'''
	global x,dx,y						# posizione pallina (globale)
	if y>240:
		x = y = 0						# ritorno posizione iniziale
	g2d.clear_canvas()					# background vuoto   
	g2d.draw_image(image, (x, y))		# disegna immagine posizione(x,y)
	x = x + dx	 						# modifica ascissa immagine
	if x<0 or x>(320-largImm):
		dx = -dx						# inversione orizzontale
		y = y + dy						# discesa

g2d.init_canvas((320, 240))				# inizializzazione (320x200)
image = g2d.load_image("ball.png")		# caricamento immagine
x = y = 0								# posizione iniziale pallina
dx = dy = 5								# spostamento verticale pallina
largImm = 20							# larghezza (e altezza immagine)
g2d.main_loop(update, 1000 // 10)		# richiama funzione 100 volte al secondo
