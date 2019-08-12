#!/usr/bin/python3

# https://www.hackerrank.com/challenges/ctci-contacts/problem


# Node Class
class Node:
	def __init__(self, value):
		self.children = {}
		self.value = value
		self.child_words = 0


# Taking O(n) n -> size of string to find
def find(node, key):
	# print('find')
	for char in key:
		# print(char)
		if char in node.children:
			node = node.children[char]
		else:
			return 0

	# After getting the node I still have to find all the children
	return node.child_words


# Taking O(n) n -> size of string to insert
def insert(root, string):
	# print('insert')
	node = root
	i = 0

	# Goes to the position that it's not inserted
	for char in string:
		# print(char)
		if char in node.children:
			node.child_words = node.child_words + 1
			node = node.children[char]
			i = i + 1
		else:
			break

	# Insert what's lefting
	while i < len(string):
		node.children[string[i]] = Node(None)
		node.child_words = node.child_words + 1
		node = node.children[string[i]]
		# print(node.value, i)
		i = i + 1

	node.value = string
	node.child_words = 1
	# print(node.value)



root = Node(None)

# Handle Input
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')

    if(op == 'add'):
    	insert(root, contact)
    elif(op == 'find'):
    	print(find(root, contact))


# root.children['a'] = Node('a')
# root.children['b'] = Node('b')

# insert(root, 'bala')
# insert(root, 'ba')

# print(find(root, 'aa'))
# print(find(root, 'bc'))
# print(find(root, 'ba'))
# print(find(root, 'bala'))