'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio di scrittura su file di testo
# '''
import os

def esplora(nome_directory):
	for nome in os.listdir(nome_directory):
		percorso = os.path.join(nome_directory, nome)
		if os.path.isfile(percorso):
			print(percorso)
		else:
			esplora(percorso)

esplora("C:/Users/alber/Desktop/ILP/codice")

# errore file
myFile = open('file_inesistente.txt')

# gestione eccezioni
try:
	myFile = open('file_inesistente.txt')
except:
	print('errore apertura file')


