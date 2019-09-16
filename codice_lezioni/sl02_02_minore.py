'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 genera e stampa tre numeri interi casuali: a, b, c
 ciascuno compreso tra 1 e 6
 determina e mostra qual è il minore dei tre
'''

from random import randint

a = randint(1, 6)  
b = randint(1, 6)
c = randint(1, 6)

print("a =",a,"b =", b,"c =", c)

if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)
        
