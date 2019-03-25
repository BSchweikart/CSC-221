"""
M2T1
2/4/19
"""
##p.92
vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Enter word or phrase: ')
def listing1():
	for letter in word:
		print(letter, '<-', end= '')
		if letter in vowels:
			print('<-', letter)
		else:
			print()
		
def listing2():
	vowels = ['a', 'e', 'i', 'o', 'u']
	word = input('Enter word or phrase: ')
	found =[]
	for letter in word:
		print(letter, '<-', end= '')
		if letter in vowels:
			if letter not in found:
				found.append(letter)
		else:
			print()

listing1()
listing2()
