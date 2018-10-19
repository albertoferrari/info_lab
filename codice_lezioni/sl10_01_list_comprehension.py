'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 list comprehension
# '''
# quadrati dei numeri da 1 a 10
lista_quadrati = [x ** 2 for x in range(1,11)]
# codice equivalente
# lista_quadrati = []
# for x in range(1,11):
   # lista_quadrati.append(x ** 2)
print(lista_quadrati)

# numeri dispari da 1 a 19
dispari = [str(x) for x in range(1,20) if (x % 2) != 0]
# codice equivalente
# dispari = []
# for x in range(1,20):
	# if x%2 != 0:
		# dispari.append(str(x))
print(dispari)
