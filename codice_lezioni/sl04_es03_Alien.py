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

class Alien:
	'''
	alieno che si muove a serpentina verso il basso
	'''
		
	def __init__(self, x: int, y: int):
		''' 
		inizializzazione attributi
		'''
		self._x = x
		self._y = y
		self._dx = 10
		self._dy = 10
		self._w = 20
		self._h = 20

	def move(self):
		self._x = self._x + self._dx				# movimento orizzontale
		if self._x<0 or self._x>(ARENA_W-self._w):
			self._dx = -self._dx					# inversione orizzontale
			self._y = self._y + self._dy			# discesa
		if self._y > ARENA_H:
			self._x = self._y = 0					# ritorno posizione iniziale

	def center(self) -> (int, int):
		return int(self._x + self._w / 2), int(self._y + self._h / 2)
		
	def wide(self):
		return int(self._w)

def update():
	g2d.fill_canvas((255, 255, 255))  # BG
	b1.move()
	g2d.draw_circle((0, 0, 255), b1.center(), int(b1.wide() / 2))
    
b1 = Alien(0, 0)
ARENA_W = 320			# larghezza arena
ARENA_H = 240			# altezza arena

def main():
	g2d.init_canvas((ARENA_W, ARENA_H))
	g2d.main_loop(update, 1000 // 30)  # Millis

if __name__ == "__main__":	# solo se è il modulo principale
	main()
