#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    print("Key in a value")
    n = int(input().strip())

    remainder = n % 2
    
    if remainder == 1:
        print("Weird")
    elif (remainder == 0 and (n >= 2  and n<= 5)):
        print("Not Weird")
    elif (remainder == 0 and (n >= 6  and n<= 20)):
        print("Weird")
    elif (remainder == 0 and n > 20):
        print("Not Weird")

#   print("Enter value is: " + str(n))
#   print("The reminder is: "+ str(reminder))