'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 calcolo radice quadrata (iterativo)
'''

import math				# solo per confronto

def radice(x: float) -> float:
	'''
	approssimazione di radice quadrata di x
	'''
	vMin, vMax = 0, x			# radice di x è nell'intervallo [0,x]
	
	if (vMax < 1):
		vMax = 1  				# se x <1  allora radice(x) > x
	
	y = (vMin + vMax) / 2		#interpolazione
	delta = y ** 2 - x			#approssimazione

	while abs(delta) > 0.001:		#approssimazione troppo grande
		if delta < 0:
			vMin = y
		else:
			vMax = y
		y = (vMin + vMax) / 2		#interpolazione
		delta = y ** 2 - x			#approssimazione
	return y

def main():
	x = float(input("inserisci valore: "))

	print("radice di",x,"=",radice(x))
	print("math.sqrt(x) =",math.sqrt(x))
	
if __name__ == "__main__":	# solo se è il modulo principale
	main()
