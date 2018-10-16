'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 fibonacci (memoizzazione python)
 https://docs.python.org/3/library/functools.html
'''

from functools import lru_cache
from time import sleep

@lru_cache()                   # function decoration
def fibonacci(n: int) -> int:
    result = 1
    if n > 1:
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

@lru_cache()
def somma(a,b):
	sleep(3)
	return a + b
 
def main():
    for n in range(1,11):
       print('termine ',n,' della serie di Fibonacci = ',fibonacci(n))
    #print(somma(3,2))
    #print(somma(3,2))
    
main()
