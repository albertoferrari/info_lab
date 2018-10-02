'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio di utilizzo di una classe
'''

import g2d
from sl04_01_Ball import Ball, ARENA_W, ARENA_H

def update():
    g2d.fill_canvas((255, 255, 255))  # BG
    b1.move()
    b2.move()
    g2d.draw_rect((0, 0, 255), b1.position())  # FG
    g2d.draw_rect((255, 0, 0), b2.position())  # FG
    
b1 = Ball(40, 80)
b2 = Ball(80, 40, 12, 23)

def main():
	g2d.init_canvas((ARENA_W, ARENA_H))
	g2d.main_loop(update, 1000 // 30)  # Millis

if __name__ == "__main__":	# solo se è il modulo principale
	main()
