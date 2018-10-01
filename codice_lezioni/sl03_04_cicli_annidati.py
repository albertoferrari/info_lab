'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 cicli annidati
 (per formattazione output -> https://pyformat.info)
'''

for riga in range(1, 13):
    for colonna in range(1, 13):
        val = riga * colonna
        print(f"{val:3}", end=" ")  # val testo di almeno 3 caratteri
    print()

