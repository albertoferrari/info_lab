# ricerca data gg/mm/aaa
import re

ro = re.compile('\d{2}/\d{2}/\d{4}')

s = 'data di nascita 27/11/2019 Parma'
f = ro.search(s)

if f:
	#group()	restituisce la stringa corrispondente alla RE
	print('f.group()',f.group())

	#start()	restituisce la posizione iniziale della corrispondenza
	print('f.start()',f.start())

	#end()	restituisce la posizione finale della corrispondenza
	print('f.end()',f.end())

	#span()	restituisce una tupla contenente la (start, end) posizione della corrispondenza
	print('f.span()',f.span())
	
	start, end  = f.span()
	print('trovato: ',s[start:end])
else:
	print('no match')
