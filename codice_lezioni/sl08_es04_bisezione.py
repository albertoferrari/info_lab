'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 ricerca 0 - bisezione
'''

##from types import Callable  # f: Callable[[float], float]

def f3(x: float) -> float:
	return x ** 3 - x - 1

def find_zero(f, low: float, high: float, err: float) -> float:
	'''
	ricerca 0 della funzione f fra low e high (err = approssimazione)
	'''
	x = (low + high) / 2	#centro intervallo
	y = f(x)				#valore della funzione al centro intervallo
	if abs(y) > err:		#non trovato '0'
		if y * f(low) < 0:	#un valore positivo e uno negativo (interseca)
			x = find_zero(f, low, x, err)	#cerca '0' in questo intervallo
		else:
			x = find_zero(f, x, high, err)
	return x				#trovato '0'

def main():
	print("approssimazione %10.6f" %1e-6)
	print("ricerca 0 di f(x)=x ** 3 - x - 1      fra 1 e 2")
	x = find_zero(f3, 1, 2, 1e-6)		
	print('x=',x,'f(x)=',f3(x))

main()




