'''
 @author Alberto Ferrari - https://albertoferrari.github.io/
 @license This software is free - http://www.gnu.org/licenses/gpl.html
 
 analisi della performance di varie versioni della funzione
 che restituisce il valore dell'ennesimo termine della 
 successione di Fibonacci
'''
import time, functools, math

_termini_calcolati = [0, 1] # termini noti per fib(0)* e fib(1)

def fibonacci_01(n: int) -> int:
	'''
	ricorsione senza memoizzazione
	'''
	if n <= 1:
		return n
	return fibonacci_01(n-1) + fibonacci_01(n-2)

def fibonacci_02(n: int) -> int:
	'''
	ricorsione con memoizzazione mediante lista globale
	'''
	if n < len(_termini_calcolati):
		return _termini_calcolati[n]
	val = fibonacci_02(n-1) + fibonacci_02(n-2)
	_termini_calcolati.append(val)
	return val
	
def fibonacci_03(n: int) -> int:
	'''
	iterazione
	'''
	val = 1
	prec = 0
	for i in range(n-1):
		prec, val = val, val + prec
	return val

@functools.lru_cache()
def fibonacci_04(n: int) -> int:
	'''
	ricorsione decoratore per memoizzazione
	'''
	if n <= 1:
		return n
	return fibonacci_04(n-1) + fibonacci_04(n-2)
	
def fibonacci_05(n: int) -> int:
	'''
	formula di Binet
	'''
	r5 = math.sqrt(5)
	fi  = (1+r5)/2
	fis = (1-r5)/2
	return int(round((1/r5)*(pow(fi,n)-pow(fis,n))))

def main():
	n = 40
	
	# fibonacci_01
	start = time.clock()
	val = fibonacci_01(n)
	t = time.clock() - start
	print('senza memoizzazione: fib({}) ='.format(n), val, 'time: % 10.8f' %(t))
	# senza memoizzazione: fib(40) = 102334155 time:  67.94661130
	
	# fibonacci_02
	start = time.clock()
	val = fibonacci_02(n)
	t = time.clock() - start
	print('memoizzazione lista: fib({}) ='.format(n), val, 'time: % 10.8f' %(t))
	# memoizzazione lista: fib(40) = 102334155 time:  0.00009390
	
	# fibonacci_03
	start = time.clock()
	val = fibonacci_03(n)
	t = time.clock() - start
	print('iterazione         : fib({}) ='.format(n), val, 'time: % 10.8f' %(t))
	# iterazione         : fib(40) = 102334155 time:  0.00001080
	
	# fibonacci_04
	start = time.clock()
	val = fibonacci_04(n)
	t = time.clock() - start
	print('decorator          : fib({}) ='.format(n), val, 'time: % 10.8f' %(t))
	# decorator          : fib(40) = 102334155 time:  0.00003360
	
	# fibonacci_05
	start = time.clock()
	val = fibonacci_05(n)
	t = time.clock() - start
	print('formula di Binet   : fib({}) ='.format(n), val, 'time: % 10.8f' %(t))
	# formula di Binet   : fib(40) = 102334155 time:  0.00004190
	
if __name__ == "__main__":
	main()
