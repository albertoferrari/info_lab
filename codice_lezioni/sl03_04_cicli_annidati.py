'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 cicli annidati
'''

for riga in range(1, 13):
    for colonna in range(1, 13):
        val = riga * colonna
        print(f"{val:3}", end=" ")  # val represented as text
                                    # with at least 3 chars
    print()

