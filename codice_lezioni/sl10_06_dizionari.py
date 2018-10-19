'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 dizionari
# '''
#definizione di dizionario {}
tel = {"john": 4098, "terry": 4139}
#accesso a un elemento
print(tel["john"])	#4098
#ggiunta di una coppia chiave/valore
tel["graham"] = 4127
#visualizzazione dizionario
print(tel)			#{"graham": 4127, "terry": 4139, "john": 4098}
#visualizzazione chiavi
print(list(tel))	#['john', 'terry', 'graham']
#lista di coppie
print(list(tel.items()))
#sequenza di elementi
for k in tel.keys():
	print(k,tel[k])




