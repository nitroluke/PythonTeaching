import math
"""
 12/1/14
 session 4 over Python topic on 9.10
 by Luke Welna
"""

# Exercise 6
expression = 6 * (1 - 2)
print(expression)

# Exercise 8
r = input("Please enter a radius to calculate the area of a circle > ")
# pi * radius^2
print("The area of the circle is ", math.pi * (int(r) ** 2))

# Exercise 11

#celcius to fahrenheit = c * (9/5) + 32

c = float(input("What is the temp in celsius > "))
f = c * (9 / 5) + 32
print(c, "in celsius" , " = ", f , "in fahrenheit")
