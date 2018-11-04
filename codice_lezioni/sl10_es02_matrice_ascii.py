'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 visualizza caratteri da 32 a 126 in tabella 4 righe 24 colonne
 prima ordinati per riga
 poi ordinati per colonna
'''
INIZIO = 32
FINE = 126
RIGHE = 4
COLONNE = 24

print('ordinamento per righe')
for y in range(RIGHE):
	for x in range(COLONNE):
		c = INIZIO + x + y * COLONNE	#codice carattere
		if c <= FINE:
			print(chr(c), end="")		#visualizza carattere
	print()

print('\nordinamento per colonne')
for y in range(RIGHE):
	for x in range(COLONNE):
		c = INIZIO + y + x * RIGHE		#codice carattere
		if c <= FINE:
			print(chr(c), end="")		#visualizza carattere
	print()
