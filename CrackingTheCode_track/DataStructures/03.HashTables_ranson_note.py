#!/usr/bin/python

# A kidnapper wrote a ransom note but is worried it will be traced back to him. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use whole words available in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.

# Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

# Input Format

# The first line contains two space-separated integers describing the respective values of  (the number of words in the magazine) and  (the number of words in the ransom note). 
# The second line contains  space-separated strings denoting the words present in the magazine. 
# The third line contains  space-separated strings denoting the words present in the ransom note.

# Constraints

# .
# Each word consists of English alphabetic letters (i.e.,  to  and  to ).
# The words in the note and magazine are case-sensitive.
# Output Format

# Print Yes if he can use the magazine to create an untraceable replica of his ransom note; otherwise, print No.



m, n = map(int, raw_input().strip().split(' '))
magazine_words_ar = raw_input().strip().split(' ')
note_words = raw_input().strip().split(' ')
magazine_words = {}

for word in magazine_words_ar:
	if(word in magazine_words):
		magazine_words[word] = magazine_words[word] + 1
	else:
		magazine_words[word] = 1

def okayToWrite(array):
	for word in array:
		if word in magazine_words and magazine_words[word] > 0:
			magazine_words[word] = magazine_words[word] - 1
		else:
			return False
	return True


if okayToWrite(note_words) == True:
	print 'Yes'
else:
	print 'No' 



