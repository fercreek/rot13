def encoding():
	msg = raw_input("Enter your message: ")
	c = 13
	cipher = ""
	for char in msg:
		char = ord(char)
		if 97 <= char <= 123:
			if c+char < 123:
				cipher += chr((char) + c) 
			elif c+char >= 123:
				cipher += chr((char) - c)
		elif 65 <= char <= 90:
			if c+char < 90:
				cipher += chr((char) + c) 
			elif c+char >= 90:
				cipher += chr((char) - c)		
		else: 
			cipher += chr(char)
	return cipher
print encoding()


