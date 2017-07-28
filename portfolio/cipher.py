
#1. ord(): returns the ASCII value of a character
#2. chr(): takes in an ASCII value and returns the character
#3. isalpha(): detects if input is a character in the alphabet
#4. find(): """
import sys

#takes in user input and encodes word
def encode(plaintext, shift_num):
	encodedWord = ''
	newASCII = 0
	#loops through user input and encodes each letter by taking ASCII value of letter and adding shift num to it
	for i in plaintext:
		if (i.isalpha()): #checks if user input is a char in alphabet
			newASCII = ord(i) + shift_num
			if (newASCII > ord('z')): #wrap around function
				newASCII -= 26
			encodedWord += chr(newASCII)
	print("Your ciphertext is: " + encodedWord)


#brute force method; checks against every possible shift (does not have access to a key)
def decode(ciphertext):
	decodedWord = ''
	shift = 1
	for shift in range(27):
		for x in ciphertext:
			originalASCII = ord(x) - shift
			if (originalASCII > ord('z')):
				originalASCII -= 26
			decodedWord += chr(originalASCII)
		print("Shift " + decodedWord)

#asks user whether to decode or encode
user_input = str(input("Would you like to encode or decode a message? \n"))
plaintext = ""
shift_num = 0

#prompts user to enter message to encode
if (user_input == "encode"):
	plaintext = input("What is your message? \n")
	shift_num = int(input("What would you like to shift the message by? \n" ))
	encode(plaintext, shift_num)
#prompts user to enter ciphertext to decode
elif (user_input == "decode"):
	ciphertext = input("What is your ciphertext? \n")
	decode(ciphertext)
#if user inputs anything else
else:
	print("Please input 'encode' or 'decode'")
