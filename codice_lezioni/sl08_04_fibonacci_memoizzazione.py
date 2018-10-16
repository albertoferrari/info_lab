'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 fibonacci (memoizzazione)
'''

_fibonacci_lookup = [1, 1]	# termini già calcolati

def fibonacci(n: int) -> int:
    if n < len(_fibonacci_lookup):
        return _fibonacci_lookup[n]		# no ricorsione
    result = fibonacci(n - 1) + fibonacci(n - 2)
    _fibonacci_lookup.append(result)	# memoizzazione
    return result
    
def main():
    for n in range(1,11):
       print('termine ',n,' della serie di Fibonacci = ',fibonacci(n))
    
main()
