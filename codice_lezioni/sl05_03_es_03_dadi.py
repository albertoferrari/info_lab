'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 simulare n lanci di una coppia di dadi
 n scelto dall'utente
 contare quante volte si presenta ciascun risultato
 risultati possibili: da 2 a 12 (somma dei due dadi)
 per conteggiare i vari risultati, usare una lista di (almeno) 11 valori
'''

from random import randint

def due_dadi() -> int:
	return randint(1,6)+randint(1,6)
	
def stampa_risultati(lista: list):
	for r , v in enumerate(lista):
		print(r+2,v)

def main():
	ris = [0] * 11			#risultati lanci per i valori 2,12
	n = int(input("numero lanci: "))
	for l in range(n):
		p = due_dadi()		#punteggio ottenuto
		print("lancio",l,"punteggio",p)
		ris[p-2] += 1		#incremento
	stampa_risultati(ris)
	
main()

