# 1. Write a function that takes in a person's name, and prints out a greeting.

# The greeting must be at least three lines, and the person's name must be in each line.
# Use your function to greet at least three different people.
# Bonus: Store your three people in a list, and call your function from a for loop.
names = ["Dante","Alexa","Adama"]

for i in names:
    print("Hey", i)

# Full Names
# Write a function that takes in a first name and a last name, and prints out a nicely formatted full name, in a sentence. Your sentence could be as simple as, "Hello, full_name."
# Call your function three times, with a different name each time.
def full_name(first, last):
    print("Hello {0} {1}, nice to meet you!".format(first, last))

# Addition Calculator
# Write a function that takes in two numbers, and adds them together. Make your function print out a sentence showing the two numbers, and the result.
# Call your function with three different sets of numbers.
def add(a, b):
    x = a + b
    print("The sum of {} and {} is {}".format(a, b, x))

# Return Calculator
# Modify Addition Calculator so that your function returns the sum of the two numbers. The printing should happen outside of the function.
def addition(a, b):
    x = a + b
    return x

print(addition(3, 5))

# 2. Consider the following expression, intended to print the square  root of 16: 
pow(16,(1/2))
# What is the result of this expression? How should it be changed, still using pow, to yield the correct answer?
print(pow(16,(1/2)))

# 3. Define the variables x and y as lists of numbers, and z as a tuple.
x=[1, 2, 3, 4, 5]
y=[11, 12, 13, 14, 15]
z=(21, 22, 23, 24, 25)

# (a) What is the value of 3*x?
print(3*x)

# (b) What is the value of x+y?
print(x+y)

# (c) What is the value of x-y?
print(x-y)

# (d) What is the value of x[1]?
print(x[1])

# (e) What is the value of x[0]?
print(x[0])

# (f) What is the value of x[-1]?
print(x[-1])

# (g) What is the value of x[:]?
print(x[:])

# (h) What is the value of x[2:4]?
print(x[2:4])

# (i) What is the value of x[1:4:2]?
print(x[1:4:2])

# (j) What is the value of x[:2]?
print(x[:2])

# (k) What is the value of x[::2]?
print(x[::2])

# (l) What is the result of the following two expressions?
x[3] = 8
print(x)

# (m) What is the result of the above pair of expressions if the list x were replaced with the tuple z?
z = list(z)
z[3] = 8
z = tuple(z)
print(z)