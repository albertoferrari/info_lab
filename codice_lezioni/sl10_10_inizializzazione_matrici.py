'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 inizializzazione matrici
# '''
cols = 3	#dato noto
rows = 4	#dato noto
#inizializzazione di tutti gli elementi al ' '
matrix = [[' ' for x in range(cols)] for y in range(rows)]

for r in range(rows):
	print(matrix[r])
	

print('---------------')

#metodo alternativo
matrix = []
for y in range(rows):
    new_row = []
    for x in range(cols):
        new_row.append(' ')
    matrix.append(new_row)
    
for r in range(rows):
	print(matrix[r])
