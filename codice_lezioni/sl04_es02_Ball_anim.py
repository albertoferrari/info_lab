'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 partire dalla classe Ball vista a lezione
eseguire l'animazione:
per ogni frame, chiamare il metodo move della pallina
rappresentare un rettangolo o un cerchio nella posizione aggiornata della pallina
modificare però il metodo move
la pallina si sposta sempre di pochi pixel in orizzontale
la pallina non si sposta verticalmente
se esce dal bordo destro, ricompare al bordo sinistro e viceversa

'''
import g2d
from random import randrange

class Ball:
	'''
	pallina che si muove in orizzontale
	'''
		
	def __init__(self, x: int, y: int):
		''' 
		inizializzazione attributi
		'''
		self._x = x
		self._y = y
		self._dx = 3
		self._w = 20
		self._h = 20

	def move(self):
		self._x = (self._x + self._dx) % (ARENA_W)

	def center(self) -> (int, int):
		'''
		centro della pallina
		'''
		return int(self._x + self._w / 2), int(self._y + self._h / 2)
		
	def wide(self):
		return int(self._w)

def random_color():
	return randrange(255), randrange(255), randrange(255)

def update():
	g2d.fill_canvas((255, 255, 255))  # BG
	b1.move()
	g2d.draw_circle(random_color(), b1.center(), int(b1.wide() / 2))
    
b1 = Ball(40, 80)
ARENA_W = 320			# larghezza arena
ARENA_H = 240			# altezza arena

def main():
	g2d.init_canvas((ARENA_W, ARENA_H))
	g2d.main_loop(update, 1000 // 30)  # Millis

if __name__ == "__main__":	# solo se è il modulo principale
	main()
