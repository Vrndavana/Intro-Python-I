"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
y.append(1)
y.append(2)
y.append(3)
y.append(4)
y.append(5)
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in y : 
    print(i * i * i)


# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]
y = []
for i in a:
    y.append(i.upper())
print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')
en_li = [] 
od_li = [] 
for i in x: 
    if (int(i) % 2 == 0): 
        en_li.append(i) 
    else: 
        od_li.append(i) 
print("Even lists:", en_li) 
print("Odd lists:", od_li) 

# What do you need between the square brackets to make it work?
y = [int(i) for i in x if int(i) % 2 == 0]

print(y)