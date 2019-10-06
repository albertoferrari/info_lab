'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio composizione
'''

from sl04_00_Punto import Punto
from sl06_00_Segmento import Segmento
from math import sqrt

class Triangolo:
	'''
	rappresenta un triangolo sul piano cartesiano 
	in uno spazio bidimensionale
	'''
		
	def __init__(self, a: Punto, b:Punto, c:Punto):
		''' 
		inizializzazione attributi (lati)
		'''
		self._lati = [Segmento(a,b),Segmento(b,c),Segmento(c,a)]

	def perimetro(self) -> float:
		'''
		perimetro
		'''
		p = 0
		for l in self._lati:
			p += l.lunghezza()
		return p
		
	def area(self) ->float:
		'''
		area (formula di Erone)
		'''
		p = self.perimetro() / 2
		a , b, c = self._lati
		return sqrt(p*(p-a.lunghezza())*(p-b.lunghezza())*(p-c.lunghezza()))
		

def main():
	p1 = Punto(0,0)
	p2 = Punto(0,3)
	p3 = Punto(4,0)
	t = Triangolo(p1,p2,p3)
	print("perimetro",t.perimetro())
	print("area",t.area())
	
if __name__ == "__main__":	# solo se è il modulo principale
	main()


