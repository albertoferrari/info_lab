'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 logica di gioco
'''

import g2d
from sl07_ball_ghost_turtle import Ball, Ghost, Turtle
from sl07_actor import Arena

arena = Arena(320, 240)
b1 = Ball(arena, 40, 80)
b2 = Ball(arena, 80, 40)
g = Ghost(arena, 120, 80)
turtle = Turtle(arena, 80, 80)
sprites = g2d.load_image("sprites.png")


def update():
	if g2d.key_pressed("ArrowUp"):
		turtle.go_up()
	elif g2d.key_pressed("ArrowRight"):
		turtle.go_right()
	elif g2d.key_pressed("ArrowDown"):
		turtle.go_down()
	elif g2d.key_pressed("ArrowLeft"):
		turtle.go_left()
	elif (g2d.key_released("ArrowUp") or
			g2d.key_released("ArrowRight") or
			g2d.key_released("ArrowDown") or
			g2d.key_released("ArrowLeft")):
		turtle.stay()
	arena.move_all()  # Game logic
	g2d.clear_canvas()
	for a in arena.actors():
		if a.symbol != (0, 0, 0, 0):
			g2d.draw_image_clip(sprites, a.symbol(), a.position())
		else:
			g2d.fill_rect(a.position())

def main():
	g2d.init_canvas(arena.size())
	g2d.main_loop(update)

main()
