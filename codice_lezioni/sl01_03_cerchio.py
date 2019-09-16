'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html

 dato il raggio calcolare la circonferenza e l’area del cerchio
'''

from math import pow, pi

raggio = int(input("raggio: "))

circonf = 2 * pi * raggio
area = pi * pow(raggio,2)
print("circonferenza",circonf)
print("area",area)
