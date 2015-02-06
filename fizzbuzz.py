__author__ = 'david whritenour'

import sys

# Determine Upper Limit
if len(sys.argv) == 1:
    i = input("Enter a single, integer value for the Upper Limit:  ")
elif len(sys.argv) == 2:
    i = sys.argv[1]
else:
    print("A valid number of argument was not entered at Command Prompt")
    i = input("Enter Upper Limit:  ")

# Check Upper limit is integer
try:
    n = int(i) + 1
    # Iterate through range
    for x in range(1, n):
        fizz = (not x % 3) * "Fizz"
        buzz = (not x % 5) * "Buzz"
        if fizz or buzz:
            print(fizz+buzz)
        else:
            print(x)
# Exception for non-integer
except ValueError:
    print("An Single, Integer Value was not entered.  Please run again.")