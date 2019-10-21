'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio di lettura su file CSV
# '''

COMMA = ","

myFile = open("esCSV.txt","r")	#apertura file in lettura
for testo in myFile:
	l = testo.split(",")
	for v in l:
		print(v)
myFile.close()

