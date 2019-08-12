# A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. Longest common subsequence (LCS) of 2 sequences is a subsequence, with maximal length, which is common to both the sequences. 

# Given two sequence of integers, A=[a1, a2, ..., an] and B=[n1, b2, ..., bn], find any one longest common subsequence.

# In case multiple solutions exist, print any of them. It is guaranteed that at least one non-empty common subsequence will exist.

def print_table(table, lin, col):
	for i in range(1, lin):
		for j in range(1, col):
			print table[i][j], 
		print '\n'

m, n = map(int, raw_input().strip().split(' '))

x = map(int, raw_input().strip().split(' '))
y = map(int, raw_input().strip().split(' '))



b = [[]] * (m + 1)
for i in range(0, (m + 1)):
	b[i] = [[]] * (n + 1)

c = [[]] * (m + 1)
for i in range(0, m + 1):
	c[i] = [[]] * (n + 1)

for i in range(1, m):
	c[i][0] = 0

for j in range(0, n):
	c[0][j] = 0



for i in range(0, m):
	for j in range(0, n):
		if x[i] == y[j]:
			c[i + 1][j + 1] = c[i][j] + 1
			b[i + 1][j + 1] = 'd'
		elif c[i][j + 1] >= c[i + 1][j]:
			c[i + 1][j + 1] = c[i][j + 1]
			b[i + 1][j + 1] = 't'
		else:
			c[i + 1][j + 1] = c[i + 1][j]
			b[i + 1][j + 1] = 'l'
		# print "a[i], b[i]", x[i], y[i]
		# print_table(c, m ,n)




# print 'c *********************'
# print_table(c, m + 1, n + 1)
# print 'b *********************'
# print_table(b, m, n)

def print_LCS(b, X, i, j):
	if i == 0 or j == 0:
		return
	if b[i][j] == 'd':
		print_LCS(b, X, i - 1, j - 1)
		resposta.append(X[i - 1])
	elif b[i][j] == 't':
		print_LCS(b, X, i - 1, j)
	else: print_LCS(b, X, i, j - 1)

resposta = []
print_LCS(b, x, m, n)

for i in range(0, len(resposta)):
	print resposta[i], 
# print resposta

