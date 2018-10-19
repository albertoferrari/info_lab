'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 enumerate
# '''

colori = ["rosso", "verde", "giallo", "nero"]
for colore in enumerate(colori):
	print(colore,end=" ")
# (0, 'rosso') (1, 'verde') (2, 'giallo') (3, 'nero')

print()

# conversione in lista
lista_colori=list(enumerate(colori))
print(lista_colori)
# [(0, 'rosso'), (1, 'verde'), (2, 'giallo'), (3, 'nero')]

for i, val in enumerate(colori):
    print(i, val)
# 0 rosso
# 1 verde
# 2 giallo
# 3 nero
