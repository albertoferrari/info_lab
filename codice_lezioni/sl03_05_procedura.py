'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio di procedura
'''

def stampa_riga(y: int, size: int):
	for x in range(1, size + 1):
		val = x * y
		print(f"{val:3}", end="|")
	print()

def stampa_tabella(size: int):
	for riga in range(1, size + 1):
		stampa_riga(riga, size)

def main():
	stampa_tabella(10)
	
main()
