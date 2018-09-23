'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio __main__
'''

def ipotenusa(cateto1: float, cateto2: float) -> float:
    '''
    restituisce la misura dell'ipotenusa di un triangolo
    rettangolo con cateti cateto1 e cateto2
    '''
    return (cateto1 ** 2 + cateto2 ** 2) ** 0.5

def main():
    a = float(input('primo cateto = '))
    b = float(input('secondo cateto = '))
    c = ipotenusa(a, b)
    print("ipotenusa =",c)

if __name__ == "__main__":	# solo se è il modulo principale
	main()
