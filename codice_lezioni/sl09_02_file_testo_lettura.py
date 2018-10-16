'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio di lettura su file di testo
# '''
print('1) ---------------------')
# lettura di una singola riga dal file di testo
myFile = open("1000_parole_italiane_comuni.txt")	#apertura file
riga = myFile.readline()							#lettura riga
print(riga,len(riga))								#... compreso \n
riga_pulita = riga.strip()							#elimino spazi e \n
print(riga_pulita,len(riga_pulita))					#riga 'pulita'
myFile.close()										#chiusura file

print('2) ---------------------')
# lettura di tutte le righe dal file di testo
myFile = open("1000_parole_italiane_comuni.txt")	#apertura file
for testo in myFile:
	print(testo.strip(),len(testo.strip()))			#elimino spazi e \n
myFile.close()										#chiusura file

print('3) ---------------------')
# blocco with al termine effettua in automatico la chiusura del file
with open("1000_parole_italiane_comuni.txt","r") as myFile:
	max_len = 0
	parola = ''
	for testo in myFile:
		if len(testo)-1 > max_len:
			max_len = len(testo)-1
			parola = testo.strip()
	print('parola più lunga',parola,max_len)
	
# print('4) ---------------------')
# lettura intero file in una stringa
with open("1000_parole_italiane_comuni.txt", "r") as myFile:
    tutto = myFile.read()   
    print('tipo',type(tutto))
    print('lunghezza',len(tutto))
    print('contenuto: ----')
    print(tutto)

print('5) ---------------------')
# lettura intero file in una stringa (codifica utf-8)
with open("1000_parole_italiane_comuni.txt", mode="r", encoding="utf-8") as myFile:
    tutto = myFile.read()   
    print('tipo',type(tutto))
    print('lunghezza',len(tutto))
    print('contenuto: ----')
    print(tutto)

