'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 genera tutti gli anagrammi (permutazioni) di una stringa
'''

def anagramma(testo: str) -> [str]:
	'''
	restituisce una lista con tutti gli anagrammi di testo
	'''
	if len(testo) == 0:
		return ['']
	anagrammi = []			# lista di anagrammi
	for i in range(len(testo)):
		c = testo[i]			# per ogni lettera del testo
		altro = testo[:i] + testo[i + 1:]	# tutte le altre lettere
		for t in anagramma(altro):
			anagrammi.append(c + t)
	return anagrammi

print(anagramma("abcd"))




