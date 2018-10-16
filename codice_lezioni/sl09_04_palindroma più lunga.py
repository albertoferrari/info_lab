'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio di lettura su file di testo
# '''

def palindroma(testo: str) -> bool:
	if len(testo) <= 1:
		return True
	return testo[0] == testo[-1] and palindroma(testo[1:-1])

with open("280000_parole_italiane.txt",mode="r", encoding="utf-8") as myFile:
	max_len = 0
	par_pal = ''
	for testo in myFile:
		parola = testo.strip()
		if len(parola) > max_len and palindroma(parola):
			max_len = len(parola)
			par_pal = parola
	print('parola palindroma più lunga',par_pal,max_len,'lettere')
	
