import re

def is_alphanumeric(string):
	characherRegex = re.compile('^[a-zA-Z0-9.]*$')
	s = characherRegex.search(string)
	return bool(s)

def is_mailAddress(string):
	characherRegex = re.compile(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$')
	string = characherRegex.search(string)
	return bool(string)	

def is_CF(string):
	# characherRegex = re.compile(r'^[a-z]{6}[0-9]{2}[a-z][0-9]{2}[a-z][0-9]{3}[a-z]$')
	characherRegex = re.compile(r'^[A-Z]{6}'
								r'[0-9LMNPQRSTUV]{2}[ABCDEHLMPRST]{1}[0-9LMNPQRSTUV]{2}'
								r'[A-Z]{1}[0-9LMNPQRSTUV]{3}[A-Z]{1}$')
	string = characherRegex.search(string)
	return bool(string)	
	

print("is_alphanumeric('abYZ0099')",is_alphanumeric('abYZ0099'))	# Out: 'True'
print("is_alphanumeric('a#7')",is_alphanumeric('a#7')) 	# Out: 'False'
print("is_alphanumeric('99aBc')",is_alphanumeric('99aBc')) 	# Out: 'True'

print("is_mailAddress('alberto.ferrari@unipr.it')",is_mailAddress('alberto.ferrari@unipr.it'))
print("is_mailAddress('informatica e laboratorio')",is_mailAddress('informatica e laboratorio'))

print("is_CF('RSSVNT79B16L081E')",is_CF('RSSVNT79B16L081E'))
