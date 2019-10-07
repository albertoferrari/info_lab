'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio classe Punto
'''

class Punto:
	'''
	rappresenta un punto sul piano cartesiano 
	in uno spazio bidimensionale
	'''
		
	def __init__(self, x: float, y: float):
		''' 
		inizializzazione attributi (coordinate)
		'''
		self._x = x
		self._y = y

	def coordinate(self) -> (float, float):
		'''
		coordinate del punto
		'''
		return self._x, self._y
		
	def __str__(self) -> str:
		'''
		rappresentazione del punto
		'''
		return "(" + str(self._x) + "," + str(self._y) + ")"
		
	def distanza_origine(self) -> float:
		'''
		restituisce la distanza del punto dall'origine degli assi
		'''
		return (self._x**2 + self._y **2) ** 0.5

	def distanza_punto(self, p: 'Punto') -> float:
		'''
		restituisce la distanza dal punto p
		'''
		dx = self._x - p._x
		dy = self._y - p._y
		return (dx ** 2 + dy ** 2) ** 0.5


def main():
	p1 = Punto(3,4)
	x , y = p1.coordinate()
	# x = p1.coordinate()[0]
	# y = p1.coordinate()[1]
	print(p1,end=' ')
	#print('punto (',x,',',y,')',end = ' ')
	print("dista dall'origine",p1.distanza_origine())
	p2 = Punto(5,5)
	print(p2,end=' ')
	#print('punto (',p1.coordinate()[0],',',p1.coordinate()[1],')',end = ' ')
	print("dista dal punto",p2.coordinate(),p1.distanza_punto(p2))
	
if __name__ == "__main__":	# solo se è il modulo principale
	main()



