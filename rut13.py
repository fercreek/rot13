def encoding():
	msg = raw_input("Enter your message: ")
	c = 13
	alpha = 26
	cipher = ""
	for char in msg:
		#Si es minuscula...
		if 97 <= ord(char) <= 123:
			#Sino excedes el rango..
			if c+ord(char) < 123:
				cipher += chr(ord(char) + c) 
			elif c+ord(char) >= 123:
				cipher += chr(ord(char) - c)
		else: 
			#Sino eres una letra
			cipher += char
	return cipher
print encoding()
