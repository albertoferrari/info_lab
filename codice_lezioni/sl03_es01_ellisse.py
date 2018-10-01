'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 funzione ellipse_area (parametri i semiassi) return area
'''
from math import pi

def ellipse_area(sa1: float, sa2: float) -> float:
    '''
    restituisce l'area dell'ellisse 
    con semiassi sa1 e sa2
    '''
    return pi * sa1 * sa2

def main():
    a = float(input('primo semiasse = '))
    b = float(input('secondo semiasse = '))
    c = ellipse_area(a, b)
    print("area =",c)

main()
