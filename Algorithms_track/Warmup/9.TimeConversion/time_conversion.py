# Given a time in -hour AM/PM format, convert it to military (-hour) time.

# Note: Midnight is  on a -hour clock, and  on a -hour clock. Noon is  on a -hour clock, and  on a -hour clock.

# Input Format

# A single string containing a time in -hour clock format (i.e.:  or ), where  and .

# Output Format

# Convert and print the given time in -hour format, where .

# Sample Input

# 07:05:45PM
# Sample Output

# 19:05:45


time = raw_input().strip()
hour = int(time[:2])

if time[len(time) - 2:] == 'AM':
	if hour == 12:
		print '00' + time[2:len(time) - 2]
	else:
		print time[:len(time) - 2]
else:
	if hour == 12:
		print '12' + time[2:len(time) - 2]
	else:
		hour = (hour + 12) % 24
		print str(hour) + time[2:len(time) - 2]
	 

