#!/usr/bin/python3

# A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

# A basic queue has the following operations:

# Enqueue: add a new element to the end of the queue.
# Dequeue: remove the element from the front of the queue and return it.
# In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

# 1 x: Enqueue element  into the end of the queue.
# 2: Dequeue the element at the front of the queue.
# 3: Print the element at the front of the queue.
# Input Format

# The first line contains a single integer, , denoting the number of queries. 
# Each line  of the  subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query , but only query  is followed by an additional space-separated value, , denoting the value to be enqueued.

# Constraints

# It is guaranteed that a valid answer always exists for each query of type .
# Output Format

# For each query of type , print the value of the element at the front of the queue on a new line.

# Sample Input

# 10
# 1 42
# 2
# 1 14
# 3
# 1 28
# 3
# 1 60
# 1 78
# 2
# 2
# Sample Output

# 14
# 14



class MyQueue(object):
	push_stack = []
	pop_stack = []

	def __init__(self):
		self.push_stack = []	
		self.pop_stack = []

	def __switch(self, stack1, stack2):
		stack2 = list(reversed(stack1))
		stack1 = []
		return stack1, stack2
		# while len(stack1) > 0:
		# 	elem = stack1.pop()
		# 	stack2.append(elem)

	def peek(self):
		if len(self.push_stack) > 0:
			return self.push_stack[0]
		return self.pop_stack[len(self.pop_stack) - 1]

	def pop(self):
		# print(self.push_stack, self.pop_stack)

		# If our numbers is in the push stack we have to switch to pop
		if len(self.push_stack) > 0:
			self.push_stack, self.pop_stack = self.__switch(self.push_stack, self.pop_stack)
		
		# print('vefore pop', self.push_stack, self.pop_stack)
		last_element = self.pop_stack.pop()
		# print('after pop', self.push_stack, self.pop_stack)
		# print('last', last_element)
		return last_element

	def put(self, value):
		if len(self.pop_stack) > 0:
			self.pop_stack, self.push_stack = self.__switch(self.pop_stack, self.push_stack)

		self.push_stack.append(value)
		# print(self.push_stack, self.pop_stack)


queue = MyQueue()
t = int(input())
for line in range(t):
	values = map(int, input().split())
	values = list(values)
	if values[0] == 1:
		queue.put(values[1])
	elif values[0] == 2:
		queue.pop()
	else:
		print(queue.peek())
