'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 il giocatore si muove su una scacchiera di 5x5 celle, partendo da un angolo
 le righe e le colonne sono numerate da 0 a 4
 un tesoro ed un mostro sono nascosti in due posizioni casuali, all'inizio del gioco
 ad ogni turno, il giocatore:
 - sceglie una direzione verso cui spostarsi (alto, basso, sinistra, destra)
 - se capita sulla cella del tesoro, ha vinto
 - se capita sulla cella del mostro, ha perso
'''

from random import randint
mr = randint(0,4) 	# riga mostro
mc = randint(0,4) 	# colonna mostro
tr = randint(0,4) 	# riga tesoro
tc = randint(0,4)	# colonna tesoro
gr = 0 # riga giocatore
gc = 0 # colonna giocatore

vinto = False
perso = False
print("sei nella riga ", gr, " e colonna ", gc)
while (not vinto and not perso):
    if (gr == mr and gc == mc):
        perso = True
        print("hai incontrato il mostro e hai perso")
    elif (gr == tr and gc == tc):
        vinto = True
        print("hai trovato il tesoro e hai vinto!")
    else:
        mossa = input("mossa: a(alto) b(basso) d(destra) s(sinistra) ")
        if mossa == "a":
            gr = (gr - 1) % 5
        elif mossa == "b":
            gr = (gr + 1) % 5
        elif mossa == "s":  
            gc = (gc - 1) % 5
        elif mossa == "d":  
            gc = (gc + 1) % 5    
        print("sei nella riga ", gr, " e colonna ", gc)
