'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 determinare se un numero è primo
'''

n = int(input('inserisci un valore intero positivo: '))
divisore = 2
while n % divisore != 0:		# finchè non è stato trovato un divisore
	divisore += 1
if divisore == n:
	print(n,'è primo')
else:
	print(n,'non è primo')

# cosa succede se si riceve in input un valore <= 1?
