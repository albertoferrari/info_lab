'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 lista palline
'''
import g2d
from sl04_01_Ball import Ball, ARENA_W, ARENA_H

class BallArena:  # ...
	def __init__(self):
		self._balls = []
	def add(self, b: Ball):
		self._balls.append(b)
	def move_all(self):
		for b in self._balls:
			b.move()
			g2d.fill_rect(b.position())

def update():
	g2d.clear_canvas()  # BG
	arena.move_all()

arena = BallArena()
arena.add(Ball(40, 80))
arena.add(Ball(80, 40)) # ...
g2d.init_canvas((ARENA_W, ARENA_H))
g2d.main_loop(update)  # Millis
