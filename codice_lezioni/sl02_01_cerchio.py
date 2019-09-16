'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 chiede all'utente il valore del raggio r di un cerchio
 mostra il valore dell'area e della circonferenza
 se r è negativo, però, mostra un messaggio d'errore
'''

from math import pow, pi

raggio = int(input("raggio: "))
if (raggio < 0):
    print("raggio negativo!")
else:
    circonf = 2 * pi * raggio
    area = pi * pow(raggio,2)
    print("circonferenza",circonf)
    print("area",area)
