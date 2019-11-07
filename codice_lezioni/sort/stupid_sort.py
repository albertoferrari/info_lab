'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 ordinamento bozo sort
'''
import time
from random import randint, shuffle

def stupidSort(v: list):
	'''
	ordina la lista v 
	con algoritmo bozo sort
	'''
	while not ordinata(v):
		#print(v)
		shuffle(v)
    
def ordinata(v: list) -> bool:
	'''
	true se la lista v
	è ordinata in modo non decrescente
	'''
	for i in range(len(v)-1):
		if v[i] > v[i+1]:
			return False
	return True		
	
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
stupidSort(valori)
t = time.time() - t0
print(valori)
print(t,"secondi")
