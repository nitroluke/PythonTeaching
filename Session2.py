"""
 12/17/14
 session 2 over Python topic on 8.29 & 9.03
 by Luke Welna
"""

import math

"""
Comment
"""

print("""

+------+
|      |
| Luke |
|      |
+------+

""")

#uses the python library to calculate the factorial of a number
print(math.factorial(10))

counter = 10 # number to calculate the factorial
fact = 1 # innitialize fact to 1
for counter in range(1, counter + 1): # loop from 1 to counter + 1
    fact = fact * counter # fact will retain values from previous iterations of the for loop
print("factorial = ", fact) # print out fact
