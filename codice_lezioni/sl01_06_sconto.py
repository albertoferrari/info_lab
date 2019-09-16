'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html

 per la vendita di un prodotto si deve applicare uno sconto progressivo 
 in base al numero di pezzi ordinati in base alla regola: 
 fino a 3 pezzi 5%, fino a 5 pezzi 10%, fino a 10 pezzi 20%, 
 oltre 10 pezzi 30%. 
 Dato il prezzo del prodotto e il numero di pezzi ordinati calcolare 
 il prezzo da pagare.
'''

prezzo = float(input('prezzo del prodotto'))
n = int(input('numero di pezzi ordinati'))

if n <= 3:
	sconto = 5
elif n <= 5:
	sconto = 10
elif n <= 10:
	sconto = 20
else:
	sconto = 30

pag = (prezzo * (100 - sconto)) / 100
print('importo da pagare',pag)
