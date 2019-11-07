'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 Python sort
'''
import time
from random import randint
	
def listaCasuale(n: int, min_v: int, max_v: int) ->list:
	'''
	restituisce una lista di n valori interi
	con valori casuali compresi fra min_v e max_v
	'''
	lista = []
	for i in range(n):
		lista.append(randint(min_v,max_v))
	return lista

valori = listaCasuale(10,100,200)
print(valori)
t0 = time.time()
valori.sort()
t = time.time() - t0
print(valori)
print(t,"secondi")
