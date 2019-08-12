# Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line ( their positions are fixed), and each  of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to save money, so she needs to minimize the total number of candies given to the children.

# Input Format

# The first line of the input is an integer N, the number of children in Alice's class. Each of the following N lines contains an integer that indicates the rating of each child.

# Constraints

# Output Format

# Output a single line containing the minimum number of candies Alice must buy.

# Sample Input

# 3  
# 1  
# 2  
# 2
# Sample Output

# 4

def candies():
	n = int(raw_input())
	if n == 0: return 0

	rating = []
	candies = [0] * n 
	dic = {}
	total = 0

	for i in range(0, n):
		rating_i = int(raw_input())
		rating.append(rating_i)

		# I will put the rating in an dict that will tell me the indexes of which rating
		if rating_i in dic.keys():
			dic[rating_i].append(i)
		else:
			dic[rating_i] = [i]

			
	# Now I will run through the dictionary starting from the smaller keys
	sorted_keys = sorted(dic.keys())
	for key in sorted_keys:
		for index in dic[key]:
			right_neighbor = index + 1
			left_neighbor = index - 1
			to_right_candy_num = 0
			to_left_candy_num = 0
			
			# number of candies the neighbors have
			if(right_neighbor < n): to_right_candy_num = candies[right_neighbor]
			if(left_neighbor >= 0): to_left_candy_num = candies[left_neighbor]

			# check if the neighbor has a higher lower than me, if yes I get 
			# her rank plus one
			my_candy = 1
			if(right_neighbor < n and rating[right_neighbor] < rating[index]):
				my_candy = candies[right_neighbor] + 1
			if(left_neighbor >= 0 and rating[left_neighbor] < rating[index]):
				# if i've already put a different value then we have to compare 
				if(my_candy > 1):
					my_candy = max(my_candy, candies[left_neighbor] + 1)
				else:
					my_candy = candies[left_neighbor] + 1

			candies[index] = my_candy


	# And now sum up all the candies to the total
	for i in range(0, n):
		total = total + candies[i]

	return total

print candies()
