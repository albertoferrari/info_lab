'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 riempire una lista con i valori di sin(x)
	360 elementi, indice x tra 0 e 359
 chiedere un angolo all'utente
	visualizzare il corrispondente valore precalcolato del seno
'''

from math import pi, sin

val_sin = [0] * 360				# valori seno
for g in range(360):			# gradi
    rad = g * pi / 180			# gradi -> radianti
    val = sin(rad)
    val_sin[g] = val

# val_sin = [sin(g * pi / 180) for g in range(360)]	#list comprehensions

angolo = int(input("angolo in gradi: "))
while 0 <= angolo < 360:
    valore = val_sin[angolo]
    print("sin(",angolo,") = ",valore)
    # print(f"sin({angolo}) = {valore:.2f}")
    angolo = int(input("angolo in gradi: "))

