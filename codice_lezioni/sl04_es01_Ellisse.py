'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 classe che modella un'ellisse
 campi privati semiassi: a, b
 metodi pubblici:
 area: π⋅a⋅b
 distanza focale: 2⋅√|a2 - b2|

'''
import math

class Ellisse:
	'''
	Ellisse
	'''
		
	def __init__(self, a: float, b: float):
		''' 
		inizializzazione semiassi
		'''
		self._sa1 = a		# primo semiasse
		self._sa2 = b		# secondo semiasse

	def area(self) -> float:
		return math.pi * self._sa1 * self._sa2

	def focale(self) -> float:
		return 2 * math.sqrt(abs(self._sa1**2 - self._sa2**2))

def main():
	el = Ellisse(2,3)
	print('area =',el.area())
	print('distanza focale =',el.focale())
	
if __name__ == "__main__":		# solo se è il modulo principale
	main()



