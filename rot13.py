import sys
def encoding(msg,c):
	alpha = "abcdefghijklmnopqrstuvwxyz"
 	text = ""
 	for letter in msg:
 		pos = alpha.find(letter)
 		if pos != -1:
 			text+= alpha[(pos+13)%26]
 		else:
 			text+=""
 	return text
print encoding(sys.argv[1], 13)
