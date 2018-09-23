'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 eventi tastiera
'''

import g2d

x, dx = 50, 5						#posizione iniziale e step
image = g2d.load_image("ball.png")

def update():
	global x							# posizione pallina (globale)
	g2d.fill_canvas((255, 255, 255))	# background bianco   
	g2d.draw_image(image, (x, 50))		# disegna immagine posizione(x,y)
	x = (x + dx) % 320					# modifica ascissa immagine


def keydown(code):
	global dx
	if code == "Space":					# barra spaziatrice
		dx = -dx						# inverte direzione orizzontale

def keyup(code):
	pass								# nessun codice eseguito

def main():
	g2d.init_canvas((320, 240))				# inizializzazione (320x200)
	image = g2d.load_image("ball.png")		# caricamento immagine
	g2d.handle_keyboard(keydown, keyup)		# gestione eventi
	g2d.main_loop(update, 1000 // 30)	# richiama funzione 30 volte al secondo

main()
