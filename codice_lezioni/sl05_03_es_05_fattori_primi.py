'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 fattori primi
 funzione che trova tutti i fattori primi di un numero n
   parametro : n
   risultato : lista, contenente i fattori primi di n
   algoritmo : scorrere tutti i valori d'interesse, e cercare i divisori
       x è divisore di n sse n % x == 0
   non considerare i fattori non primi
   provare la funzione con valori inseriti dall'utente
     quando
     si trova un divisore x, dividere ripetutamente n per x, finché 
     resta divisibile valutare l'uso di un ciclo while , anzichè for
'''

def fattori(n: int) ->list:
	'''
	return lista con fattori primi di n
	'''
	fatt_primi = []		# lista fattori primi
	f = 2				# possibile fattore primo
	while f <= n:
		if primo(f):
			if n % f == 0:
				fatt_primi.append(f)
			while n % f == 0:
				n = n // f
		f += 1
	return fatt_primi

def primo(n: int) -> bool:
	'''
	return true se n è primo
	'''
	if (n==1):
		return False
	elif (n==2):
		return True;
	else:
		for d in range(2,n//2):
			if(n % d==0):
				return False
		return True 

def main():
	n = int(input("n = "))
	while n > 0:
		print(fattori(n))
		n = int(input("n = "))

if __name__ == '__main__':
    main()


