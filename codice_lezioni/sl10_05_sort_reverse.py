'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 sort reverse sorted
# '''

ingredienti = ["farina", "acqua", "olio", "sale", "lievito"]
print(ingredienti)	#['farina', 'acqua', 'olio', 'sale', 'lievito']

ingredienti.reverse()		# in place
print(ingredienti)	#['lievito', 'sale', 'olio', 'acqua', 'farina']

ingredienti.sort()
print(ingredienti)	#['acqua', 'farina', 'lievito', 'olio', 'sale']

ingredienti = ["farina", "acqua", "olio", "sale", "lievito"]
ingr_rev = sorted(ingredienti,reverse=True)	# not in place
print(ingredienti)	#['farina', 'acqua', 'olio', 'sale', 'lievito']
print(ingr_rev)		#['sale', 'olio', 'lievito', 'farina', 'acqua']
ingr_lun = sorted(ingredienti, key=len)
print(ingr_lun)		#['olio', 'sale', 'acqua', 'farina', 'lievito']



