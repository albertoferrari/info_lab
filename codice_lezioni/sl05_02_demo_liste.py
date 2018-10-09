'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 tipo di dato lista e operazioni su lista
'''
myLis = ['alfa', 'beta', 'gamma']	# variabile lista

print("myLis = ['alfa', 'beta', 'gamma']")
print('tipo di myLis', type(myLis))
print('valore di myLis', myLis)
print('primo elemento',myLis[0])
print('lunghezza',len(myLis))
print('ultimo elemento',myLis[-1])  # equivalente a myLis[len(myLis)-1]
print('accesso sequenziale agli elementi:')
for e in myLis:
	print(e,end=' | ')
print()

# confronto e concatenazione
myLis2 = ['alfa', 'zeta', 'gamma']
print("['alfa', 'beta', 'gamma'] < ['alfa', 'zeta', 'gamma'] -> ",myLis < myLis2)
print("['alfa', 'beta', 'gamma'] + ['alfa', 'zeta', 'gamma'] -> ",myLis + myLis2)

# conversione da range
myLis3 = list(range(1,10,2))
print("myLis3 = list(range(1,10,2))")
print('tipo di myLis3', type(myLis3))
print('valore di myLis3', myLis3)

# prodotto (ripetizione)
myLis4 = ['a','e'] * 3
print("myLis4 = ['a','e'] * 3 -> ",myLis4)

# lista con valori di tipo differente
myLis5 = ['alfa', 3, True, 4.5, (3,4,5), [2,6,8]]
print("myLis5 = ['alfa', 3, True, 4.5, (3,4,5), [2,6,8]] -> ")
print(myLis5)

# appartenenza a lista
print("print(3 in myLis5) -> ",3 in myLis5)
print("print([3, Ture] 3 in myLis5) -> ",[3, True] in myLis5)
print("print([2, 6, 8] 3 in myLis5) -> ",[2, 6, 8] in myLis5)

# conversione da stringa
myLis6 = list('https://dia.unipr.it')
print("myLis6 = list('https://dia.unipr.it') -> ")
print(myLis6)

# slice
print("print(myLis6[2:4]) -> ",myLis6[2:4])

