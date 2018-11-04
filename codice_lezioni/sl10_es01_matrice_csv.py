'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 legge matrice di interi da file csv
 somma su diagonale partendo da basso destra
'''
import os

# scrittura del file per test
with open("f_matrice.csv", "w") as fout:
    print("5,7,2,11", file=fout)
    print("1,3,12,9", file=fout)
    print("4,6,10,8", file=fout, end="")

matrice2d = []		# lista di liste (2D)
matrice1d = []		# lista semplice (1D)
colonne, righe = 0, 0

with open("f_matrice.csv", "r") as fin:
    for riga in fin:
        splitted = riga.split(",")
        valori = [int(i) for i in splitted]	#list comprehension
        matrice2d.append(valori)	# 2D
        matrice1d += valori  		# 1D

        colonne = len(valori)
        righe += 1

print(righe, "righe", colonne, "colonne")
print("2D",matrice2d)
print("1D",matrice1d)

somma2d = 0
somma1d = 0
x, y = colonne - 1, righe - 1
while x >= 0 and y >= 0:
    somma2d += matrice2d[y][x]				# 2D
    somma1d += matrice1d[y * colonne + x]	# 1D
    x -= 1
    y -= 1
print("somma2d",somma2d,"somma1d",somma1d)

# eliminazione del file test
os.remove("f_matrice.csv")
