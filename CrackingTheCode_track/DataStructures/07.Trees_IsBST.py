#!/usr/bin/python3

# For the purposes of this challenge, we define a binary search tree to be a binary tree with the following ordering properties:

# The  value of every node in a node's left subtree is less than the data value of that node.
# The  value of every node in a node's right subtree is greater than the data value of that node.
# Given the root node of a binary tree, can you determine if it's also a binary search tree?

# Complete the function in your editor below, which has  parameter: a pointer to the root of a binary tree. It must return a boolean denoting whether or not the binary tree is a binary search tree. You may have to write one or more helper functions to complete this challenge.

# Note: We do not consider a binary tree to be a binary search tree if it contains duplicate values.

# Input Format

# You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.

# Constraints

# Output Format

# You are not responsible for printing any output to stdout. Your function must return true if the tree is a binary search tree; otherwise, it must return false. Hidden code stubs will print this result as a Yes or No answer on a new line.



# """ Node is defined as
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# """

# def checkBST(root):
# 	stack = [root]
# 	all_data = []

# 	while len(stack) > 0:
# 		# print('stack comeco', [elem.data for elem in stack])
# 		node = stack.pop()
# 		all_data.append(node.data)

# 		if node.left:
# 			# print('left', node.left.data, '<', node.data)
# 			if node.left.data < node.data:
# 				stack.append(node.left)
# 			else:
# 				return False

# 		if node.right: 
# 			# print('right', node.data, '<', node.right.data)
# 			if node.data < node.right.data:
# 				stack.append(node.right)
# 			else:
# 				return False

# 	# print('all_data', all_data)
# 	# print('check', checkDuplicates(all_data))
# 	return True and checkDuplicates(all_data)

# def checkDuplicates(array):
# 	my_dict = dict()
# 	for elem in array:
# 		if elem in my_dict:
# 			return False
# 		else:
# 			my_dict[elem] = True
# 	return True

# For Some reason this works
def inOrderTraversalCheck(node, inValue=None):
	result = True
	if node.left is not None:
		(result, value) = inOrderTraversalCheck(node.left,min(node.data,inValue))
		if result is False:
			return (False, value)
		if value >= node.data:
			return (False, value)
	if node.right is not None:
		(result, value) = inOrderTraversalCheck(node.right, max(node.data,inValue))
		if result is False:
			return (False, value)
		if value <= node.data:
			return (False, value)
	if inValue is not None:
		if inValue >= node.data:
			return (False, node.data)
	if node.right or node.left is not None:
		return (True, max(node.data,value))
	else:
		return (True,node.data)


def checkBST(root):
	(result, value) = inOrderTraversalCheck (root)
	return (result)


elem1 = Tree(1)
elem2 = Tree(2)
elem3 = Tree(3)
elem4 = Tree(4)
elem5 = Tree(5)
elem6 = Tree(6)
elem7 = Tree(7)
elem8 = Tree(8)
elem9 = Tree(9)
elem10 = Tree(10)
elem11 = Tree(11)
elem12 = Tree(12)
elem13 = Tree(13)
elem14 = Tree(14)

# Case 1
# elem8.left = elem3
# elem8.right = elem10

# elem3.left = elem1
# elem3.right = elem6

# elem6.left = elem4
# elem6.right = elem7

# elem10.right = elem14

# elem14.left = elem13



# CAse 2
# elem4.left = elem2
# elem4.right = elem6

# elem2.left = elem1
# elem2.right = elem3

# elem6.left = elem5
# elem6.right = elem7

# Case 3
elem2.left = elem1
elem3.data = 2
elem1.right = elem3


# root = elem4
root = elem2
print(checkBST(root))
