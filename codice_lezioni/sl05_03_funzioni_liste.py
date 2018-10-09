'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 funzioni su liste
'''

def limita_valori(lis, limite):
	''' 
	fissa un limite massimo ai valori della lista lis
	'''
	for i in range(len(lis)):
		if lis[i] > limite:
			lis[i] = limite

def stampa_valori(lis):
	for i, val in enumerate(lis):
		print('indice', i, 'valore', val)

def main ():
	dati = [5, 4, 2]
	limita_valori(dati, 4)
	print(dati)
	stampa_valori(dati)
	
main()
