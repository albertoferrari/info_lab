
'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio CSP
 TWO +
 TWO =
------
FOUR 
# '''

def controlla(t,w,o,f,u,r):
	# tutti diversi --- (vincolo 1)
	if t==w or t==o or t==f or t==u or t==r:
		return False
	if w==o or w==f or w==u or w==r:
		return False
	if o==f or o==u or o==r:
		return False
	if f==u or f==r:
		return False
	if u==r:
		return False
	# ------------------
	# verifica somma --- (vncolo 2)
	two = t*100 + w*10 + o				# valore addendi
	four = f*1000 + o*100 + u*10 + r	# valore risultato
	if two + two != four:
		return False
	return True	# tutti i vincoli soddisfatti

def main():
	n_sol = 0
	# generazione valori
	for t in range(1,10):
		for w in range(10):
			for o in range(10):
				for f in range(1,10):
					for u in range(10):
						for r in range(10):
							# verifica vincoli
							if controlla(t,w,o,f,u,r):
								n_sol += 1
								print('\nsoluzione',n_sol)
								print(' ',t,w,o,'+')
								print(' ',t,w,o,'=')
								print('------------------')
								print(f,o,u,r)

main()
