'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 tipo di dato tuple e operazioni su tuple
'''

t1 = 1, 2, 3						# variabile tupla
print("tipo di t1", type(t1))
print("valore di t1", t1)
t2 = t1 + (4, 5, 6)				# concatenazione
print(t2)
t3 = t1 * 4						# prodotto (ripetizione)
print(t3)
for t in t1:					# accesso sequenziale a tutti gli elementi
    print(t)
print(t1 < (0, 8, 9))				# confronto fra tuple
t4 = tuple(range(5, 20))			# conversione da range
print(t4)
t5 = tuple(range(5, 20, 2))		# ... range con step
print(t5)
t6 = (55,)						# tupla di un elemento
								# t6 = 55 -> errore
								# t6 = (55) -> errore
print(t6)
t7 = (2*3,8.5,"hello",True)		# tipi differenti in tupla
print(t7)
t8 = tuple('albertoferrari.github.io')	# conversione da string
print(t8)
# appartenenza a tupla
print('a' in t8)
print('k' in t8)
print('rr' in t8)
print(('r','r') in t8)
print(t8[0],t8[7])				# selezione elemento
print(t8[0:7])					# slice "sottotupla"