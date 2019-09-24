'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 calcolo della media dei valori inseriti
'''
total = 0	#somma dei valori inseriti
count = 0	#numero di valori inseriti

val = int(input("Val? (0 to finish) "))

while val != 0:		# condizione per esguire il ciclo
	total = total + val	# somma il valore
	count += 1			# incrementa il contatore
	val = int(input("Val? (0 to finish) "))
	
if count != 0:
	print("The average is", total / count)
else:
	print("nessun valore eseguito")	

