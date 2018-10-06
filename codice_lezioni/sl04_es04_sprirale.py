'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 animazione di un cerchio intorno a una spirale

'''
import g2d
import math

DIM = 600				# dimensione canvas
centro = 300
raggio, n = 0, 256

def update():
    global raggio
    x = int(centro + raggio * math.cos(raggio * math.pi / 32))	
    y = int(centro + raggio * math.sin(raggio * math.pi / 32))
    g2d.fill_canvas((255, 255, 255))
    g2d.draw_circle((255 - raggio, 0, raggio), (x, y), int(raggio / 2))
    raggio = (raggio + 1) % n

def main():
    g2d.init_canvas((DIM, DIM))				# canvas quadrato
    g2d.main_loop(update, 1000 / 30)

main()
