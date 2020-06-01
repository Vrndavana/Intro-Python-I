# For the exercise, look up the methods and functions that are available for use
# with Python lists.

#    1, 2, 3  <- The numbers in the varibles X and Y 
#                 can still be seen as index items 
#    i  i  i  <-  for your for loop - check line 19
x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
for i in y : 
    x.append(i) 
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10] - just take out 8 
# YOUR CODE HERE
# extend - target y array/list - 
# - use slice array to grab everything but the first -

# This would work but it's more processing
# x.pop()
# x.pop()
# x.pop()
# x.extend(y[1:]) 

#or

x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print(x)

# Print the length of list x
print (len(x))
# YOUR CODE HERE

# Print all the values in x multiplied by 1000

for i in x : 
    print(i * 1000)
# x2 = [i * 1000 for i in x]
# print(x2)
# YOUR CODE HERE