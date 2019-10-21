'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio di scrittura su file CSV
# '''
# import os
COMMA = ","

myFile = open("esCSV.txt","w")	#apertura file in scrittura
myFile.write("ABCD"+COMMA)
myFile.write("beta"+COMMA)
myFile.write(str(123)+COMMA)
myFile.write(""+COMMA)
myFile.write(str(1.23)+COMMA)
myFile.write(str(True)+COMMA)
myFile.write("last")
myFile.close()

#os.remove("esCSV.txt")
