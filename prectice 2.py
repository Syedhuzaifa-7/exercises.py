"""import math

print(math.pi)  # Prints the value of pi
print(math.sqrt(16))  # Prints the square root of 16
print(math.sin(math.radians(30))) #prints the sin of 30 degrees.

import os

print(os.getcwd())  # Prints the current working directory
#os.mkdir("my_new_directory") #creates a new directory.
print(os.path.exists("my_file.txt")) #checks if a file exists."

import random

print(random.randint(1, 10))  # Prints a random integer between 1 and 10

import datetime
print(datetime)"""
from datetime import date, datetime

d = date(2025, 3, 15)  # Year, month, day
print(d)

dt = datetime(2025, 3, 15, 14, 30, 0)  # Year, month, day, hour, minute, second
print(dt)
