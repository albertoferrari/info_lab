'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 fibonacci (funzione ricorsiva)
'''

def fibonacci(n: int) -> int:
    result = 1
    if n > 1:
        result = fibonacci(n-1) + fibonacci(n-2)
    return result
    
def main():
    for n in range(1,11):
       print('termine ',n,' della serie di Fibonacci = ',fibonacci(n))
    
main()
