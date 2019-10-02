'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 chiedere una riga di testo all'utente
 contare separatamente le occorrenze di ciascuna lettera maiuscola (da 'A' a 'Z’)
 creare una lista (array) di 26 elementi
 inizialmente tutti posti a 0
 ciascun elemento è il contatore per una certa lettera 
'''

N = 26  					# ord('Z') - ord('A') + 1
occorrenze = [0] * N		# occorrenze di ogni lettera

testo = input("testo da analizzare: ")

for c in testo:
    if 'A' <= c <= 'Z':
        indice = ord(c) - ord('A')
        occorrenze[indice] += 1

for i in range(N):
    codice = i + ord('A')
    print(chr(codice), occorrenze[i])


