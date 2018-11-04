'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 riempie matrice di numeri crescenti a spirale
 partendo da angolo basso a sinistra
'''

def ammesso(m: list, x: int, y: int) -> bool:
	'''
	True se m[y][x] è un elemento della matrice
	e se vale 0
	'''
	w, h = len(m[0]), len(m)	#dimensioni matrice
	return 0 <= x < w and 0 <= y < h and m[y][x] == 0

def spiral(w: int, h: int) -> list:
	'''
	'''
	# imbiancamento (inizializzazione di tutti gli elementi a 0)
	m = [[0 for x in range(w)] for y in range(h)]

	# elemento iniziale basso/sinistra
	x, y = 0, h - 1
	dx, dy = 0, -1		#direzione iniziale

	for i in range(h * w):
		m[y][x] = i + 1
		# controllo se necessario svoltare
		if not ammesso(m, x + dx, y + dy):
			# calcolo nuova direzione
			dx, dy = -dy, dx
		x, y = x + dx, y + dy	#avanzamento
	return m

def main():
	lar = int(input('larghezza: '))
	alt = int(input('altezza '))
	m = spiral(lar, alt)		#riempimento a spirale
	#visualizzazione
	for y in range(alt):
		for x in range(lar):
			print('{:3}'.format(m[y][x]), end='')
		print()
	print()

main()
