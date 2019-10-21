'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 es. riscorsione conteggio vocali minuscole
'''

def contaVocali (s: str) -> int:
	'''
	restituisce numero di vocali minuscole in s
	'''
	if len(s) == 0:
		return 0
	if s[0] in "aeiou":
		return 1 + contaVocali(s[1:])
	return contaVocali(s[1:])
 
def main():
	print("Ingegneria contiene",contaVocali("Ingegneria"),"vocali minuscole")
	print("stringa vuota contiene",contaVocali(""),"vocali minuscole")
	print("qwrt contiene",contaVocali("qwrt"),"vocali minuscole")
	print("aia contiene",contaVocali("aia"),"vocali minuscole")	
main()
