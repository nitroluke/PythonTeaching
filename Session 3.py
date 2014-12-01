"""
 12/24/14
 session 3 over Python topic on 9.08
 by Luke Welna
"""

numPennies = int(input('Enter a number of pennies to convert to nickles: ' ))
numNickles = int(int(numPennies) / 5)
remainingPennies = numPennies - (numNickles * 5)
print("total number of pennies = ", numPennies)
print("number of nickles  = ", numNickles)
print("number of  remaining pennies = ", remainingPennies)
