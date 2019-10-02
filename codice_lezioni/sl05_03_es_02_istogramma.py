'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
  istogramma con barre orizzontali
  chiedere all'utente una lista di valori positivi
  la lista termina quando l'utente inserisce il valore 0
  mostrare un istogramma
  larghezza di ciascuna barra proporzionale
  al valore corrispondente
  la barra più lunga occupa tutto lo spazio disponibile
'''

import g2d

val = []
v = int(input("valore (0 fine) "))
while v > 0:
	val.append(v)
	v = int(input("valore (0 fine) "))

w = 600
h = 400
n = len(val)		#numero rettangoli
hr = h // n			#altezza rettangolo
vm = max(val)		#valore massimo nella lista
pix = w // vm		#pixel corrispondenti a unità
g2d.init_canvas((w,h))
g2d.set_color((0,0,255))
y = 0				#posizione prima barra		
for v in val:
	g2d.fill_rect((0,y,pix*v,hr-1))
	y += hr

g2d.main_loop()


