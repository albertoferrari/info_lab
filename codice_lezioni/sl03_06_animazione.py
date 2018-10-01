'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 animazione orizzontale
'''

import g2d

def update():
	''' 
	modifica il canvas
	'''
	global x							# posizione pallina (globale)
	g2d.fill_canvas((255, 255, 255))	# background bianco   
	g2d.draw_image(image, (x, 50))		# disegna immagine posizione(x,y)
	x = (x + 5) % 320          			# modifica ascissa immagine

g2d.init_canvas((320, 240))				# inizializzazione (320x200)
image = g2d.load_image("ball.png")		# caricamento immagine
x = 50									# posizione iniziale pallina

g2d.main_loop(update, 1000 // 30)	# richiama funzione 30 volte al secondo
