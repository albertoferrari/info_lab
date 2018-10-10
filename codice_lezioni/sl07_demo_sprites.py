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
    arena.move_all()  # Game logic

    g2d.fill_canvas((255, 255, 255))
    for a in arena.actors():
        g2d.draw_image_clip(sprites, a.position(), a.symbol())

def keydown(code):
    #print(code + " dn")
    if code == "ArrowUp":
        turtle.go_up()
    elif code == "ArrowDown":
        turtle.go_down()
    elif code == "ArrowLeft":
        turtle.go_left()
    elif code == "ArrowRight":
        turtle.go_right()

def keyup(code):
    #print(code + " up")
    turtle.stay()

def main():
    g2d.init_canvas(arena.size())
    g2d.handle_keyboard(keydown, keyup)
    g2d.main_loop(update, 1000 // 30)
    
main()
