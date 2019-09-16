'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 data la lunghezza di un lato di un triangolo 
 equilatero trovare il perimetro e l’area
'''

from math import pow,sqrt

lato = float(input("lato del triangolo equilatero: "))
perimetro = lato * 3
print('perimetro: ',perimetro)
m_lato = lato / 2 #metà del lato
altezza = sqrt(pow(lato,2)+pow(m_lato,2))
area = lato * altezza / 2
print('area: ',area)
