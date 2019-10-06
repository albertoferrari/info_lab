'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 lista palline
'''
import g2d
from sl04_01_Ball import Ball, ARENA_W, ARENA_H

def update():
	g2d.clear_canvas()
	for b in balls:
		b.move()
		g2d.fill_rect(b.position())

balls = [Ball(40, 80), Ball(80, 40), Ball(120, 120)]
g2d.init_canvas((ARENA_W, ARENA_H))
g2d.main_loop(update) 
