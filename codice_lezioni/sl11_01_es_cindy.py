'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 puzzle di Cindy
 soluzione ricorsiva (backtracking)
'''

def mossa(gioco: list, p: int) -> int:
	'''
	restituisce il possibile movimento del pezzo in posizione p
	'''
	if gioco[p:p+2] == ['r', '_']:			#rosso può avanzare
		return 1
	elif gioco[p:p+3] == ['r', 'v', '_']:	#rosso può scavalcare
		return 2
	elif gioco[p-1:p+1] == ['_', 'v']:		#verde può avanzare
		return -1
	elif gioco[p-2:p+1] == ['_', 'r', 'v']:	#verde può scavalcare
		return -2
	return 0								#nessuna mossa

def risolto(gioco, finale, n_mossa=0) -> bool:
	'''
	verifica se il gioco è risolto
	altrimenti tenta tutte le possibili mosse
	'''
	print('  ' * n_mossa + ''.join(gioco))  # debug (indentazione n.ro mosse)
	if gioco == finale:				#raggiunta situazione finale
		print(n_mossa,'mosse')
		return True

	for e in range(len(gioco)):		#per ogni elemento in gioco
		m = mossa(gioco, e)		#possibile mossa
		if m != 0:
			gioco[e], gioco[e + m] = gioco[e + m], gioco[e]	#effettuo mossa

			if risolto(gioco, finale, n_mossa + 1):	#risolto mossa successiva
				return True

			# non risolto: backtracking
			gioco[e], gioco[e + m] = gioco[e + m], gioco[e]	#torno indietro

	return False

def main():
	n = int(input('numero pezzi rossi/verdi '))
	gioco = ['r'] * n + ['_'] + ['v'] * n		#situazione gioco
	finale = ['v'] * n + ['_'] + ['r'] * n		#situazione finale (gioco risolto)
	if risolto(gioco, finale):					#raggiunta situazione finale
		print('trovata soluzione')

main()
