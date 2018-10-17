# shift left <<
x = 3
print(x,' in binario',bin(x))
y = x << 3		# x * 2^3
print('y = x << 3','shift left 3')
print(y,' in binario',bin(y))

# shift right >> 
x = 4
print('x =',x,' in binario',bin(x))
y = x >> 1		# x = x / (2^1), con segno
print('y = x >> 1','shift right 1')
print(y,' in binario',bin(y))

# AND (&) OR (|) XOR(^) complemento (~)
x = 10 
y = 12
print('x=',x,' in binario',bin(x))
print('y=',y,' in binario',bin(y))
z = x & y       # AND applicato bit a bit
print('z = x & y ', '  z=', z, bin(z))
z = x | y       # OR applicato bit a bit
print('z = x | y ', 'z =', z, bin(z))
z = x ^ y       # XOR applicato bit a bit
print('z = x ^ y ', '  z =', z, bin(z))
z = ~x 			# complemento di ogni bit
print('z = ~x  ', 'z =', z, bin(z))
