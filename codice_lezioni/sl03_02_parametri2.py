'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio funzioni (passaggio parametri)
'''

def inc(f):
    '''
    incrementa il valore di a
    '''
    f = f + 1
    print("funzione: valore -> ",f)

def main():
    a = 5
    inc(a)
    print("main: valore -> ",a)
	
main()  ## remove if importing the module elsewhere
