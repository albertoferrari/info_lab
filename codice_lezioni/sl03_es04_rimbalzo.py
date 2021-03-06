'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 movimento orizzontale con rimbalzo
'''

import g2d

def update():
	''' 
	modifica il canvas
	'''
	global x,dx							# posizione pallina (globale)
	g2d.clear_canvas()					# pulizia background   
	g2d.draw_image(image, (x, 50))		# disegna immagine posizione(x,y)
	x = x + dx	 						# modifica ascissa immagine
	largImm = 20						# larghezza (e altezza immagine)
	if x<0 or x>(320-largImm):
		dx = -dx
		x = x + dx


g2d.init_canvas((320, 240))				# inizializzazione (320x200)
image = g2d.load_image("ball.png")		# caricamento immagine
x = 0									# posizione iniziale pallina
dx = 5								# spostamento orizzontale pallina
g2d.main_loop(update, 1000 // 30)	# richiama funzione 30 volte al secondo
