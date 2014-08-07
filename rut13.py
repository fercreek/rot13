#m = raw_input("Please, enter your text: ")
c= 13
m = raw_input("Enter your letter: ")
m = ord(m)
if 97 <= m <= 123:
	if c+m < 123:
		val = chr(m+c)
	elif c+m>=123:	
		val = chr(m-c)
print val