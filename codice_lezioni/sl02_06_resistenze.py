'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 legge, attraverso un ciclo, una sequenza di valori di resistenze elettriche
 la sequenza termina quando l'utente immette il valore 0
 alla fine, visualizza la resistenza equivalente,
 sia nel caso di resistenze disposte in serie, che in parallelo
'''

serie = parallelo = 0

res = float(input("valore resistenza (0 per terminare) "))
while (res!=0):
    serie += res
    parallelo += 1/res
    res = float(input("valore resistenza (0 per terminare) "))
    
print("serie",serie)
print("parallelo",1/parallelo)

