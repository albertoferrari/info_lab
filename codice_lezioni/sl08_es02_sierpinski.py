'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 quadrati di sierpinski
'''

import g2d

def sierpinski(x0, y0, w0, h0, livello):
	w1 = w0 // 3	#larghezza quadrato da disegnare
	h1 = h0 // 3	#altezza quadrato da disegnare
	#print(x0, y0, w0, h0, livello)			#debug
	if livello == 0 or w1 == 0 or h1 == 0:		#terminazione
		return
	for y in range(3):
		for x in range(3):
			x1 = x0 + x * w1		#calcolo posizione
			y1 = y0 + y * h1
			if x == 1 and y == 1:		#disegno quadrato centrale
				g2d.fill_rect((x1, y1, w1, h1))
			else:
				sierpinski(x1, y1, w1, h1, livello - 1) #altri quadrati

if __name__ == '__main__':
	livello = int(input('livello? '))  ## -1 = infinito (si ferma dim. minima)
	lato = 600

	g2d.init_canvas((lato, lato))
	g2d.clear_canvas()
	g2d.set_color((0,0,0))
	sierpinski(0, 0, lato, lato, livello)

	g2d.main_loop()




