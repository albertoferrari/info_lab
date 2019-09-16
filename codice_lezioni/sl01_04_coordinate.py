'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html

 date le coordinate di due punti A e B trovare le coordinate 
 del punto medio del segmento AB
'''

x_a = int(input('ascissa  del punto A '))
y_a = int(input('ordinata del punto A '))
x_b = int(input('ascissa  del punto B '))
y_b = int(input('ordinata del punto B '))
x_c = (x_a + x_b) / 2
y_c = (y_a + y_b) / 2
print('punto medio con coordinate',x_c,y_c)
