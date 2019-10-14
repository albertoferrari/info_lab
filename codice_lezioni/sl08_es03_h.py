'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 albero di h
'''

import g2d

def center(rect: (int, int, int, int)) -> (int, int):
    x, y, w, h = rect
    return x + w / 2, y + h / 2

def htree(rect: (int, int, int, int), level: int):
    x, y, w, h = rect
    if level == 0 or w < 3 or h < 3:	#terminazione
        return
    if level % 2 == 0:					#livello pari dimezzo larghezza
        rect1 = x, y, w / 2, h			#primo rettangolo sn
        rect2 = x + w / 2, y, w / 2, h	#secondo rettangolo ds
        #print(level,'sn',rect1,'ds',rect2)	#debug
    else:								#livello dispari dimezzo altezza
        rect1 = x, y, w, h / 2			#alto
        rect2 = x, y + h / 2, w, h / 2	#basso
        #print(level,'up',rect1,'down',rect2)	#debug

    g2d.draw_line(center(rect1), center(rect2))
    htree(rect1, level - 1)
    htree(rect2, level - 1)




if __name__ == '__main__':
	level = int(input('level? '))  ## -1 = infinite
	side = 600

	g2d.init_canvas((side, side))
	g2d.set_color((0,0,0))
	htree((0, 0, side, side), level)

	g2d.main_loop()




