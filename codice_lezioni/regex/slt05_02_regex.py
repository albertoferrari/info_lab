import re

# Remove anything other than digits
phone = 'Phone: +39 0521 905708'
num = re.sub(r'\D', "", phone)    
print("Phone Num : ", num)

# Hide password
string = 'Password: mypwd'
hidden = re.sub(r"^(Password:\s*).+$", r'\1(******)', string)
print(hidden)

# part of a match
address = 'Please mail it to alberto.ferrari@unipr.it.com'
match = re.search(r'([\w.-]+)@([\w-]+).([\w]+)',address)
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))

print('match only upper and lowercase letters, numbers, and underscores')
patterns = r'^[a-zA-Z0-9_]*$'
text1 = 'Sistemi_Informativi'
#text1 = 'Sistemi_Info:rmativi'
if re.search(patterns,text1):
	print('ok')
else:
	print('error')

print('minimum eight characters, at least one uppercase letter, one lowercase letter and one number')
patterns = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
pwd = input('password ')
while not re.search(patterns,pwd):
	pwd = input('password ')

