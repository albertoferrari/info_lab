'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 conversione decimale binario (operativa)
'''

def dec_bin(n: int) ->str:
	'''
	restituisce una stringa con la rappresentazione binaria di n (naturale)
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
	
def bin_dec(b :str) ->int:
	n = 0
	p = len(b)-1							#potenza 
	for cifra in b:
		n += int(cifra)*2**p
		p -= 1
	return n

def main():
	v_dec = int(input("inserisci valore: "))	#valore 'decimale'
	v_bin = dec_bin(v_dec)
	print("rappresentazione binaria di",v_dec,"=",v_bin)
	v = bin_dec(v_bin)
	print("rappresentazione decimale di",v_bin,"=",v)
	
if __name__ == "__main__":	# solo se è il modulo principale
	main()


