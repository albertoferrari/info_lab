'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 matrici
# '''
a = [['A', 'B', 'C', 'D'],
     ['E', 'F', 'G', 'H'],
     ['I', 'L', 'M', 'N']]          # 2D

b = ['A', 'B', 'C', 'D',
     'E', 'F', 'G', 'H',
     'I', 'L', 'M', 'N']            # 1D

riga = 0							# prima riga
colonna = 2							# terza colonna
print(a[riga][colonna])				#'C'

num_colonne = 4						# la matrice ha 4 colonne

# conversione 2D -> 1D (dalla matrice a alla matrice b)
indice = riga * num_colonne + colonna
print(b[indice])					#'C'

for r in range(0,3):
	for c in range(0,4):
		i = r * num_colonne + c
		print(a[r][c],b[i])			#elementi corrispondenti
		
# conversione 1D -> 2D (dalla matrice b alla matrice a)
# riga = indice // num_colonne
# colonna = indice % num_colonne
for i in range(0,12):
	r = i // num_colonne
	c = i % num_colonne
	print(b[i],a[r][c])



