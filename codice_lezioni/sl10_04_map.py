'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 map
# '''

from math import sqrt
valori = [0, 1, 2, 3, 4]
print(list(map(sqrt, valori)))
#[0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0]

print(list(map(sqrt,range(5))))
#[0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0]
