'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio di scrittura su file di testo
# '''
import os

# scrittura in un file di testo
endl = '\n'
myFile = open("mieparole.txt","w")	#apertura file in scrittura
myFile.write("alfa"+endl)
myFile.write("beta"+endl)
myFile.write(str(123)+endl)
myFile.write(str(1.23)+endl)
myFile.write(str(True)+endl)
myFile.write(""+endl)
myFile.close()

with open("mieparole.txt", "a") as myFile:
    myFile.write("nuova_riga"+endl)

myDirectory = os.getcwd()
print('directory di lavoro',myDirectory)
