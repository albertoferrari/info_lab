'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 lista pseudo matrice - somma colonne 
# '''
matrix = [2, 4, 3, 8,
          9, 3, 2, 7,
          5, 6, 9, 1]
rows = 3  # dato non ricavabile dalla pseudomatrice
cols = len(matrix) // rows

for x in range(cols):
    total = 0
    for y in range(rows):
        val = matrix[y * cols + x]   # 2D -> 1D
        total += val
    print("Col #", x, "sums to", total)
