"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""
# print(f'{x,y,z}') <- (10, 2.24552, 'I like turtles!')
x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x is " + str(x) + ", " + "y is " + str(y) + ", " + "z is " + str(z))


# Use the 'format' string method to print the same thing
txt = "a is {a}, b is {b}, c is {c}".format(a="10",b="2.24552", c="I like TRAINS!")
print(txt)

txt2 = "My name is {0}, I'am over {1}!!!".format("V",9000)
print(txt2)

# Finally, print the same thing using an f-string
print(f'x is {x}, y is {y}, z is {z}')


