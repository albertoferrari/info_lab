'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 griglia di colori mostra una griglia di rettangoli 
 in orizzontale aumenta gradatamentela componente di blu
 in verticale aumentare gradatamente la componente di verde
'''

import g2d

LAR, ALT = 600, 400					# dimensione canvas
g2d.init_canvas((LAR, ALT))

colonne = int(g2d.prompt('numero colonne: '))
righe = int(g2d.prompt('numero righe: '))

w = LAR / colonne			# larghezza rettangolo
h = ALT / righe				# altezza rettangolo
d_blue, d_green = 0, 0

if colonne > 1:
    d_blue = 255.0 / (colonne - 1)	# delta blue
if righe > 1:
    d_green = 255.0 / (righe - 1)	# delta green

for r in range(righe):
    for c in range(colonne):
        colore = 0, int(d_green * r), int(d_blue * c)
        g2d.set_color(colore)
        rettangolo = int(w * c), int(h * r), int(w - 1), int(h - 1)
        g2d.fill_rect(rettangolo)

g2d.main_loop()

