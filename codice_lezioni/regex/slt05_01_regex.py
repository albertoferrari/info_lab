import re

ro = re.compile('[a-z]+')	# uno o più caratteri alfabetici minuscolo

f = ro.search('XXsistemi09informativi')
#f = ro.search('123')
print(f)

if f:
	#group()	restituisce la stringa corrispondente alla RE
	print('f.group()',f.group())

	#start()	restituisce la posizione iniziale della corrispondenza
	print('f.start()',f.start())

	#end()	restituisce la posizione finale della corrispondenza
	print('f.end()',f.end())

	#span()	restituisce una tupla contenente la (start, end) posizione della corrispondenza
	print('f.span()',f.span())
else:
	print('no match')

l = ro.findall('09sistemi09informativi')
print(l)

