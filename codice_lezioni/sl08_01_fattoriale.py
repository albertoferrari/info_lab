'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 fattoriale (funzione ricorsiva)
'''

def fattoriale(n: int) -> int:
	if n == 0:
		return 1
	else:
		return n * fattoriale(n-1)	
	
def main():
	print(fattoriale(5))	
	
main()
