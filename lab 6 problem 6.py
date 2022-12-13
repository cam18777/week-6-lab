# camryn echevarria
# 11/11/2022

#

import math

# ask the user for the number they liked to be factorized
number = int(input("what number would you like to factor out?\n"))

# factorize using the factorial module
answer = math.factorial(number)

# make a loop to calculate the factorization
num = 1
for numbers in range(1, number + 1):
    num = num * numbers

# pint problem 6 answer provided using factorial module
print("Answer using factorial module:", answer)

# print the answer from the loop
print("Answer using loops:", num)

# check if both answers are the same
if answer == num:
    print("Are the values the same: True")
else:
    print("Are the values the same: False")