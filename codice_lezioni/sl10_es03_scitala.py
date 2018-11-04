'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 scitala spartana
'''

#lettura intero file
with open("divina.txt",encoding="utf-8") as infile:
    testo = infile.read()

RIGHE = 10
COLONNE = 25

matrice = [[' '] * COLONNE for y in range(RIGHE)]	#matrice di spazi

i = 0
for y in range(RIGHE):
	for x in range(COLONNE):
		matrice[y][x] = testo[i]
		i += 1

print('originale 10 righe 25 colonne')
for y in range(RIGHE):
	for x in range(COLONNE):
		print(matrice[y][x],end="")
	print()	

print('\ncrittato')
for x in range(COLONNE):
	for y in range(RIGHE):
		print(matrice[y][x], end="")
