'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio funzioni (passaggio parametri)
'''

def inc(f):
    '''
    incrementa il valore di ogni elmento della lista f
    '''
    for i in range(0,len(f)):
        f[i] = f[i] + 1
    print("funzione: valore -> ",f) # [3, 4, 6]

def main():
    a = [2,3,5]
    inc(a)
    print("main: valore -> ",a)     # [3, 4, 6]
	
main()  ## remove if importing the module elsewhere
