''' 
genera un numero “segreto” a caso tra 1 e 90
chiede ripetutamente all'utente di immettere un numero
finché non indovina quello generato
ad ogni tentativo, dice se il numero immesso
è maggiore o minore del numero segreto
'''

import random
n = random.randint(1, 90)

val = int(input("inserisci un numero [1..90] "))
while (val!=n):
    if (val<n):
        print(val,"è minore del numero segreto")
    else:
        print(val,"è maggiore del numero segreto")
    val = int(input("inserisci un nuovo valore [1..90] "))

print("hai indovinato! Il numero segreto è",n)    
