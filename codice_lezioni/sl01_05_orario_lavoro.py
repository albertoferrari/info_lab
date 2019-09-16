'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html

 per il lavoro di un operaio sono registrati l’orario di entrata 
 e l’orario di uscita sia al mattino che al pomeriggio: 
 calcolare il totale delle ore e dei minuti lavorati e, 
 data la paga oraria, calcolare la paga giornaliera
'''

hEm = int(input('ora di entrata al mattino '))
mEm = int(input('minuto di entrata al mattino '))
hUm = int(input('ora di uscita al mattino '))
mUm = int(input('minuto di uscita al mattino '))

hEp = int(input('ora di entrata al pomeriggio '))
mEp = int(input('minuto di entrata al pomeriggio '))
hUp = int(input('ora di uscita al pomeriggio '))
mUp = int(input('minuto di uscita al pomeriggio '))

# mancano controlli su correttezza orari

hl = (hUm - hEm) + (hUp - hEp)		#ore lavorate mattino e pomeriggio
ml = (mUm - mEm) + (mUp - mEp)		#minuti lavorati matt e pom
while ml < 0:
	ml += 60
	hl -= 1
	
print('tempo di lavoro: ore',hl,'minuti',ml)

paga_oraria = float(input('paga oraria '))
paga_giornaliera = paga_oraria * hl + (paga_oraria / 60) * ml
print('paga giornaliera',paga_giornaliera)
