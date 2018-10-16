'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 mcd (funzione ricorsiva)
'''

def mcd(a: int, b:int) -> int:
	r = a % b
	if (r==0):  
		return b	#condizione di terminazione
	else: 
		return(mcd(b,r))
    
def main():
    v1 = int(input('primo valore '))
    v2 = int(input('secondo valore '))
    print('massimo comun divisore fra',v1,' e',v2,' = ',mcd(v1,v2))
    
main()
