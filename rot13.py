import sys
def encoding(msg, c):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	text = ""
	for letter in msg:
		if letter != " ":
			pos = alpha.find(letter)
			if pos == -1 :
				text += ""
			else:	
				text += alpha[pos+c] if pos+c<=26 else alpha[pos+c-26]
		else: 	
			text+=""	
	return text
print encoding(sys.argv[1], 13)
