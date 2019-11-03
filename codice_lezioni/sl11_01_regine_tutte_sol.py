
'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 posizionare n regine in una scacchiera nxn
 in modo che una regina non possa catturarne
 nessun'altra
 la scacchiera è rappresentata da una lista di n valori 
 il valore c di indice r della lista rappresenta
 la posizione della regina in riga r e colonna c
 visualizzazione di tutte le possibili soluzioni
'''

def stampa_scacchiera(scacchiera: list):
	''' 
	visualizza la scacchiera
	'''
	for r in range(len(scacchiera)):
		for c in range(len(scacchiera)):
			if c == scacchiera[r]: 
				print('|Q', end='')		#presente regine
			else: 
				print('| ', end='')		#casella vuota
		print('|')						#fine riga

def sotto_attacco(scacchiera: list, x: int, y: int) -> bool:
	''' 
	true se la regina in colonna x e riga y 
	è sotto attacco da altre regine
	'''
	# controllo le righe precedenti
	for r in range(1, y + 1):  # fino alla riga attuale
		# direzioni di controllo: ↖↑↗ 
		if scacchiera[y - r] in (x - r, x, x + r):
			return True
	return False

def posiziona_regine(scacchiera: list, r=0):
	'''
	cerca di posizionare una regina nella scacchiera
	in riga r (le precedenti righe contengono regine
	'''
	if r == len(scacchiera):	#posizionate tutte le regine
		stampa_scacchiera(scacchiera)
		print('*')
	else:
		# prova inserimento regina in tutte le colonne
		for c in range(len(scacchiera)):
			if not sotto_attacco(scacchiera, c, r):
				scacchiera[r] = c  # possibile inserire regina in colonna c
				# passaggio alla riga successiva
				if posiziona_regine(scacchiera, r + 1):
					return True

				scacchiera[r] = None  # non è possibile inserire, backtrack

def main():
	n_regine = int(input('dimensione scacchiera (numero di regine): '))
	scacchiera = [None] * n_regine		#scacchiera vuota

	# posiziona regine a partire dalla riga 0
	posiziona_regine(scacchiera)

main()
