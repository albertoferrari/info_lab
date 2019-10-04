'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 l'utente sceglie righe e colonne
 allocare una lista di dimensione n=righe×colonne (pari)
 inserire in ordine le prime lettere dell'alfabeto
   ciascuna ripetuta due volte
 mescolare le celle
   per ciascuna cella, scegliere una posizione a caso e scambiare il contenuto delle celle
 mostrare la lista, andando a capo per ogni riga
   usare una lista semplice, ma nella visualizzazione introdurre dei ritorni a capo
'''

import random

def stampa():
	'''
	stampa memory
	'''
	for i in range(dimensione):
		print(memory[i], end=' ')
		if i % colonne == colonne - 1:
			print()
	print()

ORD_A = ord('A')		# carattere iniziale
dimensione = 1			# dimensione matrice

while dimensione % 2 != 0:
	righe = int(input('righe: '))
	colonne = int(input('colonne: '))
	dimensione = righe * colonne

# inserimento dati
memory = [chr(ORD_A + i // 2) for i in range(dimensione)]
## 	alternativa
## 	memory = []
## 	for i in range(dimensione//2):
## 		memory.append(chr(ORD_A+i))
##		memory.append(chr(ORD_A+i))

stampa()

# shuffle
random.shuffle(memory)
## 	alternativa
##	for i in range(dimensione):
##		j = random.randrange(dimensione)
##		memory[i], memory[j] = memory[j], memory[i]

stampa()

