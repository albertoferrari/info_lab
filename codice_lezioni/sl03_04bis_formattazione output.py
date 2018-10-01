'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 esempio di formattazione output numerico
 see (https://docs.python.org/3/tutorial/inputoutput.html)
'''

for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
