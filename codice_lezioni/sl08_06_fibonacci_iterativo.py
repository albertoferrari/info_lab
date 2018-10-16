'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 fibonacci (iterativo)
'''

def fibonacci(n: int) -> int:
    value = 1
    previous = 0

    for i in range(n):
        value, previous = value + previous, value

    return value
 
def main():
    for n in range(1,11):
       print('termine ',n,' della serie di Fibonacci = ',fibonacci(n))
    
main()
