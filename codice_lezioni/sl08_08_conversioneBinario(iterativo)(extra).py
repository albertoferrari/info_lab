'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 conversione decimale binario (iterativo)
'''

def binario(n: int) ->str:
	'''
	restituisce una stringa con la rappresentazione binaria di n
	'''
	if n==0:
		cifre = "0"
	else:
		cifre = ""
	while n>0:
		r = n % 2							#resto
		cifre = str(r) + cifre
		n = n // 2
	return cifre

def main():
	v = int(input("inserisci valore intero positivo: "))	#valore 'decimale'
	print("rappresentazione binaria di",v,"=",binario(v))
	
if __name__ == "__main__":	# solo se è il modulo principale
	main()


