'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio di scrittura su file di testo
# '''
import os, random
ENDL = '\n'

def riempi_ordinato(nome_file: str, num: int):
	'''
	crea il file nome_file e inserisce num
	valori compresi fra 0 e 100 ordinati (crescente)
	'''
	fout = open(nome_file,"w")
	lis = []
	for i in range(0,num):					#genera valori
		lis.append(random.randint(0,100))
	lis.sort()								#ordina valori
	for val in lis:
		fout.write(str(val)+ENDL)			#scrive su file
	fout.close()
	


riempi_ordinato("file1.txt",10)
riempi_ordinato("file2.txt",12)

#os.remove("file1.txt")
#os.remove("file2.txt")
