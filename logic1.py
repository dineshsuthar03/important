#!/bin/python3

import math
import os
import random
import re
import sys


# Given a number n, for each integer iin the range
# from 1 to ninclusive, print one value per line as
# follows:
# .If iis a multiple of both 3 and 5, print FizzBuzz.
# If is a multiple of 3 (but not 5, print Fiz.
# If iis a multiple of 5(but not 3), print Buzz.
# If iis not a multiple of 3 or 5, print the value of i.


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    for i in range(1,n+1):
        if i%3 ==0 and i%5!=0:
            print("Fizz")
        elif i%3!=0 and i%5==0:
            print("Buzz")
        elif i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3!=0 and i%5!=0:
            print(i)
        else:
            print("In else block")

    
if __name__ == '__main__':
    
    n = int(input().strip())

    fizzBuzz(n)
