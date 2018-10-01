'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 disegna n cerchi concentrici con raggio decrescente
 fa variare il colore dei cerchi dal rosso del livello più esterno
 fino al nero del livello più interno
'''
import g2d

DIMCANVAS = 600								# dimensione canvas
CENTRO = (DIMCANVAS // 2 , DIMCANVAS // 2)	# centro dei cerchi
raggio = DIMCANVAS // 2						# raggio iniziale
rosso = 255									# rosso iniziale

n = int(input('numero cerchi: '))
d_raggio = raggio // (n+1)					# delta raggio
d_rosso = rosso // (n-1)					# delta rosso

g2d.init_canvas((DIMCANVAS, DIMCANVAS))

for i in range(n):
	# print(rosso,raggio)					# debug -> colore e raggio
	g2d.draw_circle((rosso,0,0),CENTRO,raggio)	# disegna cerchio
	rosso -=d_rosso							# nuovo raggio
	raggio -=d_raggio						# nuovo colore

g2d.main_loop()
