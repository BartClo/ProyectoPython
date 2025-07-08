#Task
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i, print i^2.

# Example
# The list of non-negative integers that are less than n is [0, 1, 2, ..., n-1]. 
# Print the square of each number on a separate line.

# 0
# 1
# 4

# Input Format
# The first and only line contains the integer, n.

# Constraints

# Output Format
# Print n lines, one corresponding to each i.

# Sample Input 0
# 5

# Sample Output 0
# 0
# 1
# 4
# 9
# 16

n = int(input())

for n in range(0, n + 1):
    n = n - 1
    if n < 0:
        continue
    else:
        print(n**2)