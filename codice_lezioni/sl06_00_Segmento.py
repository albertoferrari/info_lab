'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio composizione
'''

from sl04_00_Punto import Punto

class Segmento:
	'''
	rappresenta un segmento sul piano cartesiano 
	in uno spazio bidimensionale
	'''
		
	def __init__(self, p1: Punto, p2:Punto):
		''' 
		inizializzazione attributi (coordinate)
		'''
		self._p1 = p1
		self._p2 = p2

	def lunghezza(self) -> float:
		'''
		lunghezza del segmento
		'''
		return self._p1.distanza_punto(self._p2)
		
	def __str__(self) ->str:
		'''
		rappresentazione del segmento
		'''
		return str(self._p1) + "-" + str(self._p2)

def main():
	p1 = Punto(3,4)
	p2 = Punto(5,5)
	s = Segmento(p1,p2)
	print("lunghezza segmento" + str(s) + " = " + str(s.lunghezza()))
	
if __name__ == "__main__":	# solo se è il modulo principale
	main()


